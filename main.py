import sys,pygame,setup,AI
from gui import GUI

pygame.init()
gui = setup.gui
player = setup.player
npcs = setup.npcs
clock = pygame.time.Clock()
pygame.key.set_repeat(1)
pygame.time.set_timer(setup.UPDATESTATUS,6000)#Ten minutes until starving
endscreen = pygame.Surface((setup.screen.get_width(),setup.screen.get_height()))
endscreen.fill(55)
while True:

    while player.alive:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_d]:                
                    player.movePlayer("RIGHT")
           
                elif keys[pygame.K_s]:
                    player.movePlayer("DOWN")

                elif keys[pygame.K_a]:
                    player.movePlayer("LEFT")

                elif keys[pygame.K_w]:
                    player.movePlayer("UP")
            elif event.type == setup.UPDATESTATUS:
                print(player.stats)
                player.updateHunger()
                player.updateStamina()
    
        clock.tick(40)


        player.updatePlayer()
        AI.updateNPC(npcs)
        gui.update()

    endscreen = pygame.Surface(pygame.display.get_surface().get_size()).convert_alpha()
    endscreen.fill((0,0,0))
    alpha = 0
    endscreen.blit(pygame.display.get_surface(),(0,0))
    while alpha < 255:
        pygame.time.delay(50)
        alpha += 5
        endscreen.set_alpha(alpha)
        pygame.display.flip()



    