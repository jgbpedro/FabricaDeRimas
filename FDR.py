from tkinter import *

janela = Tk()

janela.title("Fabrica de Rimas")
janela["bg"] = "#FFFFFF"
janela.geometry("500x650+100+100")

icon = PhotoImage(file='mic.png')
janela.tk.call('wm', 'iconphoto', janela._w, icon)

lbl1 = Label(janela, text="Digite o final da palavra:")
ent1 = Entry(janela, width=100)
listbox = Listbox(janela)


def rimar():
        CX = ent1.get()
        file = open("palavras.txt", "r")
        palavra = CX.upper()+"\n"

        listbox.delete(0, END)

        for line in file:

            if (line.endswith(palavra) == True):
                print(line)

                listbox.insert(END, line)


        file.close()

bt1= Button(janela, text="Rimar", command=rimar)

lbl1.pack(side=TOP, anchor=W)
ent1.pack(side=TOP, anchor=E)
bt1.pack(side=TOP, anchor=E)
listbox.pack(side=TOP, fill=BOTH, expand=1)

janela.mainloop()

