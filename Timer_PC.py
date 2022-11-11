import os
from tkinter import *

def janela_Principal():
    janela = Tk()

    janela.title('Timer for PC')
    
    #Configurar tamanho, dimensão e centralização da janela
    largura = 350
    altura = 200
    
    largura_principal = janela.winfo_screenwidth()
    altura_principal = janela.winfo_screenheight()
    posx = largura_principal/2 - (largura/2)
    posy = altura_principal/2 - (altura/2)
    
    janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    
    
    cabecalho = Label(janela, text="Programe seu PC para desligar sozinho!")
    cabecalho.grid(column=0, row=0, padx=10, pady=10)
    
    botao_timer = Button(janela, text='Timer', command=janela_Timer,width=30,fg='black', bg='#FFA033')
    botao_timer.grid(column=0, row=1,padx=3,pady=3)
    
    botao_cancelarTimer = Button(janela, text='Cancelar Timer', command=Cancelar,width=30,fg='black', bg='#FFA033')
    botao_cancelarTimer.grid(column=0, row=2,padx=3,pady=3)
    
    botao_sair = Button(janela, text='Sair', command=janela.destroy,width=30,fg='black', bg='#FFA033')
    botao_sair.grid(column=0, row=3, pady=3,padx=3)       
    
    janela.mainloop()
    
    
def janela_Timer():
    janela2 = Toplevel()
    janela2.title('Configuração do Timer')
    
    label_timer = Label(janela2, text="Digite o valor em segundos para o PC desligar:")
    label_timer.grid(column=0, row=0, padx=5, pady=5)    
    
    global timer
    timer = Entry(janela2, width=10)
    timer.grid(column=0, row=1, padx=10, pady=10)    
    
    botao_confirmar = Button(janela2, text='Confirmar', command = Timer, width=20,fg='black', bg='#FFA033')
    botao_confirmar.grid(column=0, row=2,padx=3,pady=3)
    
    botao_fechar = Button(janela2, text='Fechar', command = janela2.destroy,width=20,fg='black', bg='#FFA033')
    botao_fechar.grid(column=0, row=3,padx=3,pady=3)
    
def Timer():
    x = timer.get()
    y = int(x)*3600
    strOne = "shutdown /s /t "
    strTwo = str(y)
    strx = strOne + strTwo
        
    os.system(strx)
    
    
def Cancelar():
    strThree = "shutdown -a"
    cancelar = strThree
    
    os.system(cancelar)
    print('Timer cancelado com sucesso!')

janela_Principal()
