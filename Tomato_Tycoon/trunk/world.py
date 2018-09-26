import pygame

class Map:
    def __init__(self, file):
        mode = None
        self.width=0
        self.height=0
        self.tileWidth=0
        self.tileHeight=0
        self.orientation=""
        self.tileCodes =[]
        self.ssheetCol = 0
        self.ssheetRow = 0
        self.areas = {}
        self.cx = 0
        self.cy = 0
        fp = open(file,"r")
        for line in fp:
            line = line.strip()
            if line == "":
                continue
            if len(line)>=2 and line[0]=="[" and line[-1]=="]":
                mode=line[1:-1]
            elif mode=="header":
                headerLines = line.split("=")
                attr = headerLines[0]
                value = headerLines[1]
                if attr=="width":
                   self.width=int(value)
                elif attr=="height":
                   self.height=int(value)
                elif attr=="tilewidth":
                    self.tileWidth=int(value)
                elif attr=="tileheight":
                    self.tileHeight=int(value)
                elif attr=="orientation":
                    self.orientation=value
            elif mode == "tilesets":
                self.tileSets = []
                fname, twidth, theight, xspacing, yspacing = line[8:].split(",")
                self.tileImage = pygame.image.load("Assets\\" + fname)
                ssheetW = self.tileImage.get_width() / self.tileWidth
                ssheetH = self.tileImage.get_height() / self.tileHeight
                totalTiles = (self.tileImage.get_width() // int(twidth)) * (self.tileImage.get_height() // int(theight)) - 1
                newTileSet = [self.tileImage, ssheetW, ssheetH, totalTiles]
                self.tileSets.append(newTileSet)
            elif mode=="layer" and line.count(","):
                codes = line.split(",")
                if codes[-1]== "":
                    del codes[-1]
                tempCodes = []
                for val in codes:
                    newVal = int(val)
                    tempCodes.append(newVal)
                    ###################################
                    for tileset in self.tileSets:
                        # prevTotal = self.tileSets[self.tileSets.index(tileset) - 1][3]
                        # if newVal > prevTotal:
                        #     self.ssheetCol = int(((newVal - prevTotal) - 1) % tileset[1])
                        #     self.ssheetRow = int(((newVal - prevTotal) - 1) // tileset[1])
                        # if newVal not in self.areas:
                        #     self.areas[newVal] = (self.ssheetCol*self.tileWidth, self.ssheetRow * self.tileHeight, self.tileWidth, self.tileHeight)
                        if newVal < tileset[3]:
                            self.ssheetCol = int(((newVal - 1) % tileset[1]))
                            self.ssheetRow = int(((newVal - 1) // tileset[2]))
                        else:
                            prevTotal = self.tileSets[self.tileSets.index(tileset) - 1][3]
                            self.ssheetCol = int(((newVal - prevTotal - 1) % tileset[1]))
                            self.ssheetRow = int(((newVal - prevTotal - 1) // tileset[2]))
                        if newVal not in self.areas:
                            self.areas[newVal] = (self.ssheetCol*self.tileWidth, self.ssheetRow * self.tileHeight, self.tileWidth, self.tileHeight)


                    self.tileCodes.append(tempCodes)
        fp.close()

    def render(self, surf):
        x = 0
        for row in self.tileCodes:
            y = 0
            for code in row:
                for tileset in self.tileSets:
                    if code < tileset[3]:
                        surf.blit(tileset[0], (x,y), self.areas[code])
                    y += self.tileHeight
            x += self.tileWidth