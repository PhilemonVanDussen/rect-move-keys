# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    pygame.font.init
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_text(screen, text, pos, font_size):
    font = pygame.font.SysFont('LiberationMono', font_size)
    display_text = font.render(str(text), True, config.BLACK)
    screen.blit(display_text, (pos))

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config
        mouse_pos = pygame.mouse.get_pos()
        draw_text(screen, mouse_pos, mouse_pos, 15) # Tells user mouse coordinates




        pygame.display.flip()
        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



