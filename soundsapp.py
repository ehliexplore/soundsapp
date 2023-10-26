from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class SoundApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create buttons
        button1 = Button(text='Play Sound 1')
        button2 = Button(text='Play Sound 2')

        # Bind the buttons to their respective functions
        button1.bind(on_release=self.play_sound1)
        button2.bind(on_release=self.play_sound2)

        # Add the buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout
    
    
    def play_sound1(self, instance):
        sound = SoundLoader.load('sound1.mp3')
        if sound:
            sound.play()
    

    def play_sound2(self, instance):
        sound = SoundLoader.load('sound2.mp3')
        if sound:
            sound.play()


if __name__ == '__main__':
    SoundApp().run()