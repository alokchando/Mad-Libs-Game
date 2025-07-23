#Mad Libs Game

#user input section 
place1 = input('Place: ')
adjective1 = input('Adjective: ')
animal1 = input('Animal: ')
noun = input('Noun: ')
verb1 = input('Verb: ')
adjective2 = input('Adjective: ')
place2 = input('Place: ')
animal2 = input('Animal: ')
adjective3 = input('Adjective: ')
verb2 = input('Verb: ')
past_tense_verb = input('Past tense verb: ')
adjective4 = input('Adjective: ')

Mad_Libs = f'Today I went to the {place1}.\
I saw a {adjective1} {animal1} jumping up and down in a {noun}.\
It {verb1} through the large tunnel that led to its {adjective2} {place2}.\
I got some peanuts and passed them through the cage to a gigantic gray {animal2} towering above my head.\
Feeding that animal made me hungry.\
I went to get a {adjective3} scoop of ice cream.\
It filled my stomach. Afterwards, I had to {verb2} to catch our bus.\
When I got home, I {past_tense_verb} my mom for a {adjective4} day at the zoo.'
print(Mad_Libs)
print('Thanks for playing Mad Libs!')
