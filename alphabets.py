#alphabets
#A
for row  in range(6):
            for col in range(15):
                if (row+col==5) or (col-row==5) or (row==3 and col>=3 and col<=7):
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
#B
for row in range(7):
    for col in range(5):
        if (row==0) or (col==0) or (row==3 and col>=0 and col<=3) or (row==6 and col>=0 and col<=5) or (row==1 and col<=4 and col>=4) or (row==2 and col<=4 and col>=4) or (row==4 and col<=4 and col>=4) or (row==5 and col<=4 and col>=4):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#C
for row in range(6):
    for col in range(6):
        if (row==0 and col>=1 and col<=4) or (col==0 and row>=1 and row<=4) or (row==5 and col>=1 and col<=4):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#D
for row in range(6):
    for col in range(6):
        if (row==0 and col>=0 and col<=4) or (col==0) or (row==5 and col>=0 and col<=4) or (col==5 and row>=1 and row<=4):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#E
for row in range(7):
    for col in range(5):
        if (row==0) or (col==0) or (row==3 and col>=0 and col<=3) or (row==6 and col>=0 and col<=5):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#F
for row in range(7):
    for col in range(5):
        if (row==0) or (col==0) or (row==3 and col>=0 and col<=3):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#G
for row in range(7):
    for col in range(6):
        if (row==0 and col>=1 and col<=5) or (col==0 and row>=1 and row<=5) or (row==3 and col>=2 and col<=5) or (row==6 and col>=1 and col<=2) or (col==3 and row>=4 and row<=5) or (col==5 and row>=4 and row<=6):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#H
for row in range(7):
    for col in range(6):
        if (col==0) or (row==3 and col>=0 and col<=5) or (col==5 and row>=0 and row<=6):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#I
for row in range(7):
    for col in range(7):
        if (row==0) or (row==6 and col>=0 and col<=6) or (col==3 and row>=0 and row<=6):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#J
for row in range(7):
    for col in range(7):
        if (row==0) or (row==6 and col>=0 and col<=2) or (col==3 and row>=0 and row<=5):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#K
for row in range(7):
    for col in range(7):
        if (col==0) or (row+col==3) or (row-col==3):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#L
for row in range(7):
    for col in range(7):
        if (col==0) or (row==6 and col>=0 and col<=6):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#M
for row in range(7):
    for col in range(7):
        if (col==0) or (row==col<=3) or (row+col==6 and col>row) or (col==6):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#N
for row in range(6):
    for col in range(6):
        if (col==0) or (row==col) or (col==5):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#O
for row in range(9):
    for col in range(6):
        if (row==0 and col>=1 and col<=4) or (col==0 and row>=1 and row<=4) or (row==5 and col>=1 and col<=4) or (col==5 and row>=1 and row<=4):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#P
for row in range(7):
    for col in range(6):
        if (col==0) or (row==0 and col>=0 and col<=4) or (row==3 and col>=0 and col<=4) or (col==5 and row>=1 and row<=2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#Q
for row in range(9):
    for col in range(7):
        if (row==0 and col>=1 and col<=4) or (col==0 and row>=1 and row<=4) or (row==5 and col>=1 and col<=4) or (col==5 and row>=1 and row<=4) or (row==col>=4):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#R
for row in range(7):
    for col in range(6):
        if (col==0) or (row==0 and col>=0 and col<=4) or (row==3 and col>=0 and col<=4) or (col==5 and row>=1 and row<=2) or (row-col==2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#S
for row in range(7):
    for col in range(4):
        if (row==0 and col>=1 and col<=2) or (row==1 and col>=3 and col<=3) or (row-col==1) or (row==5 and col>=0 and col<=0) or (row==5 and col>=3 and col<=3) or (row==6 and col>=1 and col<=2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#T
for row in range(7):
    for col in range(5):
        if (row==0) or (col==2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#U
for row in range(7):
    for col in range(4):
        if (col==0 and row>=0 and row<=5) or (col==3 and row>=0 and row<=5) or (row==6 and col>=1 and col<=2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#V
for row in range(5):
    for col in range(10):
        if (row==col) or (col+row==8):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#W
for row in range(7):
    for col in range(7):
        if (col==0) or (col==6) or (row+col==6 and row>=3 and row<=6) or (col==row and col>=4 and col<=6) :
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#X
for row in range(7):
    for col in range(7):
        if (row==col) or (row+col==6):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#Y
for row in range(7):
    for col in range(7):
        if (row==col<=3) or (row+col==6 and col>row) or (col==3 and row>=3 and row<=6):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
#Z
for row in range(7):
    for col in range(7):
        if (row==0) or (row+col==6) or (row==6):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
