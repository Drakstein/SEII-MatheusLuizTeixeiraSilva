# MATHEUS LUIZ TEIXEIRA SILVA 11311EMT025

message = 'Hello World'
message1 = 'Hello World Again'
print('Hello World')
print(message)
print(message1)

print(len(message))

print(message[0])
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])

print(message.lower())
print(message.upper())

print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))
print(message.find('Marte'))

new_message = message.replace('World','Universe')

print(new_message)

message = message.replace('World','Universe')
print(message)

greeting = 'Hello'
name = 'Matheus'

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)


message = f'{greeting}, {name}. Welcome!'
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))

print(help(str))
print(help(str.lower))