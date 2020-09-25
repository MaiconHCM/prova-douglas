from Equipamento import Equipamento
from Pessoa import Pessoa
from Emprestimo import Emprestimo

equipamento_cortador_de_grama=Equipamento('Cortador de grama',30)
equipamento_betoneira=Equipamento('Betoneira',60)
equipamento_fritadeira=Equipamento('Fritadeira',20)


pessoa_maicon=Pessoa('Maicon')
pessoa_douglas=Pessoa('Douglas')
pessoa_geri=Pessoa('géri')

emprestimos=[]
emprestimos.append(Emprestimo(pessoa_maicon,equipamento_cortador_de_grama))
emprestimos.append(Emprestimo(pessoa_geri,equipamento_fritadeira))
emprestimos.append(Emprestimo(pessoa_douglas,equipamento_betoneira))
for emprestimo in emprestimos:
    emprestimo.to_string()