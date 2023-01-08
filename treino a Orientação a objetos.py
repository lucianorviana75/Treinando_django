#FUNÇÂO


#Calcular razão do espaço pelo tempo.
#se um carro percorreu uma velocidade de 100 metros em 20 segundos.
#Sua velocidade média é ;
'''
def velocidade (espaço, tempo):
    v = espaço/tempo
    print(f'velocidade: {v} m/s')
velocidade(100,20)
'''
#R:velocidade: 5.0 m/s.

#Uma função sem parametro:
'''
def diz_oi():
    print("oi")
diz_oi()    
'''
# Para um parâmetro ser opcional,o mesmo é atribuído a um valor padrão (default).
# o mais comum é utilizar None. Por exemplo:
'''
def dados(nome, idade=None):
    print(f'nome: {nome}')
    if(idade is not None):
        print(f'idade: {idade}')
    else:
        print(f'idade não informada ')
dados('luciano')
'''
'''
def velocidade(espaço, tempo):
    v = espaço/tempo
    return v
print(velocidade(100, 20))

resultado = velocidade(100,20)
print(resultado)

aceleração = velocidade(100, 20)/20
print(aceleração)
'''
#Usando dois comandos RETURN ;
'''
def dados(nome, idade=None):
    if(idade is not None):#se a idade não for nenhuma
        return(f'nome: {nome} \n idade:{idade}')
    else:
        return(f'nome: {nome} \n idade: não informada')
print(dados('luciano',20))
print(dados('luciano'))
print(dados(20))

'''
#Para retornar múltiplos valores, retornamos os resultados separados por vírgula:
#type diz qual sera o tipo.
'''
def calculadora(x, y):
    return x+y, x-y
print(calculadora(1,2))

print(type(calculadora(1, 2)))
'''
# Neste caso específico,
#poderíamos retornar um dicionário e usar um laço for para imprimir os resultados:

def calculadora(x, y):
    return {'soma':x+y, 'subtração':x-y}


resultados = calculadora(1, 2)
for key in resultados:
    print('{}: {} ' .format(key, resultados[key]))























