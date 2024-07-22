import pyxel

# Padronização Geral dos Objetos
class Object(object):
    def __init__(self, x, y, img, imgx, imgy, w, h):
        """Inicializa um novo objeto com as coordenadas, imagem, e dimensões especificadas."""
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
        
    def verClick(self, padx1=0, padx2=0, pady1=0, pady2=0):
        """Verifica a interação do mouse com o objeto e atualiza os estados de clique e pressão."""
        POSX1 = self.x + padx1
        POSX2 = self.x + self.w + padx2
        POSY1 = self.y + pady1
        POSY2 = self.y + self.h + pady2
        
        # Verifica se o mouse está dentro da área do objeto
        if (pyxel.mouse_x >= POSX1 and
            pyxel.mouse_x <= POSX2 and
            pyxel.mouse_y >= POSY1 and
            pyxel.mouse_y <= POSY2):
            self.mouseUp = True
            
            # Mouse Click
            # Verifica se o botão do mouse está pressionado
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.mouseClick = True
            else:
                self.mouseClick = False
                
            # Mouse Pressed
            # Verifica se o botão do mouse foi pressionado no quadro atual
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.mousePressed = True
            else:
                self.mousePressed = False
            
            # Mouse released
            # Verifica se o botão do mouse foi solto
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                self.mouseReleased = True
            else:
                self.mouseReleased = False
        else:
            self.mouseUp = False
    
    def draw(self):
        """Desenha o objeto na tela usando a imagem e as coordenadas especificadas."""
        pyxel.blt(self.x,
                  self.y,
                  self.img,
                  self.imgx,
                  self.imgy,
                  self.w,
                  self.h)
