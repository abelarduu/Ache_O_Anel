#############
#Ache O Anel#
#############
import pyxel

#Padronização Geral dos Objetos
class Object(object):
    def __init__(self, x,y,img,imgx,imgy,w,h):
        self.x= x
        self.y= y
        self.img= img
        self.imgx= imgx
        self.imgy= imgy
        self.w= w
        self.h= h
        
        self.ring= pyxel.rndi(0,1)
        self.mouseUp=  False
        self.mouseClick= False
        self.mousePressed= False
        self.mouseRealesed= False
        
    def verClick(self, x1=0, x2=0, y1=0, y2=0):
        if pyxel.mouse_x >= self.x+x1 and pyxel.mouse_x <= self.x + self.w+x2 \
            and pyxel.mouse_y >= self.y+y1 and pyxel.mouse_y <= self.y + self.h+y2:
                self.mouseUp=True
                if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                    self.mouseClick=True
                else:self.mouseClick=False
                    
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.mousePressed=True
                else:self.mousePressed=False
                
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                    self.mouseRealesed=True
                else:self.mouseRealesed=False
        else:self.mouseUp=False
    
    def draw(self):
        pyxel.blt(self.x,self.y,self.img,self.imgx,self.imgy,self.w,self.h)

class Game:
    def __init__(self):
        pyxel.init(90,140,"Ache O Anel")
        #Variaveis inciais
        self.play= False
        self.chose_mode= False
        self.gameHand= False
        self.gameCup= False
        #objetos
        self.btnMode1=Object(3,44,1,0,0,40,93)
        self.btnMode2= Object(pyxel.width-43,44,1,0,93,40,93)
        self.btnMode1.modeName="Hand"
        self.btnMode2.modeName="Cup"
        self.modeList= [self.btnMode1, self.btnMode2]
        
        #Declarando variaveis dos modos de jogos
        #Variaveis do modo GAME HAND
        self.scores = 0
        self.correctHand= 1
        self.confetti_imgx,self.confetti_imgy=0,72
        self.rightHand= Object(10,50,2,0,0,32,32)#13
        self.leftHand= Object(42,50,2,0,32,32,32)#45
        self.handsList= [self.rightHand,self.leftHand]

        pyxel.load("resources/Ache_O_Anel.pyxres")
        #pyxel.playm(0, loop=True)
        pyxel.run(self.update,self.draw) 
        
    def update(self):
        if self.play:
            #Escolha do modo de game
            if self.chose_mode:
                #Interação com os Botões
                for btn in self.modeList:
                    btn.verClick(x2= -1,y2= 100)
                    
                    if btn.mouseUp:
                        btn.y,btn.imgx= 43, 40
                        
                        if btn.mouseClick:
                            btn.y, btn.imgx= 44, 80
                            
                            if btn.modeName== "Hand": 
                                self.chose_mode= False
                                self.gameHand, self.gameCup= True, False
                                
                            if btn.modeName== "Cup":
                                self.chose_mode= False
                                self.gameCup, self.gameHand= True, False
                    else:
                        btn.y, btn.imgx=44, 0

            #GAME HAND
            if self.gameHand:
                #Verifição de interação com as mãos
                for hand in self.handsList:
                    self.rightHand.verClick(x1=9, x2=-5, y1=0, y2=-7)
                    self.leftHand.verClick(x1=4, x2=-10,y2=-7)
                    if hand.mouseUp: 
                        hand.imgx= 32
                        
                        if hand.mouseClick:
                            hand.imgx= 96 if hand.ring else 64      
                        
                        if hand.mousePressed:
                            if hand.ring:
                                hand.ring=pyxel.rndi(0,1)
                                self.correctHand= 2
                                self.scores+=1 
                                
                            else:
                                self.scores= 0
                                self.correctHand=0

                        if hand.mouseRealesed: 
                            hand.ring=pyxel.rndi(0,1)
                    else: 
                        hand.imgx= 0

                #Evitando que o anel surja nas 2 mãos
                if self.rightHand.ring == self.leftHand.ring:
                    self.rightHand.ring=pyxel.rndi(0,1)
                    self.leftHand.ring= pyxel.rndi(0,1)
                    
                #Animação dos confetes
                if self.confetti_imgy < 96:
                    if self.confetti_imgx< 224:
                        self.confetti_imgx+=32
                    else:
                        self.confetti_imgy= 96
                        self.confetti_imgx=0
                else: self.confetti_imgy=64
        #Menu Inicial
        else:
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                self.play,self.chose_mode= True, True

    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(True)
        
        if self.play:
            #Escolha do modo de game
            if self.chose_mode:
                pyxel.blt(0,0,0,90,0,90,140)
                pyxel.text(pyxel.width/2 - len("Escolha um modo:")/2 *4,37,"Escolha um modo:",7)
                for btn in self.modeList:
                    btn.draw()

           #GAME HAND
            if self.gameHand:
                pyxel.text(pyxel.width/2- len(str(self.scores))/2 *4, 5, str(self.scores), 7)
                for hand in self.handsList:
                    hand.draw()

                    if self.correctHand== 2:
                        pyxel.blt(-7,-5,2,self.confetti_imgx,self.confetti_imgy, 32,32)         
                        pyxel.blt(100-37,-5,2,self.confetti_imgx,self.confetti_imgy, -32,32)
                        pyxel.text(pyxel.width/2- len("Acertou!")/2 *4, 20,"Acertou!",pyxel.frame_count %16)
                    if self.correctHand== 0: 
                        pyxel.text(pyxel.width/2-len("Errou!")/2 *4, 20,"Errou!",7)
        else:
            pyxel.blt(0,0,0,0,0,90,140)
            pyxel.text(pyxel.width/2 - len("Clique para continuar")/2 *4,133,"Clique para continuar",7)
#Verificação da execução direta do módulo
if __name__ == "__main__":
    Game()