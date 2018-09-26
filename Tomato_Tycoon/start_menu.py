import pygame
pygame.font.init()
class start_menu(object):
    def __init__(self):
        self.font2 = pygame.font.SysFont("Arial", 50)
        self.fontCred = pygame.font.SysFont("Arial", 12)
        self.xpos = 880
        self.ypos = 100
        self.width = 300
        self.height = 100
        self.background = pygame.image.load("Assets/mainmenu.jpg")
        self.tablet = pygame.image.load("Assets/tablet.png")
    def render(self, surf):
        # background
        surf.blit(self.background, (0,0))
        #start
        # pygame.draw.rect(surf, (128, 128, 128), (self.xpos, self.ypos, self.width, self.height), 0)
        surf.blit(self.tablet, (self.xpos, self.ypos))
        font_surf1 = self.font2.render("New Game", 0, (255, 255, 255))
        surf.blit(font_surf1, (self.xpos + 40, self.ypos + 20))
        #content
        # pygame.draw.rect(surf, (128, 128, 128), (self.xpos, self.ypos + 125, self.width, self.height), 0)
        surf.blit(self.tablet, (self.xpos, self.ypos + 125))
        font_surf2 = self.font2.render("Continue", 0, (255, 255, 255))
        surf.blit(font_surf2, (self.xpos + 45, self.ypos + 145))
        #credits
        # pygame.draw.rect(surf, (128, 128, 128), (self.xpos, self.ypos + 250, self.width, self.height), 0)
        # font_surf3 = self.font2.render("Credits", 0, (255, 255, 255))
        # surf.blit(font_surf3, (450, 370))
        credX = 10
        credY = 575
        emm = self.fontCred.render("Emm Oriold", 0, (255, 255, 255))
        will = self.fontCred.render("Will Rossi", 0, (255, 255, 255))
        tim = self.fontCred.render("Tim Harden", 0, (255, 255, 255))
        alex = self.fontCred.render("Alex Krauss", 0, (255, 255, 255))
        josh = self.fontCred.render("Josh Antone", 0, (255, 255, 255))
        walter = self.fontCred.render("Walter Irvin", 0, (255, 255, 255))
        imgcred = self.fontCred.render("Image Credit: http://undercurrent-32.deviantart.com/art/Magic-Shop-478507159", 0, (255, 255, 255))
        surf.blit(walter, (credX, credY))
        surf.blit(emm, (credX + 100, credY))
        surf.blit(josh, (credX + 200, credY))
        surf.blit(tim, (credX + 300, credY))
        surf.blit(alex, (credX + 400, credY))
        surf.blit(will, (credX + 500, credY))
        surf.blit(imgcred, (credX + 850, credY))

    def hitDetection(self, mpos):
        if self.xpos < mpos[0] < self.xpos + self.width:
            if self.ypos < mpos[1] < self.ypos + self.height:
                return "new game"
                #1st button hit
            if self.ypos + 125 < mpos[1] < self.ypos + 125 + self.height:
                return "load game"
                #2nd button hit
            # if self.ypos + 250 < mpos[1] < self.ypos + 250 + self.height:
            #     return "credits"
            #     #3rd button hit


class creds(object):
    def __init__(self, sw, sh):
        self.font1 = pygame.font.SysFont("Arial", 50)
        self.font2 = pygame.font.SysFont("Arial", 36)
        self.x = sw
        self.y = sh
    def render(self, surf):
        program = self.font1.render("Programmers",0,(255,255,255))
        emm = self.font2.render("Emm Oriold", 0, (255,255,255))
        will = self.font2.render("Will Rossi", 0, (255,255,255))
        tim = self.font2.render("Tim Harden", 0, (255,255,255))
        alex = self.font2.render("Alex Krauss", 0, (255,255,255))
        josh = self.font2.render("Josh Antone", 0, (255,255,255))
        surf.blit(program, (self.x - 150, self.y))
        surf.blit(emm, (self.x - 105, self.y + 50))
        surf.blit(will, (self.x - 105, self.y + 100))
        surf.blit(tim, (self.x - 105, self.y + 150))
        surf.blit(alex, (self.x - 105, self.y + 200))
        surf.blit(josh, (self.x - 105,self.y + 250))
