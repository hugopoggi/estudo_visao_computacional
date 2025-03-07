import cv2 as cv

# img = cv.imread('piramide.jpg')
#
# ## Inserindo objetos na imagem
# ## params = img, y x, y x, cor em rgb(ordem b, g, r), espessura
# cv.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 2)
#
# cv.circle(img, center=(300, 300), radius=50, color=(0, 89, 75), thickness=5)
#
# cv.line(img,(400, 400),(500,400), (0, 0, 255), 2)
#
# ## Inserindo texto
# texto = 'Piramides de Jose'
# cv.putText(img, texto,(200,200), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2)
#
# cv.imshow('img', img)
# cv.waitKey(0)

## Exemplo com video

video = cv.VideoCapture('runners.mp4')

while True:
    check, frame = video.read()
    cv.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 2)

    cv.circle(frame, center=(300, 300), radius=50, color=(0, 89, 75), thickness=5)

    cv.line(frame,(400, 400),(500,400), (0, 0, 255), 2)

    ## Inserindo texto
    texto = 'Piramides de Jose'
    cv.putText(frame, texto,(200,200), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2)

    cv.imshow('img', frame)
    cv.waitKey(10)