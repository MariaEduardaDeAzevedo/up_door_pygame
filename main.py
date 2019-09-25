from tkinter import *
import pygame
import random
import game
from tkinter import ttk

pygame.init()

menu = Tk()
#menu.geometry('500x500')
menu.title('UP DOOR!')

menu['bg'] = 'cyan'

im_sign_r = PhotoImage(file='placa_dir.png')

pers_ic = Label(menu, font='Impact 30', image=im_sign_r, fg='orange', bg='red')
pers_ic.grid(row=9, column=0, ipadx=230)
opt = {'comandos': 1, 'volume': 1}

def pers_lisa():
    global pers
    pers_ic['image'] = lisa
    pers = 1

def pers_will():
    global pers
    pers_ic['image'] = will
    pers = 2
    
def pers_louis():
    global pers
    pers_ic['image'] = louis
    pers = 3

def pers_tom():
    global pers
    pers_ic['image'] = tom
    pers = 4
    
def pers_zombie():
    global pers
    pers_ic['image'] = zombie
    pers = 5

def start():
    global pers
    global nick
    game.game(pers, opt, str(nick.get()))

def about():
    info = Tk()
    info.title('SOBRE')
    infos = Message(info)
    infos['text'] = '''
UP DOOR! é um jogo de plataforma desenvolvido por Maria Eduarda de Azevedo Silva, aluna do curso de Ciências da Computação na Universidade Federal de Campina Grande (UFCG). 

O desenvolvimento deste jogo se deu a partir de um projeto das disciplinas de Programação I e Lab. de Programação I. O projeto foi feito utilizando a linguagem Python(3.7.2)
com a framework Pygame e a biblioteca de GUI Tkinter.

Professores da Disciplina:

+ Dalton Serey
+ Jorge Abrantes
+ Wilkerson Andrade

As imagens, sons e músicas utilizadas neste jogo estão em domínio livre para uso nos seguintes sites:

https://kenney.nl
https://soundimage.org

'''
    infos.grid(row=0, column=0)

    info.mainloop()

def how_to_play():
    how = Tk()
    how.title('INSTRUÇÕES')
    how['bg'] = 'cyan'

    lab_inst = Label(how, font='Impact 15', fg='black',bg='cyan')
    lab_inst['text'] = '''
UP DOOR! é um jogo de plataforma de jogabilidade simples. O objetivo principal do game é pegar a quantidade
necessária de itens no cenário pra abrir a porta que se encontra no canto superior direito do mapa e avançar
para a próxima etapa.

COMANDOS E CONTROLE: 
Por padrão, para movimentar o personagem são utilizadas as teclas UP, RIGHT e LEFT, porém é possível alterar
tal padrão no botão OPÇÕES, encontrado no menu principal do jogo.
Para pausar pressione a tecla P e para sair da tela do jogo use a tecla ESC.

DANOS:
Você levará dano no jogo caso caia de alturas muito elevadas ou acerte um espinho.
IMPORTANTE: Espinhos fazem você voltar para a posição inicial do nível!
Quando você leva um dano, perde uma das suas 3 vidas!

PONTOS E PROGRESSO:
Para somar pontos é importante que você pegue o máximo de moedas possíveis! Chaves não somam nada à pontuação,
mas são necessárias para abrir as portas.
Para salvar o seu progresso de nível é preciso que você pressione o botão azul encontrado no mapa.
Se você morrer e ele estiver pressionado, você voltará para o mesmo nível e irá recuperar 60% da sua pontuação.
Caso contrário, você retornará para o Nível 1 com pontuação igual a 0.

'''
    lab_inst.grid(row=0, column=0, sticky=W)

    how.mainloop()


pers = None
commands = None
opt_vol = 'VOLUME'
opt_com = 'COMANDOS'
def options():
    def save(x):
        global opt
        global opt_vol
        global opt_com
        if x in val_com.keys():
            opt['comandos'] = val_com[x]
            opt_com = x
        elif x in val_vol.keys():
            opt['volume'] = val_vol[x]
            opt_vol = x
            
    option = Tk()
    option.title('OPÇÕES')
    option['bg'] = 'cyan'

    #comandos
    val_com = {'UP, LEFT, RIGHT (padrão)': 1, 'W, A, D (canhoto)': 2, 'SPACE, LEFT, RIGHT': 3, 'SPACE, A, S': 4}
    com_var = StringVar(option)
    com_var.set(opt_com)
    com_opt = OptionMenu(option, com_var, *val_com.keys(), command=save)
    com_opt['bg'] = 'purple'
    com_opt['width'] = 25
    com_opt['font'] = 'Impact 15'
    com_opt['fg'] = 'orange'
    com_opt['relief'] = FLAT
    com_opt.grid(row=0, column=0, sticky=N+S)

    #volume 
    val_vol = {'MUDO': 0, '10%': 0.1, '20%': 0.2, '30%': 0.3, '40%': 0.4, '50%': 0.5, '60%':0.6, '70%': 0.7, '80%': 0.8, '90%': 0.9, '100%': 1}
    vol_var = StringVar(option)
    vol_var.set(opt_vol)
    vol_opt = OptionMenu(option, vol_var, *val_vol.keys(), command=save)
    vol_opt['bg'] = 'purple'
    vol_opt['font'] = 'Impact 15'
    vol_opt['fg'] = 'orange'
    vol_opt['relief'] = FLAT
    vol_opt['width'] = 25
    vol_opt.grid(row=1, column=0, sticky=N+S)

    #LABEL
    to_save = Label(option, text='Para salvar suas alterações feche esta janela', font='Impact 15', fg='purple', bg='cyan')
    to_save.grid(row=2, column=0)

    option.mainloop()
    
def ranking():
    def bubble(l1, l2):
        status = False
        while not status:
            status = True
            for i in range(len(l1) - 1):
                if l1[i] < l1[i + 1]:
                    l1[i], l1[i + 1] = l1[i + 1], l1[i]
                    l2[i], l2[i + 1] = l2[i + 1], l2[i]
                    status = False
        
    rank = Tk()
    rank.geometry('300x300')
    rank.title('RANKING')
    rank['bg'] = 'cyan'
    
    file = open('ranking.txt', 'r')
    pnts = list()
    names = list()
    for e in file.readlines():
        player = e.split(' - ')
        pnts.append(player[1])
        names.append(player[0])

    bubble(pnts, names)

    lab_rank = Label(rank, font='Impact 18', fg = 'black', bg = 'cyan')
    rank_list = ''
    for i in range(len(names)):
        plr = f'{i+1}°. {names[i]} - {pnts[i]}\n'
        rank_list += plr 
        
    lab_rank['text'] = rank_list

    lab_rank.grid(row=0, column=0, sticky = N+S)

    file.close()
    
    rank.mainloop()
   
#Imagens
block = PhotoImage(file='grass.png')
logo = PhotoImage(file='logo.png')
door = PhotoImage(file='door.png')
door_top = PhotoImage(file='door_top.png')
lisa = PhotoImage(file='lisa_parada_1.png')
will = PhotoImage(file='will_parada_1.png')
louis = PhotoImage(file='louis_parada_1.png')
tom = PhotoImage(file='tom_parada_1.png')
zombie = PhotoImage(file='zombie_parada_1.png')
choice = PhotoImage(file='txt_escolha_red.png')
nick = PhotoImage(file='txt_nick.png')
im_play = PhotoImage(file='txt_jogar.png')
pers_ic['image'] = lisa
#Image logo
label_logo = Label(menu, image=logo, bg = 'cyan')
label_logo.grid(row=1, column=0, sticky = W+E+N+S)
#Composição do Cenário do Menu
label_choice = Label(menu, image=choice, bg='cyan')
label_choice.grid(row=2, column=1, sticky=W)
#Botões
but_lisa = Button(menu, image=lisa, width = 50, height = 50, command=pers_lisa, bg = 'purple', relief=FLAT)
but_lisa.grid(row=3, column=1, ipadx=200)
but_will = Button(menu, image=will, width = 50, height = 50, command=pers_will, bg = 'grey', relief=FLAT)
but_will.grid(row=4, column=1, ipadx=200)
but_louis = Button(menu, image=louis, width = 50, height = 50, command=pers_louis, bg = 'yellow', relief=FLAT)
but_louis.grid(row=5, column=1, ipadx=200)
but_tom = Button(menu, image=tom, width = 50, height = 50, command=pers_tom, bg = 'green', relief=FLAT)
but_tom.grid(row=6, column=1, ipadx=200)
but_zombie = Button(menu, image=zombie, width = 50, height = 50, command=pers_zombie, bg = 'blue', relief=FLAT)
but_zombie.grid(row=7, column=1, ipadx=200)
but_play = Button(menu, text='JOGAR', width=10, bg='green', command=start, font = 'Impact 18', fg='#ffbd4a', relief=FLAT)
but_play.grid(row=3, column=0, ipadx=200)
but_how = Button(menu, text='INSTRUÇÕES', width = 10, bg='white', font = 'Impact 18', fg='#ffbd4a', command=how_to_play, relief=FLAT)
but_how.grid(row=4, column=0, ipadx=200)
but_about = Button(menu, text='SOBRE', bg='blue', command = about, width=10, font = 'Impact 18', fg='#ffbd4a', relief=FLAT)
but_about.grid(row=5, column=0, ipadx=200)
but_about = Button(menu, text='OPÇÕES', bg='purple', command = options, width=10, font = 'Impact 18', fg='#ffbd4a', relief=FLAT)
but_about.grid(row=6, column=0, ipadx=200)
but_ranking = Button(menu, text = 'RANKING', font='Impact 18', bg = 'orange', fg = 'cyan', width=10, relief = FLAT, command = ranking)
but_ranking.grid(row=9, column=1, ipadx=200)

#Entradas
nick =Entry(menu, font='Impact 15', width=7,bg='red')
nick.grid(row=8, column=0, ipadx=85, sticky=S+E)
lab_nick = Label(menu, text='NICKNAME:', font='Impact 15', bg='red', fg='orange')
lab_nick.grid(row=8, column=0, sticky=S+W, ipadx=100)
menu.mainloop()
