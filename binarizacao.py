import cv2 as cv

img = cv.imread('binarizacao/img02.jpg')

img = cv.resize(img, (500, 600))
imgCinza = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

## Valor 127 ou seja threshold quando um pixel irá assumir cor preta ou brand 127> preta e branca<127
## Util em algoritmos que podem ler melhor imagem binaria
_, th1 = cv.threshold(imgCinza, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(imgCinza, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 16)


th3 = cv.adaptiveThreshold(imgCinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 16)


# cv.imshow('Original', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.waitKey(0)
