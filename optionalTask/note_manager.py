import os.path
import pandas as pd
from note import Note

class NoteManager():

    def __init__(self, filename):
        assert os.path.isfile(filename), "File doesn`t exist"
        self.filename = filename
        self.notes = pd.read_csv(filename)

    def addNote(self, new_note: Note):
        df = pd.DataFrame({
            'film': [new_note.film_name],
            'note': [new_note.note],
            'rating': [new_note.rating]
        })
        df.to_csv(self.filename, mode='a', index = False, header = False)
        self.notes = pd.read_csv(self.filename)

    def deleteNote(self, filmname):
        self.notes.drop(self.notes.index[(self.notes['film_name'] == filmname)],axis = 0, inplace = True)
        self.notes.to_csv(self.filename, mode='w', index = False, header = True)

    def readNotes(self):
        print(self.notes.to_string())

    def getHighRated(self):
        print(self.notes[self.notes.rating == self.notes.rating.max()])

    def getLowRated(self):
        print(self.notes[self.notes.rating == self.notes.rating.min()])

    def getAvRating(self):
        avrate = self.notes['rating'].mean()
        print(f'Average rating of films is {avrate : .2f}')

    def __getitem__(self, sliced):
        return self.notes.iloc[sliced].to_string()

    def __repr__(self):
        return self.notes.to_string()