import requests

# Solicitar al usuario ingresar la clave de API de VirusTotal
api_key = input("Por favor, ingresa tu clave de API de VirusTotal: ")

# URL base de la API de VirusTotal
base_url = 'https://www.virustotal.com/vtapi/v2/'

# Función para consultar un hash en VirusTotal
def check_hash(hash_to_check):
    params = {'apikey': api_key, 'resource': hash_to_check}
    url = base_url + 'file/report'
    
    response = requests.get(url, params=params)
    result = response.json()
    
    return result

# Función para imprimir el resultado de la consulta
def print_result(result):
    if result['response_code'] == 0:
        print("Hash no encontrado en VirusTotal")
    else:
        print("Resultados para el hash:", result['resource'])
        print("Detalles:")
        for scanner, data in result['scans'].items():
            print(f"{scanner}: {data['result']}")
        
# Main
if __name__ == "__main__":
    hash_to_check = input("Introduce el hash que deseas consultar en VirusTotal: ")
    result = check_hash(hash_to_check)
    print_result(result)
