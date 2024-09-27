def mediaMovelSimples(vetor, janela):
    if janela > len(vetor):
        # Verifica se a janela é maior que o vetor
        raise ValueError("O tamanho da janela não pode ser maior que o tamanho do vetor.")

    # Inicializa o vetor resultante
    vetorResultante = []

    # Faz o cáculo da média móvel
    for i in range(len(vetor) - janela + 1):
        media = sum(vetor[i:i + janela]) / janela
        #Faz a soma do vetor "i" até "i + janela"
        #A função sum() faz a soma desse intervalo de i até i + janela e logo após é dividido pelo tamanho da janela
        vetorResultante.append(media)
        #Acrescenta a media ao vetor resultante

    return vetorResultante
    #Retorna o valor da média que foi "Anexado" ao vetorResultante a função mediaMovelSimples


# Exemplo de uso
vetorEntrada = [1, 3, 5, 9, 21, 3, 9, 7]  # Vetor X do exemplo
tamanhoJanela = 2  # Janela Y do exemplo
#Esses valores podem ser alterados para testar com outros números e tamanhos de janela

resultado = mediaMovelSimples(vetorEntrada, tamanhoJanela)
#Atribui os valores "vetorEntrada" e "tamanhoJanela" a variável "resultado"

print(f'Vetor resultante: {resultado}')
#Printa o resultado final