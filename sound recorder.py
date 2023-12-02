pip install kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
import os

class SoundRecorderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.record_button = Button(text='Record')
        self.record_button.bind(on_press=self.toggle_recording)
        
        self.play_button = Button(text='Play')
        self.play_button.bind(on_press=self.play_recording)
        
        self.layout.add_widget(self.record_button)
        self.layout.add_widget(self.play_button)
        
        self.recording = False
        self.sound = SoundLoader.load('recording.wav')
        
        return self.layout
    
    def toggle_recording(self, instance):
        if not self.recording:
            self.sound = SoundLoader.load('recording.wav')
            self.sound.play()
            self.recording = True
            self.record_button.text = 'Stop Recording'
        else:
            self.sound.stop()
            self.recording = False
            self.record_button.text = 'Record'
    
    def play_recording(self, instance):
        if self.sound:
            self.sound.play()

if __name__ == '__main__':
    SoundRecorderApp().run()


Follow the Kivy documentation for deploying on Android: https://kivy.org/doc/stable/guide/packaging-android.html




