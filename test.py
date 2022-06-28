
import requests

response = requests.get().json()

print(response['results'])
#response que necesitamos enviar a la pag, accedemos al interior de resultados 
#python test.py