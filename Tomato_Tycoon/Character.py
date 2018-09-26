import pygame
import random
from World import *

ssimg = "Assets/rpg_maker_vx_sprite_dump_2_by_palinor-d3redzy.png"
class character(object):
    def __init__(self, sprite_sheet_img, map):
        self.mMap = map
        self.mCurWaypoint = random.choice(map.mInterestPoints)      # A Spot object from the map
        self.mDstWaypoint = self.get_new_destination()              # Also a Spot object
        self.mPos = list(self.mCurWaypoint.mPos)
        self.mSpeed = 50                                            # The speed we moved in pixels/s
        #self.mCharx = 0
        #self.mChary = 0
        self.mCharw = 32
        self.mCharh = 32
        self.mAniTime = 0
        self.mSSimg = sprite_sheet_img
        self.mSpriteNum = random.randint(0, 7)
        self.mFrame = 0
        self.mDir = 0
    def get_new_destination(self):
        neighbor_index = random.choice(self.mCurWaypoint.mNeighborIndicies)
        return self.mMap.mInterestPoints[neighbor_index]


    def update(self, dt):
        # This is based on Tim's interpolation function.  Rather than making it percentage-based (as it was), I
        # based it on the character's speed
        dist = self.mSpeed * dt                     # The distance we're going to move, in pixels

        offx = self.mDstWaypoint.mPos[0] - self.mPos[0] # The "vector" off, going from our current position to the destination waypoint
        offy = self.mDstWaypoint.mPos[1] - self.mPos[1]
        mag = (offx ** 2 + offy ** 2) ** 0.5        # The magnitude of vector off

        # Will we reach the destination this frame?
        if mag <= dist:
            # Yes, we will reach it.  Set our position to the destination waypoint and choose a new destination
            self.mPos = list(self.mDstWaypoint.mPos)
            self.mCurWaypoint = self.mDstWaypoint
            self.mDstWaypoint = self.get_new_destination()
        else:
            # No, we won't reach it.  Just move towards it
            offx /= mag;        offy /= mag             # off is now normalized
            self.mPos[0] += dist * offx                 # Move by the vector off
            self.mPos[1] += dist * offy
        self.mAniTime += dt
        if self.mAniTime > 0.5:
            #self.mCharx += 32
            #if self.mCharx > 64:
            #    self.mCharx = 0
            self.mFrame = self.mFrame + 1
            if self.mFrame > 2:
                self.mFrame = 0
            self.mAniTime = 0


        if abs(offx) >= abs(offy):
            # Left / Right
            if offx < 0:
                self.mDir = 1
            else:
                self.mDir = 2
        else:
            # Up / Down
            if offy < 0:
                self.mDir = 3
            else:
                self.mDir = 0

        """result_x = self.mDstWaypoint.mPos[0] - self.mCurWaypoint.mPos[0]
        result_y = self.mDstWaypoint.mPos[1] - self.mCurWaypoint.mPos[1]
        if result_x > result_y:
            if result_x > 0 and result_y == 0:
                if refx + offsetx == 0 and refy + offsety == 0:
                    self.mDir = 0
                elif refx + offsetx == 96 and refy + offsety == 0:
                    self.mDir = 0
                elif refx + offsetx == 192 and refy + offsety == 0:
                    self.mDir = 0
                elif refx + offsetx == 288 and refy + offsety == 0:
                    self.mDir = 0
                elif refx + offsetx == 0 and refy + offsety == 128:
                    self.mDir = 0
                elif refx + offsetx == 96 and refy + offsety == 128:
                    self.mDir = 0
                elif refx + offsetx == 192 and refy + offsety == 128:
                    self.mDir = 0
                elif refx + offsetx == 288 and refy + offsety == 128:
                    self.mDir = 0
                else:
                    self.mDir = 0
            elif result_x > 0 and result_y > 0:
                if refx + offsetx == 0 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 96 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 192 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 288 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 0 and refy + offsety == 160:
                    self.mDir = 2
                elif refx + offsetx == 96 and refy + offsety == 160:
                    self.mDir = 2
                elif refx + offsetx == 192 and refy + offsety == 160:
                    self.mDir = 2
                elif refx + offsetx == 288 and refy + offsety == 160:
                    self.mDir = 2
                else:
                    self.mDir = 2
            elif result_x > 0 and result_y < 0:
                if refx + offsetx == 0 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 96 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 192 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 288 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 0 and refy + offsety == 192:
                    self.mDir = 2
                elif refx + offsetx == 96 and refy + offsety == 192:
                    self.mDir = 2
                elif refx + offsetx == 192 and refy + offsety == 192:
                    self.mDir = 2
                elif refx + offsetx == 288 and refy + offsety == 192:
                    self.mDir = 2
                else:
                    self.mDir = 2
            else:
                if refx + offsetx == 0 and refy + offsety == 96:
                    self.mDir = 3
                elif refx + offsetx == 96 and refy + offsety == 96:
                    self.mDir = 3
                elif refx + offsetx == 192 and refy + offsety == 96:
                    self.mDir = 3
                elif refx + offsetx == 288 and refy + offsety == 96:
                    self.mDir = 3
                elif refx + offsetx == 0 and refy + offsety == 224:
                    self.mDir = 3
                elif refx + offsetx == 96 and refy + offsety == 224:
                    self.mDir = 3
                elif refx + offsetx == 192 and refy + offsety == 224:
                    self.mDir = 3
                elif refx + offsetx == 288 and refy + offsety == 224:
                    self.mDir = 3
                else:
                    self.mDir = 3
        else:
            if result_x < 0 and result_y == 0:
                if refx + offsetx == 0 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 96 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 192 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 288 and refy + offsety == 64:
                    self.mDir = 2
                elif refx + offsetx == 0 and refy + offsety == 192:
                    self.mDir = 2
                elif refx + offsetx == 96 and refy + offsety == 192:
                    self.mDir = 2
                elif refx + offsetx == 192 and refy + offsety == 192:
                    self.mDir = 2
                elif refx + offsetx == 288 and refy + offsety == 192:
                    self.mDir = 2
                else:
                    self.mDir = 2
            elif result_x < 0 and result_y < 0:
                if refx + offsetx == 0 and refy + offsety == 32:
                    self.mDir = 1
                elif refx + offsetx == 96 and refy + offsety == 32:
                    self.mDir = 1
                elif refx + offsetx == 192 and refy + offsety == 32:
                    self.mDir = 1
                elif refx + offsetx == 288 and refy + offsety == 32:
                    self.mDir = 1
                elif refx + offsetx == 0 and refy + offsety == 160:
                    self.mDir = 1
                elif refx + offsetx == 96 and refy + offsety == 160:
                    self.mDir = 1
                elif refx + offsetx == 192 and refy + offsety == 160:
                    self.mDir = 1
                elif refx + offsetx == 288 and refy + offsetx == 160:
                    self.mDir = 1
                else:
                    self.mDir = 1
            else:
                if refx + offsetx == 0 and refy + offsetx == 0:
                    self.mDir = 0
                elif refx + offsetx == 96 and refy + offsety == 0:
                    self.mDir = 0
                elif refx + offsetx == 192 and refy + offsety == 0:
                    self.mDir = 0
                elif refx + offsetx == 288 and refy + offsety == 0:
                    self.mDir = 0
                elif refx + offsetx == 0 and refy + offsetx == 128:
                    self.mDir = 0
                elif refx + offsetx == 96 and refy + offsety == 128:
                    self.mDir = 0
                elif refx + offsetx == 192 and refy + offsety == 128:
                    self.mDir = 0
                elif refx + offsetx == 288 and refy + offsety == 128:
                    self.mDir = 0
                else:
                    self.mDir = 0"""

    def render(self, surf):
        char_row = self.mSpriteNum // 4
        char_col = self.mSpriteNum % 4
        refx = char_col * self.mCharw * 3
        refy = char_row * self.mCharh * 4
        offsetx = self.mFrame * self.mCharw
        offsety = self.mDir * self.mCharh


        surf.blit(self.mSSimg,(int(self.mPos[0]),int(self.mPos[1])),(refx + offsetx, refy + offsety,self.mCharw,self.mCharh))

