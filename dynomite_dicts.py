if __name__=="__main__":
    #Create an empty dictionary called pokedex.
    pokedex = {}
    print(pokedex)

    #Add the following key, value pairs to the dictionary:
    pokedex = {
    'Venosaur':['Grass','Poisen'],
    'Charizard':['Fire','Flying'],
    'Blastoise':['Water']
    }
    print(pokedex)

    #Remove 'Blastoise' from the dictionary.
    del pokedex['Blastoise']

    print(pokedex)
