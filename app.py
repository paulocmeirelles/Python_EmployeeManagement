import app
from app.validation.app_validation import InputValues

class App():
    
    def __init__(self):
      motoboys = input("Quantos motoboys estão disponíveis para entregas?\n")
      name = input("Digite o nome do motoboy ou deixe em branco para trazer todos:\n")
      
      verificationMoto = InputValues.validationInt(motoboys)
      verificationName = InputValues.validationName(name, motoboys)
      if verificationMoto and verificationName:
        result = app.resultDeliveryDay(int(motoboys),motoboy=InputValues.validationNameExist(name))
        for status in result:
            print(f'{status} : {result[status]}')
      else:
         print("Nome motoboy não encontrado ou valor inserido não é inteiro")

if __name__ == "__main__":
    App()