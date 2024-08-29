import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controller import ControllerCadastro, ControllerLogin

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("400x300")
        self.style = ttk.Style()
        self.set_dark_mode()
        self.root.configure(bg='#2e2e2e')  # Configura o fundo da janela principal
        self.main_frame = ttk.Frame(self.root, padding="20", style='TFrame')
        self.main_frame.grid(row=0, column=0, sticky="nsew")  # Usar grid para centralizar
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def set_dark_mode(self):
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#2e2e2e')
        self.style.configure('TLabel', background='#2e2e2e', foreground='#ffffff')
        self.style.configure('TButton', background='#444444', foreground='#ffffff')
        self.style.map('TButton', background=[('active', '#666666')])

    def create_widgets(self):
        self.clear_frame()
        inner_frame = ttk.Frame(self.main_frame, style='TFrame')
        inner_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

        content_frame = ttk.Frame(inner_frame, style='TFrame')
        content_frame.grid(row=0, column=0)

        self.title_label = ttk.Label(content_frame, text="------ LOGIN ------", font=("Helvetica", 16), style='TLabel')
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.login_button = ttk.Button(content_frame, text="Logar", command=self.show_login, style='TButton')
        self.login_button.grid(row=1, column=0, padx=10, pady=10)

        self.register_button = ttk.Button(content_frame, text="Cadastrar", command=self.show_register, style='TButton')
        self.register_button.grid(row=1, column=1, padx=10, pady=10)

        self.exit_button = ttk.Button(content_frame, text="Sair", command=self.root.quit, style='TButton')
        self.exit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_login(self):
        self.clear_frame()
        inner_frame = ttk.Frame(self.main_frame, style='TFrame')
        inner_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

        content_frame = ttk.Frame(inner_frame, style='TFrame')
        content_frame.grid(row=0, column=0)

        self.title_label = ttk.Label(content_frame, text="Login", font=("Helvetica", 16), style='TLabel')
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.email_label = ttk.Label(content_frame, text="Email:", style='TLabel')
        self.email_label.grid(row=1, column=0, pady=5)
        self.email_entry = ttk.Entry(content_frame)
        self.email_entry.grid(row=1, column=1, pady=5)

        self.password_label = ttk.Label(content_frame, text="Senha:", style='TLabel')
        self.password_label.grid(row=2, column=0, pady=5)
        self.password_entry = ttk.Entry(content_frame, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)
        self.password_entry.bind("<Return>", lambda event: self.login())  # Bind Enter key to login

        self.login_button = ttk.Button(content_frame, text="Logar", command=self.login, style='TButton')
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.back_button = ttk.Button(content_frame, text="Voltar", command=self.create_widgets, style='TButton')
        self.back_button.grid(row=4, column=0, columnspan=2, pady=10)

    def show_register(self):
        self.clear_frame()
        inner_frame = ttk.Frame(self.main_frame, style='TFrame')
        inner_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

        content_frame = ttk.Frame(inner_frame, style='TFrame')
        content_frame.grid(row=0, column=0)

        self.title_label = ttk.Label(content_frame, text="Cadastro", font=("Helvetica", 16), style='TLabel')
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = ttk.Label(content_frame, text="Nome:", style='TLabel')
        self.name_label.grid(row=1, column=0, pady=5)
        self.name_entry = ttk.Entry(content_frame)
        self.name_entry.grid(row=1, column=1, pady=5)

        self.email_label = ttk.Label(content_frame, text="Email:", style='TLabel')
        self.email_label.grid(row=2, column=0, pady=5)
        self.email_entry = ttk.Entry(content_frame)
        self.email_entry.grid(row=2, column=1, pady=5)

        self.password_label = ttk.Label(content_frame, text="Senha:", style='TLabel')
        self.password_label.grid(row=3, column=0, pady=5)
        self.password_entry = ttk.Entry(content_frame, show="*")
        self.password_entry.grid(row=3, column=1, pady=5)
        self.password_entry.bind("<Return>", lambda event: self.register())  # Bind Enter key to register

        self.register_button = ttk.Button(content_frame, text="Cadastrar", command=self.register, style='TButton')
        self.register_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.back_button = ttk.Button(content_frame, text="Voltar", command=self.create_widgets, style='TButton')
        self.back_button.grid(row=5, column=0, columnspan=2, pady=10)

    def show_logged_in(self):
        self.clear_frame()
        inner_frame = ttk.Frame(self.main_frame, style='TFrame')
        inner_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

        content_frame = ttk.Frame(inner_frame, style='TFrame')
        content_frame.grid(row=0, column=0)

        self.title_label = ttk.Label(content_frame, text="Logado", font=("Helvetica", 16), style='TLabel')
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.back_button = ttk.Button(content_frame, text="Voltar para tela inicial", command=self.create_widgets, style='TButton')
        self.back_button.grid(row=1, column=0, columnspan=2, pady=10)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def login(self):
        email = self.email_entry.get()
        senha = self.password_entry.get()
        retorno = ControllerLogin.logar_usuario(email, senha)
        if isinstance(retorno, dict) and retorno.get('Login'):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.show_logged_in()
        else:
            messagebox.showerror("Erro", retorno)

    def register(self):
        nome = self.name_entry.get()
        email = self.email_entry.get()
        senha = self.password_entry.get()
        retorno = ControllerCadastro.cadastrar_usuario(nome, email, senha)
        if retorno == 1:
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.create_widgets()  # Voltar para a tela inicial após o cadastro
        else:
            messagebox.showerror("Erro", retorno)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()