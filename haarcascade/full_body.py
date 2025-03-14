import cv2 as cv

camera = cv.VideoCapture('ANEXO video.mp4')
classificador = cv.CascadeClassifier(r'C:\Users\hugo.luciano\PycharmProjects\Estudo_ia_visao_computacional\haarcascade\cascades\haarcascade_fullbody.xml')

while True:
    check, img = camera.read()
    if not check:
        break
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    objetos = classificador.detectMultiScale(imgGray, minSize=(50, 50),scaleFactor=1.5)

    for x,y,l,a in objetos:
        cv.rectangle(img, (x,y), (x+l, y+a), (255,0,0), 2)

        cv.imshow('img', img)
        cv.waitKey(1)