### Justificacion

Cambios *clases_base_abstractas.py* 
En su lugar, el Observer mismo le pide la información al Subject (generalmente a través de un método como get_temperature(), get_humidity(), etc.). Cambiamos la firma para que no acepte parametros

Cambios *subject.py*
Queremos **avisar** a cada observador que hubo un cambio

Cambios *display.py*
los Observer  tienen que ajustar update() para no recibir parámetros y en su lugar consultar al WeatherData
