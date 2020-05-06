from pokemon.pokemonTemplate import PokemonTemplate

class Torterra(PokemonTemplate):
    def __init__(self, name="torterra", type='grass', currentHp=300, moves=[], ailments=[], stats={'hp': 95, 'Attack': 109, 'Defense': 105, 'Sp. Atk': 75, 'Sp. Def': 85, 'Speed': 56}):
        super().__init__(name, type, currentHp, moves, ailments, stats)
