import pygame


class dino():
    def __init__(self, params, size=(44, 47)):
        self.char_types = {
            0: 'default',
            1: 'albino',
        }
        self.params = params
        self.actual_type = self.char_types[params['type']]
        self.image = self.load_image(str(self.actual_type) + '.png')
        self.size = size
        self.movement = 1
        self.jumping = False
        self.lives = 2

    def get_image(self):
        return self.image

    def get_position(self):
        return self.params['pos']

    def get_movement(self):
        return self.movement

    def get_size(self):
        return self.size

    def get_lives(self):
        return self.lives

    def is_jumping(self):
        return self.jumping

    def set_position(self, value):
        self.params['pos'] = value

    def set_movement(self, value):
        self.movement = value

    def set_jumping(self, value):
        self.jumping = value

    def set_lives(self, value):
        self.lives = value

    def change_type(self, type_desired):
        self.actual_type = self.char_types[type_desired]
        self.image = self.load_image(str(self.actual_type) + '.png')

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
