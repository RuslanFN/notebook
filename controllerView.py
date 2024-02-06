from tkinter import *
from tkinter import ttk
from typing import List
from Note import Note
from ViewNote import ViewNote
from Notes import Notes

class controllerView:
    def createView(self, notes: type(Notes), f_add, f_del) -> type(Tk):
        root = Tk()
        
        root.geometry("350x550")
        root.resizable(False, False)
        rootFrame = Frame(root)
        menu = Menu()
        menu.add_command(label='Добавить', command=f_add)
        root.config(menu=menu)
        index = 0

        for note in notes:
            print(type(note))
            frame = ViewNote.create_note(note.get_name(), note.get_text(), note.getDate(), rootFrame)
            frame.pack(fill=X, pady=5, padx=5)
            
            btn = Button(rootFrame, text=f'Удалить', command=lambda index = index :f_del(index))
            
            index += 1
            btn.pack()
        rootFrame.pack(expand=True, fill=BOTH, ipady=100)
        return root
    def note_form(self, title_note='', text=''):
        def onm(event):
            text_var.set(text_note.get(0.0, END))
            title_var.set(title_entry.get() )
        title_var = StringVar()
        text_var = StringVar()
        
        form = Tk()
        form.resizable(False, False)
        label1 = Label(form, text='Название')
        title_entry = Entry(form, textvariable=title_var)
        label2 = Label(form, text='Текст')
        text_note = Text(form, wrap=CHAR, width=50, height=7)
        btn = Button(form, text='Сохранить', command=form.destroy)
        #title_entry.insert(0, title_note)
        text_note.insert(0.0, text)
        text_note.bind('<KeyRelease>', onm)
        label1.pack(anchor=W)
        title_entry.pack(anchor=W)
        label2.pack(anchor=W)
        text_note.pack()
        btn.pack(anchor=SE)
        form.wait_window()
        
        return {'title':title_var.get(), 'text':text_var.get()}
    

    


