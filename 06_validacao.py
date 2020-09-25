import re
import unicodedata

#O professor pediu uma classe nessa questão, então fiz essa classe

class Controle_senha:
  def __init__(self, senha):
    self.senha = senha

  def verifica_senha(self):
      #VERIFICA SEM TEM NÚMERO
      if re.search("[0-9]", self.senha):

          #AGORA REMOVE CARACTERES ESPECIAIS
          senha_sem_caracters=re.sub('[^a-zA-Z0-9 \\\]', '', self.senha)

          #CASO O TAMNHO FOR DIDERENTE
          if(len(senha_sem_caracters)!=len(self.senha)):
            #SIGNIFICA QUE POSSUI CARACTERES ESPECIAIS
            print('Senha válida')
          else:
              print('Senha invalida')
      else:
          print('Senha invalida')

controle_senha=Controle_senha(input('Informe sua senha:\n'))
controle_senha.verifica_senha()