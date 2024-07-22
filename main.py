import pyxel
from src.object import Object
from datetime import datetime, timedelta

class Game:
    def __init__(self):
        pyxel.init(90, 140, "Ache O Anel")
        self.play = False
        self.chose_mode = False
        self.gameHand = False
        self.gameCup = False
        self.correctObj = 1
        self.scores = 0
        self.confetti_imgx = 0
        self.confetti_imgy = 96
        
        # Variaveis dos modos de games
        self.btnMode1 = Object(3, 44, 1, 0, 0, 40, 93)
        self.btnMode2 = Object(pyxel.width - 43, 44, 1, 0, 93, 40, 93)
        self.btnMode1.modeName="Hand"
        self.btnMode2.modeName="Cup"
        self.modeList = [self.btnMode1, self.btnMode2]
        
        # Variaveis do Game Hand
        self.rightHand = Object(13, 53, 2, 0, 0, 32, 32)
        self.leftHand = Object(45, 53, 2, 0,32, 32, 32)
        self.handsList = [self.rightHand, self.leftHand]
        
        # Variaveis do Game Cup
        self.rightCup = Object(5, 88, 2, 128, 0, 22, 35)
        self.centerCup = Object(34, 98, 2, 128, 35, 22, 35)
        self.leftCup = Object(63, 88, 2, 128, 0, 22, 35)
        self.cupsList = [self.rightCup, self.centerCup, self.leftCup]
        
        # Variaveis da Rodada Bônus
        self.bonusRound = False
        self.new_timer = False
        self.timer_final = datetime.now() + timedelta(seconds=5)

        self.ring1 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring2 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring3 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring4 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring5 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ringList = [self.ring1, self.ring2, self.ring3, self.ring4, self.ring5]
        
        pyxel.load("src/assets/Ache_O_Anel.pyxres")
        pyxel.playm(0, loop= True)
        pyxel.run(self.update, self.draw) 

    def reset(self):
        """Reseta o estado do jogo ao clicar com o botão esquerdo do mouse"""
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.play = False
            self.chose_mode = False
            self.gameHand = False
            self.gameCup = False
            self.correctObj = 1
            self.scores = 0

    # Verificação do temporizador
    def timerBonus(self):
        """Verificação do temporizador para a rodada bônus"""
        if self.new_timer:
            self.timer_final = datetime.now() + timedelta(seconds= 5)
            self.new_timer = False

        if datetime.now() >= self.timer_final:
            self.bonusRound= False 
                
    def check_interaction(self, objList, imgxM1, imgxM2, imgxC1, imgxC2):
        """Verifica a interação do mouse com os objetos fornecidos na lista objList."""
        for obj in objList:
            # Mouse Up
            if obj.mouseUp:
                obj.imgx = imgxM1
                
                # Mouse Click
                if obj.mouseClick:
                    if obj.ring:
                        obj.imgx = imgxC1
                    else:
                        obj.imgx = imgxC2
                        
                # Mouse Pressed
                if obj.mousePressed:
                    if obj.ring:
                        self.correctObj = 2
                        self.scores += 1
                    else:self.correctObj = 0
                        
                # Mouse released
                if obj.mouseReleased: 
                    obj.ring=pyxel.rndi(0, 1)
                    
            # Mouse Out
            else:
                obj.imgx= imgxM2
                
    def check_equal_values(self, obj1, obj2, obj3= None):
        """Evita que múltiplos objetos tenham o mesmo valor de 'ring'."""
        if  not obj3 == None:
            if  obj1.ring and obj2.ring: 
                obj1.ring = pyxel.rndi(0, 1)
                obj2.ring = pyxel.rndi(0, 1)
            
            if obj1.ring and obj3.ring:
                obj1.ring = pyxel.rndi(0, 1)
                obj3.ring = pyxel.rndi(0, 1)  
            
            if obj2.ring and obj3.ring:
                obj2.ring = pyxel.rndi(0, 1)
                obj3.ring = pyxel.rndi(0, 1)

            if obj1.ring == obj2.ring == obj3.ring: 
                obj1.ring = pyxel.rndi(0, 1)
                obj2.ring = pyxel.rndi(0, 1)
                obj3.ring = pyxel.rndi(0, 1)
        else:
            if obj1.ring == obj2.ring:
                obj1.ring = pyxel.rndi(0,1)
                obj2.ring = pyxel.rndi(0,1)
                
    def draw_centered_text(self, txt, y, col, padx= 0):
        """Centraliza e desenha o texto na tela"""
        text_center_x = len(txt) / 2 * pyxel.FONT_WIDTH
        if padx > 0:
            text_center_x+= int(padx)
        else:
            text_center_x-= int(padx)
            
        pyxel.text(pyxel.width / 2 - text_center_x, y, txt, col)
    
    def update(self):
        """Verifica interação a cada quadro."""
        if self.play:
            # Escolha do modo de game
            if self.chose_mode:
                # Interação com os Botões
                for btn in self.modeList:
                    btn.verClick(padx2= -1, pady2= 100)
                    
                    # Mouse Up
                    if btn.mouseUp:
                        btn.y = 43
                        btn.imgx = 40
                        
                        # Mouse Pressed
                        if btn.mousePressed:
                            btn.y = 44 
                            btn.imgx = 80
                            
                            # Mode Game1
                            if btn.modeName == "Hand": 
                                self.chose_mode = False
                                self.gameHand = True
                                self.gameCup = False
                                
                            # Mode Game2
                            if btn.modeName == "Cup":
                                self.chose_mode = False
                                self.gameCup = True
                                self.gameHand = False
                    # Mouse Out
                    else: 
                        btn.y = 44
                        btn.imgx = 0
                        
            # Gameplay
            # GAME HAND
            if self.gameHand and not self.bonusRound:
                if not self.correctObj == 0:
                    # Verifição de interação com as mãos
                    self.rightHand.verClick(padx1= 9, padx2= -5, pady1= 0, pady2= -7)
                    self.leftHand.verClick(padx1= 4, padx2= -10, pady2= -7)
                    self.check_interaction(self.handsList, 32, 0, 96, 64)

                    # Evitando que o anel surja em mais de 1 mão
                    self.check_equal_values(self.rightHand, self.leftHand)
                else: 
                    self.reset()
                 
            # GAME CUP
            if self.gameCup and not self.bonusRound:
                if not self.correctObj == 0:
                    # Verifição de interação com os Copos
                    self.rightCup.verClick(padx1= 1, padx2= -2, pady1= 7, pady2= -2)
                    self.centerCup.verClick(padx1= 1,padx2= -2, pady1= 7, pady2= -2)
                    self.leftCup.verClick(padx1= 1, padx2= -2, pady1= 7, pady2= -2)
                    self.check_interaction(self.cupsList, 150, 128, 194, 172)

                    # Evitando que o anel surja nas 2 mãos
                    self.check_equal_values(self.rightCup, self.centerCup , self.leftCup)
                else:
                    self.reset()
                    
            # Acerto
            if self.correctObj == 2:
                # Animação dos confetes
                if self.confetti_imgy < 128:
                    if self.confetti_imgx < 224:
                        self.confetti_imgx += 32
                    else:
                        self.confetti_imgy = 128
                        self.confetti_imgx = 0
                else: self.confetti_imgy = 96

                # Verificação da validação da rodada bonus                 
                if (self.bonusRound == False and
                    self.scores > 0 and self.scores % 5 == 0):
                    self.new_timer = True
                    self.bonusRound = True
                
            # Bonus:"Chuva de Aneis"
            # Verificação do temporizador
            if self.bonusRound:
                self.timerBonus()               

                for ring in self.ringList:
                    ring.verClick(padx1= 1, padx2= -2, pady1= 7, pady2= -2)
                    
                    if ring.y > pyxel.height:
                        ring.x = pyxel.rndi(0, 74)
                        ring.y = -16
                    else:
                        ring.y += 3
                        
                    if ring.mouseUp and ring.mouseClick:
                        pyxel.play(3, 3)
                        self.scores += 1
                        ring.y = -16
                        ring.x = pyxel.rndi(0, 74)
            else:
                # Troca de posição dos aneis
                for ring in self.ringList:
                    ring.x = pyxel.rndi(0, 74)
                    ring.y =pyxel.rndi(-32, -16)
                    
        # Menu Inicial
        else:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.play = True
                self.chose_mode = True

    def draw(self):
        """Atualiza os elementos gráficos na tela"""
        pyxel.cls(0)
        pyxel.mouse(True)
        
        if self.play:
            # Escolha do modo de game
            if self.chose_mode:
                pyxel.blt(0, 0, 0, 90, 0, 90, 140)
                self.draw_centered_text("Escolha um modo:", 37, 7 ,padx= +1)
                for btn in self.modeList:
                    btn.draw()

            # Gameplay
            if (self.gameHand or self.gameCup or self.bonusRound):
                self.draw_centered_text(str(self.scores), 5, 7)
               
                # GAME HAND
                if self.gameHand and not self.bonusRound:
                    for hand in self.handsList:
                        hand.draw()

               # GAME CUP
                if self.gameCup and not self.bonusRound:
                    pyxel.blt(0, 104, 0, 0, 140, 90, 36)
                    for cup in self.cupsList:
                        cup.draw()
    
                # Erros e acertos
                # Acerto
                if self.correctObj == 2 and not self.bonusRound:
                    self.draw_centered_text("Acertou!", 20, pyxel.frame_count %16)
                    pyxel.blt(-6, -5, 2, self.confetti_imgx, self.confetti_imgy, 32, 32)         
                    pyxel.blt(64, -5, 2, self.confetti_imgx, self.confetti_imgy, -32, 32)
                    
                # Erro
                if self.correctObj == 0 and not self.bonusRound:
                    self.draw_centered_text("Errou!", 20, 7)
                    self.draw_centered_text("Clique para voltar", 120, 7)
                    self.draw_centered_text("ao menu inicial", 130, 7)
                    
                    #Total de scores
                    pyxel.rect(pyxel.width /2 - 15, 90, 27, 20, 0)
                    pyxel.rectb(pyxel.width /2 - 15, 90, 27, 20, 10)
                    self.draw_centered_text("Total:", 93, 7)
                    self.draw_centered_text(str(self.scores), 101, 7, padx= -3)
                    pyxel.blt(pyxel.width /2 + 1, 100, 2, 235, 0, 5, 7)
                    
                    
                # Rodada Bonus
                if self.bonusRound:
                    TEXT_CENTER_X = lambda txt: len(txt)/2 * pyxel.FONT_WIDTH
                  
                    for ring in self.ringList:
                        ring.draw()
                            
                    self.draw_centered_text("Rodada Bonus", 11, 8)
                    self.draw_centered_text("Chuva de Aneis", 18, 10)
                    self.draw_centered_text("Pegue os Aneis", 25, pyxel.frame_count %16)
        
        # Menu Inicial
        else:
            pyxel.blt(0, 0, 0, 0, 0, 90, 140)
            self.draw_centered_text("Clique para continuar", 133, 7)

if __name__ == "__main__":
    Game()