#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        if self.name == 'Enemy3':
            self.vertical_speed = random.choice((2, -1))
        else:
            self.vertical_speed = 0

    def move(self):
        if self.name == 'Enemy3':
            if self.rect.bottom >= WIN_HEIGHT:
                self.vertical_speed = -1
            elif self.rect.top <= 0:
                self.vertical_speed = 2

        self.rect.centerx -= ENTITY_SPEED[self.name]
        self.rect.centery += self.vertical_speed

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
