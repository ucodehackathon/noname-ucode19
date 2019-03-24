import datetime

contadorClicks = 0
contadorTeclado = 0
contadorAcciones = 0
contadorLineas = 0
inicio = False
lineaFinal = 0

#cantidad de acciones cada 20 segundos
cantidadAcciones = 0
cantidadClicks = 0
cantidadTeclado = 0

#Fichero En el que voy a guardas cuantas acciones hay cada 20 segs
# empieza en 0 
facciones = open ('datosLog20A.txt','w')
facciones.write(str(cantidadAcciones) + " ")

fclicks = open ('datosLog20C.txt','w')
fclicks.write(str(cantidadClicks) + " ")

fteclado = open ('datosLog20T.txt','w')
fteclado.write(str(cantidadTeclado) + " ")



with open("mouse_log.txt") as fich:
    array = fich.readlines()
for n in array:
    contadorLineas = contadorLineas + 1
    #obtenemos la fecha en la que empezamos a obtener datos
    if inicio == False:
        inicio = True
        x = n.split(",")
        fechaInicio =  datetime.datetime.strptime(x[0] + ".0", '%Y-%m-%d %H:%M:%S.%f')
        lineaAnterior = contadorLineas
        fechaAnterior =  datetime.datetime.strptime(x[0] + ".0", '%Y-%m-%d %H:%M:%S.%f')

    if "Mouse" in n:
        contadorClicks = contadorClicks + 1
        contadorAcciones = contadorAcciones + 1
        lineaFinal = contadorLineas
        lineaSiguiente = contadorLineas
        if lineaSiguiente > lineaAnterior:
            x = n.split(",")
            fechaSiguiente =  datetime.datetime.strptime(x[0] + ".0", '%Y-%m-%d %H:%M:%S.%f')
            aux = (fechaSiguiente - fechaAnterior)
            segundos = aux.total_seconds()
            if segundos >= 20:
                lineaAnterior = contadorLineas
                fechaAnterior = fechaSiguiente

                facciones.write(str(cantidadAcciones) + " ")
                cantidadAcciones = 0

                fclicks.write(str(cantidadClicks) + " ")
                cantidadClicks = 0

                fteclado.write(str(cantidadTeclado) + " ")
                cantidadTeclado = 0

            else:
                cantidadAcciones = cantidadAcciones + 1
                cantidadClicks = cantidadClicks + 1
                

        
    else:
        if "released" in n:
            contadorTeclado = contadorTeclado + 1
            contadorAcciones = contadorAcciones + 1
            lineaFinal = contadorLineas
            lineaSiguiente = contadorLineas
        if lineaSiguiente > lineaAnterior:
            x = n.split(",")
            fechaSiguiente =  datetime.datetime.strptime(x[0] + ".0", '%Y-%m-%d %H:%M:%S.%f')
            aux = (fechaSiguiente - fechaAnterior)
            segundos = aux.total_seconds()
            if segundos >= 20:
                lineaAnterior = contadorLineas
                fechaAnterior = fechaSiguiente

                facciones.write(str(cantidadAcciones) + " ")
                cantidadAcciones = 0

                fclicks.write(str(cantidadClicks) + " ")
                cantidadClicks = 0

                fteclado.write(str(cantidadTeclado) + " ")
                cantidadTeclado = 0

            else:
                cantidadAcciones = cantidadAcciones + 1
                cantidadTeclado = cantidadTeclado + 1

facciones.write(str(cantidadAcciones))
fclicks.write(str(cantidadClicks))
fteclado.write(str(cantidadTeclado))
facciones.close()
fclicks.close()
fteclado.close()
#obtenemos la fecha de la ultima linea
x = array[lineaFinal - 1].split(",")
fechaFinal =  datetime.datetime.strptime(x[0] + ".0", '%Y-%m-%d %H:%M:%S.%f')

print("Clicks realizados: " + str(contadorClicks))
print("Teclas pulsadas: " + str(contadorTeclado))
print("AccionesTotales: " + str(contadorAcciones))
print("fechaI = " + str(fechaInicio))
print("fechaF = " + str(fechaFinal))
print("tiempo total = " + str(fechaFinal - fechaInicio))
a = (fechaFinal - fechaInicio)
print("pulsaciones= " + str(contadorAcciones/a.total_seconds()) + " segs")

f = open ('datosLog.txt','w')
f.write("Clicks=" + str(contadorClicks))
f.write("\nTeclas=" + str(contadorTeclado))
f.write("\nAcciones=" + str(contadorAcciones))
f.write("\nfechaI=" + str(fechaInicio))
f.write("\nfechaF=" + str(fechaFinal))
f.write("\ntTotal=" + str(fechaFinal - fechaInicio))
f.write("\npulsacionesSeg=" + str(contadorAcciones/a.total_seconds()))
f.close()