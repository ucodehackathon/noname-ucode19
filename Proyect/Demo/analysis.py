import boto3


if __name__ == "__main__":


    imageFile = 'C:/Users/carme/PycharmProjects/prueba1/data/input1.jpg'
    client = boto3.client('rekognition')
    counter = 0

    with open(imageFile, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])

    print('Detected labels in ' + imageFile)
    open = response['FaceDetails'][0]["EyesOpen"]["Value"]
    print(open)
    if open == True:
        pass
    else:
        counter = counter + 1

    print('Done')