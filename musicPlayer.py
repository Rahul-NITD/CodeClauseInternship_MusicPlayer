# written by : https://github.com/Rahul-NITD/

from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x500')
        self.root.title('CodeClause Music Player')
        self.root.resizable(0, 0)
        self.root.configure(bg='#212121')

        self.current_song = StringVar(value='Please select A song by loading the directory')
        self.song_status = StringVar(value='Please select A song by loading the directory')

        self.create_frames()
        self.create_widgets()

    def create_frames(self):
        self.song_frame = Frame(self.root, bg='#212121')
        self.song_frame.pack(fill=BOTH, padx=30, pady=20)

        self.button_frame = Frame(self.root, bg='#212121')
        self.button_frame.pack(pady=20)

        self.listbox_frame = Frame(self.root, bg='#212121')
        self.listbox_frame.pack(fill=BOTH, padx=30, pady=20)

    def create_widgets(self):
        self.song_lbl = Label(self.song_frame, textvariable=self.current_song, font=("Helvetica", 18), bg='#212121', fg='white')
        self.song_lbl.pack()

        self.create_buttons()
        self.create_playlist()

        Label(self.root, textvariable=self.song_status, font=('Helvetica', 12), bg='#212121', fg='white').pack(side=BOTTOM, fill=X)

    def create_buttons(self):
        buttons = [('Play', self.play_song), ('Pause', self.pause_song), ('Stop', self.stop_song), ('Resume', self.resume_song)]
        for label_text, command_func in buttons:
            Button(self.button_frame, text=label_text, font=("Helvetica", 14), width=10, height=2, command=command_func, bg='#37474F', fg='white').pack(side=LEFT, padx=10)

        Button(self.button_frame, text='Load Directory', font=("Helvetica", 14), height=2, command=self.load_directory, bg='#37474F', fg='white').pack(pady=10)

    def create_playlist(self):
        self.playlist = Listbox(self.listbox_frame, font=('Helvetica', 14), selectbackground='Gold', selectmode=SINGLE, bg='#303030', fg='white', bd=0, activestyle='none')

        scroll_bar = Scrollbar(self.listbox_frame, orient=VERTICAL)
        scroll_bar.pack(side=RIGHT, fill=Y)

        self.playlist.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

    def play_song(self):
        selected_song = self.playlist.get(ACTIVE)
        if selected_song:
            self.current_song.set(selected_song)
            mixer.music.load(selected_song)
            mixer.music.play()
            self.song_status.set("Song PLAYING")

    def stop_song(self):
        mixer.music.stop()
        self.song_status.set("Song STOPPED")

    def pause_song(self):
        mixer.music.pause()
        self.song_status.set("Song PAUSED")

    def resume_song(self):
        mixer.music.unpause()
        self.song_status.set("Song RESUMED")

    def load_directory(self):
        chosen_directory = filedialog.askdirectory(title='Open a songs directory')
        os.chdir(chosen_directory)
        tracks = os.listdir()
        self.playlist.delete(0, END)
        for track in tracks:
            self.playlist.insert(END, track)

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
