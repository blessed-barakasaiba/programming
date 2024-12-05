from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

# Define your Screen for the Notepad
class NotepadScreen(Screen):
    pass

class NotepadApp(MDApp):
    def build(self):
        # Set window size for desktop use
        Window.size = (400, 600)

        # Load the KV file
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("notepad.kv")

    def save_note(self):
        """Save the current text to a file."""
        note_text = self.root.ids.text_input.text
        try:
            with open("saved_note.txt", "w") as f:
                f.write(note_text)
            self.show_snackbar("Note saved successfully!")
        except Exception as e:
            self.show_snackbar(f"Error saving note: {str(e)}")

    def load_note(self):
        """Load the note from the file."""
        try:
            with open("saved_note.txt", "r") as f:
                note_text = f.read()
            self.root.ids.text_input.text = note_text
            self.show_snackbar("Note loaded successfully!")
        except FileNotFoundError:
            self.show_snackbar("No saved note found!")
        except Exception as e:
            self.show_snackbar(f"Error loading note: {str(e)}")

    def clear_note(self):
        """Clear the text input."""
        self.root.ids.text_input.text = ""
        self.show_snackbar("Text cleared!")

    def show_snackbar(self, message):
        """Display a simple Snackbar with a message."""
        from kivymd.uix.snackbar import Snackbar
        Snackbar(text=message).open()

    def menu_callback(self):
        """Callback for menu button (can add more functionality)."""
        self.show_snackbar("Menu clicked!")

    def show_info(self):
        """Show information about the app."""
        self.show_snackbar("Notepad App v1.0")

# Run the app
if __name__ == "__main__":
    NotepadApp().run()
