from nicegui import ui # Importa la interfaz gráfica NiceGUI

with ui.row(): # Crea una fila horizontal que contiene varias tarjetas
  # Tarjeta para mostrar ventas
 with ui.card():
  ui.label('Ventas')
  ui.label(' $1,200')
  # Tarjeta para mostrar usuarios
 with ui.card():
  ui.label('Usuarios')
  ui.label(' 342')
   # Tarjeta para mostrar tickets
 with ui.card():
  ui.label('Tickets')
  ui.label(' 18')
ui.run() # Ejecuta la aplicación web en localhost





