import pygame,setup
from pygame.sprite import Group


class Player(Group):
    def __init__(self, x_pos=None, y_pos=None, imagemap=None,imagemap2=None):

        Group.__init__(self)        

        self.player = pygame.sprite.Sprite()
        self.player.x_pos = x_pos
        self.player.y_pos = y_pos
        imagemap = pygame.image.load(imagemap).convert_alpha()
        imagemap2 = pygame.image.load(imagemap2).convert_alpha()
        self.player.front1 = imagemap.subsurface(0,0,12,20)
        self.player.back1 = imagemap.subsurface(12,0,12,20)
        self.player.left1= imagemap.subsurface(24,0,10,20)
        self.player.right1 = imagemap.subsurface(34,0,10,20)
        self.player.front2 = imagemap2.subsurface(0,0,12,20)
        self.player.back2 = imagemap2.subsurface(12,0,12,20)
        self.player.left2= imagemap2.subsurface(24,0,10,20)
        self.player.right2 = imagemap2.subsurface(34,0,10,20)

     

        #Initial attributes
        self.health = 100 #percent
        self.hunger = 0
        self.alive = True
        self.starving = False
        self.encumbrance = 0
        self.stamina = 100
        self.exhausted = False
        self.basespeed = 2
        self.inventory = []
        self.moving = False
        self.player.image = self.player.front1
        self.dir = 0
        self.FRAMERATE = 10
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = x_pos
        self.player.rect.y = x_pos
        self.add(self.player)
        self.running = False
        

    def updateHunger(self):
        if self.hunger < 100:
            self.hunger += 1
        else:
            self.starving = True
            print("starving")
            print(self.health)
    def updateStamina(self):
        if self.moving == True:
            staminaloss = .01+(self.encumbrance%25)*.01
            if self.running:
                staminaloss *= 5
                self.running = False
            if self.stamina > -5:
                self.stamina -= staminaloss
            if self.stamina < 0:
                self.exhausted = True
            self.moving = False
        else:
            if self.stamina < 100:
                self.stamina += .01
            if self.stamina > 0:
                self.exhausted = False
    def movePlayer(self,direction):
        SPEED = self.basespeed
        if self.running:
            SPEED *= 2
        if pygame.sprite.spritecollideany(self.player,setup.longgrass) != None or self.exhausted:
            SPEED = 1
     
        VIEWDISTANCE = 150
        GUIWIDTH = 200
        self.moving = True

        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                self.dir = 1
                SPEED *= -1
                #self.player.image = self.player.left1
                if setup.frame % self.FRAMERATE == 0:
                    if self.player.image == self.player.left1:
                        self.player.image = self.player.left2
                    else:
                        self.player.image = self.player.left1
            else:
                self.dir = 3
                #self.player.image = self.player.right1
                if setup.frame % self.FRAMERATE == 0:
                    if self.player.image == self.player.right1:
                        self.player.image = self.player.right2
                    else:
                        self.player.image = self.player.right1
            
            if self.player.rect.x < VIEWDISTANCE:               
                if setup.gui.bgx < 0:
                    self.player.rect.x = VIEWDISTANCE
                    setup.gui.bgx -= SPEED
                    
                    for rect in setup.buildings:
                        rect.rect.x -= SPEED
                    for spr in setup.npcs:
                        spr.rect.x -= SPEED
                    for item in setup.items:
                        item.rect.x -= SPEED
                    for object in setup.longgrass:
                        object.rect.x -= SPEED
                    for object in setup.trees:
                        object.rect.x -= SPEED

            elif self.player.rect.x > setup.screen.get_width()-VIEWDISTANCE-GUIWIDTH:
                if setup.gui.bgx >(0-setup.background.get_width()+setup.screen.get_width()-GUIWIDTH):
                    self.player.rect.x = setup.screen.get_width()-VIEWDISTANCE-GUIWIDTH
                    setup.gui.bgx -= SPEED
                
                    for rect in setup.buildings:
                        rect.rect.x -= SPEED
                    for spr in setup.npcs:
                        spr.rect.x -= SPEED
                    for item in setup.items:
                        item.rect.x -= SPEED
                    for object in setup.longgrass:
                        object.rect.x -= SPEED
                    for object in setup.trees:
                        object.rect.x -= SPEED

            self.player.rect.x += SPEED

            if pygame.sprite.spritecollideany(self.player,setup.buildings) != None\
            or pygame.sprite.spritecollideany(self.player,setup.npcs) != None\
            or pygame.sprite.spritecollideany(self.player,setup.trees) != None:

                self.player.rect.x -= SPEED

        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                self.dir = 1
                SPEED *= -1
                #self.player.image = self.player.back1

                if setup.frame % self.FRAMERATE == 0:
                    if self.player.image == self.player.back1:
                        self.player.image = self.player.back2
                    else:
                        self.player.image = self.player.back1
            else:
                self.dir = 0
              #  self.player.image = self.player.front1

                if setup.frame % self.FRAMERATE == 0:
                    if self.player.image == self.player.front1:
                        self.player.image = self.player.front2
                    else:
                        self.player.image = self.player.front1

            if self.player.rect.y > setup.screen.get_height() - VIEWDISTANCE: 
                if setup.gui.bgy >(0-setup.background.get_height()+setup.screen.get_height()):
                    self.player.rect.y = setup.screen.get_height()-VIEWDISTANCE         
                    setup.gui.bgy -= SPEED
                    
                    for rect in setup.buildings:
                        rect.rect.y -= SPEED
                    for spr in setup.npcs:
                        spr.rect.y -= SPEED
                    for item in setup.items:
                        item.rect.y -= SPEED
                    for object in setup.longgrass:
                        object.rect.y -= SPEED
                    for object in setup.trees:
                        object.rect.y -= SPEED
            
            elif self.player.rect.y < VIEWDISTANCE:
                if setup.gui.bgy < 0:
                    self.player.rect.y = VIEWDISTANCE
                    setup.gui.bgy -= SPEED
                
                    for rect in setup.buildings:
                        rect.rect.y -= SPEED
                    for spr in setup.npcs:
                        spr.rect.y -= SPEED
                    for item in setup.items:
                        item.rect.y -= SPEED
                    for object in setup.longgrass:
                        object.rect.y -= SPEED
                    for object in setup.trees:
                        object.rect.y -= SPEED

            self.player.rect.y += SPEED

            if pygame.sprite.spritecollideany(self.player,setup.buildings) != None\
            or pygame.sprite.spritecollideany(self.player,setup.npcs) != None\
            or pygame.sprite.spritecollideany(self.player,setup.trees) != None:

                self.player.rect.y -= SPEED



    def updatePlayer(self):
        #Takes roughly 4 min. from full health to death when starving.

        self.updateStamina()
            
        if self.starving:
            self.health -= .1
        if self.health <= 0:
            self.alive = False
            
