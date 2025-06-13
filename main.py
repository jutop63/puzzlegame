import pygame
from constants import *
from player import Player

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updateable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit the framerate to 60 fps
        dt = clock.tick(60)/1000
    

if __name__ == "__main__":
    main()