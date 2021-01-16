if __name__ == "__main__":
    # Create a list named food with two elements 'rice' and 'beans'.
    food = ['rice', 'beans']
    print(food)

    # Append the string 'broccoli' to food using .append().
    food.append('broccoli')
    print(food)

    # Add the strings 'bread' and 'pizza' to food using .extend().
    additional_food = ['bread', 'pizza']
    food.extend(additional_food)
    print(food)

    # Print the first two items in the food list using print() and slicing notation.
    print(food[0:2])

    # Print the last item in food using print() and index notation.
    print(food[-1])

    # Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.
    foods = 'eggs,fruit,orange juice'
    breakfast = foods.split(',')
    print(breakfast)

    # Verify that breakfast has 3 elements using the len built-in.
    print(len(breakfast))

    # prompts the user for a floating-point value until they enter stop. Store their entries in a list, and then find the average, min, and max of their entries and print them those values.
    x = 'Go'

    values = []
    while x != 'stop':
        value = input("Enter your floating-point values (enter stop to end):")
        if value != 'stop':
            values.append(float(value))
        x = value
    print(max(values))
    print(min(values))
    average = sum(values)/len(values)
    print(average)
    #print(dir(values))
