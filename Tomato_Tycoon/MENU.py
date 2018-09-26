import pygame


class Item:
    def __init__(self, name, fname, desc, amount, type, sellprice):
        self.name = name
        self.fname = fname
        f = pygame.image.load(fname)
        self.img = pygame.transform.scale(f, (32, 32))
        self.description = desc
        self.amount = int(amount)
        self.type = type
        self.sellprice = sellprice
        self.selling = False
        self.planting = False
        self.smelting = False
        self.mining = False
        self.selected = False
        self.percent = 0
        self.percent2 = 0
        self.highlight = (0, 50, 0)


class Craftables:
    def __init__(self, name, recipe_known, timer, recipe):
        self.name = name
        self.crafting = False
        self.selling = False
        self.recipe_known = int(recipe_known)
        self.timer = float(timer)
        self.temp_timer = float(timer)
        #need a self.recipe for file saving purposes
        self.recipe = recipe
        # need to split at the = then , and - to get name and numeric value
        self.recipe_name = []
        self.recipe_cost = []
        temp_r = recipe.split("=")
        temp_r1 = temp_r[-1].split(",")
        for i in range(len(temp_r1)):
            temp_r2 = temp_r1[i].split("-")
            if temp_r2[-1] != "None":
                self.recipe_name.append(temp_r2[0])
                self.recipe_cost.append(int(temp_r2[-1]))
        #recipedata should be passed as ex. "recipe=Wood-5,Iron-3"


class Plantables:
    def __init__(self, name, level, timer, cost, output, baseyield):
        self.name = name
        self.level = int(level)
        self.timer = float(timer)
        self.temptimer = float(timer)
        self.cost = int(cost)
        self.output = output
        self.planting = False
        self.baseyield = int(baseyield)


class Mineables:
    def __init__(self, name, level, minetimer, baseyield, output):
        self.name = name
        self.output = output
        self.level = level
        self.selling = False
        self.digging = False
        self.minetimer = float(minetimer)
        self.temptimer = float(minetimer)

        self.smelttimer = float(minetimer)
        self.temptimer2 = float(minetimer)

        self.baseyield = int(baseyield)


class Harvestables:
    def __init__(self, name, sellprice):
        self.name = name
        self.sellprice = int(sellprice)


class UI:
    def __init__(self, surf, font, imglist, player):
        self.imglist = []
        self.clicked = False
        self.button = 0
        self.map = 0
        self.imgtext = imglist
        for i in imglist:
            temp_img = pygame.image.load(i)
            temp_img = pygame.transform.scale(temp_img, (50, 50))
            temp_img.set_colorkey((255, 255, 255))
            self.imglist.append(temp_img)
        self.g_img = pygame.image.load("Assets/gold.png")

        self.surf = surf
        self.sw = surf.get_width()
        self.sh = surf.get_height()
        self.font = font
        self.gray = (128, 128, 128)
        self.buttonpos = (0, self.sh - 50, self.sw // 10, 50)
        self.player = player

    def update(self, mpos):
        if mpos[0] >= self.buttonpos[0] and mpos[0] <= self.buttonpos[0] + self.buttonpos[2]:
            if mpos[1] >= self.buttonpos[1] and mpos[1] <= self.buttonpos[1] + self.buttonpos[3]:
                if not self.clicked:
                    self.button = 0
                    self.clicked = True
                    return True, False
                else:
                    self.clicked = False
                    return False, False
        if mpos[0] >= self.buttonpos[0] + self.buttonpos[2] and mpos[0] <= self.buttonpos[0] + self.buttonpos[2] * 2:
            if mpos[1] >= self.buttonpos[1] and mpos[1] <= self.buttonpos[1] + self.buttonpos[3]:
                if not self.clicked:
                    self.button = 1
                    self.clicked = True
                    return False, True
                else:
                    self.clicked = False
                    return False, False
        return None

    def arrow(self, mpos):
        if self.map == 0:
            if mpos[0] >= 400 and mpos[0] <= 450 and mpos[1] >= 10 and mpos[1] <= 60:
                self.map = 2
                return [self.map, True]
            elif mpos[0] >= 1150 and mpos[0] <= 1200 and mpos[1] >= 300 and mpos[1] <= 350:
                self.map = 1
                return [self.map, True]
            else:
                return [self.map, False]
        elif self.map == 1:
            if mpos[0] >= 0 and mpos[0] <= 50 and mpos[1] >= 300 and mpos[1] <= 350:
                self.map = 0
                return [self.map, True]
            else:
                return [self.map, False]
        elif self.map == 2:
            if mpos[0] >= 400 and mpos[0] <= 450 and mpos[1] >= 550 and mpos[1] <= 600:
                self.map = 0
                return [self.map, True]
            else:
                return [self.map, False]

    def render(self):
        textlist = ["Inventory", "Upgrade"]
        for i in range(2):
            invtext = pygame.font.Font.render(self.font, textlist[i], True, (255, 255, 255))
            #Grey / dark grey box.
            if self.button == i and self.clicked:
                pygame.draw.rect(self.surf, (64, 64, 64),
                                 (self.buttonpos[0] + self.buttonpos[2] * i, self.buttonpos[1],
                                  self.buttonpos[2], self.buttonpos[3]), 0)
            else:
                pygame.draw.rect(self.surf, (128, 128, 128),
                                 (self.buttonpos[0] + self.buttonpos[2] * i, self.buttonpos[1],
                                  self.buttonpos[2], self.buttonpos[3]), 0)
            #Outline box.
            pygame.draw.rect(self.surf, (255, 255, 255),
                             (self.buttonpos[0] + self.buttonpos[2] * i, self.buttonpos[1],
                              self.buttonpos[2], self.buttonpos[3]), 1)
            self.surf.blit(invtext, (25 + (self.buttonpos[2] * i), self.sh - 30))
        #Gold
        temps = pygame.Surface((150, 60))
        pygame.draw.rect(temps, (0, 0, 0), (0, 0, 150, 60))
        temps.set_alpha(155)
        self.surf.blit(temps, (self.buttonpos[0] + self.buttonpos[2] * 2, self.buttonpos[1]))
        self.surf.blit(self.g_img, (self.buttonpos[0] + self.buttonpos[2] * 2, self.buttonpos[1]))
        gfont = pygame.font.SysFont("Assets//fonts//prototype.ttf", 40)
        temp_a = pygame.font.Font.render(gfont, str(self.player.gold), True, (255, 255, 255))
        self.surf.blit(temp_a, (self.buttonpos[0] + self.buttonpos[2] * 2 + 50, self.buttonpos[1] + 15))
        #Arrows
        if self.map == 0:  # This means we are in shop map as shop == 0
            self.surf.blit(self.imglist[2], (400, 10))
            self.surf.blit(self.imglist[3], (1150, 300))
        elif self.map == 1:  # This means we are in the garden map as garden == 1
            self.surf.blit(self.imglist[0], (0, 300))
        elif self.map == 2:  # This means we are in the mines, as mine == 2
            self.surf.blit(self.imglist[1], (400, 550))

class Inventory:
    def __init__(self, sw, sh, textfile, bigfont, font, map, player):
        self.player = player
        self.selltimer = 1
        self.maxcraft = 0
        self.amountcrafted = 0
        self.actualcraft = 0
        self.actualsmelt = 0
        self.maxsmelt = 0
        self.maxmine = 0
        self.amountsmelt = 0
        self.amountmine = 0
        self.actualmine = 0
        self.slider = 0
        self.selected = False
        self.temp_h = []
        self.temp_c = []
        self.gardenerlevel = 0
        self.minerlevel = 0
        self.amountofscroll = 0
        self.map = map
        self.row = 0
        self.iconsize = 32
        self.templist = []
        self.font = font
        self.bigfont = bigfont
        self.sw = sw
        self.sh = sh
        self.mode = None
        self.inventory = pygame.Surface((sw // 1.2, sh // 1.5))
        self.itemlist = []
        self.craftables = []
        self.plantables = []
        self.mineables = []
        self.harvestables = []
        self.origin = self.sw // 4
        fp = open(textfile, "r")
        for line in fp:
            line = line.strip()
            if line[0] == "[" and line[-1] == "]":
                self.mode = line[1:-1]
            if line[0] != "[" and line[-1] != "]":
                unparsed = line.split(":")
                if self.mode == "Inventory":
                    name = unparsed[0]
                    fname = unparsed[1]
                    desc = unparsed[2]
                    amount = unparsed[3]
                    type = unparsed[4]
                    sellprice = unparsed[5]
                    new_item = Item(name, fname, desc, amount, type, sellprice)
                    self.itemlist.append(new_item)

                if self.mode == "Craftables":
                    name = unparsed[0]
                    recipe_known = unparsed[1]
                    timer = unparsed[2]
                    raw_recipe = unparsed[3]
                    new_craftable = Craftables(name, recipe_known, timer, raw_recipe)
                    self.craftables.append(new_craftable)

                if self.mode == "Plantables":
                    name = unparsed[0]
                    level = unparsed[1]
                    timer = unparsed[2]
                    cost = unparsed[3]
                    output = unparsed[4]
                    baseyield = unparsed[5]
                    new_plantable = Plantables(name, level, timer, cost, output, baseyield)
                    self.plantables.append(new_plantable)

                if self.mode == "Mineables":
                    name = unparsed[0]
                    level = unparsed[1]
                    timer = unparsed[2]
                    baseyield = unparsed[3]
                    output = unparsed[4]
                    new_mineable = Mineables(name, level, timer, baseyield, output)
                    self.mineables.append(new_mineable)

    def sayslider(self):
        z = 0
        if self.amountcrafted > 0:
            z = (self.actualcraft - self.amountcrafted) + 1
        if z <= 0:
            z = 0
        return [str(z), str(round(self.maxcraft, 0))]

    def saveInventory(self, savefile):
        fp = open(savefile, "w")
        fp.write("[Inventory]\n")
        for item in self.itemlist:
            fp.write(item.name + ":" + item.fname + ":" + item.description + ":" + str(item.amount) + ":" + item.type + ":" + item.sellprice + "\n")
        fp.write("[Craftables]\n")
        for craftable in self.craftables:
            fp.write(craftable.name + ":" + str(craftable.recipe_known) + ":" + str(craftable.timer) + ":" + craftable.recipe + "\n")
        fp.write("[Mineables]\n")
        for mineable in self.mineables:
            fp.write(mineable.name + ":" + mineable.level + ":" + str(mineable.minetimer) + ":" + str(mineable.baseyield) + ":" + mineable.output + "\n")
        fp.write(("[Plantables]\n"))
        for plantable in self.plantables:
            fp.write(plantable.name + ":" + str(plantable.level) + ":" + str(plantable.timer) + ":" + str(plantable.cost) + ":" + plantable.output + ":" + str(plantable.baseyield) + "\n")
        fp.close()

    def slide(self, mpos):
        if 300 <= mpos[0] - 50 and mpos[0] + 10 <= 750:
            if 400 <= mpos[1] <= 450:
                self.origin = mpos[0] - 50
                self.slider = (self.origin - 300) / (750 - 350)
                self.selected = True
        if self.selected:
            if mpos[0] > 750:
                self.origin = 690
                self.slider = (self.origin - 300) / (750 - 350)
            if mpos[0] < 300:
                self.origin = 300
                self.slider = (self.origin - 300) / (750 - 350)
            elif 300 <= mpos[0] - 50 and mpos[0] + 10 <= 750:
                self.origin = mpos[0] - 50
                self.slider = (self.origin - 300) / (750 - 350)
        self.maxcraft = self.slider * 100
        if self.maxcraft <= 0:
            self.maxcraft = 1
        if self.maxcraft >= 97.5:
            self.maxcraft = 100

    def released(self):
        self.selected = False

    def mapupdate(self, mapnum):
        self.map = mapnum
        self.amountofscroll = 0
        self.row = 0

    def update(self, dt):
        self.templist = []
        if self.map == 0:
            for l in self.itemlist:
                if l.type == "c" or l.type == "h":
                    self.templist.append(l)
            for t in self.templist:
                if t.type == "c":
                    for c in self.craftables:
                        if c.name == t.name:
                            if c.crafting:
                                if self.amountcrafted <= self.actualcraft:
                                    c.temp_timer -= dt
                                    t.percent = c.temp_timer / c.timer
                                    if c.temp_timer <= 0:
                                        c.temp_timer = c.timer
                                        t.amount += 1
                                        self.amountcrafted += 1
                                else:
                                    self.amountcrafted = 0
                                    c.crafting = False
                if t.type == "c" or t.type == "h":
                    if t.selling:
                        self.selltimer -= dt
                        if self.selltimer <= 0:
                            self.selltimer = 1
                            if t.amount > 0:
                                t.amount -= 1
                                self.player.changeGold(t.sellprice)

        if self.map == 1:
            for l in self.itemlist:
                if l.type == "p":
                    self.templist.append(l)
                if l.type == "h":
                    self.temp_h.append(l)
            for l in self.templist:
                for p in self.plantables:
                    if l.name == p.name:
                        if l.amount >= 1:
                            p.planting = True
                            p.temptimer -= dt
                            l.percent = p.temptimer / p.timer
                            if p.temptimer <= 0:
                                l.amount -= 1
                                p.planting = False
                                for h in self.temp_h:
                                    if h.name == p.output:
                                        h.amount += p.baseyield
                                        break
                                p.temptimer = p.timer
                                
        if self.map == 2:
            for l in self.itemlist:
                if l.type == "m":
                    self.templist.append(l)
            for t in self.templist:
                for c in self.mineables:
                    if t.name == c.name:
                        if t.mining:
                            if self.amountmine < self.maxcraft:
                                c.temptimer -= dt
                                t.percent = c.temptimer / c.minetimer
                                if c.temptimer <= 0:
                                    c.temptimer = c.minetimer
                                    t.amount += 1 * c.baseyield
                                    self.amountmine += 1
                            else:
                                t.mining = False
                                self.amountmine = 0

                            if t.smelting:
                                if self.amountsmelt < self.actualsmelt:
                                    c.temptimer2 -= dt
                                    t.percent2 = c.temptimer2 / c.smelttimer
                                    if c.temptimer2 <= 0:
                                        c.temptimer2 = c.smelttimer
                                        t.amount -= 3
                                        self.amountsmelt += 1
                                        for i in self.itemlist:
                                            if c.output == i.name:
                                                i.amount += 1
                                                break
                                else:
                                    t.smelting = False
        for l in self.templist:
            if l.selling and l.selected:
                l.highlight = (180, 150, 0)
            if l.selling and not l.selected:
                l.highlight = (255, 200, 0)
            if not l.selling and not l.selected:
                l.highlight = (0, 50, 0)
            if not l.selling and l.selected:
                l.highlight = (128, 200, 128)

    def hitbox(self, mpos, inventory):
        if inventory:
            if self.map == 0:
                if 50 < mpos[0] < (self.sw // 4) + 50:
                    if 50 < mpos[1] < (self.sh // 1.5) + 50:
                        self.row = mpos[1] // 32 + self.amountofscroll - 2
                        for i in self.templist:
                            i.selected = False
                        if self.row < len(self.templist):
                            self.templist[self.row].selected = True
            if self.map == 1:
                if 50 < mpos[0] < (self.sw // 4) + 50:
                    if 50 < mpos[1] < (self.sh // 1.5) + 50:
                        self.row = mpos[1] // 32 + self.amountofscroll - 2
                        for i in self.templist:
                            i.selected = False
                        if self.row < len(self.templist):
                            self.templist[self.row].selected = True

            if self.map == 2:
                if 50 < mpos[0] < (self.sw // 4) + 50:
                    if 50 < mpos[1] < (self.sh // 1.5) + 50:
                        self.row = mpos[1] // 32 + self.amountofscroll - 2
                        for i in self.templist:
                            i.selected = False
                        if self.row < len(self.templist):
                            self.templist[self.row].selected = True

            if self.sw // 1.2 - self.sw // 4 + 50 < mpos[0] < self.sw // 1.2 + 50:
                if 50 < mpos[1] < self.sh // 1.5 + 50:
                    button_num = (mpos[1] - 50) // 81  # Button nums are as follows: (0 = Crafting, 1 = plant, etc.)

                    if self.templist[self.row].type == "c":
                        total = 0
                        num = 0
                        if button_num == 0:
                            for c in self.craftables:
                                if c.name == self.templist[self.row].name:
                                    print(c.recipe_known, self.player.craftskill)
                                    if c.recipe_known <= self.player.craftskill:
                                        for r in range(len(c.recipe_name)):
                                            for j in self.itemlist:
                                                if c.recipe_name[r] == j.name:
                                                    if j.amount >= c.recipe_cost[r]:
                                                        total += 1
                                        if total == len(c.recipe_name)  and self.player.craftskill >= c.recipe_known:
                                            for z in range(int(self.maxcraft)):
                                                for r in range(len(c.recipe_name)):
                                                    for j in self.itemlist:
                                                        if c.recipe_name[r] == j.name:
                                                            if j.amount >= c.recipe_cost[r]:
                                                                j.amount -= c.recipe_cost[r]
                                                                num = z
                                            self.actualcraft = num
                                            c.crafting = True
                                            break
                        if button_num == 4:
                            if self.templist[self.row].selling:
                                self.templist[self.row].selling = False
                            elif self.templist[self.row].type != "p" and self.templist[self.row].type != "m":
                                self.templist[self.row].selling = True
                    if self.templist[self.row].type == "p":
                        if button_num == 1:
                            for p in self.plantables:
                                if p.name == self.templist[self.row].name:
                                    for z in range(int(self.maxcraft)):
                                        if self.player.gold >= p.cost:
                                            self.player.changeGold(-p.cost)
                                            self.templist[self.row].planting = True
                                            self.templist[self.row].amount += 1
                                        else:
                                            break
                    if self.templist[self.row].type == "m":
                        if button_num == 2:
                            self.templist[self.row].mining = True

                        if button_num == 3 and self.templist[self.row].amount >= 3:
                            self.templist[self.row].smelting = True
                            b = self.templist[self.row].amount
                            self.maxsmelt = self.maxcraft
                            for i in range(int(self.maxsmelt)):
                                if b >= 1:
                                    b -= 1
                                    self.actualsmelt = i
                                else:
                                    self.maxsmelt = self.actualsmelt

                        
                    if self.templist[self.row].type == "h":
                        if button_num == 4:
                            if self.templist[self.row].selling:
                                self.templist[self.row].selling = False
                            else:
                                self.templist[self.row].selling = True

    def scroll(self, scrolling):
        if self.amountofscroll <= 0 and scrolling == -1:
            return False
        if self.templist != []:
            if self.amountofscroll >= len(self.templist) - ((self.sh // 1.5) / 32) and scrolling == 1:
                return False
            else:
                self.amountofscroll += scrolling
        elif self.templist == []:
            return False


    def render(self, surf, inventory):
        if inventory:
            y = 32 * self.amountofscroll
            self.inventory.fill((0, 55, 0))
            # Description box
            if self.row < (len(self.templist)):
                temp_a = pygame.font.Font.render(self.font, self.templist[self.row].description, True, (255, 255, 255))
                pygame.draw.rect(self.inventory, (255, 255, 255), (self.sw // 4, 0, self.sw // 3, self.sh // 3), 1)
                self.inventory.blit(temp_a, (self.sw // 4, 0))
            else:
                self.row = 0
            # Recipe box
            if self.map == 0:
                pygame.draw.rect(self.inventory, (255, 255, 255), (self.sw // 4, self.sh // 3, self.sw // 3, self.sh // 3), 1)
                for i in range(len(self.craftables)):
                    if self.craftables[i].name == self.templist[self.row].name:
                        for g in range(len(self.craftables[i].recipe_name)):
                            temp_name = self.craftables[i].recipe_name[g]
                            temp_cost = self.craftables[i].recipe_cost[g]
                            temp_a = pygame.font.Font.render(self.font, str(temp_name) + "  " + str(temp_cost), True,
                                                             (255, 255, 255))
                            self.inventory.blit(temp_a, (self.sw // 4, (self.sh // 3) + 10 * g))

            # The slider, Goes in the middle.
            pygame.draw.line(self.inventory, (255, 255, 255), (self.sw // 4, self.sh // 1.5 - 25),
                             (self.sw // 4 + self.sw // 3, self.sh // 1.5 - 25))
            # self.origin = the leftmost part of the slider
            pygame.draw.rect(self.inventory, (128, 128, 128), (self.origin, self.sh // 1.5 - 50, 10, 50))
            pygame.draw.rect(self.inventory, (255, 255, 255), (self.sw // 4, self.sh // 1.5 - 50, self.sw // 3, 50), 1)

            # Left hand box - pretty standard stuff, just blit all things in inv list to scroll through.
            # Future plans for this area- Seperate items based on [c,p,m,h] variables. make all p in the Garden, etc.

            pygame.draw.rect(self.inventory, (255, 255, 255),
                             (0, 0, self.sw // 4, len(self.itemlist) * self.iconsize), 1)

            for l in self.templist:
                pygame.draw.rect(self.inventory, l.highlight, (1, (32 * (self.templist.index(l) - self.amountofscroll))
                                                               + 1, (self.sw // 4) - 1, 32))

            if self.map == 0:
                g = 0
                for l in self.templist:
                    if l.type == "c":
                        for c in self.craftables:
                            if c.name == l.name:
                                if c.crafting:
                                    #pygame.draw.rect(self.inventory, (128, 128, 128), (0,
                                    #                (32 * (self.row - self.amountofscroll)),self.sw // 4, 32))
                                    pygame.draw.rect(self.inventory, (255, 0, 0), (0,
                                                    (32 * (g - self.amountofscroll) + 1), (self.sw // 4) * l.percent, 32))
                                if l == self.templist[self.row]:
                                    if c.crafting is False:
                                        #pygame.draw.rect(self.inventory, (128, 128, 128), (0,
                                        #                (32 * (self.row - self.amountofscroll)), self.sw // 4, 32))
                                        pass
                    if l.type == "h":
                        if l == self.templist[self.row]:
                            #pygame.draw.rect(self.inventory, (128, 128, 128), (0,
                            #                (32 * (self.row - self.amountofscroll)),self.sw // 4, 32))
                            pass
                    temp_a = pygame.font.Font.render(self.font, str(l.name), True, (255, 255, 255))
                    temp_b = pygame.font.Font.render(self.font, "x " + str(l.amount), True, (255, 255, 255))
                    self.inventory.blit(l.img, (0, (32 * g) - y))
                    self.inventory.blit(temp_a, (32, (32 * g) - y + 12))
                    self.inventory.blit(temp_b, (self.sw // 5, (32 * g) - y + 12))
                    g += 1

            if self.map == 1:
                g = 0
                for l in self.templist:
                    if l.type == "p":
                        for p in self.plantables:
                            if p.name == l.name:
                                if p.planting:
                                    #pygame.draw.rect(self.inventory, (128, 128, 128), (0,
                                    #                (32 * (self.row - self.amountofscroll)),self.sw // 4, 32))
                                    pygame.draw.rect(self.inventory, (0, 200, 0), (0,
                                                    (32 * (g - self.amountofscroll) + 1), (self.sw // 4) * l.percent, 32))
                    temp_a = pygame.font.Font.render(self.font, str(l.name), True, (255, 255, 255))
                    temp_b = pygame.font.Font.render(self.font, "x " + str(l.amount), True, (255, 255, 255))
                    self.inventory.blit(l.img, (0, (32 * g) - y))
                    self.inventory.blit(temp_a, (32, (32 * g) - y + 12))
                    self.inventory.blit(temp_b, (self.sw // 5, (32 * g) - y + 12))
                    g += 1

            if self.map == 2:
                g = 0
                for l in self.templist:

                    if l.type == "m":
                        if l == self.templist[self.row]:
                            pass
                            #pygame.draw.rect(self.inventory, (128, 128, 128), (0,
                            #                (32 * (self.row - self.amountofscroll)), self.sw // 4, 32))
                    for m in self.mineables:
                        if m.name == l.name:
                            if l.mining:
                                #pygame.draw.rect(self.inventory, (128, 128, 128),
                                #                 (0, (32 * (self.row - self.amountofscroll)), self.sw // 4, 32))
                                pygame.draw.rect(self.inventory,(0, 0, 255), (0, (32 * (g - self.amountofscroll)+ 1),
                                                                              (self.sw // 4) * l.percent, 32))
                            if l.smelting:
                                #pygame.draw.rect(self.inventory, (128, 128, 128),
                                #                 (0, (32 * (self.row - self.amountofscroll)), self.sw // 4, 32))
                                pygame.draw.rect(self.inventory,(180, 0, 255), (0, (32 * (g - self.amountofscroll)+ 1),
                                                                              (self.sw // 4) * l.percent2, 32))
                            if l == self.templist[self.row]:
                                if l.mining is False:
                                    pass
                                    #pygame.draw.rect(self.inventory, (128, 128, 128), (0,
                                    #                (32 * (self.row - self.amountofscroll)), self.sw // 4, 32))

                    temp_a = pygame.font.Font.render(self.font, str(l.name), True, (255, 255, 255))
                    temp_b = pygame.font.Font.render(self.font, "x " + str(l.amount), True, (255, 255, 255))
                    self.inventory.blit(l.img, (0, (32 * g) - y))
                    self.inventory.blit(temp_a, (32, (32 * g) - y + 12))
                    self.inventory.blit(temp_b, (self.sw // 5, (32 * g) - y + 12))
                    g += 1

            # Right hand box - For the buttons [Craft, Plant, Dig, Smelt, Sell] - make them grey out if not available
            buttonlist = ["Craft", "Plant", "Dig", "Smelt", "Sell"]
            color = (128, 128, 128)
            if self.templist != []:
                for i in range(len(buttonlist)):
                    if self.templist[self.row].type == "c":
                        if 0 < i < 4:
                            color = (64, 64, 64)
                        if i >= 4:
                            color = (128, 128, 128)
                    if self.templist[self.row].type == "h":
                        if i < 4:
                            color = (64, 64, 64)
                        else:
                            color = (128, 128, 128)
                    if self.templist[self.row].type == "m":
                        if i < 2 or i == 4:
                            color = (64, 64, 64)
                        else:
                            color = (128, 128, 128)
                    if self.templist[self.row].type == "p":
                        if i == 0 or i > 1:
                            color = (64, 64, 64)
                        if i == 1:
                            color = (128, 128, 128)
                    spacing_y = (self.sh // 1.5) // len(buttonlist) + 1
                    temp_a = pygame.font.Font.render(self.bigfont, buttonlist[i], True, (255, 255, 255))
                    pygame.draw.rect(self.inventory, color, (self.sw // 1.2 - self.sw // 4, spacing_y * i,
                                                                       self.sw // 4, spacing_y * (i + 1)))
                    pygame.draw.rect(self.inventory, (255, 255, 255), (self.sw // 1.2 - self.sw // 4, spacing_y * i,
                                                                       self.sw // 4, spacing_y * (i + 1)), 1)
                    self.inventory.blit(temp_a, (self.sw // 1.2 - self.sw // 4 + 10, spacing_y * i + 10))
            else:
                for i in range(len(buttonlist)):
                    color = (64, 64, 64)
                    spacing_y = (self.sh // 1.5) // len(buttonlist) + 1
                    temp_a = pygame.font.Font.render(self.bigfont, buttonlist[i], True, (255, 255, 255))
                    pygame.draw.rect(self.inventory, color, (self.sw // 1.2 - self.sw // 4, spacing_y * i,
                                                             self.sw // 4, spacing_y * (i + 1)))
                    pygame.draw.rect(self.inventory, (255, 255, 255), (self.sw // 1.2 - self.sw // 4, spacing_y * i,
                                                                       self.sw // 4, spacing_y * (i + 1)), 1)
                    self.inventory.blit(temp_a, (self.sw // 1.2 - self.sw // 4 + 10, spacing_y * i + 10))

            pygame.draw.rect(self.inventory, (255, 255, 255), (self.sw // 1.2 - self.sw // 4, 0, self.sw // 4,
                                                               self.sh // 1.5), 1)
            surf.blit(self.inventory, (50, 50))


class Player:
    def __init__(self, loadfile):
        self.mode = ""
        self.gold = 0
        self.upgradeList = []
        fp = open(loadfile, "r")
        for line in fp:
            line = line.strip()
            if line[0] == "[" and line[-1] == "]":
                self.mode = line[1:-1]
            if line[0] != "[" and line[-1] != "]":
                unparsed = line.split(":")
                if self.mode == "Upgrades":
                    newUpgrade = [unparsed[0], unparsed[1], unparsed[2]]
                    self.upgradeList.append(newUpgrade)
                if self.mode == "Gold":
                    self.gold = int(unparsed[0])
        self.craftskill = int(self.upgradeList[0][1])
        self.plantskill = int(self.upgradeList[1][1])
        self.mineskill = int(self.upgradeList[2][1])
        self.workercount = int(self.upgradeList[3][1])

    def saygold(self):
        return self.gold

    def upgrade(self, input):
        if str(input[0]) == "craftskill":
            self.craftskill += input[1]
        if str(input[0]) == "plantskill":
            self.plantskill += input[1]
        if str(input[0]) == "mineskill":
            self.mineskill += input[1]
        if str(input[0]) == "worker":
            self.workercount += input[1]

    def savePlayer(self, saveitem):
        #Very hardcoded, needs gold cost of upgrades to be implented. Dictionary would also be a good idea
        #in case future upgrades are created.
        fp = open(saveitem, "w")
        fp.write("[Upgrades]\n")
        fp.write("crafting:" + str(self.craftskill) + ":100\n")
        fp.write("gardening:" + str(self.plantskill) + ":100\n")
        fp.write("mining:" + str(self.mineskill) + ":100\n")
        fp.write("worker:" + str(self.workercount) + ":300\n")
        fp.write("[Gold]\n")
        fp.write(str(self.gold))

    def changeGold(self, amount):
        self.gold += int(amount)

class Upgrade:
    def __init__(self, surf, font, player):
        self.cost = {}
        self.cost["craftskill"] = 100
        self.cost["mineskill"] = 100
        self.cost["plantskill"] = 100
        self.cost["worker"] = 100
        self.button = 0
        self.clicked = False
        self.font = font
        self.player = player
        self.sw = surf.get_width()
        self.sh = surf.get_height()
        self.surf = surf
        self.window = pygame.Surface((200, 200))
        self.windowh = self.window.get_height()
        self.buttonpos = [0, 0, 200, self.windowh // 4]

    def hitbox(self, mpos, upgrade):
        if upgrade:
            if 50 < mpos[0] < 250:
                if 50 < mpos[1] < 250:
                    self.button = (mpos[1] // 50) - 1
                    self.clicked = True

    def released(self, gold):
        if self.clicked:
            self.clicked = False
            if self.button == 0 and self.cost["craftskill"] <= gold:
                self.cost["craftskill"] += 20 * int(self.player.craftskill)
                self.player.changeGold(-20 * int(self.player.craftskill))
                return ["craftskill", 1]
            elif self.button == 1 and self.cost["plantskill"] <= gold:
                self.cost["plantskill"] += 20 * int(self.player.plantskill)
                self.player.changeGold(-20 * int(self.player.plantskill))
                return ["plantskill", 1]
            elif self.button == 2 and self.cost["mineskill"] <= gold:
                self.cost["mineskill"] += 20 * int(self.player.mineskill)
                self.player.changeGold(-20 * int(self.player.mineskill))
                return ["mineskill", 1]
            elif self.button == 3 and self.cost["worker"] <= gold:
                self.cost["worker"] += 20 * int(self.player.workercount)
                self.player.changeGold(-20 * int(self.player.workercount))
                return ["worker", 1]
            return None

    def render(self, player):
        self.window.fill((0, 55, 0))
        pygame.draw.rect(self.window, (255, 255, 255), (0, 0, 500, 400), 1)
        textlist = ["Smith Skill: " + str(player.craftskill) + "    costs: " + str(self.cost["craftskill"]),
                    "Plant Skill: " + str(player.plantskill) + "    costs: " + str(self.cost["plantskill"]),
                    "Miner Skill: " + str(player.mineskill) + "    costs: " + str(self.cost["mineskill"]),
                    "Hire Worker: " + str(player.workercount) + "   costs: " + str(self.cost["worker"])]
        for i in range(4):
            temp_a = pygame.font.Font.render(self.font, str(textlist[i]), True, (255, 255, 255))
            if i == self.button and self.clicked:
                pygame.draw.rect(self.window, (64, 64, 64), (self.buttonpos[0],
                                                                self.buttonpos[1] + (self.buttonpos[3] * i),
                                                                self.buttonpos[2], self.buttonpos[3]), 0)
                pygame.draw.rect(self.window, (255, 255, 255), (self.buttonpos[0],
                                                                self.buttonpos[1] + (self.buttonpos[3] * i),
                                                                self.buttonpos[2], self.buttonpos[3]), 1)

            else:
                pygame.draw.rect(self.window, (128, 128, 128), (self.buttonpos[0],
                                                                self.buttonpos[1] + (self.buttonpos[3] * i),
                                                                self.buttonpos[2], self.buttonpos[3]), 0)
                pygame.draw.rect(self.window, (255, 255, 255), (self.buttonpos[0],
                                                                self.buttonpos[1] + (self.buttonpos[3] * i),
                                                                self.buttonpos[2], self.buttonpos[3]), 1)
            self.window.blit(temp_a, (5, self.buttonpos[1] + (self.buttonpos[3] * i) + 20))
        self.surf.blit(self.window, (50, 50))
