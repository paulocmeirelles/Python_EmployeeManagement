import app
from app.validation.app_validation import InputValues

class App():
    
    def __init__(self):
      # motoboys = input("Quantos motoboys estão disponíveis para entregas?\n")
      # store1 = input("Digite os valores de cada entrega da loja 1, separados por vírgula:\n")
      # store2 = input("Digite os valores de cada entrega da loja 2, separados por vírgula:\n")
      # store3 = input("Digite os valores de cada entrega da loja 3, separados por vírgula:\n")
      # share1 = input("Digite a comissão para entregas da loja 1 (em porcentagem):\n")
      # share2 = input("Digite a comissão para entregas da loja 2 (em porcentagem):\n")
      # share3 = input("Digite a comissão para entregas da loja 3 (em porcentagem):\n")
      
      name = input("Digite o nome do motoboy ou deixe em branco para trazer todos:\n")
      motoboys = 5

      verificationMoto = InputValues.validationInt(motoboys)
      verificationName = InputValues.validationName(name, motoboys)

      if verificationMoto and verificationName:
        result = app.resultDeliveryDay(int(motoboys),
                                       motoboy=InputValues.validationNameExist(name))
        for status in result:
            print(f'{status} : {result[status]}')
      else:
         print("Nome motoboy não encontrado")
        #  print("Nome motoboy não encontrado ou valor inserido não é inteiro")

if __name__ == "__main__":
    App()