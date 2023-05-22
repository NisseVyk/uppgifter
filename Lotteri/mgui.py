from tkinter import *
from tkinter import messagebox
import lotteri

#create root window
root = Tk()
root.title("Lotteri")

listbox = Listbox(root,
                  width = 30,
                  bg="white",
                  activestyle="dotbox",
                  font="Helvetica",
                  fg="blue"
                  )

root.geometry("380x300")

lotteriet = lotteri.Lotteri()

#create label
label_antal = Label(root, text="Antal lotter, max 3st: ")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

#create text field
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def clickSlumpButton():
    print("Tryck!")

#create button
button_slumpa = Button(text="TURKNAPP", command=clickSlumpButton)
button_slumpa.grid(row=2, column=0, sticky=E, padx=15, pady=15)



root.mainloop()