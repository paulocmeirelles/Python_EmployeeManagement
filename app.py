import app
from app.validation.app_validation import InputValues

class App():
    
    def __init__(self):
      print("""Primeiramente Obrigado por utilizar este programa!\nVisando em trazer trazer mais informações sobre, leia o ReadMe!""")
      
      name = input("""Digite o nome do motoboy (exemplo: motoboy3) ou deixe em branco para trazer todos motoboys(pressione apenas ENTER):\n""")
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

if __name__ == "__main__":
    App()