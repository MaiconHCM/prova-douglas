#A classe emprestimo vai fazer função de controlar os emprestimos.
from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, pessoa, equipamento):
        self.pessoa=pessoa
        self.equipamento=equipamento

        #soma dias ao dia de hoje que seria o tempo de devolução sem contar feriado :/
        d = datetime.today() + timedelta(equipamento.tempo_devolucao)
        self.data_devolucao=d

    def to_string(self):
        print(f'Pessoa:{self.pessoa.nome}\nEquipamento:{self.equipamento.nome}\nDevolução em:{self.data_devolucao}')