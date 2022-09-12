import sys
try:
    from PIL import Image
except ImportError:
    import Image

try:
    largura_desejada = int(sys.argv[2])
    imagem = Image.open(str(sys.argv[1]))

    largura_imagem = imagem.size[0]
    altura_imagem = imagem.size[1]
    percentual_largura = float(largura_desejada) / float(largura_imagem)
    altura_desejada = int((altura_imagem * percentual_largura))

    imagem = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
    imagem.save('imagem-{}x{}.png'.format(imagem.size[0], imagem.size[1]))

except IndexError:
    print('Insira o nome da imagem e 1 inteiro com a largura desejada.')
    print('Exemplo: C:\>python proporcional_img.py imagem.png 300')