import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
import pygame
import sys
import os

# Create the Tkinter root window
root = tk.Tk()

# Hide the root window since we won't be using it directly
root.withdraw()

# Use the file dialog to allow the user to select a video file
file_path = filedialog.askopenfilename()

# Check if the user cancelled the file dialog
if not file_path:
    print("No video file selected")
    sys.exit()

# Check if file exists
if not os.path.isfile(file_path):
    print(f"Can't find {file_path}.")
    sys.exit()

# Check if the file is a supported video type
supported_extensions = ['.mp4', '.avi', '.mov', '.wmv']
if os.path.splitext(file_path)[1] not in supported_extensions:
    print(f"Unsupported video type. Please select a file with one of the following extensions: {', '.join(supported_extensions)}")
    sys.exit()

player_icon = 'icon.png'

# Create a VideoFileClip object for the video file
video = VideoFileClip(file_path)
# Create an AudioFileClip object for the audio file
audio = AudioFileClip(file_path)
# Set the audio for the video clip
video = video.set_audio(audio)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption('Custom MoviePy Player')
pygame.display.set_icon(pygame.image.load(player_icon))

# Play the video in the player
video.preview(fps=120, fullscreen=False)
