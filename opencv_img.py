import cv2 as cv


img = cv.imread('farol.jpg')

# # Extraindo dimensão da img
# print(img.shape)

# Mostrando imagem e travando imagem na tela
# cv.imshow('img', img)
# cv.waitKey(0)

# # Alterando tamanho
# imgResize = cv.resize(img, (500, 500))
# cv.imshow('imgResize', imgResize)
# cv.waitKey(0)
#
# # Convertendo img em escala de cinza
# imgCinza = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
#
#
# cv.imshow('imgCinza', imgCinza)
# cv.waitKey(0)

## Recorte img utilizando o paint como guia
# primeiro o eixo y pxp
# eixo X pixel pxp
# recorte =  img[310:520, 120:420]
# cv.imshow('recorte', recorte)
# cv.waitKey(0)

## Recorte

# Seleciona onde voce quer, apos apertar 'enter' grava os pxs onde foram selecionados
dim = cv.selectROI('Selecione a area de recorte', img, False)

# Fechar janelas
cv.destroyAllWindows()
print(dim)

# extraindo valores armazenados
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

# posição do array para obter os pxs corretos
recorte = img[v2:v2+v4, v1:v1+v3]

# cv.imshow('recorte', recorte)
# cv.waitKey(0)

# salvando imagem

caminho = 'recortes/'
nome_arquivo = input('Digite o nome do arquivo: ')

cv.imwrite(f'{caminho}{nome_arquivo}.jpg', recorte)
print('Imagem salva com sucesso!')