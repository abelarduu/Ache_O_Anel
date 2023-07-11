#############
#Ache O Anel#
#############
import pyxel

class Object(object):
    def __init__(self, x,y,img,imgx,imgy,w,h):
        self.x, self.y= x, y
        self.img, self.imgx,self.imgy= img, imgx, imgy
        self.w, self.h= w,h
        self.mouseClick= False
                
    def draw(self):
        pyxel.blt(self.x,self.y,self.img,self.imgx,self.imgy,self.w,self.h)

class Game:
    def __init__(self):
        pyxel.init(90,140,"Ache O Anel")
        #Variaveis inciais
        self.play= False
        self.chose_mode= False
        #objetos
        self.gameHand=Object(3,44,1,0,0,40,93)
        self.gameCup= Object(pyxel.width-43,44,1,0,93,40,93)
        self.modeList= [self.gameHand, self.gameCup]
        
        pyxel.load("resources/Ache_O_Anel.pyxres")
        pyxel.run(self.update,self.draw)
        
    def update(self):
        #Game Em execução
        if self.play:
             #Escolha do modo de game
            if self.chose_mode:
                for btn in self.modeList:
                    if pyxel.mouse_x >= btn.x and pyxel.mouse_x <= btn.x + btn.w:
                        if pyxel.mouse_y >= btn.y and pyxel.mouse_y <= btn.y +btn.h:
                            btn.imgx= 40
                            btn.y= 43
                            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                                btn.y= 44
                                btn.imgx= 80
                    else: 
                        btn.imgx= 0
                        btn.y= 44 
        #Menu Inicial
        else:
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                self.play= True
                self.chose_mode= True

    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(True)
        #Game Em execução
        if self.play:
            #Escolha do modo de game
            if self.chose_mode:

                pyxel.blt(0,0,0,90,0,90,140)
                for btn in self.modeList: btn.draw()
                pyxel.text(pyxel.width/2 - len("Escolha um modo:")/2 *4,37,"Escolha um modo:",7)
            #if modo mão
            #if modo copo
                
        #Menu Inicial
        else:
            pyxel.blt(0,0,0,0,0,90,140)
            pyxel.text(pyxel.width/2 - len("Clique para continuar")/2 *4,133,"Clique para continuar",7)#pyxel.frame_count %16)

#Verificação da execução direta do módulo
if __name__ == "__main__":
    Game()