#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font(None, 30)  # Define a fonte e o tamanho

        # Defina seu nome completo e RU
        self.player_name = "Seu Nome Completo"
        self.ru = "4548943"

    def draw_name_and_ru(self):
        # Desenha o nome e o RU em qualquer canto da tela
        # Canto superior esquerdo
        text_name = self.font.render(self.player_name, True, (255, 255, 255))  # Branco
        text_ru = self.font.render(self.ru, True, (255, 255, 255))
        self.window.blit(text_name, (10, 10))  # 10px de distância da borda
        self.window.blit(text_ru, (10, 40))  # 10px abaixo do nome

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            # Aqui, antes de entrar no loop de jogos, desenha o nome e o RU
            self.draw_name_and_ru()
            pygame.display.update()  # Atualiza a tela

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        # Após o Level 2, chama o Level 3
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Fecha a janela
                quit()  # Encerra o pygame
            else:
                pygame.quit()
                sys.exit()
