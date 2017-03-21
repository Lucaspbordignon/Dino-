from utils import *


class menu():
    def __init__(self, surface, screen_settings):
        self.resources = {}
        self.screen = surface
        self.screen_size = screen_settings['size']
        self.background_color = screen_settings['color']
        self.caption = screen_settings['caption']
        self.resources['ground'] = load_image('ground.png')

    def show_initial_menu(self):
        # Setup
        pygame.display.set_caption(self.caption + ': Main Menu')
        self.last_mouse_click = (-1, -1)
        new_game_pos = (40, 40)
        new_game_size = (159, 29)
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '')
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.last_mouse_click = pygame.mouse.get_pos()

            # New game button
            if (new_game_pos[0] <= self.last_mouse_click[0] <=
                    new_game_pos[0] + new_game_size[0]):
                if (new_game_pos[1] <= self.last_mouse_click[1] <=
                        new_game_pos[1] + new_game_size[1]):
                    print('Botão de iniciar novo jogo')
                    self.last_mouse_click = (-1, -1)
                    return (1, 'choose_char')

            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], (0, self.screen_size[1] - 30))
            self.screen.blit(load_image('new_game_button.png'), new_game_pos)

            # Updates the game display
            pygame.display.flip()

    def show_choose_char(self):
        # Setup
        pygame.display.set_caption(self.caption + ': Choose Character')
        self.last_mouse_click = (-1, -1)
        char_properties = {}
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return (0, '', None)
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.last_mouse_click = pygame.mouse.get_pos()

            self.screen.fill(self.background_color)
            self.screen.blit(self.resources['ground'], (0, self.screen_size[1] - 30))

            # Updates the game display
            pygame.display.flip()
