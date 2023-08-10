import math

def arrayMoto(quantity):
    arrayMotoboy = []
    for i in range(1,quantity+1):
        arrayMotoboy.append(f"Motoboy{i}")
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


def MotoBoyDelivery(numberMotoboys,store1,store2,store3,share1,share2,share3):
    arrayOrder = []
    round = 0
    didStore1 = False
    didStore2 = False
    didStore3 = False
    arrayMotoboy = arrayMoto(numberMotoboys)
    dictMotoBoy = createDictMotoboy(arrayMotoboy)

    for i in range(math.ceil((len(store1)+len(store2)+len(store3))/numberMotoboys)):
       
      if arrayOrder.count('Motoboy4') == round and len(store1)>0:
          # print('Motoboy4 em direção a loja 1')
          dictMotoBoy["Motoboy4"][f"{round}"]= {"delivery":"loja 1","share":share1,"value":store1[0]}
          store1.pop(0)
          arrayOrder.append("Motoboy4")
          didStore1 = True

      for moto in arrayMotoboy:

        if didStore1 and didStore2 and didStore3:
          didStore1 = False
          didStore2 = False
          didStore3 = False

        if arrayOrder.count(moto) == round and not didStore2 and len(store2)>0: 
          # print(f"{moto} em direção a loja 2")
          dictMotoBoy[moto][f"{round}"] = {"delivery":"loja 2","share":share2,"value":store2[0]}
          store2.pop(0)
          arrayOrder.append(moto)
          didStore2 = True

        elif arrayOrder.count(moto) == round and not didStore3 and len(store3)>0: 
          # print(f"{moto} em direção a loja 3")
          dictMotoBoy[moto][f"{round}"] = {"delivery":"loja 3","share":share3,"value":store3[0]}
          store3.pop(0)
          arrayOrder.append(moto)
          didStore3 = True

        elif arrayOrder.count(moto) == round and not didStore1 and len(store1)>0: 
          # print(f"{moto} em direção a loja 1")
          dictMotoBoy[moto][f"{round}"] = {"delivery":"loja 3","share":share3,"value":store1[0]}
          store1.pop(0)
          arrayOrder.append(moto)
          didStore1 = True

        else:
          didStore1 = False
          didStore2 = False
          didStore3 = False

    
      round +=1

    return dictMotoBoy

def resultDeliveryDay(numberMotoboys,**kwargs):
    
    store1 = kwargs['store1'] if 'store1' in kwargs else [50,50,50]
    store2 = kwargs['store2'] if 'store2' in kwargs else [50,50,50,50]
    store3 = kwargs['store3'] if 'store3' in kwargs else [50,50,100]
    share1 = kwargs['share1'] if 'share1' in kwargs else 0.05
    share2 = kwargs['share2'] if 'share2' in kwargs else 0.05
    share3 = kwargs['share3'] if 'share3' in kwargs else 0.15
    motoboy = kwargs['motoboy'] if 'motoboy' in kwargs else None

    result = MotoBoyDelivery(numberMotoboys,store1,store2,store3,share1,share2,share3)
    motoboys = arrayMoto(numberMotoboys) 

    if motoboy:
       sum = 0
       deliveries = "Entregas em "
       summary = {}
       for delivery in result[motoboy].values():
          if motoboy == "Motoboy5":
            sum += 3 + delivery["value"]*delivery["share"]
          else:
            sum += 2 + delivery["value"]*delivery["share"]
          deliveries += delivery["delivery"] + ";"
       
       summary['deliveries'] = deliveries
       summary['total'] = sum
       return summary
        

    else:
      for moto in motoboys:
        sum = 0
        deliveries = "Entregas em "
        summary = {}
        for delivery in result[moto].values():
            if moto == "Motoboy5":
              sum += 3 + delivery["value"]*delivery["share"]
            else:
              sum += 2 + delivery["value"]*delivery["share"]
            deliveries += delivery["delivery"] + ";"
        
        summary['deliveries'] = deliveries
        summary['total'] = sum
        result[moto]['summary'] = summary
        
      
      return summaryMotoBoy(result,motoboys)


print(resultDeliveryDay(5))



