import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def play_music(folder, song_name):
    file_path = os.path.join(folder, song_name)
    if not os.path.exists(file_path):
        print("file not found")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print (f"\nnow playing: {song_name}")
    print ("press 'S' to stop the music or 'P' to pause the music or 'R' to resume the music")

    while True:

        command = input("> ").upper()

        if command =='P':
            pygame.mixer.music.pause()
        elif command =='R':
            pygame.mixer.music.unpause()
        elif command =='S':
            pygame.mixer.music.stop()
            break

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Error initializing mixer: {e}")
        return

    print("this is a test")

    folder = "music"
    if not os.path.isdir(folder):
        print(f"folder '{folder}' does not exist")
        return

    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    if not mp3_files:
         print ("No mp3 files found in the folder")

    while True:
        print ("******MP3 PLAYER******")
        print ("my song list: ")

        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")

        choice_input = input("\nEnter the number of the song you want to play (or 'q' to quit): ")
        if choice_input.lower() == 'q':
            print("Exiting the program.")
            break

        if not choice_input.isdigit() or not (1 <= int(choice_input) <= len(mp3_files)):
            print("Invalid choice. Please enter a valid number.")
            continue

        choice = int(choice_input) - 1

        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice. Please enter a valid number.")



if __name__ == "__main__":
        main()    