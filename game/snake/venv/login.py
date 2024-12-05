import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.logger import Logger


      
class LoginApp(App):
    def build(self):
        
        main_layout = BoxLayout(orientation ='vertical')
        self.username_label = Label(text="username: ")
        main_layout.add_widget(self.username_label)
        self.username_input = TextInput()
        main_layout.add_widget(self.username_input)
        
       
       
        
       
    
    
    
            

    
if __name__ == "__main__":
    
    LoginApp().run()
    
        
     