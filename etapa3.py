def colisao_ponto_retangulo(x_ponto, y_ponto, x_retangulo, y_retangulo, largura_retangulo, altura_retangulo):
    if x_retangulo <= x_ponto <= x_retangulo + largura_retangulo and y_retangulo <= y_ponto <= y_retangulo + altura_retangulo:
        return True
    else:
        return False
