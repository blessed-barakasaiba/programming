import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 1)
class NoteGridLayout(GridLayout):
    pass

class NotesApp(App):
    def build(self):
        return NoteGridLayout()
NoteApp = NotesApp()
NoteApp.run()   
    
