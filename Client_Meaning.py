import re
import tkinter as tk

class ChordsAndMeaningApp:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lyrics = []
        self.chords = []
        self.meanings = []
        self.parse_lyrics_file()
        self.init_ui()
    
    def parse_lyrics_file(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                match = re.match(r'\[(\d\d:\d\d\.\d\d)\]\s*\[(.*?)\]\s*(.*?)\s*\[/.*?\:(.*?)\]', line)
                if match:
                    self.lyrics.append(match.group(3))
                    self.chords.append(match.group(2))
                    self.meanings.append(match.group(4))
    
    def init_ui(self):
        root = tk.Tk()
        root.title("Chords and Meaning")
        
        lyrics_frame = tk.Frame(root)
        lyrics_frame.pack(side=tk.LEFT)
        
        meaning_frame = tk.Frame(root)
        meaning_frame.pack(side=tk.RIGHT)
        
        lyrics_label = tk.Label(lyrics_frame, text='\n'.join(self.lyrics))
        lyrics_label.pack()
        
        for i in range(len(self.meanings)):
            meaning_button = tk.Button(meaning_frame, text=self.chords[i], command=lambda i=i: self.show_meaning(i))
            meaning_button.pack()
        
        self.meaning_label = tk.Label(meaning_frame, text='')
        self.meaning_label.pack()
        
        root.mainloop()
    
    def show_meaning(self, index):
        self.meaning_label.config(text=self.meanings[index])
