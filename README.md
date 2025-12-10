# Carro zumo autónomo por medio de sensor ultrasónico
Este proyecto consiste en la construcción y programación de un carro tipo Zumo controlado mediante una tarjeta ESP32, utilizando un puente H L298N para manejar los motores y un sensor ultrasónico HC-SR04 para detectar obstáculos. El objetivo es que el vehículo avance de manera autónoma y se detenga o cambie de dirección al acercarse a un objeto.

# Materiales:
1 x ESP32
1 x Puente H L298N
1 x Sensor Ultrasónico HC-SR04
2 x Motores reductores de doble eje tipo I, 3 Vcc, 1:120
2 x Llantas de plástico 
2 x Baterias de 5v (un PowerBank)
1 x Protoboard
Jumpers (macho-macho y macho-hembra)

# Descripción:
ESP32
Microcontrolador que procesa el programa, recibe la distancia y controla el movimiento del carro.
L298N
Módulo puente H que permite invertir el giro de los motores (adelante/atrás) y alimentarlos con una fuente externa.
HC-SR04
Sensor ultrasónico que mide distancias enviando pulsos de sonido. Permite detectar obstáculos.
Chasis y Motores
Base donde se montan los componentes, incluye los motores que permiten la movilidad.

# Conexiones:
