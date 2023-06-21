def who_won(game_board: list) -> int:
    pl1_count = 0
    pl2_count = 0
    for row in game_board:
        for cell in row:
            if cell == 1:
                pl1_count += 1
            elif cell == 2:
                pl2_count += 1

    if pl1_count > pl2_count:
        return 1
    elif pl2_count > pl1_count:
        return 2
    else:
        return 0
    
if __name__ == "__main__":
    board = [
    [1, 0, 1],
    [2, 1, 0],
    [2, 1, 2]
    ]
    print(who_won(board))