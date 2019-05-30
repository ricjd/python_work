name = ['suzanne', 'jim', 'john', 'ann marie', 'greg', 'kevin']

print('{} can\'t make it dinner'.format(name[2].title()))

name[2] = 'karren'

name.insert(0, 'stan')
name.insert(3, 'janki')
name.append('kai')

print('Currently there are {} guests'.format(len(name)))

cant_come = name.pop()
print('Sorry {}, you can\'t come to dinner'.format(cant_come.title()))
cant_come = name.pop()
print('Sorry {}, you can\'t come to dinner'.format(cant_come.title()))
cant_come = name.pop()
print('Sorry {}, you can\'t come to dinner'.format(cant_come.title()))
cant_come = name.pop()
print('Sorry {}, you can\'t come to dinner'.format(cant_come.title()))
cant_come = name.pop()
print('Sorry {}, you can\'t come to dinner'.format(cant_come.title()))
cant_come = name.pop()
print('Sorry {}, you can\'t come to dinner'.format(cant_come.title()))
cant_come = name.pop()
print('Sorry {}, you can\'t come to dinner'.format(cant_come.title()))

print('Welcome to dinner {}'.format(name[0].title()))
print('Welcome to dinner {}'.format(name[1].title()))

name.remove('stan')
name.remove('suzanne')
print(name)


places = ['italy', 'japan', 'new zeland', 'australia']

print('normal', places)
print('sorted', sorted(places))
print('normal', places)
print('S reversed', sorted(places,reverse=True))
print('normal', places)
places.reverse()
print('resversed', places)
places.reverse()
print('normal', places)