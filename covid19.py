import requests

url = "https://coronavirus-smartable.p.rapidapi.com/stats/v1/UZ/"

headers = {
 "X-RapidAPI-Key": "f4152adb40mshddc3034080b186bp18b494jsn1bd9726ff216",
 "X-RapidAPI-Host": "coronavirus-smartable.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

kasallanaganlar_soni = response.json()['stats']['totalConfirmedCases']
vafot_etganlar_soni = response.json()['stats']['totalDeaths']
tuzalganlar_soni = response.json()['stats']['totalRecoveredCases']
vaqt = response.json()['updatedDateTime']
print(f"O'zbekistonda {vaqt} holatiga ko'ra, COVID19 bo'yicha\nkassalanganlar soni: {kasallanaganlar_soni},\ntuzlaganlar soni:{tuzalganlar_soni}\nVafot etganlar soni {vafot_etganlar_soni}")