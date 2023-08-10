import app
from app.validation import app_validation


# motoboys = input("Quantos motoboys estão disponíveis para entregas?\n")
# #Validation here
# motoboys = int(motoboys)
motoboys = 5
# name = input("Digite o nome do motoboy ou deixe em branco para trazer todos:\n")
# if(name==""):
#     name = None
name=None
#Validation here5
result = app.resultDeliveryDay(motoboys,motoboy=name)
for status in result:
    print(f'{status} : {result[status]}')