from nicegui import ui
def enviar():
 ui.notify(f'Usuario {nombre.value} registrado con éxito')
nombre = ui.input(label='Nombre')
email = ui.input(label='Email')
contraseña = ui.input(label='Contraseña', password=True)
ui.checkbox('Acepto los términos')
ui.button('Registrarse', on_click=enviar)
ui.run()