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
        self.mouseReleased= False
        
    def verClick(self, x1=0, x2=0, y1=0, y2=0):
        #Mouse Up
        if pyxel.mouse_x >= self.x+x1 and pyxel.mouse_x <= self.x + self.w+x2 \
            and pyxel.mouse_y >= self.y+y1 and pyxel.mouse_y <= self.y + self.h+y2:
                self.mouseUp=True
                
                #Mouse Click
                if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                    self.mouseClick=True
                else:self.mouseClick=False
                    
                #Mouse Pressed
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.mousePressed=True
                else:self.mousePressed=False
                
                #Mouse released
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                    self.mouseReleased=True
                else:self.mouseReleased=False
        #Mouse Out
        else:self.mouseUp=False
    
    def draw(self):
        pyxel.blt(self.x,self.y,self.img,self.imgx,self.imgy,self.w,self.h)

class Game:
    def __init__(self):
        pyxel.init(90,140,"Ache O Anel")
        self.play= False
        self.chose_mode= False
        self.gameHand= False
        self.gameCup= False
        self.correctObj= 1
        self.scores = 0
        self.confetti_imgx=0
        self.confetti_imgy=96
        
        #Variaveis dos modos de games
        self.btnMode1=Object(3,44,1,0,0,40,93)
        self.btnMode2= Object(pyxel.width-43,44,1,0,93,40,93)
        self.btnMode1.modeName="Hand"
        self.btnMode2.modeName="Cup"
        self.modeList= [self.btnMode1, self.btnMode2]
        
        #Variaveis do Game Hand
        self.rightHand= Object(13,53,2,0,0,32,32)
        self.leftHand= Object(45,53,2,0,32,32,32)
        self.handsList= [self.rightHand,self.leftHand]
        
        #Variaveis do Game Cup
        self.rightCup= Object(5,88,2,128,0,22,35)
        self.centerCup= Object(34,98,2,128,35,22,35)
        self.leftCup= Object(63,88,2,128,0,22,35)
        self.cupsList= [self.rightCup,self.centerCup,self.leftCup]
        
        pyxel.load("resources/Ache_O_Anel.pyxres")
        #pyxel.playm(0, loop=True)
        pyxel.run(self.update,self.draw) 
        
    def reset(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.play,self.chose_mode= False, False
            self.gameHand,self.gameCup= False, False
            self.correctObj=1
            self.scores= 0

    def check_interaction(self, objList, imgxM1, imgxM2, imgxC1, imgxC2):
        for obj in objList:
            #Mouse Up
            if obj.mouseUp:
                obj.imgx= imgxM1
                #Mouse Click
                if obj.mouseClick:
                    if obj.ring:
                        obj.imgx= imgxC1 
                    else:obj.imgx= imgxC2
                #Mouse Pressed
                if obj.mousePressed:
                    if obj.ring:
                        self.correctObj= 2
                        self.scores+=1 
                    else:self.correctObj=0
                #Mouse released
                if obj.mouseReleased: 
                    obj.ring=pyxel.rndi(0,1)
            #Mouse Out
            else: obj.imgx= imgxM1
                
    def update(self):
        if self.play:
            #Escolha do modo de game
            if self.chose_mode:
                #Interação com os Botões
                for btn in self.modeList:
                    btn.verClick(x2= -1,y2= 100)
                    
                    #Mouse Up
                    if btn.mouseUp:
                        btn.y,btn.imgx= 43, 40
                        
                        #Mouse Pressed
                        if btn.mousePressed:
                            btn.y, btn.imgx= 44, 80
                            
                            #Mode Game1
                            if btn.modeName== "Hand": 
                                self.chose_mode= False
                                self.gameHand, self.gameCup= True, False
                                
                            #Mode Game1
                            if btn.modeName== "Cup":
                                self.chose_mode= False
                                self.gameCup, self.gameHand= True, False
                    #Mouse Out
                    else: btn.y, btn.imgx=44, 0
                        
           #GAME HAND
            if self.gameHand:
                if not self.correctObj==0:
                    #Verifição de interação com as mãos
                    self.rightHand.verClick(x1=9, x2=-5, y1=0, y2=-7)
                    self.leftHand.verClick(x1=4, x2=-10,y2=-7)
                    self.check_interaction(self.handsList, 32, 0, 96, 64)

                    #Evitando que o anel surja nas 2 mãos
                    if self.rightHand.ring == self.leftHand.ring:
                        self.rightHand.ring=pyxel.rndi(0,1)
                        self.leftHand.ring= pyxel.rndi(0,1)
                else: self.reset()
                     
            #GAME CUP
            if self.gameCup:
                if not self.correctObj==0:
                    #Verifição de interação com os Copos
                    self.rightCup.verClick(x1=1,x2=-2,y1=7,y2=-2)
                    self.centerCup.verClick(x1=1,x2=-2,y1=7,y2=-2)
                    self.leftCup.verClick(x1=1,x2=-2,y1=7,y2=-2)
                    self.check_interaction(self.cupsList, 150, 128, 194, 172)

                    #Evitando que o anel surja nas 2 mãos
                    if self.rightCup.ring == self.centerCup.ring \
                        or self.rightCup.ring == self.leftCup.ring:
                        self.rightCup.ring= pyxel.rndi(0,1)
                        self.centerCup.ring=pyxel.rndi(0,1)
                        self.leftCup.ring= pyxel.rndi(0,1)
                else: self.reset()
                    
            #Acerto
            if self.correctObj == 2:
                    #Animação dos confetes
                    if self.confetti_imgy < 128:
                        if self.confetti_imgx< 224:
                            self.confetti_imgx+=32
                        else:
                            self.confetti_imgy= 128
                            self.confetti_imgx=0
                    else: self.confetti_imgy=96
        #Menu Inicial
        else:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.play,self.chose_mode= True, True

    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(True)
        if self.play:
            #Escolha do modo de game
            if self.chose_mode:
                pyxel.blt(0,0,0,90,0,90,140)
                pyxel.text(pyxel.width/2+1 - len("Escolha um modo:")/2 *4,37,"Escolha um modo:",7)
                for btn in self.modeList:
                    btn.draw()

           #GAME HAND
            if self.gameHand:
                print(self.rightHand.ring, self.leftHand.ring)
                pyxel.text(pyxel.width/2- len(str(self.scores))/2 *4, 5, str(self.scores), 7)
                for hand in self.handsList:
                    hand.draw()

           #GAME CUP
            if self.gameCup:
                print(self.rightCup.ring, self.centerCup.ring, self.leftCup.ring)
                pyxel.text(pyxel.width/2- len(str(self.scores))/2 *4, 5, str(self.scores), 7)
                pyxel.blt(0,104,0,0,140,90,36)
                for cup in self.cupsList:
                    cup.draw()
    
            #Erros e acertos
            #Acerto
            if self.correctObj== 2:
                pyxel.blt(-6,-5,2,self.confetti_imgx,self.confetti_imgy, 32,32)         
                pyxel.blt(101-37,-5,2,self.confetti_imgx,self.confetti_imgy, -32,32)
                pyxel.text(pyxel.width/2+1 -len("Acertou!")/2 *4, 20,"Acertou!",pyxel.frame_count %16)
            #Erro
            if self.correctObj== 0: 
                pyxel.text(pyxel.width/2-len("Errou!")/2 *4, 20,"Errou!",7)
                pyxel.text(pyxel.width/2 - len("Clique para voltar")/2 *4,120,"Clique para voltar",7)
                pyxel.text(pyxel.width/2 - len("ao menu inicial")/2 *4,130,"ao menu inicial",7)
                
                pyxel.rectb(pyxel.width/2 -15,90,27,20,7)
                pyxel.text(pyxel.width/2 - len("Total:")/2 *4,93,"Total:",7)
                pyxel.text(pyxel.width/2-3 - len(str(self.scores))/2 *4, 101, str(self.scores), 7)
                pyxel.blt(pyxel.width/2,100,2,235,0,5,7)
        #Menu Inicial
        else:
            pyxel.blt(0,0,0,0,0,90,140)
            pyxel.text(pyxel.width/2 - len("Clique para continuar")/2 *4,133,"Clique para continuar",7)
#Verificação da execução direta do módulo
if __name__ == "__main__":
    Game()