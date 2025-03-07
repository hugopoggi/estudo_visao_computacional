import cv2 as cv

video = cv.VideoCapture('runners.mp4')

# Criando looping infinito, para execução do video
while True:
    check, img = video.read()

    # Redimensionando img
    imgResize = cv.resize(img, (640, 420))

    cv.imshow('video', imgResize)

    # 1 ms por looping(o video ficara acelerado), recomendado por 10 para ficar original
    cv.waitKey(30)
