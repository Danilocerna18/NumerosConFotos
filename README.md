# Proyecto Danilo y Miguel

## Que hicimos

Este proyecto genera 160,000 numeros entre 0 y 255 utilizando fotos y bytes aleatorios de nuestro sistema operativo

## Como hicimos el funcionamiento
 
Esto es solo a grandes razgos esta mas explicado en nuestro video 
1. Busca las fotos dentro de la carpeta `fotos`.
2. Convierte las imagenes a escala de grises.
3. Extrae los pixeles y selecciona posiciones aleatorias para decidir cuales usar.
4. Combina los pixeles con bytes aleatorios usando XOR que es una operacion clave aca.
5. Guarda los numeros en `resultados/numeros_generados.txt`.

## Como ejecutarlo

Suponiendo que tienen todas las librerias instaladas desde la terminal, dentro de la carpeta del proyecto:

```bash
python generador_fotos.py
```

Los numeros generados se guardaran en la carpeta `resultados`.

## Pruebas

Los resultados se pueden analizar con pruebas estadisticas para revisar su distribucion y posibles patrones, y en este caso nos dimos cuenta que no tienen ningun patron 
