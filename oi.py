# -*- coding: UTF-8 -*-

#Não consegui resolver o problema da acentuação, se morassemos num país que falasse uma lingua sem isso a vida seria mais simples
while(7==7):
    print ("Insira a palavra a ser codificada (1 para encerrar):")
    word = input()
    if(word == "1"):
        break
    #Passa todas as letras para minusculas, para não gerar erros
    word = word.lower()
    bword = ""

    #Converte a palavra para binário
    for x in word:
        bword += ''.join(format(ord(x),'b'))

    #Separa a palavra em uma lista (vetor)
    separated_word = list(bword)

    #A conversão estava gerando um conflito com 0s faltantes em alguns pontos, while feito para corrigir isso
    i = 0
    while i < len(separated_word):
        if (i % 8 == 0):
            if (i + 1 < len(separated_word) and separated_word[i+1] == "1"):
                separated_word.insert(i, "0")
        i += 1
                       
    print ("Palavra inserida: " + word +"\nPalavra em binário: "+ bword +"\nPalavra codificada:\n")

    #Conversão da palavra para representação em forma de onda
    i = 0                   
    graph_rep = ""
    while i < len(separated_word):
        if (i==0):
            if (separated_word[i] == "1"):
                graph_rep += "'|_"
            else:
                graph_rep += "_|'"
        else: 
            if (separated_word[i] == "1" and separated_word[i-1] == "1"):
                graph_rep += "|'|_"
            elif (separated_word[i] == "1" and separated_word[i-1] == "0"):
                graph_rep += "'|_"
            elif (separated_word[i] == "0" and separated_word[i-1] == "0"):
                graph_rep += "|_|'"
            else:
                graph_rep += "_|'"
        i += 1
    print (graph_rep)

    #Conversão da onda para binário novamente
    split_result = list(graph_rep)
    decoded_word = ""
    i = 0
    while(i < len(split_result)):
        if (i+3 > len(split_result)):
            break
        if(split_result[i] == "_" and split_result[i+1] == "|"):
            decoded_word += "0"
            i += 2
            if (split_result[i] == "|"):
                i += 1
        elif (split_result[i] == "'" and split_result[i+1] == "|"):
            decoded_word += "1"
            
            i += 2
            if (split_result[i] == "|"):
                i += 1
        i +=1                         

    #Retorna a string binária no valor de um objeto int
    int_word = int(decoded_word, 2)

    #Depois de muito extresse peguei esse método [pronto] aqui https://stackoverflow.com/a/40566161
    final_word = (int_word.to_bytes((int_word.bit_length() + 7) // 8, 'big').decode())
    print (final_word.capitalize())

# A onda não era pra ter ficado com essa representação ridicula, mas o terminal se recusa a interpretar o overline > ¯
