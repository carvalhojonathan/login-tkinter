import hashlib
from models import Usuario
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def retorna_session():
    USUARIO = 'root'
    SENHA = ''
    HOST = 'localhost'
    PORTA = '3306'
    BANCO = 'login-terminal-db'
    CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}'
    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class ControllerCadastro():
    @classmethod
    def verificar_dados(cls, nome, email, senha):
        if len(nome) < 3:
            return 'Seu nome deve ter no mínimo 3 caracteres'
        elif len(nome) > 50:
            return 'Seu nome deve ter no máximo 50 caracteres'
        elif len(email) < 5:
            return 'Seu email deve ter no mínimo 5 caracteres'
        elif len(email) > 50:
            return 'Seu email deve ter no máximo 50 caracteres'
        elif len(senha) < 6:
            return 'Sua senha deve ter no mínimo 6 caracteres'
        elif len(senha) > 100:
            return 'Sua senha deve ter no máximo 100 caracteres'
        else:
            return 1
        
    @classmethod
    def cadastrar_usuario(cls, nome, email, senha):
        session = retorna_session()
        verifica_email = session.query(Usuario).filter_by(email=email).first()

        if verifica_email:
            session.close()
            return 'Email já cadastrado no sistema'
        
        usuario_verificado = cls.verificar_dados(nome, email, senha)
        if usuario_verificado != 1:
            session.close()
            return usuario_verificado
        
        try:
            senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            usuario = Usuario(nome=nome, email=email, senha=senha_hash)
            session.add(usuario)
            session.commit()
            session.close()
            return 1
        except Exception as e:
            session.rollback()
            session.close()
            return f'Erro interno do sistema: {str(e)}'
        
class ControllerLogin():        
    @classmethod
    def logar_usuario(cls, email, senha):
        session = retorna_session()        
        usuario = session.query(Usuario).filter_by(email=email).first()
        
        if usuario:
            senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            if senha_hash == usuario.senha:
                session.close()
                print('-'*30)
                print('Logado com sucesso.')
                print('-'*30)
                return {'Login': True, 'id': usuario.id}
            else: 
                session.close()
                return 'Senha incorreta.'
        else:
            session.close()
            return 'Email incorreto.'