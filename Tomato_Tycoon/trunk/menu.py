class MenuItem:
    """ A single line of text in a menu similar to.  On the "Task List" pane (6th page of Emm's original pitch), this
        might represent the "Hot Water" line, for example.  """
    def __init__(self, icon, text, color):
        pass


    def render(self, surf, isActive):
        pass


class Menu:
    """ A menu page (see the "Task List" menu pane on the 6th page of Emm's original pitch for a visual reference """
    def __init__(self, font_object, background, area, text_normal_color, text_hilight_color):
        self.mItems = []                        # A list of MenuItem objects
        self.mFont = font_object                # The font used to render all text in this menu
        self.mBackground = background           # A color or an image
        self.mArea = area                       # A pygame rectangle
        self.mNormalTextColor = text_normal_color   # The color to draw the text of a not-highlighted menu item
        self.mHilightTextColor = text_hilight_color # The color to draw the text of a highlighted menu item
        self.mActiveItem = None                 # A reference to one element of mItems that's "active" (or None if no
                                                #    items are active (and this won't be highlighted)


    def addItem(self, I):
        self.mItems.append(I)

    def render(self, surf):
        """ Draws the background then draws all menu items in order.  Eventually we'll need to add the ability to
            scroll (for now, though, just assume everything will fit).  Make sure the highlight the active item,
            if there is one. """
        pass

    def handleEvent(self, event):
        """ Handle this pygame event, if it's something related to menu's.  In particular, change the
            active item if up / down (W / S) are pressed or if the mouse is hovering over an item. """
        pass