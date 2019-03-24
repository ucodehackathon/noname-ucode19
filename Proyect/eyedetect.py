import boto3
import json

if __name__ == "__main__":
    photo = 'input.jpg'#Imagen a introducir
    bucket = 'bucket'#Cambiar por el bucket
    client = boto3.client('rekognition')

    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])


    counter = 0
    print('Detected faces for ' + photo)
    eyesOpen = response["FaceDetails"][0]["EyesOpen"]["Value"]
    print(eyesOpen)
    if eyesOpen == False:
        counter += 1
