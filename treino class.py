class LojaRoupa ():
    def __init__(self,modelo,sexo,cor,tamanho):
        self.modelo = modelo
        self.sexo = sexo
        self.cor = cor
        self.tamanho = tamanho

    def estilo (self):
        print(f'O produto {self.modelo} do sexo {self.sexo} é da cor {self.cor} e do tamanho {self.tamanho} , e são todas peças belicimas.')    
    

    def venda (self):
        print(f'O produto {self.modelo} esta em promoção neste domingo.')

produto_01 = LojaRoupa('camiseta','Masculino','amarela','g')
produto_02 = LojaRoupa('short','Feminino','amarela','p')  
produto_03 = LojaRoupa('calsa','Feminino','amarela','m')  
produto_04 = LojaRoupa('camiseta','Masculino','amarela','p')  

produto_01.estilo()
produto_02.estilo()
produto_03.estilo()
produto_04.estilo()

produto_01.venda()
produto_02.venda()
produto_03.venda()
produto_04.venda()


