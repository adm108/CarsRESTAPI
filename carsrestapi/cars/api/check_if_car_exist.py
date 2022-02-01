from msilib.schema import Error
import requests,json


def check_if_car_exist(make, model):
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/'
    ready_url = url + make + '?format=json'
    response = requests.get(ready_url)
    data = response.json()
    if data['Count'] == 0:
        return False
    else:
        for element in data['Results']:
            if element['Model_Name'] == model:
                return True
    return False
