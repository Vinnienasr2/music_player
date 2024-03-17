from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.audio import SoundLoader
import os

class MusicPlayerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.title = "Music Player"
        self.songs = self.scan_music()
        self.current_song = None
        
        self.root = MDScreen()
        self.song_list = MDBoxLayout(orientation="vertical")
        self.load_songs()
        self.root.add_widget(self.song_list)
        return self.root
    
    def scan_music(self):
        songs = []
        for root, dirs, files in os.walk('/path/to/your/music/directory'):
            for file in files:
                if file.endswith('.mp3'):
                    songs.append(os.path.join(root, file))
        return songs
    
    def load_songs(self):
        for song in self.songs:
            self.song_list.add_widget(TwoLineListItem(text=song.split('/')[-1], secondary_text=song))
    
    def play_song(self, song_path):
        if self.current_song:
            self.current_song.stop()
        self.current_song = SoundLoader.load(song_path)
        self.current_song.play()
    
    def on_stop(self):
        if self.current_song:
            self.current_song.stop()
    
    def on_pause(self):
        if self.current_song:
            self.current_song.stop()
    
    def show_player(self, song_path):
        self.play_song(song_path)
        dialog = MDDialog(
            title="Now Playing",
            text=song_path.split('/')[-1],
            buttons=[MDFlatButton(text="Close", on_release=self.stop_player)]
        )
        dialog.open()
    
    def stop_player(self, *args):
        if self.current_song:
            self.current_song.stop()
        dialog = self.root.children[-1]  # Assuming dialog is the last child
        dialog.dismiss()

if __name__ == "__main__":
    MusicPlayerApp().run()
