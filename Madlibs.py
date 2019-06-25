
STORY = """
At a certain time in his life, %s mentioned his/her love and respect for %s
things. A friend told %s it was a %s thing to say! Meanwhile though, the %ss
were busy exorcising some %s from a %s. While they began to %s because of
a pretty funny %s, all the %ss got together to make something terribly %s.
Concerned, %s texted %s, who flew %s to %s and managed to perfectly land %s in
a shimmering lake of molten %s. %s woke up covered in %ss, and thought:
'Well, no more %s for me!'

"""

print("You're now playing Madlibs!")
name = input("Enter a name: ")

print("Hello {}!".format(name))
print("Please enter three different adjectives below: ")
adjective1 = input("Number one: ")
adjective2 = input("Number two: ")
adjective3 = input("Number three: ")
verb1 = input("Please enter a single verb: ")
noun1 = input("Please enter a noun: ")
noun2 = input("Please enter another noun: ")
noun3 = input("Please enter another noun: ")
print("Please enter each of one of the following: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
leader = input("Enter a leader: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
fish = input("Enter a fish: ")

print(STORY %(name, adjective1, name, adjective2, animal, food, noun1, verb1, noun2, fruit, adjective3, name, leader, name, country, name, dessert, name, fish, noun3))
