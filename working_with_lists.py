sandwiches = ['cheese', 'ham', 'beef', 'chicken']
for sandwich in sandwiches:
  print('I like {}, lettuce and mayonaise sandwich'.format(sandwich))

print('i like all sandwiches')

animals_4_legs = ['dog', 'cat', 'lion', 'giraffe', 'elephant']
for animal in animals_4_legs:
  print('{} has four legs'.format(animal))
print('All these animals have four legs')

for number in range(1, 21):
  print(number)

# sum_million = sum(range(1, 1000000001))
# print(sum_million)

for odd_number in range(1, 20, 2):
  print(odd_number)

threes = [value * 3 for value in range(1,11)]
print(threes)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)