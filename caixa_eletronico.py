import tkinter as tk
from tkinter import messagebox

# Dados do usuário fictício
USUARIO = "cliente"
SENHA = "1234"
saldo = 0.0

# Janela principal do caixa eletrônico
def criar_janela_principal():
    def atualizar_saldo():
        lbl_saldo.config(text=f"Saldo atual: R$ {saldo:.2f}")

    def depositar():
        global saldo
        try:
            valor = float(entry_valor.get())
            if valor > 0:
                saldo += valor
                messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado.")
                atualizar_saldo()
            else:
                messagebox.showwarning("Erro", "Informe um valor positivo.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido.")

    def sacar():
        global saldo
        try:
            valor = float(entry_valor.get())
            if valor <= 0:
                messagebox.showwarning("Erro", "Informe um valor positivo.")
            elif valor > saldo:
                messagebox.showwarning("Erro", "Saldo insuficiente.")
            else:
                saldo -= valor
                messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado.")
                atualizar_saldo()
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido.")

    janela = tk.Tk()
    janela.title("Caixa Eletrônico")
    janela.geometry("300x250")

    lbl_saldo = tk.Label(janela, text=f"Saldo atual: R$ {saldo:.2f}", font=("Arial", 12))
    lbl_saldo.pack(pady=10)

    tk.Label(janela, text="Valor (R$):").pack()
    entry_valor = tk.Entry(janela)
    entry_valor.pack(pady=5)

    tk.Button(janela, text="Depositar", width=15, command=depositar).pack(pady=5)
    tk.Button(janela, text="Sacar", width=15, command=sacar).pack(pady=5)

    janela.mainloop()

# Tela de login
def criar_tela_login():
    def verificar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if usuario == USUARIO and senha == SENHA:
            login.destroy()
            criar_janela_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    login = tk.Tk()
    login.title("Login")
    login.geometry("250x180")

    tk.Label(login, text="Usuário:").pack()
    entry_usuario = tk.Entry(login)
    entry_usuario.pack()

    tk.Label(login, text="Senha:").pack()
    entry_senha = tk.Entry(login, show="*")
    entry_senha.pack()

    tk.Button(login, text="Entrar", command=verificar_login).pack(pady=10)

    login.mainloop()

# Início do programa
criar_tela_login()
