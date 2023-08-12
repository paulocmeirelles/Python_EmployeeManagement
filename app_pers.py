import app
from app.validation.app_validation import InputValues

class App():
    
    def __init__(self):
      print("""Primeiramente Obrigado por utilizar este programa!\nVisando em trazer trazer mais informações sobre, leia o ReadMe!""")
      motoboys = input("Quantos motoboys estão disponíveis para entregas?\n")
      store1 = input("Digite os valores de cada entrega da loja 1, separados por vírgula:\n")
      store2 = input("Digite os valores de cada entrega da loja 2, separados por vírgula:\n")
      store3 = input("Digite os valores de cada entrega da loja 3, separados por vírgula:\n")
      share1 = input("Digite a comissão para entregas da loja 1 (em porcentagem):\n")
      share2 = input("Digite a comissão para entregas da loja 2 (em porcentagem):\n")
      share3 = input("Digite a comissão para entregas da loja 3 (em porcentagem):\n")
      name = input("""Digite o nome do motoboy (exemplo: motoboy3) ou deixe em branco para trazer todos motoboys(pressione apenas ENTER):\n""")
      
      verificationStore1 = InputValues.validationOrders(store1)
      verificationStore2 = InputValues.validationOrders(store2)
      verificationStore3 = InputValues.validationOrders(store3)
      verificationShare1 = InputValues.validationShare(share1)
      verificationShare2 = InputValues.validationShare(share2)
      verificationShare3 = InputValues.validationShare(share3)

      verificationMoto = InputValues.validationInt(motoboys)
      verificationName = InputValues.validationName(name, motoboys)

      if verificationMoto and verificationName:
        result = app.resultDeliveryDay(int(motoboys),
                                       motoboy=InputValues.validationNameExist(name),
                                       share1=verificationShare1,
                                       share2=verificationShare2,
                                       share3=verificationShare3,
                                       store1=verificationStore1,
                                       store2=verificationStore2,
                                       store3=verificationStore3)
        for status in result:
            print(f'{status} : {result[status]}')
      else:
         print("Nome motoboy não encontrado ou valor inserido não é inteiro")

if __name__ == "__main__":
    App()