import os
import json
import requests
from dotenv import load_dotenv

#1. nutrient_api_key 가져오기
load_dotenv(verbose=True)
API_KEY = os.getenv('NUT_API_KEY')
nutrient_list = []

st = 1
end = 10
i = 17
url = f'http://openapi.foodsafetykorea.go.kr/api/{API_KEY}/I2790/json/{st}/{end}'
response = requests.get(url).json()
# print(response['I2790']['row'])
for res in response['I2790']['row']:
    nutrient = {
        'model': 'HDMD.nutritional',
        'nutritionalNo': str(i),
        'fields': {
        'nutritionalName': res['DESC_KOR'],
        'tan': res['NUTR_CONT2'],
        'dan': res['NUTR_CONT3'],
        'ji': res['NUTR_CONT4'],
        'dang': res['NUTR_CONT5'],
        'na': res['NUTR_CONT6'],
        'cal': res['NUTR_CONT1'],
        'col': res['NUTR_CONT7']
    }}
    i += 1
    nutrient_dict['rows'].append(nutrient)

# Write JSON
with open('nutrient.json', 'w', encoding="utf-8") as make_file:
    json.dump(nutrient_dict, make_file, ensure_ascii=False, indent="\t")
