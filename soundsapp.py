from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.core.window import Window

class SoundApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create buttons
        button_kick = Button(text='Kick')
        button_snare = Button(text='Snare')
        button_hihat = Button(text='HiHat')
        button_clap = Button(text='Clap')

        # Bind the buttons to their respective functions
        button_kick.bind(on_release=self.play_kick)
        button_snare.bind(on_release=self.play_snare)
        button_hihat.bind(on_release=self.play_hihat)
        button_clap.bind(on_release=self.play_clap)

        # Add the buttons to the layout
        layout.add_widget(button_kick)
        layout.add_widget(button_snare)
        layout.add_widget(button_hihat)
        layout.add_widget(button_clap)

        # Bind keyboard keys to button actions
        Window.bind(on_key_down=self.on_key_down)

        return layout
    
    
    def play_kick(self, instance):
        sound = SoundLoader.load('kick.wav')
        if sound:
            sound.play()
    
    def play_snare(self, instance):
        sound = SoundLoader.load('snare.wav')
        if sound:
            sound.play()

    def play_hihat(self, instance):
        sound = SoundLoader.load('hihat.wav')
        if sound:
            sound.play()
    
    def play_clap(self, instance):
        sound = SoundLoader.load('clap.wav')
        if sound:
            sound.play()

    def on_key_down(self, keyboard, keycode, text, modifiers, key, scancode):
        if keycode == 'q':
            self.play_kick(None)
        elif keycode == 's':
            self.play_snare(None)
        elif keycode == 'd':
            self.play_clap(None)
        elif keycode == 'p':
            self.play_hihat(None)


if __name__ == '__main__':
    SoundApp().run()