import pygame

# pygame.init()
# screen = pygame.display.set_mode((800,600))
# clock = pygame.time.Clock()
class KeyFrame(object):
    #This class creates keyframes to be used
    def __init__(self,t,x,y):
        #self.t, self.x, and self.y are where the needs to go in this class object
        self.t = t
        self.x = x
        self.y = y

class character(object):
    #Creates character object
    def __init__(self,x,y,time):
        #self.t, self.x, and self.y are where the character currently is in this class object
        self.t = time
        self.x = x
        self.y = y
        self.keyframes = []
        self.index = 0
        self.cx = 0
        self.cy = 0
        self.cw = 32
        self.ch = 32
        self.cimg = pygame.image.load("Assets/rpg_maker_vx_sprite_dump_2_by_palinor-d3redzy.png")
        # self.cimg.set_colorkey((255, 255, 255))
        self.aniFrame = 0
        self.aniTime = 0
    def add_keyframe(self,keyPosition,time_offset):
        #Adds a keyframe knowing the position and time offset
        k = KeyFrame(time_offset,keyPosition[0],keyPosition[1])
        self.keyframes.append(k)
    def update(self,dt):
        #Updates on the screen
        if self.index >= len(self.keyframes) - 1:
            return
        self.t += dt
        curkeyF = self.keyframes[self.index]
        nextkeyF = self.keyframes[self.index + 1]
        self.x,self.y = interpolation(curkeyF.x,curkeyF.y,nextkeyF.x,nextkeyF.y,curkeyF.t,nextkeyF.t,self.t)
        result_x = nextkeyF.x - curkeyF.x
        result_y = nextkeyF.y - curkeyF.y
        if self.t >= nextkeyF.t:
            print("Changing current keyframe")
            self.index += 1
        if result_x > result_y:
            if result_x > 0 and result_y == 0:
                self.cy = 64
            elif result_x > 0 and result_y > 0:
                self.cy = 0
            else:
                self.cy = 96
        else:
            if result_x < 0 and result_y == 0:
                self.cy = 32
            elif result_x < 0 and result_y > 0:
                self.cy = 0
            else:
                self.cy = 0
#        print(nextkeyF.x - curkeyF.x)
#        print(nextkeyF.y - curkeyF.y)
        self.aniTime += dt
        if self.aniTime > 0.5:
            self.cx += 32
            if self.cx > 64:
                self.cx = 0
            self.aniTime = 0

    def render(self, screen):
        #Renders character on the screen
        screen.blit(self.cimg,(int(self.x),int(self.y)),(self.cx,self.cy,self.cw,self.ch))
def interpolation(x0,y0,x1,y1,start_time,end_time,current_time):
    #The interpolation function that I think is right
    pcent = (current_time - start_time)/(end_time - start_time)
    x = x0 + pcent * (x1 - x0)
    y = y0 + pcent * (y1 - y0)
    return (x,y)
# x = 400
# y = 300
# c = character(x,y,0)
# c.add_keyframe((800,300),0.0)
# c.add_keyframe((200,300),3.0)
# c.add_keyframe((200,100),6.0)
# c.add_keyframe((600,100),9.0)
# c.add_keyframe((650,290),12.0)
# c.add_keyframe((100,550),15.0)
# c.add_keyframe((100,100),20.0)
# c.add_keyframe((800,600),25.0)
# while True:
#     #Change in time
#     time = clock.tick(60) / 1000
#     c.update(time)
#     #Keyboard events
#     event = pygame.event.poll()
#     if event.type == pygame.QUIT:
#         break
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_ESCAPE]:
#         break
#     #Renders on the screen
#     screen.fill((0,0,0))
#     c.render()
#     pygame.display.flip()
# pygame.display.quit()