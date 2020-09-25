#NO CASO ESCOLHI POR DEIXAR O TEMPO DE DEVOLUÇÃO NO EQUIPAMENTO, CASO O DONO DO ESTABELECIMENTO QUEIRA CRIAR MULTIPLOS
#EQUIPAMENTO COM TEMPO DE DEVOLUÇAO VARIANDO
class Equipamento:

    def __init__(self,nome,tempo_devolucao):
        self.nome = nome

        #Cada equipamento tem seus dias de devolucao definido
        self.tempo_devolucao=tempo_devolucao