import pytest

# HELPERS
from app.main.helpers import app_helper
def test_arrayMoto():
    assert app_helper.arrayMoto(3) == ['motoboy1','motoboy2','motoboy3']

def test_createDictMotoboy():
    assert app_helper.createDictMotoboy(['motoboy1']) == {"motoboy1":{}}

def test_summaryMotoBoy():
    dictionary = {'test1': {'0': {'delivery': 'loja 2', 'share': 0.10, 'value': 100},
                            '1': {'delivery': 'loja 3', 'share': 0.50, 'value': 100},
                            "summary":{"deliveries":"loja 2; loja 3;","total":64.0}
                            }}
    assert app_helper.summaryMotoBoy(dictionary,['test1']) == {"test1":{'deliveries': 'loja 2; loja 3;', 'total': 64.0}}


# VALIDATION
from app.validation.app_validation import InputValues
def test_validationInt():
  assert InputValues.validationInt(10)

def test_validationName():
    assert InputValues.validationName("motoboy30",30)

def test_validationNameExist():
    assert InputValues.validationNameExist("TEST@") == "test@"

# APP FUNCTIONS
import app
def test_MotoBoyDelivery():
    assert app.MotoBoyDelivery(3,store1=[100,100,100],
                               store2=[50,75],store3=[150],
                               share1=0.15,share2=0.25,share3=0.35) == {
                                   'motoboy1': {'0': {'delivery': 'loja 2', 'share': 0.25, 'value': 50}, 
                                                '1': {'delivery': 'loja 2', 'share': 0.25, 'value': 75}}, 
                                   'motoboy2': {'0': {'delivery': 'loja 3', 'share': 0.35, 'value': 150}, 
                                                '1': {'delivery': 'loja 1', 'share': 0.15, 'value': 100}}, 
                                   'motoboy3': {'0': {'delivery': 'loja 1', 'share': 0.15, 'value': 100}}}