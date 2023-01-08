'''
def dados(nome, idade=None):
    print(f'nome: {nome}')
    if(idade is not None):
        print(f'idade: {idade}')
    else:
        print('idade: não informa')
dados('joão', 20)        
dados('pedro')
dados(45)
'''
'''
def dados(idade, nome=None):
    print(f'idade:{idade}')
    if(idade is not None):
        print(f'nome{nome}')
    else:
        print('nome nao informa')
dados( '65', 'lucas')
dados(65)
'''
'''
def velocidade(espaço, tempo):
    v = espaço/tempo
    return v
print(velocidade(100,20))
'''
'''
resultado = velocidade(100,20)/20
print(resultado)
'''
def dados(nome, idade=None):
    if(idade is not None ):
        return(f'nome:{nome} \nidade: {idade}.')
    else:
        return(f'nome:{nome} \nidade: não informada .')
dados(print('lucas', 34))    


