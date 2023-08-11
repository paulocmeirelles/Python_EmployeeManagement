from app.main.helpers.app_helper import arrayMoto
from ast import literal_eval
class InputValues():
    
    @staticmethod
    def validationInt(number):
        try:
            number = int(number)
            return True
        except:
            return  False
        
    @staticmethod
    def validationName(name,number):
        """Here is a possibility to validate with db"""
        try:
            array = arrayMoto(int(number))
            name = name.replace(" ","").lower()
            if name in array or name=="":  
              return True
            else:
                return False
        except:
            return  False
        
    @staticmethod
    def validationNameExist(name):
        if name=="":
            name = None
            return name
        else:
            return name.lower()
        
    @staticmethod
    def validationShare(number):
        if number=="":
            number = None
            return number
        else:
            number = number.replace(",",".").replace("%","")
            try:
                number = float(number)
                return number
            except:
                return False
            
    @staticmethod
    def validationOrders(array):
        if array=="":
            array = None
            return array
        else:
            array = "["+array.replace(",",".").replace("[","").replace("]","")+"]"
            try:
                array = literal_eval(array)
                return array
            except:
                return None
            