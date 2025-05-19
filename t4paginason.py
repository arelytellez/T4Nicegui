from nicegui import ui

# URL de un archivo de audio público
AUDIO_URL = 'https://www.soundhelix.com/examples/mp3/SoundHelixSong-1.mp3'

# Etiqueta del reproductor
ui.label('🎵 Reproductor de audio')

# Componente de audio con controles
audio = ui.audio(AUDIO_URL, autoplay=False, controls=True)

# Fila de botones para controlar la reproducción manualmente
with ui.row():
    ui.button('▶ Reproducir', on_click=lambda: audio.run_method('play'))
    ui.button('⏸ Pausar', on_click=lambda: audio.run_method('pause'))

# Ejecuta la aplicación en localhost:8080
ui.run()
