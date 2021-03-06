import pygame
from os import path
game_folder = path.dirname(__file__)[0:-3]

from strings import *

size= [SCREEN_WIDTH, SCREEN_HEIGHT]
screen= pygame.display.set_mode(size)

# default_sprite= pygame.image.load(path.join(game_folder, 'assets/images/trainer_f.png')).convert_alpha()
class NpcTemplate(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, name, sprite, dialog):
        self.npc_group = pg.sprite.Group()
        pygame.sprite.Sprite.__init__(self, self.npc_group)
        self.name = name
        self.game=game
        self.x=x
        self.y=y
        self.vx=x
        self.vy= y
        self.width= 16
        self.height= 32
        self.image= pygame.Surface((16,32), pygame.SRCALPHA)
        self.sprite = sprite
        self.rect= pygame.Rect(x,y,w,h)
        self.dialog = dialog
        self.font = pygame.font.SysFont(None, 25)
        default_sprite= pygame.image.load(path.join(game_folder, 'assets/images/'+ self.name+'_npc.png')).convert_alpha()
        self.image= default_sprite

        # self.game.npcs

    def hit(self):
        print("hit")

    def dialogue (self, text):
        screen= self.game.screen
        for line in text:
            # blackBarRectPos = (64, 64) # For now.
            # blackBarRectSize= (screen.get_width()- 64, 64)
            pygame.draw.rect(screen, BLACK, pygame.Rect(blackBarRectPos, blackBarRectSize))
            font = pygame.font.Font(None, 32)
            text = font.render(text, True, BLACK, WHITE)
            textRect = text.get_rect()
            X = 400
            Y = 400
            textRect.center = (X // 2, Y // 2)
            screen.blit(text, textRect)


    # def runDialog(self, screen):
    #     done = False
    #     while not done:
    #         for i, line in enumerate(dialog):
    #             #display to the player the dialog
    #             screen_text = font.render(line, True, (255, 255, 255))
    #             pygame.draw.rect(screen, (0, 0, 0), [100, 100, 100, 200])
    #             screen.blit(screen_text, [100, 100])
    #             for e in pygame.even.get():
    #                 #if player clicks screen display next option or breakout of loop
    #                 if e.type == pygame.MOUSEBUTTONDOWN:
    #                     if dialog[i] == dialog.length - 1:
    #                         done = True
    #                         break
    #                     else:
    #                         continue

    # def giveItem(self, player):
    #     if self.item != None:
    #         if self.item.name in player.inventory:
    #             for key, value in player.inventory.items()
    #                 if key == self.item.name:
    #                     player.inventory[key] = value + 1
    #         else:
    #             player.inventory[self.item.name] = 1
