from Notes import Notes
from Note import Note
from controllerView import controllerView
class controller():
    def __init__(self) -> None:
        self.notes = Notes('notes.json')
        self.notes.init_notes()
        self.controller = controllerView()
        self.root = self.controller.createView(self.notes, f_add=self.add_notes, f_del=self.remove_note)
        
    def start_menu(self):  
        self.root.mainloop()
        
        
    def printNotes(self):
        self.notes.printNotes()
     
    def add_notes(self):
        form = controllerView.note_form('', '')
        title = form['title']
        text = form['text']
        self.notes.add_notes(Note(title, text))
        self.notes.saveNotes()
        self.root.destroy()
        self.root = self.controller.createView(self.notes, f_add=self.add_notes, f_del=self.remove_note)
    def remove_note(self, index):
        print(index)
        self.notes.remove(index)
        self.notes.saveNotes()
        
        self.root.destroy()
        self.root = self.controller.createView(self.notes, f_add=self.add_notes, f_del=self.remove_note)
    def interface(self):
        while True:
            cmnd = input()
            if cmnd == '1':
                self.printNotes()
                self.start_menu()
            elif cmnd == "2":
                self.add_notes()
                self.start_menu()
            elif cmnd == "3":
                self.remove_note()
                self.start_menu()
            else:
                break


        

    
