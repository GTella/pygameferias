def colisao_ponto_retangulo(x_ponto, y_ponto, x_retangulo, y_retangulo, largura_retangulo, altura_retangulo):
    if x_retangulo <= x_ponto <= x_retangulo + largura_retangulo and y_retangulo <= y_ponto <= y_retangulo + altura_retangulo:
        return True
    else:
        return False

def verificar_correspondencia(quadrados, x_clicado, y_clicado):
    for i, quadrado in enumerate(quadrados):
        x = quadrado['x']
        y = quadrado['y']
        lado = quadrado['lado']

        if colisao_ponto_retangulo(x_clicado, y_clicado, x, y, lado, lado):
            if 'ultimo_clicado' not in globals():
                global ultimo_clicado
                ultimo_clicado = i
            else:
                if quadrados[ultimo_clicado]['cor'] == quadrado['cor']:
                    del quadrados[i]
                    del quadrados[ultimo_clicado]
                else:
                    quadrados[ultimo_clicado]['revelado'] = False
                    quadrados[i]['revelado'] = False

                del globals()['ultimo_clicado']