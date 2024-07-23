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
        
        self.mouse_up = False
        self.mouse_click = False
        self.mouse_pressed = False
        self.mouse_released = False
        self.ring = pyxel.rndi(0, 1)
        
    def check_click(self, padx1=0, padx2=0, pady1=0, pady2=0):
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
            self.mouse_up = True
            
            # Mouse Click
            # Verifica se o botão do mouse está pressionado
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.mouse_click = True
            else:
                self.mouse_click = False
                
            # Mouse Pressed
            # Verifica se o botão do mouse foi pressionado no quadro atual
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.mouse_pressed = True
            else:
                self.mouse_pressed = False
            
            # Mouse released
            # Verifica se o botão do mouse foi solto
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                self.mouse_released = True
            else:
                self.mouse_released = False
        else:
            self.mouse_up = False
    
    def draw(self):
        """Desenha o objeto na tela usando a imagem e as coordenadas especificadas."""
        pyxel.blt(self.x,
                  self.y,
                  self.img,
                  self.imgx,
                  self.imgy,
                  self.w,
                  self.h)
