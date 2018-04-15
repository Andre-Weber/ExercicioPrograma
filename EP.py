# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:14:24 2018

@author: abrahao de weber
"""
import json
#Escolhas
print("0 - sair")
print("1 - adicionar item")
print("2 - remover item")
print("3 - alterar item")
print("4 - imprimir estoque")
menu = input("Faça sua escolha: ")

estoque = {}
with open("arquivo.txt", "r") as arquivo:
        estoque = json.loads(arquivo.read())


#Escolha 0 - sair
if menu == "0":
    print("Até mais")

while menu != "0":
    #Escolha 1 - adicionar item
    if menu == "1":
        while menu == "1":
            produto = input("Digite um produto: ")
            if produto in estoque:
                print("Produto já está cadastrado")
                menu = input("Faça sua escolha do menu: ")
            while produto not in estoque:
                quantidade1 = int(input("Digite a quantidade de produto: "))
                preco = float(input("Digite um preço por unidade para o produto: "))
                while quantidade1 < 0:
                    print("A quantidade não pode ser negativa")
                    quantidade1 = int(input("Digite a quantidade de produto: "))
                while preco < 0:
                    print("O preço não pode ser negativo")
                    preco = float(input("Digite um preço por unidade para o produto: "))
                if quantidade1 > 0 and preco > 0:
                    quant_prod = {}
                    quant_prod['quantidade'] = quantidade1
                    quant_prod['preco'] = preco
                    estoque[produto] = quant_prod
                    print("Produto {0} adicionado com uma quantidade de {1} e preço de {2} reais por {0}, totalizando {3} reais deste produto.".format(produto,quantidade1,preco,quantidade1*preco))
                    menu = input("Faça sua escolha do menu: ")
    
            
    #Escolha 2 - remover item
    if menu == "2":
        while menu == "2":
            produto = input("Digite um produto a ser removido: ")
            if produto in estoque:
                del[estoque[produto]]
                print("Produto {0} deletado.".format(produto))
                menu = input("Faça sua escolha do menu: ")
            else:
                print("Elemento não encontrado")
                menu = input("Faça sua escolha do menu: ")
                
    #Escolha 3 - alterar item
    if menu == "3":
        while menu == "3":
            produto = input("Digite um produto a ter seu valor alterado: ")
            valor = int(input("Digite a quantidade a ser somada: "))
            preco = float(input("Digite o preço a ser somado: "))
            if produto in estoque:
                if valor < 0 or preco < 0:
                    while estoque[produto]['quantidade'] + valor < 0:
                        print("Quantidade final não pode ser negativa")
                        valor = int(input("Digite a quantidade a ser somada: "))
                    if estoque[produto]['quantidade'] + valor >= 0:
                        estoque[produto]['quantidade'] += valor
                    while estoque[produto]['preco'] + preco < 0:
                        print("Preço final não pode ser negativo")
                        preco = float(input("Digite o preço a ser somado: "))
                    if estoque[produto]['preco'] + preco >= 0:
                        estoque[produto]['preco'] += preco
                        print("O produto {0} passa a ter {1} itens ao valor de {2} reais cada, totalizando {3} reais".format(produto,estoque[produto]['quantidade'],estoque[produto]['preco'],estoque[produto]['preco']*estoque[produto]['quantidade']))
                        menu = input("Faça sua escolha do menu: ")
                else:
                    estoque[produto]['quantidade'] += valor
                    estoque[produto]['preco'] += preco
                    print("O produto {0} passa a ter {1} itens ao valor de {2} reais cada, totalizando {3} reais".format(produto, estoque[produto]['quantidade'],estoque[produto]['preco'],estoque[produto]['quantidade']*estoque[produto]['preco']))
                    menu = input("Faça sua escolha do menu: ")
            else:
                print("Elemento não encontrado")
                menu = input("Faça sua escolha do menu: ")
    #Escolha 4 - imprimir estoque
    if menu == "4":
        soma_quant = 0
        soma_preco = 0
        for e in estoque:
            soma_quant += estoque[e]['quantidade']
            soma_preco += estoque[e]['preco']*estoque[e]['quantidade']
            print("{0}: {1}: {2}".format(e, estoque[e]['quantidade'],estoque[e]['preco']))
        print("A quantidade total do carrinho é de {0} itens e o preço total é de {1} reais".format(soma_quant,soma_preco))
        menu = input("Faça sua escolha do menu: ")
    #Escolha 0 - sair
    if menu == "0":
        print("Até mais")
        #Implementação do json
    texto = json.dumps(estoque, sort_keys = True, indent = 4)
    with open("arquivo.txt", "w") as arquivo:
        conteudo = arquivo.write(texto)

        
                
                
                
            
            
                
            
        
    

    
    


