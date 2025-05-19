from nicegui import ui  # Se importa la biblioteca NiceGUI para crear interfaces gráficas web

# Lista de diccionarios que representa los datos a mostrar en la tabla
datos = [
    {'Nombre': 'Ana', 'Edad': 21},
    {'Nombre': 'Luis', 'Edad': 23},
    {'Nombre': 'Carla', 'Edad': 22},
]

# Crea una tabla con columnas definidas y filas cargadas desde la variable 'datos'
ui.table(
    columns=['Nombre', 'Edad'],  # Nombres de las columnas que se mostrarán en la cabecera
    rows=datos,                  # Lista de diccionarios que representa las filas de la tabla
    row_key='Nombre'            # Clave única por fila (en este caso, el campo 'Nombre' se usará como identificador)
)

# Ejecuta la aplicación web en localhost:8080
ui.run()
