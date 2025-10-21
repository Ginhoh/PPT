import customtkinter as ctk 
import random
ctk.set_appearance_mode('dark')
def game(op):
    machine = ['pedra', 'papel', 'tesoura']
    bot = random.choice(machine)
    andamento.configure(text=f'O computador escolheu: {bot}')

    if op == bot:
        resultado.configure(text=f'Empate!', text_color='yellow')
    if op == 'pedra':
        if bot == 'tesoura':
            resultado.configure(text=f'Você ganhou!', text_color='green')
    elif op == 'papel':
        if bot == 'pedra':
            resultado.configure(text=f'Você ganhou!', text_color='green')
    elif op == 'tesoura':
        if bot == 'papel':
            resultado.configure(text=f'Você ganhou!', text_color='green')
    else:
        resultado.configure(text=f'Você perdeu!', text_color='red')


app = ctk.CTk()
app.title('Pedra, Papel e Tesoura')
app.geometry('400x300')
select = ctk.CTkRadioButton(app, text='Escolha sua jogada:', value='jknjnnj')
select.pack(pady=10)
up = ctk.CTkRadioButton(app, text='jknjnnj:', value='jknjnnj')
up.pack(pady=10)
pedra = ctk.CTkButton(app, text='Pedra', command=game)
pedra.pack(pady=5)

papel = ctk.CTkButton(app, text='Papel', command=game)
papel.pack(pady=5)

tesoura = ctk.CTkButton(app, text='Tesoura', command=game)
tesoura.pack(pady=5)
andamento = ctk.CTkLabel(app, text='')
andamento.pack(pady=20)

resultado = ctk.CTkLabel(app, text='')
resultado.pack(pady=10)


app.mainloop()
