lista_palavras = []
for i in range(10):
    palavra=input(f"Escreva uma palavra, letra ou número (independente do que escrever, tudo se torna string) {i+1} de 10)\n")
    lista_palavras.append( palavra + '\n')
txt = open("lista.txt", "w+")
txt.writelines(lista_palavras)
