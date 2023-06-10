import numpy as np
import pickle
import json
import sklearn
__city=None
__data_column=None
__model=None
__brand=None

def predict_prices(kms_driven,owner,age,power,city,brand):
    try:
        city_index=__data_column.index(city.lower())
    except:
        city_index=-1  
    try:      
        brand_index=__data_column.index(brand.lower())
    except:
        brand_index=-1    
    x=np.zeros(len(__data_column))
    x[0]=kms_driven
    x[1]=owner
    x[2]=age
    x[3]=power
    if city_index>=0:
        x[city_index]=1
    print(__data_column[city_index])
    if brand_index>=0:
        x[brand_index]=1
    print(__data_column[brand_index])
    return (__model.predict([x])[0])

def get_brand_names():
    return __brand
def load_saved_artifacts():
    print("loading saved artifacts started")
    global __data_column
    global __city
    global __brand
    
    with open("C:/Users/91904/OneDrive/Desktop/SECOND HAND BIKE SALE/Server/Artifacts/columns.json",'r') as f:
        __data_column= json.load(f)["data_columns"]
        __city=__data_column[4:63]
        __brand=__data_column[64:85]
        
        
    global __model    
    with open("C:/Users/91904/OneDrive/Desktop/SECOND HAND BIKE SALE/Server/Artifacts/India_bike_prices_model.pickle",'rb',) as f:
        __model=pickle.load(f)
        print("Loading saved artifacts done")
def get_city_name():
    global __city
    return __city     