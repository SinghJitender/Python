result_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def whoWins(temp_list):
    return  temp_list[0] == temp_list[1] == temp_list[2] or \
            temp_list[3] == temp_list[4] == temp_list[5] or \
            temp_list[7] == temp_list[8] == temp_list[9] or \
            temp_list[0] == temp_list[3] == temp_list[6] or \
            temp_list[1] == temp_list[4] == temp_list[7] or \
            temp_list[2] == temp_list[5] == temp_list[8] or \
            temp_list[0] == temp_list[4] == temp_list[8] or \
            temp_list[6] == temp_list[4] == temp_list[2]

def printGrid(temp_list):
    print(f"  {temp_list[6]}  |  {temp_list[7]}  |  {temp_list[8]}")
    print(f"  {temp_list[3]}  |  {temp_list[4]}  |  {temp_list[5]}")
    print(f"  {temp_list[0]}  |  {temp_list[1]}  |  {temp_list[2]}")


player1 = str(input("Player 1 choose your player X or O ? : "))

player_flag = 0

if player1 == 'X':
    print("Player 1 goes first")
    player2 = 'O'
    playerName = "Player 1"
else:
    print("Player 2 goes first")
    player2 = 'X'
    playerName = "Player 2"

printGrid(result_list)

turn = 1;
while turn <= 9:
    player_input = int(input(f"{playerName} choose your position (1-9) : "))
    if result_list[player_input-1] != "O" and result_list[player_input-1] != "X":
        if playerName == 'Player 1':
                result_list[player_input-1] = player1
        else:
                result_list[player_input-1] = player2

        printGrid(result_list)

        if (whoWins(result_list)):
            print(f"{playerName} wins. " )
            break

        if playerName == 'Player 1':
            playerName = 'Player 2'
        else:
            playerName = 'Player 1'

        turn += 1
    else:
        print("Cell already filled. Choose another one")


