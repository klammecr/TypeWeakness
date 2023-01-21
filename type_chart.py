#pokemon_type = ""
from enum import Enum
class PokemonType(Enum):
    FIRE= 'Fire'
    WATER= 'Water'
    GRASS= 'Grass'
    ELECTRIC= 'Electric'
    ICE= 'Ice'
    GROUND= 'Ground'
    ROCK= 'Rock'
    FAIRY= 'Fairy'
    DRAGON= 'Dragon'
    DARK= 'Dark'
    GHOST= 'Ghost'
    PSYCHIC= 'Psychic'
    BUG= 'Bug'
    STEEL= 'Steel'
    POISON= 'Poison'
    NORMAL= 'Normal'
    FIGHTING= 'Fighting'
    FLYING= 'Flying'

print(f'number of valid types:{len(valid_pokemon_type)}')
weak_table = {PokemonType.BUG:[PokemonType.FIRE, PokemonType.FLYING,PokemonType.ROCK],
              PokemonType.DARK:[PokemonType.BUG, PokemonType.FAIRY, PokemonType.ICE], 
              PokemonType.DRAGON:[PokemonType.DRAGON, PokemonType.FAIRY, PokemonType.ICE],
              PokemonType.ELECTRIC
              PokemonType.FIRE:[PokemonType.GROUND, PokemonType.ROCK, PokemonType.WATER],
              PokemonType.WATER:[PokemonType.ELECTRIC,PokemonType.GRASS], 
              PokemonType.GRASS:['bug','fire',]}