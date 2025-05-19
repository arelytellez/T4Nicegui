from nicegui import ui
# Título
ui.label(' Calculadora de Suma Simple').classes('text-h4')
# Entradas de número
num1 = ui.number(label='Número 1', value=0)
num2 = ui.number(label='Número 2', value=0)
# Resultado
resultado = ui.label('Resultado: 0').classes('text-h6')
# Botón para calcular
with ui.row():
 def suma():
  suma = num1.value + num2.value
  resultado.text = f'Resultado: {suma}'
  ui.notify(f'La suma es {suma}')
 ui.button('suma', on_click=suma)
 def resta():
  resta = num1.value - num2.value
  resultado.text = f'Resultado: {resta}'
  ui.notify(f'La resta es {resta}')
 ui.button('Resta', on_click=resta)

 def multiplicacion():
  multiplicacion = num1.value * num2.value
  resultado.text = f'Resultado: {multiplicacion}'
  ui.notify(f'La resta es {multiplicacion}')
 ui.button('Multiplicacion', on_click=multiplicacion)

 def divicion():
  divicion = num1.value / num2.value
  resultado.text = f'Resultado: {divicion}'
  ui.notify(f'La resta es {divicion}')
 ui.button('Divicion', on_click=divicion)
# Ejecutar la app
ui.run()