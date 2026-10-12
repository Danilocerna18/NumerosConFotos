import os

# configuraremos el proyecto 

CANTIDAD = 160000
VALOR_MIN = 0
VALOR_MAX = 255

CARPETA_FOTOS = "fotos"
CARPETA_RESULTADOS = "resultados" # aca se guardaran las fotos y los resultados

# Creamos las carpetas si no existen(esto es por si solo tengo el python para no crearlas a mano)
os.makedirs(CARPETA_FOTOS, exist_ok=True)
os.makedirs(CARPETA_RESULTADOS, exist_ok=True) #ALGO IMPORTANTE ES QUE AL CORRERLO TENGO QUE ESTAR DENTRO DEL PROYECTTO

print("Configuracion lista")
print(f"Cantidad de numeros que queremos obtener {CANTIDAD:,}")
print(f"Nuestro Rango es de {VALOR_MIN} a {VALOR_MAX}")
print(f"Carpeta de fotos {CARPETA_FOTOS}")
print(f"Carpeta de resultados: {CARPETA_RESULTADOS}")

#ahora vamos a buscar nuestras fotos
extensiones = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

nombres_fotos = sorted([
    nombre
    for nombre in os.listdir(CARPETA_FOTOS)
    if nombre.lower().endswith(extensiones)
])

print()
print("Fotos enconstrada")

for nombre in nombres_fotos:
    print(nombre)

print(f"Total de fotos que tienes {len(nombres_fotos)}")


#Antes de seguir vamos a validat siempre tener fotos ya que son claves

if len(nombres_fotos) == 0:
    raise ValueError(
        "No tienes fotos, ponlas dentro de la carpeta llamada fotos"
    )

print("ya validamos")
print(f"Se utilizaran {len(nombres_fotos)} fotos")


# ahora si abriremos las fotos que tengamos

from PIL import Image

imagenes = []

for nombre in nombres_fotos:

    ruta = os.path.join(CARPETA_FOTOS, nombre)

    try:
        # Abriremos la imagen y guardaremos una copia en memoria
        imagen = Image.open(ruta)
        imagen.load()
        imagenes.append((nombre, imagen.copy()))

        print(
            f"la imagen abierta fue: {nombre} "
            f"({imagen.width} x {imagen.height})"
        )

    except Exception as error:
        print(f"No se pudo ver la imagen {nombre}: {error}")

if len(imagenes) == 0:
    raise ValueError("No se pudo abrir ninguna foto porque no existe")

print(f"las fotos que fueron abiertas correctamente fueron {len(imagenes)}")


# tenemos que convertirlo todo a grises 

imagenes_grises = []

for nombre, imagen in imagenes:

    # Convertir cada imagen a un solo canal de intensidad
    imagen_gris = imagen.convert("L")

    imagenes_grises.append((nombre, imagen_gris))

print()
print("Conversion a grises terminada")

for nombre, imagen in imagenes_grises:
    print(f"{nombre}: modo {imagen.mode}") 

# extraeremos nuestros pixeles 
import numpy as np

pixeles_fotos = []

for nombre, imagen in imagenes_grises:

    # Convertiremos la imagen en un arreglo 
    pixeles = np.asarray(imagen, dtype=np.uint8).ravel()
    pixeles_fotos.append(pixeles)

    print(
        f"{nombre}: {len(pixeles):,} pixeles obtenidos de las imagenes"
    )
# y los combinaremos

pixeles_totales = np.concatenate(pixeles_fotos)
print()
print(f"el total de todos los pixeles de las fotos que tienes es de {len(pixeles_totales):,}") 

# verificamos la cantidad de pixeles que tenemos

if len(pixeles_totales) < CANTIDAD:
    raise ValueError(
        f"Necesitamos {CANTIDAD:,}  de pixeles ")

print("si tenemos suficientes pixeles para continuar.")
print(f"tenemos disponibles: {len(pixeles_totales):,}")
print(f"y necesitamos: {CANTIDAD:,}")
# seleccionamos los numeros ya finales que tendremos
# Elegir posiciones distribuidas a lo largo de todos los pixeles
# Asi se utilizan zonas de todas las fotografias combinadas (mientras mas fotos mejor)
posiciones = np.linspace(
    0,
    len(pixeles_totales) - 1,
    CANTIDAD,
    dtype=np.int64
)

# Sacamos los valores de los pixeles que seleccionamos
datos = pixeles_totales[posiciones].astype(np.int64)

print(f"Numeros seleccionados: {len(datos):,}") #este lo puse solo para ver que si agarrara los mismos que en cantidad
print(f"Valor minimo: {datos.min()}")
print(f"Valor maximo: {datos.max()}")
print(f"Valores distintos: {len(np.unique(datos)):,}")