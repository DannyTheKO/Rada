import tkinter as tk
from tkinter import filedialog,messagebox
import vlc
import os
import platform

# Determine the system type
system_type = platform.system()

# Configure VLC based on the system type
if system_type == 'Windows':
    vlc_options = ['--video-on-top']
elif system_type == 'Linux':
    vlc_options = ['--no-xlib']




class VideoPlayer:
    def __init__(self, master,frame):
        self.master = master
        self.frame=frame
        self.video=None
        self.is_muted = False  # to keep track of whether the video is muted or not
        # Create the player controls
        self.create_controls()

    def create_controls(self):
        # Create the open file button
        self.btn_open = tk.Button(self.master, text="Open File", command=self.open_file)
        self.btn_open.pack(side="left")

        # Create the play button
        self.btn_play = tk.Button(self.master, text="Play", command=self.play)
        self.btn_play.pack(side="left")

        # Create the pause button
        self.btn_pause = tk.Button(self.master, text="Pause", command=self.pause)
        self.btn_pause.pack(side="left")


        # Create the backward button
        self.btn_stop = tk.Button(self.master, text="Backward", command=self.backward)
        self.btn_stop.pack(side="left")

        # Create the forward button
        self.btn_stop = tk.Button(self.master, text="Forward", command=self.forward)
        self.btn_stop.pack(side="left")

        # Create the mute button
        self.btn_mute = tk.Button(self.master, text="Mute", command=self.mute_unmute)
        self.btn_mute.pack(side="right")

        

    def open_file(self):
        if self.video:
            self.video.stop()
        root.withdraw()
        # Open a file dialog to select a video file
        file_path = filedialog.askopenfilename()

        supported_extensions = ['.mp4', '.avi', '.mov', '.wmv']
        # Check if the user cancelled the file dialog
        if not file_path:
            messagebox.showinfo("Error", "No video file selected")
            root.deiconify()
        # Check if file exists
        elif not os.path.isfile(file_path):
            messagebox.showinfo("Error", "Can't find the video")
            root.deiconify()
             # Check if the file is a supported video type
        elif os.path.splitext(file_path)[1] not in supported_extensions:
            messagebox.showinfo("Error",f"Unsupported video type. Please select a file with one of the following extensions: {', '.join(supported_extensions)}")
            root.deiconify()
        else:   
            root.deiconify()
            instance = vlc.Instance(vlc_options)
            video = instance.media_player_new()
            media = instance.media_new(f"{file_path}")
            video.set_media(media)
            self.video = video


    def play(self):
        if self.video:
            match system_type:
                case 'Linux':
                    self.video.set_xwindow(self.frame.winfo_id())
                    self.video.play()
                case 'Windows':
                    self.video.set_hwnd(self.frame.winfo_id())
                    self.video.play()
            
            

    def pause(self):
        if self.video:
            self.video.pause()

    
    def backward(self):
        if self.video:
            current_time = self.video.get_time()
            if current_time > 5000:
                self.video.set_time(current_time - 5000)


    def forward(self):
        if self.video:
            current_time = self.video.get_time()
            if self.video.get_length()-current_time > 5000:
                self.video.set_time(current_time + 5000)




    def mute_unmute(self):
        if self.video:
            if self.is_muted:
                # Unmute the video
                self.video.audio_toggle_mute()
                self.is_muted = False
                self.btn_mute.config(text="Mute")
            else:
                # Mute the video
                self.video.audio_toggle_mute()
                self.is_muted = True
                self.btn_mute.config(text="Unmute")
    

    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("RaDa")
    root.geometry('1270x720')
    root.resizable(True, True)
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)  # set the root window to be resizable in both directions
    app = VideoPlayer(root,frame)
    root.deiconify()
    root.mainloop()
   
