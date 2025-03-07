from queue import PriorityQueue

import cv2 as cv

img = cv.imread('objetos.jpg')
img = cv.resize(img, (600, 500))

imgCinza = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
imgCanny = cv.Canny(imgCinza, 30, 200)
imgClose = cv.morphologyEx(imgCanny, cv.MORPH_CLOSE, (7, 7))

# Identificando contornos
# RETR_EXTERNAL contorno de fora
contours, hierarchy = cv.findContours(imgClose, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

numOb = 1
for cnt in contours:
    # # Desenhando contorno no objeto
    # cv.drawContours(img, cnt, -1, (255,0,0), 2)
    # Desenhando retangulo no objeto
    x, y, w, h=cv.boundingRect(cnt)

    # Recortando img
    objeto = img[y:y+h, x:x+w]
    cv.imwrite(f'objetos/objet{numOb}.jpg', objeto)
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    numOb += 1
cv.imshow('img', img)
cv.imshow('imgCinza', imgCinza)
cv.imshow('imgCanny', imgCanny)
cv.waitKey(0)