
# Describe the sketch comedy group
name = 'Monty Python'
description = 'sketch comedy group'
year = 1969

# Introduce them

sentence = name + ' is a ' + description + ' formed in ' + str(year)

print(sentence)

# print also casts to string automatically.
# So this works:

print(name, 'is a', description, 'formed in', year)


#describe MP work:

famous_sketch = "\n\tHell's Grannies"
famous_sketch2 = "\n\tThe Dead Parrot"
print('Famous Work:', famous_sketch, famous_sketch2)

word1 = 'Good'
word2 = 'Evening'

half1 = len(word1)//2
half2 = len(word2)//2
print(word1[half1:],word2[half2:])
