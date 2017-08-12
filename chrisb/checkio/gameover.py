game_result = ["X.O","XX.","XOO"]

def checkio(game_result):

    game_over = False
    print(game_result)
    #check horizontals
    for row in game_result:
        if row[0] == row[1] == row[2] and row[0] != '.':
            game_over = True
            print("We got here")
            return row[0]
            
    #check verticals
    rotated_game = zip(*game_result)
    for row in game_result:
        if row[0] == row[1] == row[2] and row[0] != '.':
            game_over = True
            return row[0]
            
    #check diagonals        
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
        game_over = True
        return game_result[0][0]
        
    elif game_result[2][2] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
        game_over = True
        return game_result[2][2]
    
    if not game_over:
        return "D"

checkio(game_result)