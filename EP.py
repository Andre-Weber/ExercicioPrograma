# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:14:24 2018
@author: abrahao de weber
"""
from firebase import firebase
firebase = firebase.FirebaseApplication("https://ep-dsoft-6cc2f.firebaseio.com/",None)
if firebase.get("Estoque", None) is None:
    lojas = {}
else:
    lojas = firebase.get("Estoque", None)

#Escolhas lojas
print("0 - sair")
print("1 - adicionar loja")
print("2 - remover loja")
print("3 - imprimir loja")
print("4 - editar loja")
cardapio = input("Faça sua escolha: ")    

if cardapio == "0":
    print("Até mais")

 

while cardapio != "0":
    
    # Adicionando lojas - opção 1
    if cardapio == "1":
        while cardapio == "1":
            nomeloja = input("Nome da loja a adicionar: ")
            if nomeloja in lojas:
                print("loja já cadastrada")
                print("0 - sair")
                print("1 - adicionar loja")
                print("2 - remover loja")
                print("3 - imprimir loja")
                print("4 - editar loja")
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
                lojas[nomeloja] = {}
                #Escolha 0 - sair
                if menu == "0":
                    lojas[nomeloja] = {}
                    print("Até mais")
                    print("0 - sair")
                    print("1 - adicionar loja")
                    print("2 - remover loja")
                    print("3 - imprimir loja")
                    print("4 - editar loja")
                    cardapio = input("Faça sua escolha: ")   
                
                while menu != "0":
                    #Escolha 1 - adicionar item
                    if menu == "1":
                        while menu == "1":
                            produto = input("Digite um produto: ")
                            if produto in lojas[nomeloja]:
                                print("Produto já está cadastrado")
                                print("0 - sair")
                                print("1 - adicionar item")
                                print("2 - remover item")
                                print("3 - alterar item")
                                print("4 - imprimir estoque")
                                menu = input("Faça sua escolha do menu: ")
                            while produto not in lojas[nomeloja]:
                                lojas[nomeloja][produto] = {}
                                quantidade1 = int(input("Digite a quantidade de produto: "))
                                preco = float(input("Digite um preço por unidade para o produto: "))
                                while preco < 0:
                                    print("O preço não pode ser negativo")
                                    preco = float(input("Digite um preço por unidade para o produto: "))
                                if preco > 0:
                                    lojas[nomeloja][produto]['quantidade'] = quantidade1
                                    lojas[nomeloja][produto]['preco'] = preco
                                    lojas[nomeloja][produto]['total'] = quantidade1*preco
                                    print("Produto {0} adicionado com uma quantidade de {1} e preço de {2} reais por {0}, totalizando {3} reais deste produto.".format(produto,quantidade1,preco,quantidade1*preco)) 
                                    print("0 - sair")
                                    print("1 - adicionar item")
                                    print("4 - imprimir estoque")
                                    menu = input("Faça sua escolha do menu: ")
                                    
                    
                    
                    #Escolha 2 - remover item
                    if menu == "2":
                        while menu == "2":
                            produto = input("Digite um produto a ser removido: ")
                            if produto in estoque:
                                del[lojas[nomeloja]]
                                print("Produto {0} deletado.".format(produto))
                                print("0 - sair")
                                print("1 - adicionar item")
                                print("2 - remover item")
                                print("3 - alterar item")
                                print("4 - imprimir estoque")
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
                                    estoque[produto]['total'] = estoque[produto]['preco']*estoque[produto]['quantidade']
                                    print("O produto {0} passa a ter {1} itens ao valor de {2} reais cada, totalizando {3} reais".format(produto, estoque[produto]['quantidade'],estoque[produto]['preco'],estoque[produto]['quantidade']*estoque[produto]['preco']))
                                    print("0 - sair")
                                    print("1 - adicionar item")
                                    print("2 - remover item")
                                    print("3 - alterar item")
                                    print("4 - imprimir estoque")
                                    menu = input("Faça sua escolha do menu: ")
                            else:
                                print("Elemento não encontrado")
                                print("0 - sair")
                                print("1 - adicionar item")
                                print("2 - remover item")
                                print("3 - alterar item")
                                print("4 - imprimir estoque")
                                menu = input("Faça sua escolha do menu: ")
                        
                    #Escolha 4 - imprimir estoque
                    if menu == "4":
                        soma_quant = 0
                        soma_preco = 0
                        print("0 - imprimir todo estoque")
                        print("1 - imprimir apenas estoque positivo")
                        print("2 - imprimir apenas estoque negativo")
                        submain = input("Digite sua escolha para imprimir o estoque: ")
                        for e in lojas[nomeloja]: 
                            if submain == "0":
                                soma_quant += lojas[nomeloja][e]['quantidade'] 
                                soma_preco += lojas[nomeloja][e]['preco']*lojas[nomeloja][e]['quantidade'] 
                                print("{0}: {1}: {2}".format(e, lojas[nomeloja][e]['quantidade'],lojas[nomeloja][e]['preco'])) 
                            if submain == "1":
                                if lojas[nomeloja][e]['quantidade'] >= 0: 
                                    soma_quant += lojas[nomeloja][e]['quantidade'] 
                                    soma_preco += lojas[nomeloja][e]['preco'] * lojas[nomeloja][e]['quantidade'] 
                                    print("{0}: {1}: {2}".format(e, lojas[nomeloja][e]['quantidade'],lojas[nomeloja][e]['preco'])) 
                            if submain == "2":
                                if lojas[nomeloja][e]['quantidade'] < 0: 
                                    soma_quant += lojas[nomeloja][e]['quantidade'] 
                                    soma_preco += lojas[nomeloja][e]['preco'] * lojas[nomeloja][e]['quantidade'] 
                                    print("{0}: {1}: {2}".format(e, lojas[nomeloja][e]['quantidade'],lojas[nomeloja][e]['preco']))
                        print("A quantidade total do carrinho é de {0} itens e o preço total é de {1} reais".format(soma_quant,soma_preco))
                        print("0 - sair")
                        print("1 - adicionar item")
                        print("4 - imprimir estoque")            
                        menu = input("Faça sua escolha do menu: ")
                        
                    #Escolha 0 - sair
                    if menu == "0":
                        print("0 - sair")
                        print("1 - adicionar loja")
                        print("2 - remover loja")
                        print("3 - imprimir loja")
                        print("4 - editar loja")
                        cardapio = input("Faça sua escolha: ")
                        
    # Remover Lojas - Opção 2       
    if cardapio == "2":
        while cardapio == "2":
            nomeloja = input("Digite o nome da loja a ser removida: ")
            if nomeloja in lojas:
                del lojas[nomeloja]
                firebase.delete("Estoque", nomeloja)
                print(nomeloja)
                print("Loja {0} deletado".format(nomeloja))
                cardapio = input("Faça uma escolha: ")
            else:
                print("Loja não encontrada")
                print("0 - sair")
                print("1 - adicionar loja")
                print("2 - remover loja")
                print("3 - imprimir loja")
                print("4 - editar loja")
                cardapio = input("Faça uma escolha: ")

    # Imprimir Lojas - Opção 3
    if cardapio == "3":
        nomeloja = input("Nome da loja: ")
        if nomeloja in lojas:
            print(lojas[nomeloja])
        else:
            print("Loja inexistente")
        print("0 - sair")
        print("1 - adicionar loja")
        print("2 - remover loja")
        print("3 - imprimir loja")
        print("4 - editar loja")
        cardapio = input("Faça escolha: ")
    
    # Editar Loja - Opção 4   
    if cardapio == "4":
        while cardapio == "4":
                
            nomeloja = input("Digite o nome da loja a ser alterada: ")
            if nomeloja in lojas:
                print("0 - sair")
                print("1 - adicionar item")
                print("2 - remover item")
                print("3 - alterar item")
                print("4 - imprimir estoque")
                menu = input("Faça sua escolha do menu: ")
                while menu != "0":
                     
                    #Escolha 1 - adicionar item
                    if menu == "1":
                        while menu == "1":
                            estoque = {}
                            produto = input("Digite um produto: ")
                            if produto in lojas[nomeloja]:
                                print("Produto já está cadastrado")
                                print("0 - sair")
                                print("1 - adicionar item")
                                print("2 - remover item")
                                print("3 - alterar item")
                                print("4 - imprimir estoque")
                                menu = input("Faça sua escolha do menu: ")
                                if menu == "0":
                                    print("0 - sair")
                                    print("1 - adicionar loja")
                                    print("2 - remover loja")
                                    print("3 - imprimir loja")
                                    print("4 - editar loja")
                                    cardapio = input("Faça escolha do cardapio: ")
                            while produto not in lojas[nomeloja]:
                                quantidade1 = int(input("Digite a quantidade de produto: "))
                                preco = float(input("Digite um preço por unidade para o produto: "))
                                while preco < 0:
                                    print("O preço não pode ser negativo")
                                    preco = float(input("Digite um preço por unidade para o produto: "))
                                if preco > 0:
                                    lojas[nomeloja][produto] = {}
                                    lojas[nomeloja][produto]['preco'] = preco
                                    lojas[nomeloja][produto]['quantidade'] = quantidade1
                                    lojas[nomeloja][produto]['total'] = preco*quantidade1
                                    print("Produto {0} adicionado com uma quantidade de {1} e preço de {2} reais por {0}, totalizando {3} reais deste produto.".format(produto,quantidade1,preco,quantidade1*preco)) 
                                    print("0 - sair")
                                    print("1 - adicionar item")
                                    print("2 - remover item")
                                    print("3 - alterar item")
                                    print("4 - imprimir estoque")
                                    menu = input("Faça sua escolha do menu: ")
                                    print("0 - sair")
                                    print("1 - adicionar loja")
                                    print("2 - remover loja")
                                    print("3 - imprimir loja")
                                    print("4 - editar loja")
                                    cardapio = input("Faça escolha do cardapio: ")
                                    
                            
                    #Escolha 2 - remover item
                    if menu == "2":
                        while menu == "2":
                            produto = input("Digite um produto a ser removido: ")
                            if produto in lojas[nomeloja]:
                                del lojas[nomeloja][produto]
                                firebase.delete("Estoque/{0}".format(nomeloja),produto)
                                print("Produto {0} deletado.".format(produto))
                                print("0 - sair")
                                print("1 - adicionar item")
                                print("2 - remover item")
                                print("3 - alterar item")
                                print("4 - imprimir estoque")
                                menu = input("Faça sua escolha do menu: ")
                                print("0 - sair")
                                print("1 - adicionar loja")
                                print("2 - remover loja")
                                print("3 - imprimir loja")
                                print("4 - editar loja")
                                cardapio = input("Faça escolha do cardapio: ")
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
                            if produto in lojas[nomeloja]:
                                if preco < 0:
                                    while lojas[nomeloja][produto]['preco'] + preco < 0:
                                        print("Preço final não pode ser negativo")
                                        preco = float(input("Digite o preço a ser somado: "))
                                else:
                                    lojas[nomeloja][produto]['quantidade'] += valor
                                    lojas[nomeloja][produto]['preco'] += preco
                                    lojas[nomeloja][produto]['total'] = lojas[nomeloja][produto]['preco']*lojas[nomeloja][produto]['quantidade']
                                    print("O produto {0} passa a ter {1} itens ao valor de {2} reais cada, totalizando {3} reais".format(produto, lojas[nomeloja][produto]['quantidade'],lojas[nomeloja][produto]['preco'],lojas[nomeloja][produto]['quantidade']*lojas[nomeloja][produto]['preco']))
                                    print("0 - sair")
                                    print("1 - adicionar item")
                                    print("2 - remover item")
                                    print("3 - alterar item")
                                    print("4 - imprimir estoque")
                                    menu = input("Faça sua escolha do menu: ")
                                    print("0 - sair")
                                    print("1 - adicionar loja")
                                    print("2 - remover loja")
                                    print("3 - imprimir loja")
                                    print("4 - editar loja")
                                    cardapio = input("Faça sua escolha do cardapio: ")
                            else:
                                print("Elemento não encontrado")
                                print("0 - sair")
                                print("1 - adicionar item")
                                print("2 - remover item")
                                print("3 - alterar item")
                                print("4 - imprimir estoque")
                                menu = input("Faça sua escolha do menu: ")
                                
                    #Escolha 4 - imprimir estoque
                    if menu == "4":
                        soma_quant = 0
                        soma_preco = 0
                        print("0 - imprimir todo estoque")
                        print("1 - imprimir apenas estoque positivo")
                        print("2 - imprimir apenas estoque negativo")
                        submain = input("Digite sua escolha para imprimir o estoque: ")
                        for e in lojas[nomeloja]: 
                            if submain == "0":
                                soma_quant += lojas[nomeloja][e]['quantidade'] 
                                soma_preco += lojas[nomeloja][e]['preco']*lojas[nomeloja][e]['quantidade'] 
                                print("{0}: {1}: {2}".format(e, lojas[nomeloja][e]['quantidade'],lojas[nomeloja][e]['preco'])) 
                            if submain == "1":
                                if lojas[nomeloja][e]['quantidade'] >= 0: 
                                    soma_quant += lojas[nomeloja][e]['quantidade'] 
                                    soma_preco += lojas[nomeloja][e]['preco'] * lojas[nomeloja][e]['quantidade'] 
                                    print("{0}: {1}: {2}".format(e, lojas[nomeloja][e]['quantidade'],lojas[nomeloja][e]['preco'])) 
                            if submain == "2":
                                if lojas[nomeloja][e]['quantidade'] < 0: 
                                    soma_quant += lojas[nomeloja][e]['quantidade'] 
                                    soma_preco += lojas[nomeloja][e]['preco'] * lojas[nomeloja][e]['quantidade'] 
                                    print("{0}: {1}: {2}".format(e, lojas[nomeloja][e]['quantidade'],lojas[nomeloja][e]['preco']))
                        print("A quantidade total do carrinho é de {0} itens e o preço total é de {1} reais".format(soma_quant,soma_preco))
                        print("0 - sair")
                        print("1 - adicionar item")
                        print("2 - remover item")
                        print("3 - alterar item")
                        print("4 - imprimir estoque")            
                        menu = input("Faça sua escolha do menu: ")
                   
            else:
                print("Loja inexistente")
                print("0 - sair")
                print("1 - adicionar loja")
                print("2 - remover loja")
                print("3 - imprimir loja")
                print("4 - editar loja")
                cardapio = input("Faça sua escolha do cardapio: ")
  
        
    # Sair - Opção - 0
    if cardapio == "0":
        print("Até mais")
    
firebase.patch("/Estoque", lojas)


        
                
                
                
            
            
                
            
        
    

    
    


