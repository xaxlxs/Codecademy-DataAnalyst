a1 = ' '
b1 = ' '
c1 = ' '
a2 = ' '
b2 = ' '
c2 = ' '
a3 = ' '
b3 = ' '
c3 = ' '

dic = {'a1':a1, 'b1':b1, 'c1':c1, 'a2':a2, 'b2':b2, 'c2':c2, 'a3':a3, 'b3':b3, 'c3':c3}

board = '  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3
print(board) 

moves = []

round = 1
while round < 10:
    if round % 2 == 0:
        active_player = "O"
    else:
        active_player = "X"
    print("Player " + active_player + " chose your cell.")
    cell = input()
    if cell in moves:
        print('Chose another cell.')
        continue
    else:
        space = dic[cell]
        space = active_player
        if active_player in (a1 and b1 and c1):
            board = '  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3
            print(board) 
            print("Player " + active_player + " wins!")
            break
        else:
            board = '  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3
            print(board)
            continue
        round += 1





'''
Psudo:
check which player is active (counter)
ask player for their move
if requested square != ' ' ask to pick again (loop)
increment counter
set requested square to player's character
check for winner
'''