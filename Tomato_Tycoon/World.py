import pygame


class Spot(object):
    def __init__(self, num, line):
        self.mNum = num  # The id number of this spot (these start at 0 and represent the index in the Map's self.mInterestPoints list
        elements = line.split(":")
        self.mName = elements[0]                            # The name of this spot (e.g. Front Door)
        self.mPos = elements[1].split(",")                  # The pixel position of this spot (e.g. (400, 300))
        self.mPos[0] = int(self.mPos[0])
        self.mPos[1] = int(self.mPos[1])
        self.mNeighborIndicies = []                         # A list of index/id numbers (also indicies in Maps's self.mInterestPoints list
                                                            #    of spots we're connected to.
        if line.count(":") == 2:
            indicies = elements[2].split(",")
            for i in range(len(indicies)):
                self.mNeighborIndicies.append(int(indicies[i]) - 1)




class Map:
    def __init__(self, file):
        self.mInterestPoints = []   # A list of Spot objects (waypoints) within the map

        mode = None
        self.width=0
        self.height=0
        self.tileWidth=0
        self.tileHeight=0
        self.orientation=""
        self.tileCodes =[]          # Access an individual tile code like: self.tileCodes[layerNum][row][col]
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
                if mode == "layer":
                    # Make a new (empty) layer
                    self.tileCodes.append([])
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
                fname, twidth, theight, xspacing, yspacing = line[8:].split(",")
                self.tileImage = pygame.image.load("Assets\\" + fname)
                self.ssheetW = self.tileImage.get_width() / self.tileWidth
                self.ssheetH = self.tileImage.get_height() / self.tileHeight
            elif mode == "interest_points":
                if len(line) > 0 and line.count(":") >= 1:
                    self.mInterestPoints.append(Spot(len(self.mInterestPoints), line))
            elif mode=="layer" and line.count(","):
                codes = line.split(",")
                if codes[-1]=="":
                    del codes[-1]
                tempCodes = []
                for val in codes:
                    newVal = int(val)
                    tempCodes.append(newVal)
                    ###################################
                    self.ssheetCol = int((newVal - 1) % self.ssheetW)
                    self.ssheetRow = int((newVal - 1) // self.ssheetW)
                    if newVal not in self.areas:
                        self.areas[newVal] = (self.ssheetCol*self.tileWidth, self.ssheetRow * self.tileHeight, self.tileWidth, self.tileHeight)

                self.tileCodes[-1].append(tempCodes)
        fp.close()

    def render(self, surf):
        for layer in self.tileCodes:
            y = 0
            for row in layer:
                x = 0
                for code in row:
                    surf.blit(self.tileImage, (x,y), self.areas[code])
                    x += self.tileHeight
                y += self.tileWidth


        # Temporary (draw the interest points and connections between them)
        for s in self.mInterestPoints:
            # ... draw the connections between interest points
            for neighbor_index in s.mNeighborIndicies:
                pygame.draw.line(surf, (255,0,0), s.mPos, self.mInterestPoints[neighbor_index].mPos, 2)
        for s in self.mInterestPoints:
            # ... draw the spots
            pygame.draw.circle(surf, (255,0,0), s.mPos, 10)


    def loadPoints(self, pointsText):
        mode = None
        self.storeNames = []
        self.storeCoords = []
        self.storeConnectors = []
        self.gardenNames = []
        self.gardenCoords = []
        self.gardenConnectors = []
        self.mineNames = []
        self.mineCoords = []
        self.mineConnectors = []
        fp = open(pointsText, "r")
        for line in fp:
            line = line.strip()
            if line == "":
                continue
            if len(line) >= 2 and line[0] == "[" and line[-1] == "]":
                mode = line[1:-1]
            elif mode == "Store":
                name, coords, connectors = line.split(":")
                self.storeNames.append(name)
                x, y = coords.split(",")
                self.storeCoords.append((int(x), int(y)))
                connectorList = []
                for connector in connectors.split(","):
                    connectorList.append(int(connector))
                self.storeConnectors.append(connectorList)
            elif mode == "Garden":
                name, coords, connectors = line.split(":")
                self.gardenNames.append(name)
                x, y = coords.split(",")
                self.gardenCoords.append((int(x), int(y)))
                connectorList = []
                for connector in connectors.split(","):
                    connectorList.append(int(connector))
                self.gardenConnectors.append(connectorList)
            elif mode == "Mine":
                name, coords, connectors = line.split(":")
                self.mineNames.append(name)
                x, y = coords.split(",")
                self.mineCoords.append((int(x), int(y)))
                connectorList = []
                for connector in connectors.split(","):
                    connectorList.append(int(connector))
                self.mineConnectors.append(connectorList)


    def get_interest_points(self):
        # Return a list of pixel coordinates (e.g. counter, pedestal1)
        pass

