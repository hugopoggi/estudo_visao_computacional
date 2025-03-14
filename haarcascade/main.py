import cv2 as cv

camera = cv.VideoCapture(0)
classificador = cv.CascadeClassifier('cascades/haarcascade_eye.xml')

while True:
    check, img = camera.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(imgGray, minSize=(50, 50),scaleFactor=1.5)

    for x,y,l,a in objetos:
        cv.rectangle(img,(x,y),(x+l,y+a),(0,255,0),2)

    cv.imshow('Imagem', img)
    cv.imshow('Imagem', imgGray)
    cv.waitKey(1)