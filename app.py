import customtkinter as ctk 
import random
ctk.set_appearance_mode('dark')

def pedra():
    machine = ['pedra', 'papel', 'tesoura']
    bot = random.choice(machine)
    op = 'pedra'
    andamento.configure(text=f'Sua escolha: {op}\nO computador escolheu: {bot}')
    if op == bot:
        resultado.configure(text=f'Empate!', text_color='yellow')
    elif bot == 'tesoura':
        resultado.configure(text=f'Você ganhou!', text_color='green')
    elif bot == 'papel':
        resultado.configure(text=f'Você perdeu!', text_color='red')

def papel():
    machine = ['pedra', 'papel', 'tesoura']
    bot = random.choice(machine)
    op = 'papel'
    andamento.configure(text=f'Sua escolha: {op}\nO computador escolheu: {bot}')
    if op == bot:
        resultado.configure(text=f'Empate!', text_color='yellow')
    elif bot == 'pedra':
        resultado.configure(text=f'Você ganhou!', text_color='green')
    elif bot == 'tesoura':
        resultado.configure(text=f'Você perdeu!', text_color='red')

def tesoura():
    machine = ['pedra', 'papel', 'tesoura']
    bot = random.choice(machine)
    op = 'tesoura'
    andamento.configure(text=f'Sua escolha: {op}\nO computador escolheu: {bot}')
    if op == bot:
        resultado.configure(text=f'Empate!', text_color='yellow')
    elif bot == 'papel':
        resultado.configure(text=f'Você ganhou!', text_color='green')
    elif bot == 'pedra':
        resultado.configure(text=f'Você perdeu!', text_color='red')

app = ctk.CTk()
app.title('Pedra, Papel e Tesoura')
app.geometry('400x300')

inicio = ctk.CTkLabel(app, text='Clique em um botão para escolher, e jogar. Boa sorte!')
inicio.pack(pady=10)

pedra = ctk.CTkButton(app, text='Pedra', command=pedra)
pedra.pack(pady=5)

papel = ctk.CTkButton(app, text='Papel', command=papel)
papel.pack(pady=5)

tesoura = ctk.CTkButton(app, text='Tesoura', command=tesoura)
tesoura.pack(pady=5)
andamento = ctk.CTkLabel(app, text='', justify='left')
andamento.pack(pady=20, anchor='w')

resultado = ctk.CTkLabel(app, text='')
resultado.pack(pady=10)

app.mainloop()
