from Equipamento import Equipamento
from Pessoa import Pessoa
from Emprestimo import Emprestimo

equipamentos=[]
#Lista os equipamentos e seus respectiva data de devolução pré-estabelecida
equipamentos.append(Equipamento('Cortador de grama',30))
equipamentos.append(Equipamento('Betoneira',60))
equipamentos.append(Equipamento('Fritadeira',20))


pessoa_maicon=Pessoa('Maicon')
pessoa_douglas=Pessoa('Douglas')
pessoa_geri=Pessoa('géri')

emprestimos=[]

#Aqui são realizado vários emprestimos (como exemplo)

#Maicon pegou emprestado o cortador de grama
emprestimos.append(Emprestimo(pessoa_maicon,equipamentos[0],0))

#Géri pegou emprestado uma betoneira
emprestimos.append(Emprestimo(pessoa_geri,equipamentos[1],0))

#Douglas pegou emprestado uma fritadeira, mandando "um dia" para devolucao
emprestimos.append(Emprestimo(pessoa_douglas,equipamentos[2],1))

for emprestimo in emprestimos:
    emprestimo.to_string()