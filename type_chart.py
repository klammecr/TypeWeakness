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


weak_table = \
{
    PokemonType.BUG:[PokemonType.FIRE, PokemonType.FLYING,PokemonType.ROCK],
    PokemonType.DARK:[PokemonType.BUG, PokemonType.FAIRY, PokemonType.FIGHTING], 
    PokemonType.DRAGON:[PokemonType.DRAGON, PokemonType.FAIRY, PokemonType.ICE],
    PokemonType.ELECTRIC:[PokemonType.GROUND], 
    PokemonType.FAIRY:[PokemonType.POISON, PokemonType.STEEL], 
    PokemonType.FIGHTING:[PokemonType.FAIRY, PokemonType.FLYING, PokemonType.PSYCHIC], 
    PokemonType.FLYING:[PokemonType.ELECTRIC, PokemonType.ICE, PokemonType.ROCK], 
    PokemonType.GHOST:[PokemonType.DARK, PokemonType.GHOST], 
    PokemonType.GROUND:[PokemonType.GRASS, PokemonType.ICE, PokemonType.WATER], 
    PokemonType.ICE:[PokemonType.FIGHTING, PokemonType.FIRE, PokemonType.ROCK, PokemonType.STEEL],
    PokemonType.NORMAL:[PokemonType.FIGHTING], 
    PokemonType.POISON:[PokemonType.GROUND, PokemonType.PSYCHIC], 
    PokemonType.PSYCHIC:[PokemonType.BUG, PokemonType.DARK, PokemonType.GHOST], 
    PokemonType.ROCK:[PokemonType.FIGHTING, PokemonType.GRASS, PokemonType.GROUND, PokemonType.STEEL, PokemonType.WATER], 
    PokemonType.STEEL:[PokemonType.FIGHTING, PokemonType.FIRE, PokemonType.GROUND], 
    PokemonType.FIRE:[PokemonType.GROUND, PokemonType.ROCK, PokemonType.WATER], 
    PokemonType.WATER:[PokemonType.ELECTRIC, PokemonType.GRASS], 
    PokemonType.GRASS:[PokemonType.BUG, PokemonType.FIRE, PokemonType.FLYING, PokemonType.ICE, PokemonType.POISON]
}

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