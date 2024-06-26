import pygame
import sys
from game_parameters import *

# Initialize Pygame
pygame.init()
from player import Player
from dot import Dot

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dot Chomper!")


clock = pygame.time.Clock()

# Main loop
running = True

# add the fish, enemies, and player

player1 = Player(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, "red")
player2 = Player(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, "blue")
dots = [Dot() for _ in range(NUM_DOTS)]

score_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 48)
time_remaining = GAME_LENGTH

frame_count = 0
while time_remaining > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # control player with arrow keys
    
    ### TODO: CONTROL PLAYER WITH CAMERA ###

    x,y = pygame.mouse.get_pos()
    player1.set_position(x,y)
    player2.set_position(3* SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2)

    ### END TODO ###

    # collide the players with the dots, remove dots that have been hit
    for dot in dots:
        if player1.collide(dot):
            dots.remove(dot)
        if player2.collide(dot):
            dots.remove(dot)
    # create new dots to replace the ones that were removed,
    # put them in a random position around the screen
    while len(dots) < NUM_DOTS:
        dots.append(Dot())

    # draw the background
    screen.fill((255, 255, 255))

    # draw game objects
    player1.draw(screen)
    player2.draw(screen)
    for dot in dots:
        dot.draw(screen)
    # draw the score in the upper left corner
    message = score_font.render(f"{time_remaining}", True, (0, 0, 0))
    screen.blit(message, (SCREEN_WIDTH/2 - message.get_width() - 10, 0))


    # Update the display
    pygame.display.flip()

    # keep track of elapsed seconds
    if frame_count % 60 == 0:
        time_remaining -= 1
    frame_count+=1
    # Limit the frame rate
    clock.tick(60)

screen.fill((255, 255, 255))

# show a game over message
if player1.size > player2.size:
    message = score_font.render("Player 1 Wins!", True, (255, 0, 0))
elif player1.size < player2.size:
    message = score_font.render("Player 2 Wins!", True, (0, 0, 255))
else:
    message = score_font.render("It's a tie!", True, (0, 0, 0))


screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2 - message.get_height() / 2))

pygame.display.flip()

# wait for user to exit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Pygame
            pygame.quit()
            sys.exit()
