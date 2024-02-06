import json
from typing import List

from Note import Note
class Notes:
    def __init__(self, file_fath):
        self.__filepath__ = file_fath
        self.__Notes__ = []
    def add_notes(self, note : Note):
        self.__Notes__.append(note)
    def init_notes(self):
        with open(self.__filepath__) as f:
            self.__Notes__ = NotesConvert.jsonToList(f)

    def printNotes(self):
        for i in range(len(self.__Notes__)):
            print(f'Заметка №{i +1}')
            print(self.__Notes__[i])

    def saveNotes(self):
        
        with open(self.__filepath__, mode='w') as f:
            to_json = NotesConvert.toJson(self.__Notes__)
            json.dump(to_json, f)
    def remove(self, index:int):
        self.__Notes__.pop(index)
    def __iter__(self):
        return notesIterator(self.__Notes__)

class NotesConvert:
    def toJson(notes : List[type(Note)]) -> List[type(Note)]:
        to_json = []
        for o in notes:
            note = {'title': o.get_name(), 'text': o.get_text(), 'date': o.getDate()}
            to_json.append(note)
        
        return to_json
    def jsonToList(f):
        notes = []
        json_notes = json.load(f)
        for note in json_notes:
            title = note['title']
            text = note['text']
            date = note['date']
            notes.append(Note(title, text, date))
        return notes.copy()
class notesIterator():
    def __init__(self, notes: List[type(Note)]) -> None:
        self.index = 0
        self.notes = notes
        self.len = len(notes)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < self.len:
            self.index += 1
            return self.notes[self.index - 1]
        else: raise StopIteration

        
    
    