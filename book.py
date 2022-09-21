import math

jogo = [["", "", ""], ["", "", ""], ["", "", ""]]

def turn_x():
    jogada = int(input("Jogador X insira a posição: "))
    if jogo[math.ceil(jogada/3)-1][round((((jogada/3)-(math.ceil(jogada/3)-1))*3))-1] == "":
        if jogada <= 9 and jogada > 0:
            jogo[math.ceil(jogada/3)-1][round((((jogada/3)-(math.ceil(jogada/3)-1))*3))-1] = "x"
        else:
            print("Utilize apenas numeros de 1 a 9")
            turn_x()
    else:
        print("Já foi jogado!")
        turn_x()

def turn_o():
    jogada = int(input("Jogador O insira a posição: "))
    if jogo[math.ceil(jogada/3)-1][round((((jogada/3)-(math.ceil(jogada/3)-1))*3))-1] == "":
        if jogada <= 9 and jogada > 0:
            jogo[math.ceil(jogada/3)-1][round((((jogada/3)-(math.ceil(jogada/3)-1))*3))-1] = "o"
        else:
            print("Utilize apenas numeros de 1 a 9")
            turn_o()
    else:
        print("Já foi jogado!")
        turn_o()

def check():
    if  jogo[0].count("x") == 3 or jogo[1].count("x") == 3 or jogo[2].count("x") == 3:
        print("Jogador X venceu!")
        return True
    if jogo[0][0] == "x" and jogo[1][0] == "x" and jogo[2][0] == "x":
        print("Jogador X venceu!")
        return True
    if jogo[0][1] == "x" and jogo[1][1] == "x" and jogo[2][1] == "x":
        print("Jogador X venceu!")
        return True
    if jogo[0][2] == "x" and jogo[1][2] == "x" and jogo[2][2] == "x":
        print("Jogador X venceu!")
        return True
    if jogo[0][0] == "x" and jogo[1][1] == "x" and jogo[2][2] == "x":
        print("Jogador X venceu!")
        return True
    if jogo[0][2] == "x" and jogo[1][1] == "x" and jogo[2][0] == "x":
        print("Jogador X venceu!")
        return True
    if  jogo[0].count("o") == 3 or jogo[1].count("o") == 3 or jogo[2].count("o") == 3:
        print("Jogador O venceu!")
        return True
    if jogo[0][0] == "o" and jogo[1][0] == "o" and jogo[2][0] == "o":
        print("Jogador O venceu!")
        return True
    if jogo[0][1] == "o" and jogo[1][1] == "o" and jogo[2][1] == "o":
        print("Jogador O venceu!")
        return True
    if jogo[0][2] == "o" and jogo[1][2] == "o" and jogo[2][2] == "o":
        print("Jogador O venceu!")
        return True
    if jogo[0][0] == "o" and jogo[1][1] == "o" and jogo[2][2] == "o":
        print("Jogador O venceu!")
        return True
    if jogo[0][2] == "o" and jogo[1][1] == "o" and jogo[2][0] == "o":
        print("Jogador O venceu!")
        return True
    if jogo[0].count("") == 0 and jogo[1].count("") == 0 and jogo[2].count("") == 0:
        print("Deu velha!")
        return True
    return False
    
    
        

def render():
    y = 0
    while y < len(jogo):

        x = 0
        while x<len(jogo[y]):
            print(jogo[y][x].center(3), end="")
            if x != len(jogo[y])-1:
                print("|", end="")
            x+=1

        print()

        if y != len(jogo)-1:
            print("---+---+---")

        y+=1

render()

while 1:
    turn_x()
    render()
    if check(): break
    turn_o()
    render()
    if check(): break