def hello(name = 'Happy'):
    print("Hello " + name )

hello()
print('*^*' * 20)


a = hello

print(a)
print(a())
print(a('Khusi'))