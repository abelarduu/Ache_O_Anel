import pyxel
from src.object import Object
from datetime import datetime, timedelta

class Game:
    def __init__(self):
        pyxel.init(90, 140, "Ache O Anel")
        self.play = False
        self.chose_mode = False
        self.game_hand = False
        self.game_cup = False
        self.correct_obj = 1
        self.scores = 0
        self.confetti_imgx = 0
        self.confetti_imgy = 96
        
        # Variaveis dos modos de games
        self.btn_mode1 = Object(3, 44, 1, 0, 0, 40, 93)
        self.btn_mode2 = Object(pyxel.width - 43, 44, 1, 0, 93, 40, 93)
        self.btn_mode1.mode_name="Hand"
        self.btn_mode2.mode_name="Cup"
        self.mode_list = [self.btn_mode1, self.btn_mode2]
        
        # Variaveis do Game Hand
        self.right_hand = Object(13, 53, 2, 0, 0, 32, 32)
        self.left_hand = Object(45, 53, 2, 0,32, 32, 32)
        self.hands_list = [self.right_hand, self.left_hand]
        
        # Variaveis do Game Cup
        self.right_cup = Object(5, 88, 2, 128, 0, 22, 35)
        self.center_cup = Object(34, 98, 2, 128, 35, 22, 35)
        self.left_cup = Object(63, 88, 2, 128, 0, 22, 35)
        self.cups_list = [self.right_cup, self.center_cup, self.left_cup]
        
        # Variaveis da Rodada Bônus
        self.bonus_round = False
        self.new_timer = False
        self.timer_final = datetime.now() + timedelta(seconds=5)

        self.ring1 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring2 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring3 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring4 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring5 = Object(pyxel.rndi(0, 74), pyxel.rndi(-32, 0), 2, 220, 0, 13, 16)
        self.ring_list = [self.ring1, self.ring2, self.ring3, self.ring4, self.ring5]
        
        pyxel.load("src/assets/Ache_O_Anel.pyxres")
        pyxel.playm(0, loop= True)
        pyxel.run(self.update, self.draw) 

    def reset(self):
        """Reseta o estado do jogo ao clicar com o botão esquerdo do mouse"""
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.play = False
            self.chose_mode = False
            self.game_hand = False
            self.game_cup = False
            self.correct_obj = 1
            self.scores = 0

    # Verificação do temporizador
    def timer_bonus(self):
        """Verificação do temporizador para a rodada bônus"""
        if self.new_timer:
            self.timer_final = datetime.now() + timedelta(seconds= 5)
            self.new_timer = False

        if datetime.now() >= self.timer_final:
            self.bonus_round= False 
                
    def check_interaction(self, objList, imgxM1, imgxM2, imgxC1, imgxC2):
        """Verifica a interação do mouse com os objetos fornecidos na lista objList."""
        for obj in objList:
            # Mouse Up
            if obj.mouse_up:
                obj.imgx = imgxM1
                
                # Mouse Click
                if obj.mouse_click:
                    if obj.ring:
                        obj.imgx = imgxC1
                    else:
                        obj.imgx = imgxC2
                        
                # Mouse Pressed
                if obj.mouse_pressed:
                    if obj.ring:
                        self.correct_obj = 2
                        self.scores += 1
                    else:self.correct_obj = 0
                        
                # Mouse released
                if obj.mouse_released: 
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
                for btn in self.mode_list:
                    btn.check_click(padx2= -1, pady2= 100)
                    
                    # Mouse Up
                    if btn.mouse_up:
                        btn.y = 43
                        btn.imgx = 40
                        
                        # Mouse Pressed
                        if btn.mouse_pressed:
                            btn.y = 44 
                            btn.imgx = 80
                            
                            # Mode Game1
                            if btn.mode_name == "Hand": 
                                self.chose_mode = False
                                self.game_hand = True
                                self.game_cup = False
                                
                            # Mode Game2
                            if btn.mode_name == "Cup":
                                self.chose_mode = False
                                self.game_cup = True
                                self.game_hand = False
                    # Mouse Out
                    else: 
                        btn.y = 44
                        btn.imgx = 0
                        
            # Gameplay
            # GAME HAND
            if self.game_hand and not self.bonus_round:
                if not self.correct_obj == 0:
                    # Verifição de interação com as mãos
                    self.right_hand.check_click(padx1= 9, padx2= -5, pady1= 0, pady2= -7)
                    self.left_hand.check_click(padx1= 4, padx2= -10, pady2= -7)
                    self.check_interaction(self.hands_list, 32, 0, 96, 64)

                    # Evitando que o anel surja em mais de 1 mão
                    self.check_equal_values(self.right_hand, self.left_hand)
                else: 
                    self.reset()
                 
            # GAME CUP
            if self.game_cup and not self.bonus_round:
                if not self.correct_obj == 0:
                    # Verifição de interação com os Copos
                    self.right_cup.check_click(padx1= 1, padx2= -2, pady1= 7, pady2= -2)
                    self.center_cup.check_click(padx1= 1,padx2= -2, pady1= 7, pady2= -2)
                    self.left_cup.check_click(padx1= 1, padx2= -2, pady1= 7, pady2= -2)
                    self.check_interaction(self.cups_list, 150, 128, 194, 172)

                    # Evitando que o anel surja nas 2 mãos
                    self.check_equal_values(self.right_cup, self.center_cup , self.left_cup)
                else:
                    self.reset()
                    
            # Acerto
            if self.correct_obj == 2:
                # Animação dos confetes
                if self.confetti_imgy < 128:
                    if self.confetti_imgx < 224:
                        self.confetti_imgx += 32
                    else:
                        self.confetti_imgy = 128
                        self.confetti_imgx = 0
                else: self.confetti_imgy = 96

                # Verificação da validação da rodada bonus                 
                if (self.bonus_round == False and
                    self.scores > 0 and self.scores % 5 == 0):
                    self.new_timer = True
                    self.bonus_round = True
                
            # Bonus:"Chuva de Aneis"
            # Verificação do temporizador
            if self.bonus_round:
                self.timer_bonus()               

                for ring in self.ring_list:
                    ring.check_click(padx1= 1, padx2= -2, pady1= 7, pady2= -2)
                    
                    if ring.y > pyxel.height:
                        ring.x = pyxel.rndi(0, 74)
                        ring.y = -16
                    else:
                        ring.y += 3
                        
                    if ring.mouse_up and ring.mouse_click:
                        pyxel.play(3, 3)
                        self.scores += 1
                        ring.y = -16
                        ring.x = pyxel.rndi(0, 74)
            else:
                # Troca de posição dos aneis
                for ring in self.ring_list:
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
                for btn in self.mode_list:
                    btn.draw()

            # Gameplay
            if (self.game_hand or self.game_cup or self.bonus_round):
                self.draw_centered_text(str(self.scores), 5, 7)
               
                # GAME HAND
                if self.game_hand and not self.bonus_round:
                    for hand in self.hands_list:
                        hand.draw()

               # GAME CUP
                if self.game_cup and not self.bonus_round:
                    pyxel.blt(0, 104, 0, 0, 140, 90, 36)
                    for cup in self.cups_list:
                        cup.draw()
    
                # Erros e acertos
                # Acerto
                if self.correct_obj == 2 and not self.bonus_round:
                    self.draw_centered_text("Acertou!", 20, pyxel.frame_count %16)
                    pyxel.blt(-6, -5, 2, self.confetti_imgx, self.confetti_imgy, 32, 32)         
                    pyxel.blt(64, -5, 2, self.confetti_imgx, self.confetti_imgy, -32, 32)
                    
                # Erro
                if self.correct_obj == 0 and not self.bonus_round:
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
                if self.bonus_round:
                    for ring in self.ring_list:
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