frase=input('Escreva sua frase:\n')
frase_sem_pares=''
i=1
for letra in frase:
    if i%2:
        frase_sem_pares+=letra
    i+=1

print(f'Frase sem pares:\n{frase_sem_pares}')