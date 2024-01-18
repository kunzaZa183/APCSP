import pygame, sys, random, re

# Initialize Pygame
pygame.init()

"""
heart = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart, (50, 50))
"""

# Open word file
word_list = open("hangman.txt", "r").read().split()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
SANS = pygame.font.Font("comic.ttf", 100)

# Set lives
lives = 5

# Creating the screen
screen = pygame.display.set_mode((1200, 800))

# Function to draw the rectangle and clean the screen
def clean(topleft, bottomright):
    pygame.draw.rect(
        screen, WHITE, (topleft[0], topleft[1], bottomright[0], bottomright[1])
    )

clean((0,0), (1200, 800))

# Draw the ground
pygame.draw.line(screen, BLACK, (400, 400), (800, 400), 5)

# Pole
pygame.draw.line(screen, BLACK, (450, 400), (450, 50), 5)
pygame.draw.line(screen, BLACK, (450, 50), (600, 50), 5)

# Rope
pygame.draw.line(screen, BLACK, (600, 50), (600, 115), 5)

""" Oly fix this plz smh
def draw_hearts(lives, position):
    for iterator in range(lives):
        position[0] = position[0] + 50
        print(position)
        tupled_position = tuple(position)
        screen.blit(heart, tupled_position)
    for iterator in range(5 - lives):
        coordinates_of_rectangle = (position[0], position[1], (position[0]), (position[1]))
        pygame.draw.rect(screen, BLACK, coordinates_of_rectangle)
        position[0] -= 50
"""

pygame.display.update()

word = random.choice(word_list)

print(word)

# Creates a list for every letter in the selected word. 1 means that letter has been guessed and 0 means it has not.
guessedlist = [0] * len(word)

# Out is the string that is displayed on pygame.
out = "-" * len(word)

# Renders the string
text_surface = SANS.render(out, False, (0, 0, 0))
screen.blit(text_surface, (100, 600))
pygame.display.update()

while lives != 0:

    #prevents the game from crashing
    pygame.event.get()

    guess = str(input("What is your guess: ")).lower()

    # Variable to check if a new letter has been guessed or not
    found = False

    # Resets the out string
    out = ""

    # Iterates through the word
    for i in range(len(word)):
        # if a letter has just recently been guessed
        if guessedlist[i] == 0 and word[i] == guess:
            guessedlist[i] = 1
            found = 1

        # if a letter has been guessed
        if guessedlist[i] == 1:
            out += word[i]
        else:
            out += "-"

    # Clears out the words
    clean((100, 600), (700, 700))

    # Renders the string
    text_surface = SANS.render(out, False, (0, 0, 0))
    screen.blit(text_surface, (100, 600))
    pygame.display.update()
    
    if not found:
        lives -= 1
        # draw_hearts(lives, [800, 400])

        if lives == 4:
            # Head
            pygame.draw.circle(screen, BLACK, (600, 150), 35)
            # Body
            pygame.draw.line(screen, BLACK, (600, 185), (600, 285), 9)
        elif lives == 3:
            # Left arm
            pygame.draw.line(screen, BLACK, (600, 200), (550, 250), 9)
        elif lives == 2:
            # Right arm
            pygame.draw.line(screen, BLACK, (600, 200), (650, 250), 9)
        elif lives == 1:
            # Left leg
            pygame.draw.line(screen, BLACK, (600, 285), (550, 335), 9)
        elif lives == 0:
            # Right leg
            pygame.draw.line(screen, BLACK, (600, 285), (650, 335), 9)
        pygame.display.update()

    if not (0 in guessedlist):
        break

if not (0 in guessedlist):
    print("GOOD")
else:
    print("YOU SUCK")