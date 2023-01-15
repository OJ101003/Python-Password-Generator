import random
import string

# Contains string list of lowercase and uppercase letters, and numbers
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numbers = string.digits

# Stores the string variables in a dictionary
locations = {
    1 : lowerCase,
    2 : upperCase,
    3 : numbers
}

# Dictionary that stores previously used characters and numbers
previouslyUsed = {}

# Asks for desired password length, makes sure length isn't negative
passwordLength = int(input("Password Length: "))
while passwordLength < 0:
    print("Invalid length")
    passwordLength = int(input("Password Length: "))

# String that contains password output
outputPassword = ""

# Stores the last location used
prevLoc = 0

while len(outputPassword) < passwordLength:
    # If the password length is greater than 62, it requires the previously used dictionary to be reset in order to generate longer password
    if (len(outputPassword)% 62) == 0:
        previouslyUsed = {}
    # Gives a location to go to in the location dictionary
    loc = random.randint(1,3)
    # Makes a random choice from the location picked
    rand = random.choice(locations[loc])
    # Makes sure selected choice wasn't previously used
    if (rand not in previouslyUsed):
        # Personal desire to not have numbers next to each other, if they are it redoes the loop
        if (prevLoc == 3) and loc == 3:
            continue
        # Appends the random char to the string, updates previous location and previously used char
        outputPassword += rand
        prevLoc = loc
        previouslyUsed[rand] = 0
# Prints output password
print(outputPassword)