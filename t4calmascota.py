from nicegui import ui

# Función que calcula la edad perruna
def calcular():
    if humano.value is not None:
        edad_mascota = int(humano.value) * 7
        resultado.set_text(f'Edad estimada en años perrunos: {edad_mascota}')
    else:
        resultado.set_text("Por favor ingresa una edad válida.")

# Campo de entrada numérica
humano = ui.number(label='Edad humana')

# Botón para ejecutar el cálculo
ui.button('Calcular edad de mascota', on_click=calcular)

# Etiqueta para mostrar el resultado
resultado = ui.label()

# Ejecutar la app
ui.run()


