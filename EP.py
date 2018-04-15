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

#Escolha 0 - sair
if menu == "0":
    print("Até mais")

while menu != "0":
    #Escolha 1 - adicionar item
    if menu == "1":
        while menu == "1":
            produto = input("Digite um produto: ")
            quantidade1 = int(input("Digite a quantidade de produto: "))
            if produto in estoque:
                print("Produto já está cadastrado")
                menu = input("Faça sua escolha do menu: ")
            while produto not in estoque:
                if quantidade1 < 0:
                    print("A quantidade não pode ser negativa")
                    quantidade1 = int(input("Digite a quantidade de produto: "))
                else:
                    quant_prod = {}
                    quant_prod['quantidade'] = quantidade1
                    estoque[produto] = quant_prod
                    print("Produto {0} adicionado com uma quantidade de {1}.".format(produto,quantidade1))
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
            valor = int(input("Digite o valor a ser somado: "))
            if produto in estoque:
                if valor < 0:
                    if estoque[produto]['quantidade'] + valor > 0:
                        estoque[produto]['quantidade'] += valor
                        print("O produto {0} passa a ser {1}".format(produto, estoque[produto]['quantidade']))
                        menu = input("Faça sua escolha do menu: ")
                    else:
                        print("Quantidade final não pode ser negativa")
                        menu = input("Faça sua escolha do menu: ")
                else:
                    estoque[produto]['quantidade'] += valor
                    print("O produto {0} passa a ser {1}".format(produto, estoque[produto]['quantidade']))
                    menu = input("Faça sua escolha do menu: ")
            else:
                print("Elemento não encontrado")
                menu = input("Faça sua escolha do menu: ")
    #Escolha 4 - imprimir estoque
    if menu == "4":
        soma = 0
        for e in estoque:
            soma += estoque[e]['quantidade']
            print("{0}: {1}".format(e, estoque[e]['quantidade']))
        print("A quantidade total do carrinho é: {0}".format(soma))
        menu = input("Faça sua escolha do menu: ")
    #Escolha 0 - sair
    if menu == "0":
        print("Até mais")
    with open("arquivoEP.txt", "r") as arquivo:
        conteudo = arquivo.read
    texto = json.dumps(estoque, sort_keys = True, indent = 4)
    with open("arquivoEP.txt", "w") as arquivo:
        conteudo = arquivo.write(texto)

        
                
                
                
            
            
                
            
        
    

    
    


