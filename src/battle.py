import sys
from os import path
import pygame
from random import randint

from pokemon import blastoise, blaziken, charizard, empoleon, feraligatr, infernape, meganium, sceptile, swampert, torterra, typhlosion, venusaur
from pokemon.pokemonTemplate import PokemonTemplate
from strings import *
from dialogue import *

class Battle():
    def __init__(self, game):
        pygame.mixer.init()
        self.turns=0
        self.player_poke=[]
        self.enemy_poke=[]
        self.won= None # Not True not False it's just ¯\_(ツ)_/¯
        self.done= False
        self.game= game
        self.font= pygame.font.Font('freesansbold.ttf', 16)
        # Remove later
        #self.player_poke.append(charizard.Charizard())
        #self.enemy_poke.append(meganium.Meganium())
        self.music= pygame.mixer.Sound("sounds/battle.wav")

    def quit(self):
        pygame.mixer.pause()
        pygame.quit()
        sys.exit()

    def draw(self, screen):
        self.enemy_poke[0].currentHp= self.enemy_poke[0].stats['hp']
        self.player_poke[0].currentHp= self.player_poke[0].stats['hp']
        player_name= str(self.player_poke[0].name).capitalize()
        enemy_name= str(self.enemy_poke[0].name).capitalize()
        player_hp= str(self.player_poke[0].currentHp) + "/" + str(self.player_poke[0].stats['hp'])
        enemy_hp= str(self.enemy_poke[0].currentHp) + "/" + str(self.enemy_poke[0].stats['hp'])
        text_p = self.font.render(player_hp, True, WHITE, BLACK)
        text_p_name = self.font.render(player_name, True, WHITE, BLACK)
        text_e = self.font.render(enemy_hp, True, WHITE, BLACK)
        text_e_name = self.font.render(enemy_name, True, WHITE, BLACK)
        textRect_p = text_p.get_rect()
        textRect_p_name = text_p_name.get_rect()
        textRect_e = text_e.get_rect()
        textRect_e_name = text_e_name.get_rect()
        X_p = 50
        X_e = 500
        Y = screen.get_height()
        textRect_p.center = (X_p, Y // 2 - 200)
        textRect_p_name.center = (X_p, Y // 2 - 250)
        textRect_e.center = (X_e, Y // 2 - 200)
        textRect_e_name.center = (X_e, Y // 2 - 250)
        screen.blit(text_p, textRect_p)
        screen.blit(text_p_name, textRect_p_name)
        screen.blit(text_e, textRect_e)
        screen.blit(text_e_name, textRect_e_name)

    def events(self):
        if self.game.battling== True:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    print("Bye bye...")
                    self.quit()
                elif event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        print("See ya.")
                        self.quit()
                    elif event.key== pygame.K_q:
                        print("Q key pressed.")
                        self.game.battling=False
                        self.done= True
                        pygame.mixer.Sound.fadeout(self.music,1000)
                        self.game.run()

    def getPokemon(self, num):
        rand_pokemon = 0
        if num == 0:
            rand_pokemon = blastoise.Blastoise()
        elif num == 1:
            rand_pokemon = blaziken.Blaziken()
        elif num == 2:
            rand_pokemon = charizard.Charizard()
        elif num == 3:
            rand_pokemon = empoleon.Empoleon()
        elif num == 4:
            rand_pokemon = feraligatr.Feraligatr()
        elif num == 5:
            rand_pokemon = infernape.Infernape()
        elif num == 6:
            rand_pokemon = meganium.Meganium()
        elif num == 7:
            rand_pokemon = sceptile.Sceptile()
        elif num == 8:
            rand_pokemon = swampert.Swampert()
        elif num == 9:
            rand_pokemon = torterra.Torterra()
        elif num == 10:
            rand_pokemon = typhlosion.Typhlosion()
        elif num == 11:
            # rand_pokemon = venusaur.Venusaur()
            rand_pokemon = typhlosion.Typhlosion()

        return rand_pokemon

    def battle(self): #self, player, enemy
        p = randint(0, 11)
        e = randint(0, 11)
        pokeP = self.getPokemon(p)
        pokeE = self.getPokemon(e)

        self.player_poke.append(pokeP)
        self.enemy_poke.append(pokeE)


    def main(self):
        self.battle()
        self.game.battling=True
        size= [self.game.width,self.game.height]
        screen= pygame.display.set_mode(size)
        screen.fill(BLACK)
        game_folder = path.dirname(__file__)[0:-3]

        pp_name= self.player_poke[0].name
        pe_name= self.enemy_poke[0].name

        play_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pp_name.lower() +'.png')).convert_alpha()
        play_poke= pygame.transform.flip(play_poke, True, False)
        enemy_poke=pygame.image.load(path.join(game_folder, 'assets/images/'+ pe_name.lower() +'.png')).convert_alpha()


        screen.blit(play_poke, (50, 100))
        screen.blit(enemy_poke, (380, 100))

        self.battle()

        pygame.mixer.music.pause()
        # pygame.mixer.Sound.play(self.music)
        while self.done== False:
            self.draw(screen)
            self.events()
            pygame.display.flip()

        #  Make own events loop?
