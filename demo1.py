f= open('first file.txt')

content = f.read()
print(content)
f.close()

f= open('first file.txt','w')
f.write("i am a humble person")
f.close()