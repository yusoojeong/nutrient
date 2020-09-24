import os
import json
import requests
from dotenv import load_dotenv

#1. nutrient_api_key 가져오기
load_dotenv(verbose=True)
API_KEY = os.getenv('NUT_API_KEY')
nutrient_list = []

st = 1001
end = 2000
i = 1017
url = f'http://openapi.foodsafetykorea.go.kr/api/{API_KEY}/I2790/json/{st}/{end}'
response = requests.get(url).json()
for res in response['I2790']['row']:
    nutrient = {
        'model': 'menus.nutritional',
        'pk': str(i),
        'fields': {
            'nutritionalname': res['DESC_KOR'],
            'tan': 0 if not res['NUTR_CONT2'] else int(float(res['NUTR_CONT2'])),
            'dan': 0 if not res['NUTR_CONT3'] else int(float(res['NUTR_CONT3'])),
            'ji': 0 if not res['NUTR_CONT4'] else int(float(res['NUTR_CONT4'])),
            'dang': 0 if not res['NUTR_CONT5'] else int(float(res['NUTR_CONT5'])),
            'na': 0 if not res['NUTR_CONT6'] else int(float(res['NUTR_CONT6'])),
            'cal': 0 if not res['NUTR_CONT1'] else int(float(res['NUTR_CONT1'])),
            'col': 0 if not res['NUTR_CONT7'] else int(float(res['NUTR_CONT7']))
        }
    }
    i += 1
    nutrient_list.append(nutrient)

# Write JSON
with open('nutritional/nutrient2.json', 'w', encoding="utf-8") as make_file:
    json.dump(nutrient_list, make_file, ensure_ascii=False, indent="\t")
