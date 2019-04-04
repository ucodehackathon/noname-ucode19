import boto3
import os
import cv2
import time



def grabar():#splitvideo2
    video = cv2.VideoCapture(0)
    nframes = 0
    hora_inicio = time.time()
    print(hora_inicio)
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    while True:
        nframes += 1
        check, frame = video.read()
        print(check)
        print(frame)
        cv2.imshow("Capturing", frame)
        name = './data/input' + str(nframes) + '.jpg'
        cv2.imwrite(name, frame)
        time.sleep(0.20)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    tiempo = time.time()-hora_inicio
    print("El tiempo de captura ha sido de "+str(tiempo))
    cv2.destroyAllWindows()
    print("Durante este tiempo se han capturado "+str(nframes)+" frames.")
    video.release()
    return nframes, tiempo

def analisis(num,tiem):
    client = boto3.client('rekognition')
    counter = 0
    for i in range(num):

        imageFile = 'C:/Users/carme/PycharmProjects/prueba1/data/input' + str(i + 1) + '.jpg'

        image = open(imageFile, 'rb')
        response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])

        open_aux = response['FaceDetails'][0]["EyesOpen"]["Value"]
        if open == True:
            pass
        else:
            counter = counter + 1

        image.close()
        print("Imagen "+str(i)+" Procesada")
    print("\nAnálisis Terminado.")
    frec=float(counter)/tiem
    norm_frec=15
    print("Has parpadeado durante la prueba con una frecuencia de "+str(frec)+" por minuto")
    if frec >= norm_frec:
        print("Una media aceptable de parpadeos/minuto es de 15, por lo tanto te encuentras dentro de un rango correcto.")

    else:
        print("Una media aceptable de parpadeos/minuto es de 15, lo cual significa que estás perjudicando a tu vista.")
        print("Trata de parpadear con una mayor frecuencia para evitar problemas futuros como fatiga visual y la vista cansada o presbicia .")




#HASTA AQUÍ FUNCIONES----------------------------------

if __name__ == "__main__":

    print("Bienvenido al asistente Beta de Esport.")
    time.sleep(2)
    print("A continuación, comenzaremos con la monitorización de sus datos de juego para así poder optimizar su rendimiento.")
    time.sleep(2)
    print("La monitorización consistirá en un seguimiento del parpadeo, para así tratar de evitar progresivamente la fatiga visual.")
    time.sleep(4)
    numero,tiempo = grabar()
    analisis(numero, tiempo/60)



