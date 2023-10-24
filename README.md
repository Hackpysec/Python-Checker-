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

![Python Checker GIF](blob:https://itlaedudo-my.sharepoint.com/ec24c060-7a5f-409a-b5a1-8b80acaf2baa)


> [!NOTE]
> El token de Virustotal se obtiene al registrarnos en su sitio web.


