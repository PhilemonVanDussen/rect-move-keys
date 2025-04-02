# Pygame game template

import pygame
import sys
import config # Import the config module
import random
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

def draw_rect(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
   
    
    # Rectangle 1
    color1 = config.RED
    color2 = config.WHITE
    x1, y1 = 95, 325
    x2,y2 = 345, 255
    width1 = 150
    width2 = 100
    height1 = 150
    height2 = 100

    font = pygame.font.Font(None, 36)
    text_surface1 = font.render('Press the arrows to move Red Square', True, config.BLACK)
    text_surface2 = font.render('Press WASD to move the White Square', True, config.YELLOW)
    text_width1 = text_surface1.get_width()
    text_width2 = text_surface2.get_width()
    text_x1 = (config.WINDOW_WIDTH - text_width1) / 2
    text_x2 = (config.WINDOW_WIDTH - text_width2) /2
    text_y1 = 50
    text_y2 = 550

    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config

        mouse_pos = pygame.mouse.get_pos()
        draw_text(screen, mouse_pos, mouse_pos, 15) # Tells user mouse coordinates

        value = 1

        key = pygame.key.get_pressed()
        # Movement Square 1
        if  key[pygame.K_LEFT]:
            x1 -= value
        if key[pygame.K_RIGHT]:
            x1 += value
        if key[pygame.K_UP]:
            y1 -= value
        if key[pygame.K_DOWN]:
            y1 += value
        # Movement Square 2
        if  key[pygame.K_a]:
            x2 -= value
        if key[pygame.K_d]:
            x2 += value
        if key[pygame.K_w]:          
            y2 += value
        

        draw_rect(screen, color1, x1, y1, width1, height1)
        draw_rect(screen, color2, x2, y2, width2, height2)

        if key[pygame.K_SPACE]:
            draw_rect(screen, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), x1 + 37.5 , y1 +  37.5, 75, 75)
        # if key[pygame.MOUSEWHEEL]:
        #     draw_rect(screen, config.BLACK, )
        

        screen.blit(text_surface1, (text_x1, text_y1))
        screen.blit(text_surface2, (text_x2, text_y2))

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



