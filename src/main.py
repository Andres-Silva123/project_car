from machine import Pin, time_pulse_us
import time

# Pines del sensor ultrasónico
TRIG = Pin(5, Pin.OUT)
ECHO = Pin(18, Pin.IN)

# Pines del L298N 
M1_IN1 = Pin(14, Pin.OUT)
M1_IN2 = Pin(27, Pin.OUT)
M2_IN3 = Pin(26, Pin.OUT)
M2_IN4 = Pin(25, Pin.OUT)

# Función para medir distancia
def medir_distancia():
    TRIG.value(0)
    time.sleep_us(5)
    
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    duracion = time_pulse_us(ECHO, 1, 30000)

    if duracion < 0:
        return None

    distancia = (duracion / 2) / 29.1
    return distancia

# Funciones de movimiento
def avanzar():
    M1_IN1.value(1); M1_IN2.value(0)
    M2_IN3.value(1); M2_IN4.value(0)

def detener():
    M1_IN1.value(0); M1_IN2.value(0)
    M2_IN3.value(0); M2_IN4.value(0)

def girar():
    M1_IN1.value(0); M1_IN2.value(1)
    M2_IN3.value(1); M2_IN4.value(0)

# Programa principal
while True:
    d = medir_distancia()

    if d is None:
        print("Fuera de rango")
        detener()
    else:
        print("Distancia:", round(d, 2), "cm")
        
        if d > 20:
            avanzar()
        else:
            detener()
            time.sleep(0.5)
            girar()
            time.sleep(0.8)

    time.sleep(0.2)