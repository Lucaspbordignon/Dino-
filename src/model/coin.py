import pygame
from random import randint

class coin():
    def __init__(self, position):
        random = randint(0,9)
        if random >= 3:
            self.__image = pygame.image.load('../resources/eth.png')
            self.__value = 1
        else:
            if random == 2:
                self.__image = pygame.image.load('../resources/dogecoin.png')
                self.__value = 4
            else:
                self.__image = pygame.image.load('../resources/bit.png')
                self.__value = 2
        self.__position = position

    def get_position(self):
        return self.__position

    def get_size(self):
        return (self.__image.get_width(), self.__image.get_height())

    def get_image(self):
        return self.__image

    def value(self):
        return self.__value

    def set_position(self, value):
        self.__position = value

    def hitted(self, char_pos, char_size):
        coin_pos = self.get_position()
        coin_size = self.get_size()
        if (coin_pos[0] <= char_pos[0] + char_size[0] <= coin_pos[0] + coin_size[0]):
            if (coin_pos[1] <= char_pos[1] <= coin_pos[1] + coin_size[1]):
                return True
        return False
