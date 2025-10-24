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
        #pontos.configure(text=f'XP: {xp}')
    elif bot == 'papel':
        resultado.configure(text=f'Você perdeu!', text_color='red')
        #pontos.configure(text=f'XP: {xp-1}')

def papel():
    machine = ['pedra', 'papel', 'tesoura']
    bot = random.choice(machine)
    op = 'papel'
    andamento.configure(text=f'Sua escolha: {op}\nO computador escolheu: {bot}')
    if op == bot:
        resultado.configure(text=f'Empate!', text_color='yellow')
    elif bot == 'pedra':
        resultado.configure(text=f'Você ganhou!', text_color='green')
        #pontos.configure(text=f'XP: {xp+1}')
    elif bot == 'tesoura':
        resultado.configure(text=f'Você perdeu!', text_color='red')
        #pontos.configure(text=f'XP: {xp-1}')

def tesoura():
    while True:
        machine = ['pedra', 'papel', 'tesoura']
        bot = random.choice(machine)
        op = 'tesoura'
        andamento.configure(text=f'Sua escolha: {op}\nO computador escolheu: {bot}')
        if op == bot:
            resultado.configure(text=f'Empate!', text_color='yellow')
            break
        elif bot == 'papel':
            resultado.configure(text=f'Você ganhou!', text_color='green')
            #pontos.configure(text=f'XP: {xp+1}')
            break
        elif bot == 'pedra':
            resultado.configure(text=f'Você perdeu!', text_color='red')
            #pontos.configure(text=f'XP: {xp-1}')
            break

app = ctk.CTk()
app.title('Pedra, Papel e Tesoura')
app.geometry('400x400')

inicio = ctk.CTkLabel(app, text='Clique em um botão para escolher, e jogar. Boa sorte!', font=('Arial', 14)) #para mudar a fonte, coloca o tipo e depois o tamanho
inicio.pack(pady=10)

pedra = ctk.CTkButton(app, text='Pedra', command=pedra, fg_color='darkred', hover_color='red')
pedra.pack(pady=20)

papel = ctk.CTkButton(app, text='Papel', command=papel,fg_color='darkred',hover_color='red')
papel.pack(pady=20)

tesoura = ctk.CTkButton(app, text='Tesoura', command=tesoura,fg_color='darkred',hover_color='red')
tesoura.pack(pady=20)
andamento = ctk.CTkLabel(app, text='', justify='center', font=('Arial', 14))
andamento.pack(pady=20, anchor='center')

resultado = ctk.CTkLabel(app, text='')
resultado.pack(pady=10)

'''
xp = 0
pontos = ctk.CTkLabel(app, text=f'XP: {xp}', justify='left', font=('Arial', 16))
pontos.pack(padx=40, anchor='e')
'''
app.mainloop()
