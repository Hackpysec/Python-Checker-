# Python-Checker


# Verificador de Hash en VirusTotal

Este proyecto es un script de Python que permite a los usuarios verificar hashes en VirusTotal.

## Requisitos

- Python 3
- Módulo `requests` de Python

## Uso

1. Clona este repositorio a tu máquina local.
```
git clone https://github.com/Hackpysec/Python-Checker-.git
```

2. Instala el módulo `requests` de Python si aún no lo has hecho. Puedes hacerlo con el siguiente comando: 
```
pip install requests
```

3. Ejecuta el script con el comando:
```
python check_hash.py
```

4. Cuando se te solicite, ingresa tu clave de API de VirusTotal.
5. Ingresa el hash que deseas verificar.

El script consultará el hash en VirusTotal y mostrará los resultados.

## Funciones

El script contiene las siguientes funciones:

- `check_hash(hash_to_check)`: Esta función toma un hash como argumento y realiza una solicitud a la API de VirusTotal para obtener información sobre ese hash.
- `print_result(result)`: Esta función toma el resultado de la consulta a VirusTotal y lo imprime de manera legible.





## Demo

![Python Checker GIF](https://file.notion.so/f/f/1cd5049b-3b5a-4577-b5c5-17f623e92663/1a00c381-33a8-47c1-9d08-2fbb1b95598c/python_checker.gif?id=1222fe67-7cd5-4da4-90d4-bf135d3e39a1&table=block&spaceId=1cd5049b-3b5a-4577-b5c5-17f623e92663&expirationTimestamp=1698192000000&signature=2HYcbq3_WYXDdJ7VDqVKQeHVmvSHeA2r5NqlFbsu7O8&downloadName=python+checker.gif)


