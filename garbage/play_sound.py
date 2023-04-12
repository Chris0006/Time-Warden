import pygame

pygame.init() # Initialize Pygame
file_name = "game_over.mp3" # Set the file name
pygame.mixer.music.load(file_name) # Load the file
pygame.mixer.music.play() # Play the file

while pygame.mixer.music.get_busy(): # Wait for the file to finish playing
    pass

pygame.quit() # Quit Pygame