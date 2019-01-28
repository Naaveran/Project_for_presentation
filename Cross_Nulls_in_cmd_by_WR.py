A1 = [" ", " ", " ", " "]
A2 = [" ", " ", " ", " "]
A3 = [" ", " ", " ", " "]                               # Версія хрестиків-нуликів для командної строки)
Lines = ["---------"]
def adder_x_ (a, b):
    if a == 1:
        if A1[b] != "O" and A1[b] != "X":
            A1.pop (b)
            A1.insert (b, "X")
        else:
            print ("Комірка вже зайнята, спробуй іншу.")
            adder_x_ (int (input ("X: ")), int (input ("X: ")))
    if a == 2:
        if A2[b] != "O" and A2[b] != "X":
            A2.pop (b)
            A2.insert (b, "X")
        else:
            print ("Комірка вже зайнята, спробуй іншу.")
            adder_x_ (int (input ("X: ")), int (input ("X: ")))
    if a == 3:
        if A3[b] != "O" and A3[b] != "X":
            A3.pop (b)
            A3.insert (b, "X")
        else:
            print ("Комірка вже зайнята, спробуй іншу.")
            adder_x_ (int (input ("X: ")), int (input ("X: ")))

def adder_o_ (a, b):
    if a == 1:
        if A1[b] != "O" and A1[b] != "X":
            A1.pop (b)
            A1.insert (b, "O")
        else:
            print ("Комірка вже зайнята, спробуй іншу.")
            adder_o_ (int (input ("O: ")), int (input ("O: ")))
    if a == 2:
        if A2[b] != "O" and A2[b] != "X":
            A2.pop (b)
            A2.insert (b, "O")
        else:
            print ("Комірка вже зайнята, спробуй іншу.")
            adder_o_ (int (input ("O: ")), int (input ("O: ")))
    if a == 3:
        if A3[b] != "O" and A3[b] != "X":
            A3.pop (b)
            A3.insert (b, "O")
        else:
            print ("Комірка вже зайнята, спробуй іншу.")
            adder_o_ (int (input ("O: ")), int (input ("O: ")))

def toprint ():
    print ("  ", A1[1], "|", A1[2], "|", A1[3])
    print ("  ", Lines[0])
    print ("  ", A2[1], "|", A2[2], "|", A2[3])
    print ("  ", Lines[0])
    print ("  ", A3[1], "|", A3[2], "|", A3[3])

def winx ():
    if (A1[1] == "X" and A1[2] == "X" and A1[3] == "X") or (A2[1] == "X" and A2[2] == "X" and A2[3] == "X") or (A3[1] == "X" and A3[2] == "X" and A3[3] == "X") or (A1[1] == "X" and A2[1] == "X" and A3[1] == "X") or (A1[2] == "X" and A2[2] == "X" and A3[2] == "X") or (A1[3] == "X" and A2[3] == "X" and A3[3] == "X") or (A1[1] == "X" and A2[2] == "X" and A3[3] == "X") or (A1[3] == "X" and A2[2] == "X" and A3[1] == "X"):
        print ("Player 1 wins")
        quit ()
def wino ():
    if (A1[1] == "O" and A1[2] == "O" and A1[3] == "O") or (A2[1] == "O" and A2[2] == "O" and A2[3] == "O") or (A3[1] == "O" and A3[2] == "O" and A3[3] == "O") or (A1[1] == "O" and A2[1] == "O" and A3[1] == "O") or (A1[2] == "O" and A2[2] == "O" and A3[2] == "O") or (A1[3] == "O" and A2[3] == "O" and A3[3] == "O") or (A1[1] == "O" and A2[2] == "O" and A3[3] == "O") or (A1[3] == "O" and A2[2] == "O" and A3[1] == "O"):
        print ("Player 2 wins")
        quit ()
def noone ():
    print ("Noone wins")


n = 1
print ("Привіт, це хрестики-нулики. \nПравила прості - спочатку ходять хрестики, потім нулики. \nЩоб походити, необхідно спочатку ввести номер рядка (1, 2, 3) і натиснути Ентер, а потім ввести номер позиції (1, 2, 3) після чого знову натиснути Ентер. ")
print ("Хто складе ряд з трьох хрестиків чи нуликів - виграв.\n")
toprint ()
for n in range (9):
    adder_x_ (int (input ("X: ")), int (input ("X: ")))
    toprint ()
    winx ()
    adder_o_ (int (input ("O: ")), int (input ("O: ")))
    toprint ()
    wino ()
    if n == 9:
        noone ()
    n += 1
input()
