import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import time
import threading
from mutagen.mp3 import MP3  # For getting MP3 duration

# Initialize Pygame mixer
pygame.mixer.init()

# Global variables
music_file = None
is_playing = False
song_length = 0

# Function to load an audio file
def load_music():
    global music_file, song_length
    music_file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if music_file:
        song_label.config(text=f"Now Playing: {music_file.split('/')[-1]}", fg="green")
        # Get song duration
        audio = MP3(music_file)
        song_length = int(audio.info.length)
        update_time_display(0, song_length)

# Function to play the music
def play_music():
    global is_playing
    if music_file:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        is_playing = True
        threading.Thread(target=update_progress, daemon=True).start()
    else:
        messagebox.showwarning("Warning", "Please select an MP3 file first!")

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume the music
def resume_music():
    pygame.mixer.music.unpause()

# Function to stop the music
def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    update_time_display(0, song_length)

# Function to update the volume
def set_volume(val):
    pygame.mixer.music.set_volume(float(val) / 100)

# Function to update the playback time display
def update_time_display(elapsed, total):
    time_label.config(text=f"Time: {time.strftime('%M:%S', time.gmtime(elapsed))} / {time.strftime('%M:%S', time.gmtime(total))}")

# Function to track progress
def update_progress():
    global is_playing
    start_time = time.time()
    while is_playing:
        elapsed = int(time.time() - start_time)
        if elapsed > song_length:
            break
        update_time_display(elapsed, song_length)
        time.sleep(1)

# Create the main window
root = tk.Tk()
root.title("🎵 Enhanced Media Player")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Song Label
song_label = tk.Label(root, text="No file selected", font=("Arial", 12), bg="#f0f0f0", fg="red")
song_label.pack(pady=10)

# Load Music Button
load_btn = tk.Button(root, text="📂 Open File", command=load_music, bg="blue", fg="white", font=("Arial", 10))
load_btn.pack(pady=5)

# Control Buttons (Play, Pause, Resume, Stop)
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

play_btn = tk.Button(btn_frame, text="▶ Play", command=play_music, bg="green", fg="white", width=8)
play_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(btn_frame, text="⏸ Pause", command=pause_music, bg="orange", fg="white", width=8)
pause_btn.grid(row=0, column=1, padx=5)

resume_btn = tk.Button(btn_frame, text="⏯ Resume", command=resume_music, bg="purple", fg="white", width=8)
resume_btn.grid(row=1, column=0, padx=5, pady=5)

stop_btn = tk.Button(btn_frame, text="⏹ Stop", command=stop_music, bg="red", fg="white", width=8)
stop_btn.grid(row=1, column=1, padx=5, pady=5)

# Playback Time Display
time_label = tk.Label(root, text="Time: 00:00 / 00:00", font=("Arial", 12), bg="#f0f0f0", fg="black")
time_label.pack(pady=10)

# Volume Control
volume_frame = tk.Frame(root, bg="#f0f0f0")
volume_frame.pack(pady=5)

volume_label = tk.Label(volume_frame, text="🔊 Volume", bg="#f0f0f0")
volume_label.pack(side=tk.LEFT, padx=5)

volume_slider = tk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
volume_slider.set(50)  # Default volume level
volume_slider.pack(side=tk.RIGHT)

# Run the Tkinter event loop
root.mainloop()
