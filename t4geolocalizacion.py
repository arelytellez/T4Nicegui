from nicegui import ui

# Definir las coordenadas 
lat = 20.08406
lon = -98.77505

# Crear un enlace de Google Maps con la ubicación
map_url = f"https://www.google.com/maps?q={lat},{lon}&hl=es"

# Crear un botón que abre Google Maps en una nueva pestaña
ui.button(
    'Ver mapa en Google Maps',
    on_click=lambda: ui.run_javascript(f'window.open("{map_url}", "_blank")')
)

# Ejecutar la aplicación
ui.run()
