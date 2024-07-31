import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        mixer.init()

        self.current_song_index = 0
        self.playlist = []

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.load_button = tk.Button(root, text="Load Folder", command=self.load_folder)
        self.load_button.pack()

    def load_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav'))]
            if self.playlist:
                messagebox.showinfo("Music Player", f"{len(self.playlist)} songs loaded.")
                self.current_song_index = 0
            else:
                messagebox.showwarning("Music Player", "No music files found in the folder.")

    def play_music(self):
        if self.playlist:
            mixer.music.load(self.playlist[self.current_song_index])
            mixer.music.play()
        else:
            messagebox.showwarning("Music Player", "No music loaded. Please load a folder first.")

    def stop_music(self):
        mixer.music.stop()

    def pause_music(self):
        if mixer.music.get_busy():
            if mixer.music.get_pos() > 0:
                mixer.music.pause()
            else:
                mixer.music.unpause()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
