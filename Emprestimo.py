#A classe emprestimo vai fazer função de controlar os emprestimos.
from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, pessoa, equipamento,dias):
        self.pessoa=pessoa
        self.equipamento=equipamento

        #caso ele definir dias de devolução na criação do emprestimo, ele seta ela
        if(dias):
            d = datetime.today() + timedelta(dias)
            self.data_devolucao = d
        else:
            #caso não, ele se baseia na data limite do equipamento
            # soma dias ao dia de hoje que seria o tempo de devolução sem contar feriado :/
            d = datetime.today() + timedelta(equipamento.tempo_devolucao)
            self.data_devolucao=d

    def to_string(self):
        print(f'Pessoa:{self.pessoa.nome}\nEquipamento:{self.equipamento.nome}\nDevolução em:{self.data_devolucao}')