from PIL import Image

# Carregar a imagem
image = Image.open("Lenna.png")

# Operação a) x[-nV, nH]
image_a = image.rotate(180)

# Operação b) x[nV, -nH]
image_b = image.transpose(Image.FLIP_LEFT_RIGHT)

# Operação c) x[-nV, -nH]
image_c = image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)

# Operação d) x[nV - n0, nH], n0 é um número inteiro
n0 = 50
image_d = image.transform(image.size, Image.AFFINE, (1, 0, -n0, 0, 1, 0))

# Operação e) x[nV, nH - n1], n1 é um número inteiro
n1 = 30
image_e = image.transform(image.size, Image.AFFINE, (1, 0, 0, 0, 1, -n1))

# Operação f) x[nV - n2, nH - n3], n2 e n3 são números inteiros
n2, n3 = 20, 40
image_f = image.transform(image.size, Image.AFFINE, (1, 0, -n2, 0, 1, -n3))

# Exibir as imagens resultantes
""" image_a.show()
image_b.show()
image_c.show()
image_d.show()
image_e.show()
image_f.show()
 """

# Salvando no disco
image_a.save("resultado/imagem_a.png")
image_b.save("resultado/imagem_b.png")
image_c.save("resultado/imagem_c.png")
image_d.save("resultado/imagem_d.png")
image_e.save("resultado/imagem_e.png")
image_f.save("resultado/imagem_f.png")