if __name__ == "__main__":
    #Create a tuple named pokemon that holds the strings 'picachu', 'charmander', and 'bulbasaur'.
    pokemon = ('picachu','charmander','bulbasaur')
    print(type(pokemon))
    print(pokemon)

    #Using index notation, print() the string that located at index 1 in pokemon
    print(pokemon[0])

    #Unpack the values of pokemon into the following three new variables with names starter1, starter2, starter3.
    (starter1, starter2, starter3) = pokemon 
    print(starter1+' '+starter2+' '+starter3)

    #Create a tuple using the tuple() built-in, that contains the letters of your name.
    name = tuple('Leonard')
    print(name)
    
    #Check whether the character i is in your tuple representation of your name.
    letter='i'
    print(f'Is the letter "i" in your name?:{letter in name}')

    #Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function.
    print('for loop')
    for i in range(2,10):
        print(i)
    
    #Use a while loop that prints out the integers 2 through 10.
    print('while loop')
    x=2
    print(x)
    while x <= 10:
        print(x)
        x+=1
    
    #Write a for loop that iterates over the string 'This is a simple string' and prints each character.
    string = 'This is a simple string'
    for i in tuple(string):
        print(i)

    #Using a nested for loop, iterate over the following set ('this', 'is', 'a', 'simple', 'set') and print each word, three times.
    tuple_word = ('this', 'is', 'a', 'simple', 'set')
    for i in tuple_word:
        for x in range(0,3):
            print(i)

