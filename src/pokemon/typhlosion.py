from pokemon.pokemonTemplate import PokemonTemplate

class Typhlosion(PokemonTemplate):
    def __init__(self, name="typhlosion", type='fire', currentHp=266, moves=[], ailments=[], stats={'hp': 78, 'Attack': 84, 'Defense': 78, 'Sp. Atk': 109, 'Sp. Def': 85, 'Speed': 100}):
        super().__init__(name, type, currentHp, moves, ailments, stats)
