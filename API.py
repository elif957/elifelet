import requests 

API_KEY = "a90b4cb0bddf86780a4d04e71418417d" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def obtener_clima(ciudad):
    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    respuesta = requests.get(BASE_URL, params=params)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        clima = datos["weather"][0]["description"]
        temperatura = datos["main"]["temp"]
        return f"El clima en {ciudad} es {clima} con una temperatura de {temperatura}°C."
    else:
        return "No se pudo obtener el clima."

print(obtener_clima("Ciudad de México"))

