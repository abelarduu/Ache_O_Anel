import pyxel

# Padronização Geral dos Objetos
class Object(object):
    def __init__(self, x, y, img, imgx, imgy, w, h):
        self.x = x
        self.y = y
        self.img = img
        self.imgx = imgx
        self.imgy = imgy
        self.w = w
        self.h = h
        
        self.mouseUp = False
        self.mouseClick = False
        self.mousePressed = False
        self.mouseReleased = False
        self.ring = pyxel.rndi(0, 1)
        
    def verClick(self, padx1= 0, padx2= 0, pady1= 0, pady2= 0):
        POSX1 = self.x + padx1
        POSX2 = self.x + self.w + padx2
        POSY1 = self.y + pady1
        POSY2 = self.y + self.h + pady2
        # Mouse Up
        if (pyxel.mouse_x >= POSX1 and
            pyxel.mouse_x <= POSX2 and
            pyxel.mouse_y >= POSY1 and
            pyxel.mouse_y <= POSY2):
            self.mouseUp = True
            
            # Mouse Click
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.mouseClick = True
            else:
                self.mouseClick = False
                
            # Mouse Pressed
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.mousePressed = True
            else:
                self.mousePressed = False
            
            # Mouse released
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                self.mouseReleased = True
            else:
                self.mouseReleased = False
        # Mouse Out
        else:
            self.mouseUp = False
    
    def draw(self):
        pyxel.blt(self.x,
                  self.y,
                  self.img,
                  self.imgx,
                  self.imgy,
                  self.w,
                  self.h)