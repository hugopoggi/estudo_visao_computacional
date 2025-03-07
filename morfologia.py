import cv2 as cv

img = cv.imread('piramide.jpg')
img = cv.resize(img, (500, 400))
imgCinza = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

## Morfologia gaussian BLUR para borrar img
## Mais utilizada para visao computacional melhorando funcionamento do algoritmo para algumas operações
imgBlur = cv.GaussianBlur(imgCinza, (7, 7),0)

## Morfologia CannyEdge para realçar contornos
## Util para extrar coisas ex: placa de carro
##threshold limite de confiança para ser considerar contorno - por variação de cor
imgCanny = cv.Canny(img, 50, 100)

## Dilatação - expandir objetos
## primeiro parametro imagem, qtd linhas e colunas que vao sofrer alteração, iteração> iteração > dilatacao
imgDilat = cv.dilate(imgCanny,(5,5), iterations=5)

##Erode - desfragmenta os objetos ou linhas da imagem
imgErode = cv.erode(imgCanny,(5,5), iterations=2)

## Openning retirar ruidos da imagem, deixando apenas objeto central
imgOpening = cv.morphologyEx(imgCanny, cv.MORPH_OPEN, (5,5))

## Close retirar os ruidos do objeto
imgClosing = cv.morphologyEx(imgCanny, cv.MORPH_CLOSE, (5,5))

# cv.imshow('Img original', img)
# cv.imshow('Img Cinza', imgCinza)
# cv.imshow('Img Blur', imgBlur)
cv.imshow('Img Canny', imgCanny)
# cv.imshow('Img Dilat', imgDilat)
# cv.imshow('Img Erode', imgErode)
cv.imshow('Img Opening', imgOpening)
cv.imshow('Img Closing', imgClosing)
cv.waitKey(0)