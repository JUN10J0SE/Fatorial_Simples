#programa que gera um fatorial. Analise combinatoria
#funcao fatorial deve ter inicio e fim do loop

#funcao fatorial
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)#chama a propria funcao dentro dela mesma mesnos 1 ate chegar a 0
    
#protecao do programa principal
if __name__=='__main__':
    try:
        n = int(input('Informe um numero inteiro positivo: '))

        if n >=0:
            print(f'O fatorial de {n} é {fatorial(n)}.')
        else:
            print(f'Não existe fatorial de {n}.')
    except:
        print('Não foi possivel calcular o fatorial')