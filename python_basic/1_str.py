greeting = 'Hello World'
name = 'Michael'

welcome = f'{greeting.upper()}, {name}'

print(welcome)

print(len(greeting))
print(greeting[0:5])
print(greeting[:5])
print(greeting[6:])

print(greeting.lower())
print(greeting.count('l'))
print(greeting.find('l'))

msg = greeting.replace('World', 'Universe')
print(msg)


#print(dir(str))
#print(help(str))
#print(help(str.lower))

# concatenate string...
arr = []
arr.append(greeting)
arr.append(name)
str = ' '.join(arr)
print(str)

str = "-"
seq = ("a", "b", "c")       # 字符串序列
print(str.join( seq ))
