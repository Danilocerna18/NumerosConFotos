import os

# configuraremos el proyecto 

CANTIDAD = 160000
VALOR_MIN = 0
VALOR_MAX = 255

CARPETA_FOTOS = "fotos"
CARPETA_RESULTADOS = "resultados" # aca se guardaran las fotos y los resultados

# Creamos las carpetas si no existen(esto es por si solo tengo el python para no crearlas a mano)
os.makedirs(CARPETA_FOTOS, exist_ok=True)
os.makedirs(CARPETA_RESULTADOS, exist_ok=True)

print("Configuracion lista")
print(f"Cantidad de numeros que queremos obtener {CANTIDAD:,}")
print(f"Nuestro Rango es de {VALOR_MIN} a {VALOR_MAX}")
print(f"Carpeta de fotos {CARPETA_FOTOS}")
print(f"Carpeta de resultados: {CARPETA_RESULTADOS}")