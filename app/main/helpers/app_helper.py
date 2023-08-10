def arrayMoto(quantity):
    arrayMotoboy = []
    [arrayMotoboy.append(f"motoboy{x}") for x in range(1,quantity+1)]
    return arrayMotoboy

def createDictMotoboy(array):
   dictMotoBoy = {}
   for moto in array:
      dictMotoBoy[f"{moto}"] = {}
   return dictMotoBoy

def summaryMotoBoy(dict,motoboys):
   dictionary = {}
   for moto in motoboys:
      dictionary[moto] = dict[moto]['summary']
      
   return dictionary