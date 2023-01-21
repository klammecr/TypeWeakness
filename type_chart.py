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

strong_table = \
{
    PokemonType.BUG : [PokemonType.GRASS, PokemonType.DARK, PokemonType.PSYCHIC],        
    PokemonType.DARK : [PokemonType.GHOST, PokemonType.PSYCHIC],
    PokemonType.DRAGON : [PokemonType.DRAGON],
    PokemonType.ELECTRIC : [PokemonType.FLYING, PokemonType.WATER],
    PokemonType.FAIRY : [PokemonType.FIGHTING, PokemonType.DARK, PokemonType.DRAGON],
    PokemonType.FIGHTING : [PokemonType.DARK, PokemonType.ICE, PokemonType.NORMAL, PokemonType.ROCK, PokemonType.STEEL],
    PokemonType.FIRE : [PokemonType.BUG, PokemonType.GRASS, PokemonType.ICE, PokemonType.STEEL],
    PokemonType.FLYING : [PokemonType.BUG, PokemonType.FIGHTING, PokemonType.GRASS],
    PokemonType.GHOST : [PokemonType.GHOST, PokemonType.PSYCHIC],
    PokemonType.GRASS : [PokemonType.GROUND, PokemonType.ROCK, PokemonType.WATER],
    PokemonType.GROUND : [PokemonType.ELECTRIC, PokemonType.FIRE, PokemonType.POISON, PokemonType.ROCK, PokemonType.STEEL],
    PokemonType.ICE : [PokemonType.DRAGON, PokemonType.FLYING, PokemonType.GRASS, PokemonType.GROUND],
    PokemonType.NORMAL : [],
    PokemonType.POISON : [PokemonType.FAIRY, PokemonType.GRASS],
    PokemonType.PSYCHIC : [PokemonType.FIGHTING, PokemonType.POISON],
    PokemonType.ROCK : [PokemonType.BUG, PokemonType.FIRE, PokemonType.FLYING, PokemonType.ICE],
    PokemonType.STEEL : [PokemonType.FAIRY, PokemonType.ICE, PokemonType.ROCK],
    PokemonType.WATER : [PokemonType.FIRE, PokemonType.GROUND, PokemonType.ROCK]      
}