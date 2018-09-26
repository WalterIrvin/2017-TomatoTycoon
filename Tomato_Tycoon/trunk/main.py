import pygame
import menu
import world
import character


pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 16)
done = False

# Test menu (temporary)
M = menu.Menu(font, (255,100,100), (100, 100, 600, 400), (100,255,100), (0,255,0))
M.addItem(menu.MenuItem("Assets\\tomato.png", "Tomatoes", (100,255,100)))
M.addItem(menu.MenuItem("Assets\\sword.jpg", "Swords", (100,255,100)))
M.addItem(menu.MenuItem("Assets\\potion.png", "Potions", (100,255,100)))
menu_active = False


# Test character (temporary)
C = character.Character("bob", pygame.image.load("Assets\\smiley.png"))
C.addKeyFrame(0.0, (850, 300))
C.addKeyFrame(2.0, (500, 300))
C.addKeyFrame(6.0, (100, 100))
C.addKeyFrame(10.0, (400, 500))
C.addKeyFrame(12.0, (800, 300))
C.addKeyFrame(12.5, (850, 300))


W = world.Map("Assets\\Store_Placerholder\\store_placeholderV1.txt")

while not done:
    # UPDATE
    dt = clock.tick() / 1000.0
    C.update(dt)


    # INPUT HANDLING
    evt = pygame.event.poll()
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True
        if evt.key == pygame.K_SPACE:
            menu_active = not menu_active
    # ... Make the menu update if this is a pertinent event
    if menu_active:
        M.handleEvent(evt)

    # DRAWING
    screen.fill((0,0,0))
    W.render(screen)
    C.render(screen, font)
    if menu_active:
        M.render(screen)
    pygame.display.flip()

pygame.font.quit()
pygame.display.quit()


