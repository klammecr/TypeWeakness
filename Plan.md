# Big Picture
- Pokemon -> Black Box -> What is it weak against, and how weak/strong (2x, 4x, .5x, .25x)

# Step 1
## Big Picture:
Name -> Type Information
## Details
- Have a database of pokemon
- Be able to query type information based on name, id, etc.

# Step 2
## Big Picture:
Type Information -> Description of Weakness

## Details:
- Create a chart/matrix in which we can see which types are weak to which types
- Define some sort of schema a data structure for the weakness description
    - Ex: {"0.25":[], "0.5": [], "2.0": ["fire", "water]}
    - Concretely, you will want to define a data structure that is consistent across all possible conjurging of type weakness and that it's enforced