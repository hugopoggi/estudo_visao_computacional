import cv2 as cv

# Índice da câmera
camera = cv.VideoCapture(0)

# Setando configurações da camera
"""
cada configuração possui um índice:
índice 3 = largura em px da img
índice 4 = altura em px da img
índice 10 = brilho da img
"""
camera.set(3, 640) #largura
camera.set(4, 420) #altura
camera.set(10, 180) #brilho

while True:
    check, img = camera.read()

    cv.imshow('webcam', img)

    # Função waitKey para esperar uma chave, 0xFF ler o teclado caso clique na tecla 'q' encerre a aplicação
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
