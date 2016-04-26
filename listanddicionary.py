lista = ["arroz","feijao","carne","queijo"]

print lista;

lista.sort();

print lista;

sublista = lista[0:2];

print lista

print sublista

sublista = lista[1:];

print lista

print sublista

print lista[2]

print lista.index("carne")

lista.remove("carne")

print lista

dicionario = {"nome":"Ivan","idade":28,"lista":lista}

print(dicionario)

for item in lista:
    print "Item:"+item
    
for i in dicionario:
    if type(dicionario[i]) == str:
        print "Item dic:"+dicionario[i]
    else:
        print type(dicionario[i])