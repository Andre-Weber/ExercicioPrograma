# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:14:24 2018

@author: abrahao de weber
"""
import json

#Escolhas lojas
print("0 - sair")
print("1 - adicionar loja")
print("2 - remover loja")
print("3 - imprimir loja")
cardapio = input("Faça sua escolha: ")

lojas = {}

with open("arquivo.txt", "r") as arquivo:
    lojas = json.loads(arquivo.read())
    


if cardapio == "0":
    print("Até mais")

try:
    while cardapio != "0":
        
        # Adicionando lojas - opção 1
        if cardapio == "1":
            while cardapio == "1":
                nomeloja = input("Nome da loja a adicionar:")
                if nomeloja in lojas:
                    print("loja já cadastrada")
                    cardapio = input("Faça sua escolha: ")
                
                else:
                    # Escolhas de Estoque
                    print("0 - sair")
                    print("1 - adicionar item")
                    print("2 - remover item")
                    print("3 - alterar item")
                    print("4 - imprimir estoque")
        
                    menu = input("Faça sua escolha: ")
         
                    estoque = {}     
                    #Escolha 0 - sair
                    
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
                                    while preco < 0:
                                        print("O preço não pode ser negativo")
                                        preco = float(input("Digite um preço por unidade para o produto: "))
                                    if preco > 0:
                                        quant_prod = {}
                                        quant_prod['quantidade'] = quantidade1
                                        quant_prod['preco'] = preco
                                        quant_prod['total'] = quantidade1*preco
                                        estoque[produto] = quant_prod
                                        print("Produto {0} adicionado com uma quantidade de {1} e preço de {2} reais por {0}, totalizando {3} reais deste produto.".format(produto,quantidade1,preco,quantidade1*preco)) 
                                        print("0 - sair")
                                        print("1 - adicionar item")
                                        print("2 - remover item")
                                        print("3 - alterar item")
                                        print("4 - imprimir estoque")
                                        menu = input("Faça sua escolha do menu: ")
                        lojas[nomeloja] = estoque
                        
                                
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
                                    print("0 - sair")
                                    print("1 - adicionar item")
                                    print("2 - remover item")
                                    print("3 - alterar item")
                                    print("4 - imprimir estoque")
                                    menu = input("Faça sua escolha do menu: ")
                                    
                        #Escolha 3 - alterar item
                        if menu == "3":
                            while menu == "3":
                                produto = input("Digite um produto a ter seu valor alterado: ")
                                valor = int(input("Digite a quantidade a ser somada: "))
                                preco = float(input("Digite o preço a ser somado: "))
                                if produto in estoque:
                                    if preco < 0:
                                        while estoque[produto]['preco'] + preco < 0:
                                            print("Preço final não pode ser negativo")
                                            preco = float(input("Digite o preço a ser somado: "))
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
                            print("0 - imprimir todo estoque")
                            print("1 - imprimir apenas estoque positivo")
                            print("2 - imprimir apenas estoque negativo")
                            submain = input("Digite sua escolha para imprimir o estoque: ")
                            for e in estoque: 
                                if submain == "0":
                                    soma_quant += estoque[e]['quantidade'] 
                                    soma_preco += estoque[e]['preco']*estoque[e]['quantidade'] 
                                    print("{0}: {1}: {2}".format(e, estoque[e]['quantidade'],estoque[e]['preco'])) 
                                if submain == "1":
                                    if estoque[e]['quantidade'] >= 0: 
                                        soma_quant += estoque[e]['quantidade'] 
                                        soma_preco += estoque[e]['preco'] * estoque[e]['quantidade'] 
                                        print("{0}: {1}: {2}".format(e, estoque[e]['quantidade'],estoque[e]['preco'])) 
                                if submain == "2":
                                    if estoque[e]['quantidade'] < 0: 
                                        soma_quant += estoque[e]['quantidade'] 
                                        soma_preco += estoque[e]['preco'] * estoque[e]['quantidade'] 
                                        print("{0}: {1}: {2}".format(e, estoque[e]['quantidade'],estoque[e]['preco']))
                            print("A quantidade total do carrinho é de {0} itens e o preço total é de {1} reais".format(soma_quant,soma_preco))
                            print("0 - sair")
                            print("1 - adicionar item")
                            print("2 - remover item")
                            print("3 - alterar item")
                            print("4 - imprimir estoque")            
                            menu = input("Faça sua escolha do menu: ")
                            
                      
                            
                        #Escolha 0 - sair
                        if menu == "0":
                            print("0 - sair")
                            print("1 - adicionar loja")
                            print("2 - remover loja")
                            print("3 - imprimir loja")
                            cardapio = input("Faça sua escolha: ")
                            #Implementação do json
                        texto = json.dumps(lojas, sort_keys = True, indent = 4)
                        with open("arquivo.txt", "w") as arquivo:
                            conteudo = arquivo.write(texto)
    
    
            
        # Remover Lojas - Opção 2       
        if cardapio == "2":
            while cardapio == "2":
                nomeloja = input("Digite o nome da loja a ser removida: ")
                if nomeloja in lojas:
                    del[lojas[nomeloja]]
                    print("Loja {0} deletado".format(nomeloja))
                    cardapio = input("Faça uma escolha: ")
                else:
                    print("Loja não encontrada")
                    cardapio = input("Faça uma escolha: ")
    
        # Imprimir Lojas - Opção3
        if cardapio == "3":
            print(lojas)
            cardapio = input("Faça escolha:")
            
        # Sair - Opção - 0
        if cardapio == "0":
            print("Até mais")
except:
    print("Algo errado!!")
    #Implementação do json
texto = json.dumps(lojas, sort_keys = True, indent = 4)
with open("arquivo.txt", "w") as arquivo:
    conteudo = arquivo.write(texto)

        
                
                
                
            
            
                
            
        
    
