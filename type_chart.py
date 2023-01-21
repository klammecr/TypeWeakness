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

# # Enum tutorial
# print(f"Number of Pokemon Types: {len(PokemonType)}")

# # Call Syntax
# fire_type = PokemonType("Fire")
# print(f"Call Syntax: Fire Type: {fire_type}")

# # Illegal Call Syntax
# # fire_type = PokemonType("alk;fdsjlk")
# # print(f"Call Syntax: Fire Type: {fire_type}")

# # Index Syntax
# fire_type = PokemonType.FIRE
# print(f"Index Syntax: Fire Type: {fire_type}")

# # Create the flying type
# flying_type = PokemonType.FLYING
# print(f"String that is mapped to the pokemon type {flying_type} is {flying_type.value}")


# # For a concrete pokemon
# charizard_type = [PokemonType.FLYING, PokemonType.FIRE]

# charizard_type_strs = []
# charizard_type_names = []
# for type in charizard_type:
#     # Getting a list of type strings
#     charizard_type_strs.append(type.value)
#     charizard_type_names.append(type.name)

# print(f"Full type representation: {charizard_type}")
# print(f"String list for Charizard's type: {charizard_type_strs}")
# print(f"Name list for Charizard's type: {charizard_type_names}")

# # # Check to see if we can get charizard's type
# reconstructed_charizard_types = []
# for type_str in charizard_type_strs:
#     reconstructed_charizard_types.append(PokemonType(type_str))

# print(f"Reconstructed charizard types: {reconstructed_charizard_types}")
# print(reconstructed_charizard_types)
# print(charizard_type)

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