f = open('mateus.txt', 'r')
texto = f.readlines()

a = 0

while a < len(texto):
    if texto[a] == '\n':
        local = texto.index(texto[a])
        texto.pop(local)
    else:
        texto[a] = texto[a].split(' ')
        a += 1

for i in texto:
    local = texto.index(i)
    for b in i:
        local2 = texto[local].index(b)
        if "\n" in b:
            texto[local][local2] = b.replace("\n", '')

lista1 = texto
print(lista1)

def bubblesorte(lista1):
    final=len(lista1)
    while final>0:
        i=0
        while i<final-1:
            if lista1[i]>lista1[i+1]:
                temp=lista1[i]
                lista1[i]=lista1[i+1]
                lista1[i+1]=temp

            i +=1
        final-=1
v=(lista1)
bubblesorte(v)
print(v)


