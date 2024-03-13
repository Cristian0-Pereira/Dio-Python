nome = "Cristiano"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá mundo!   "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("<<<<" + menu + ">>>>")
print(menu.center(14, "#"))
print("-".join(menu))

PI = 3.14159
print(f'{PI:10.2f}')

dados = {"nome": "Cristiano", "idade": 40}
# Biblioteca.
print("Nome: {nome} \nIdade: {idade}".format(**dados))

# "Fatiamento de String"

nome = "Cristiano Pereira da Silva Cabral"
nome[0] 
'C'
nome[-1] # pega a última letra
'l' 
nome[:9]
'Cristiano'
nome[10:]
'Pereira da Silva Cabral'
nome[10:16]
'Pereir'
nome[10:16:2]
'Pri'
nome[:]
'Cristiano Pereira da Silva Cabral'
nome[::-1] # espelhamento
'larbaC avliS ad ariereP onaitsirC'
nome[start:stop:step]
