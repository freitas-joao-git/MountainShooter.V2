#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_WIDTH, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed_y = 3  # Velocidade de movimento no eixo Y
        self.speed_x = -5  # Movimenta-se da direita para a esquerda no eixo X

    def move(self):
        # Movimenta no eixo X (da direita para a esquerda)
        self.rect.x += self.speed_x

        # Movimenta no eixo Y (subindo e descendo)
        self.rect.y += self.speed_y

        # Se bater na borda inferior, sobe com a velocidade normal
        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            self.speed_y = -3  # Inicia a subida com a velocidade normal

        # Se bater na borda superior, desce com o dobro da velocidade
        elif self.rect.top <= 0:
            self.rect.top = 0
            self.speed_y = 6  # Acelera a descida

        # Se estiver dentro da tela, mantém a velocidade normal no eixo Y
        elif 0 < self.rect.top < WIN_HEIGHT:
            if self.speed_y > 0:
                self.speed_y = 3  # Velocidade de descida normal
            elif self.speed_y < 0:
                self.speed_y = -3  # Velocidade de subida normal
