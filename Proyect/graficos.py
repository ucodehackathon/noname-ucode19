# Importamos los módulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt
import sys

#Comprobamos los argumentos
if(len(sys.argv) > 3):
    print ("El nombre del programa es: " + sys.argv[0])
    print ("El fichero de Acciones se llama: " + sys.argv[1])
    print ("El fichero de Clicks se llama: " + sys.argv[2])
    print ("El fichero de pulsacines de teclado se llama: " + sys.argv[3])

    #inicializamos el eje de las x y la lista de datos
    x = ['0', '20', '40', '60', '80', '100', '120', '140', '160', '180']
    D = []
    print('La toma de datos se llevará a cabo en los siguientes intervalos:')
    print(x)
    #abrimos los ficheros y leemos los datos de las gráficas
    for i in range(len(sys.argv) -1):
        ficheroDatos = open('/home/jaime/Downloads/' + str(sys.argv[i+1]), 'r')
        cadena = ficheroDatos.read()
        cadena = cadena.split(' ')
        print(cadena)
        del cadena[-1]
        print(cadena)
        print (len(cadena))
        print (cadena)
        ficheroDatos.close()
        # Generamos los datos del gráfico correspondiente
        y = np.zeros(len(x))
        for j in range(len(x)):
            y[j] = cadena[j]
        D.append(y)

    # Creamos los gráficos
    plt.subplot(221)
    plt.plot(x,D[0],'--' 'o')
    plt.xlabel("Tiempo(s)")
    plt.ylabel("nº Acciones")
    plt.title("RepresentacionAcciones")
    plt.subplot(222)
    plt.plot(x,D[1],'o' 'r' '--')
    plt.xlabel("Tiempo(s)")
    plt.ylabel("nº Clicks")
    plt.title("RepresentacionClicks")
    plt.subplot(223)
    plt.plot(x,D[2],'o' '--' 'y')
    plt.xlabel("Tiempo(s)")
    plt.ylabel("nº PulsacionesTeclado")
    plt.title("RepresentacionPulsacionesTeclado")
    # Grafico de pestanyeo a mano, cambiar a parametros
    aux = ['0', '1', '4', '6', '1', '1', '3', '1', '3', '1']
    y = np.zeros(len(x))
    for j in range(len(x)):
            y[j] = aux[j]
    
    D.append(y)
    plt.subplot(224)
    print("error:")
    print(x)
    print(D)
    plt.plot(x,D[3],'g' '*' '--')
    plt.xlabel("Tiempo(s)")
    plt.ylabel("nº parpadeos")
    plt.title("RepresentacioParpadeos")

    plt.show()
else:
    print ("Necesario ejecutar con al menos 4 parametros: ")
    print ("python3 nombrePrograma nombreAcciones nombreClicks nombrePulsTeclado")

