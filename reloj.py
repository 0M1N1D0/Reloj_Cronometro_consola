import time
from datetime import datetime


class  Reloj():

    # loop del cronometro (límite: 24 hrs)    
    def cronometro():
        for h in range(0, 24): 
            for m in range(0, 60):
                for s in range(0, 60):  

                    # ralentiza el tiempo en 1 seg
                    time.sleep(1)

                    # da el formato de 00:00:00 de las horas, minutos, segundo
                    if s < 10:
                        segundos = "0" + str(s)
                    else:
                        segundos = s
                    if m < 10:
                        minutos = "0" + str(m)
                    else:
                        minutos = m
                    if h < 10:
                        horas = "0" + str(h)
                    else:
                        horas = h

                    # imprimen los datos
                    print("{}:{}:{}".format(horas,minutos,segundos))
                   
            

    def hora_actual():
        hora = datetime.now().strftime("%d %m %Y  %H:%M:%S")
        print(hora)


Reloj.cronometro()