from MENU import *
import pygame
from Character import *
from World import *
from start_menu import *
from Messages import *
import time
stime = time.time()
pygame.init()
news = Message()
screen = pygame.display.set_mode((1200, 600))
sw = screen.get_width()
sh = screen.get_height()
data = ""
playerData = ""
onMainMenu = True
onCredits = False
mainMenu = start_menu()
s = "None"
#This Section takes in load menu clicks and loads saves or newgames accordingly.
while onMainMenu:
    if onCredits == False:
        evt = pygame.event.poll()
        pos = pygame.mouse.get_pos()
        if evt.type == pygame.QUIT:
            done = True
            break
        if evt.type == pygame.MOUSEBUTTONDOWN:
            s = mainMenu.hitDetection(pos)
        screen.fill((0, 0, 0))
        mainMenu.render(screen)
        pygame.display.flip()
        if s == "new game":
            data = "items.txt"
            playerData = "player.txt"
            onMainMenu = False
            done = False
        elif s == "load game":
            data = "itemsSaved.txt"
            playerData = "playerSaved.txt"
            onMainMenu = False
            done = False
        # elif s == "credits":
        #     onCredits = True
    if onCredits:
        pass

if not done:
    savefileItems = "itemsSaved.txt"
    savefilePlayer = "playerSaved.txt"
    font = pygame.font.SysFont("Assets//fonts//prototype.ttf", 20)
    bigfont = pygame.font.SysFont("Assets//fonts//prototype.ttf", 70)
    imglist = ["Assets//arrows//shopleft.bmp", "Assets//arrows//shopdown.bmp",
               "Assets//arrows//mine.bmp", "Assets//arrows//garden.bmp"]
    char_img = pygame.image.load("Assets/rpg_maker_vx_sprite_dump_2_by_palinor-d3redzy.png")
    p = Player(playerData)
    i = Inventory(sw, sh, data, bigfont, font, 0, p)
    u = UI(screen, font, imglist, p)
    g = Upgrade(screen, font, p)
    done = False

    clock = pygame.time.Clock()
    inv = False
    w = Map("Assets/Store_placeholder/store_placeholderV4.txt")
    c = character(char_img, w)
    ch = character(char_img, w)
    ch1 = character(char_img, w)
    ch2 = character(char_img, w)
    upgrade = False
    t_room = 0
    h1 = None
while not done:
    evt = pygame.event.poll()
    dt = clock.tick() / 1000.0
    etime = time.time()
    mouse = pygame.mouse.get_pressed()
    if etime - stime >= 15:
        news.update(p.saygold())
        stime = time.time()
    i.update(dt)
    c.update(dt)
    ch.update(dt)
    ch1.update(dt)
    ch2.update(dt)
    if evt.type == pygame.QUIT:
        i.saveInventory(savefileItems)
        p.savePlayer(savefilePlayer)
        done = True
    elif evt.type == pygame.MOUSEBUTTONUP:
        i.released()
        h1 = g.released(p.gold)
        if h1 is not None:
            p.upgrade(h1)
            h1 = None
    elif evt.type == pygame.MOUSEBUTTONDOWN:
        if evt.button == 1:
            mpos = pygame.mouse.get_pos()
            t_inv = u.update(mpos)
            room = u.arrow(mpos)
            if room[0] == 0:
                w = Map("Assets/Store_placeholder/store_placeholderV4.txt")
            if room[0] == 1:
                w = Map("Assets/Garden_placeholder/gardenV2.txt")
            if room[0] == 2:
                w = Map("Assets/Mine_placeholder/mineV2.txt")

            # i.mapupdate resets the self.row to 0 each time a room is changed, to prevent crashes.
            if room != t_room:
                t_room = room
                i.mapupdate(room[0])
            # t_inv purpose is sometimes, the click will be outside the button when inv is up,
            # so this leaves inv alone in that case
            i.hitbox(mpos, inv)
            g.hitbox(mpos, upgrade)

            if t_inv is not None:
                inv = t_inv[0]
                upgrade = t_inv[1]
        if evt.button == 4 and inv is not False:
            i.scroll(-1)
        if evt.button == 5 and inv is not False:
            i.scroll(1)
    if mouse[0] and inv is not False:
        mpos = pygame.mouse.get_pos()
        i.slide(mpos)
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True
    screen.fill((0, 0, 0))
    w.render(screen)
    u.render()
    c.render(screen)
    ch.render(screen)
    ch1.render(screen)
    ch2.render(screen)
    if upgrade:
        g.render(p)
    i.render(screen, inv)
    sliderstr = i.sayslider()
    temp_a = pygame.font.Font.render(font, "crafting... " + sliderstr[0], True, (255, 255, 255))
    temp_b = pygame.font.Font.render(font, "Craft amount: " + sliderstr[1], True, (255, 255, 255))
    if inv:
        screen.blit(temp_a, (350, 350))
        screen.blit(temp_b, (350, 360))
    pygame.display.flip()
pygame.quit()
