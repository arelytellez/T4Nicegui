from nicegui import ui  # Importa el módulo de interfaz gráfica NiceGUI

# Función que se ejecuta al presionar el botón
def mostrar():
    # Muestra una notificación con los valores seleccionados por el usuario
    ui.notify(f'Color: {color.value}, Tema oscuro: {tema.value}')

# Crea un menú desplegable para seleccionar el color favorito
color = ui.select(['Rojo', 'Verde', 'Azul'], label='Color favorito')

# Crea un interruptor (switch) para activar o desactivar el tema oscuro
tema = ui.switch('Tema oscuro')

# Botón que ejecuta la función `mostrar` al hacer clic
ui.button('Guardar preferencias', on_click=mostrar)

# Inicia la aplicación web en localhost:8080 por defecto
ui.run()
