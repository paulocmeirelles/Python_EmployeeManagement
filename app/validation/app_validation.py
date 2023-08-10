from app.main.helpers.app_helper import arrayMoto
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