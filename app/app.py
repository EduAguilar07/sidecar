from EventLoggerSidecar import EventLoggerSidecar
from flask import Flask


# Clase Main con método process_message para procesar mensajes y utilizar el Sidecar
class Main:

    # Método para procesar mensajes y registrar eventos usando EventLoggerSidecar
    def process_message(self, message, sidecar):
        print("Message received:", message)
        sidecar.log_event("Processing message: " + message)

# Crear instancias de las clases
event_logger = EventLoggerSidecar()
main_app = Main()

# Configurar la aplicación Flask
app = Flask(__name__)

# Ruta para procesar mensajes y registrar eventos
@app.route('/process_message/<message>')
def procesar(message):
    main_app.process_message(message, event_logger)
    return "Message processed and event logged" + message

# Ejecutar la aplicación Flask
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)