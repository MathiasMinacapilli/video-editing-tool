# Video Editing Tool

Herramienta pensada para edicion de videos a traves de listas de comandos sobre porciones de
videos desde la consola de comandos.

# Ejemplos

## Cortar video

El "array" de tiempos que le pasamos como input es los "pedazos"
de video que queremos mantener.

```
poetry run python3 edit.py test.mp4 0:02-01:11,1:12-5:04
```

## Concatenar videos de un directorio (videos/)

1. Crear directorio "videos/" bajo este directorio
1. Agregar los videos bajo el directorio "videos/" y cambiar el nombre por numeros en el
   orden en que se quieran concatenar
1. Ejecutar el siguiente comando:

```bash
poetry run python3 edit.py videos/
```

## Concatenar videos a partir de una lista

` TODO`` `
