import random


MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

contador_simbolos = {
    "$" : 2,    #Existem 2 $
    "#" : 4,    #Existem 4 #
    "!" : 6,    #Existem 6 !
    "&" : 8     #Existem 8 &
}

multiplicador_simbolos = {
    "$" : 5,    
    "#" : 4,    
    "!" : 3,    
    "&" : 2     
}


def check_win(colunas,linhas,bet,values):
    ganhos = 0
    ganhos_linha = []
    for line in range(linhas):
        simbolo = colunas[0][line]
        for coluna in colunas:
            simbolo_verif = coluna[line] 
            if simbolo != simbolo_verif:
                break
        else:
            ganhos += values[simbolo] * bet
            ganhos_linha.append(line+1)

    return ganhos,ganhos_linha





def get_slot_spin(rows,cols,caracter):
    all_symbols = []

    for simbolos, contador_simbolos in caracter.items():
        for _ in range(contador_simbolos):
            all_symbols.append(simbolos)
    
    colunas = []

    for _ in range(cols):   #Gerar colunas
        coluna = []
        current_simbolos = all_symbols[:]   #Copiar lista
        for _ in range(rows):   #Gerar linhas
            valor = random.choice(current_simbolos) #Escolher simbolo aleatorio
            current_simbolos.remove(valor)  #Remover simbolo escolhido para nao ter chance de calhar o mesmo
            coluna.append(valor)    #Atribuir o valor

        colunas.append(coluna)

    return colunas


def print_slot_spin(colunas):   #Virar as colunas ao contrario para ficarem lindas
    for row in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):        #Percorrer todos os itens de colunas     
            if i != len(colunas) - 1:   #Verificar se estamos na ultima coluna para nao colocar | em um lugar que nao precisa
                print(coluna[row], end=" | ")     #Imprimir valores
            else:   #Se estivermos na ultima
                print(coluna[row], end= "")

        print()




def deposit():
    while True:
        deposito = input("Indique quanto quer depositar: $")    #Receber input
        if deposito.isdigit():  #Verificar se é digito
            deposito = int(deposito)    #Converter para inteiro
            if deposito > 0:    #Se o numero for maior que 0
                break 
            else:   #Se for menor ou igual a 0
                print("Numero tem de ser maior que 0.")
        else:   #Se nao for digito
            print("Escreva um numero.")

    return deposito #Retornar deposito

def get_bet():
    while True:
        bet = input("Indique quanto quer apostar: $")   #Input
        if bet.isdigit():   #Verificar se e um numero
            bet = int(bet)  #Converter para inteiro
            if MIN_BET <= bet <= MAX_BET:   #Se estiver entre os intervalos definidos
                break   
            else:   #Se na obedecer aos intervalos
                print(f"Valor deve estar entre ({MIN_BET}-{MAX_BET}).")
        else:   #Se nao for um numero
            print("Introduz um numero.")
    
    return bet  #Retornar valor


def get_num_of_lines():
    while True:
        linhas = input("Indique a quantidade de linhas que quer apostar:(1-" + str(MAX_LINES) +  "):")  #input
        if linhas.isdigit():    #Verificar se e numero
            linhas = int(linhas)    #Converter para inteiro
            if 1 <= linhas <= MAX_LINES:    #Se estiver entre os intervalos definidos
                break 
            else:   #Se nao obedecer aos intervalos
                print(f"Numero de linhas tem de estar entre 1 e {MAX_LINES}")
        else:   #Se nao for um numero
            print("Escreva um numero.")

    return linhas



def game(credito):

    linhas = get_num_of_lines() #Ter numero de linhas a apostar
    while True:
        bet = get_bet() #Ter a aposta
        if bet * linhas > credito:  #Se a aposta total for maior que dinehri disponivel
            print(f"Nao tens credito suficiente para fazer isso.Tens ${credito}")
        else:
            break
    total_bet = bet*linhas  #Aposta total

    print(f"\nCredito:{credito}\nApostando:{total_bet}\nQuantidade de linhas:{linhas}")

    slot = get_slot_spin(ROWS, COLS,contador_simbolos)

    print_slot_spin(slot)

    ganhos,ganho_linha= check_win(slot,linhas,bet,multiplicador_simbolos)

    print(f"Ganhaste ${ganhos}!")
    print(f"Gnhaste nas linhas:", *ganho_linha)

    return ganhos - total_bet

def main():
    credito = deposit() #Ter quantidade de dinheiro inicial

    while True:
        print(f"Credito atual e: ${credito}")
        spin = input("Pressiona enter para girar ou q para sair.")
        if spin == 'q':
            break
            
        credito += game(credito)
    print(f"Saiste com ${credito}!")

main()

