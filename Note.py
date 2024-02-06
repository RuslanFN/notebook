from datetime import datetime  
class Note:
    def __init__(self, title, text, date = datetime.now().isoformat()):
        self.__title__ = title
        self.__text__ = text
        self.__date__ = date
    def get_name(self):
        return self.__title__
    def get_text(self):
        return self.__text__
    def getDate(self):
        return self.__date__
    def __iter__(self):
        return NoteIterator(self)
    def __str__(self) -> str:
        s = f'{self.get_name()} \n{self.get_text()} \n{self.getDate()}'
        return s
        
class NoteIterator:
    def __init__(self, note:Note) -> None:
        self.index = 1
        self.Note = note
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 1:
            return self.Note.get_name()
        elif self.index == 2:
            return self.Note.get_text()
        elif self.index == 3:
            return self.Note.getDate()
        else: raise StopIteration
    
    
    