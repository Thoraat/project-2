# Importing necessary libraries
import kivy
from kivy.app import App
from kivy.uix.label import Label

# Define the app class
class HelloWorldApp(App):
    def build(self):
        # Creating a label widget with "Hello, World!" text
        label = Label(text="Hello, World!")
        return label

# Running the app
if __name__ == '__main__':
    HelloWorldApp().run()

