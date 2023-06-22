def print_sudoku(sudoku: list):
    # print original sudoku grid
    # for r in sudoku:
    #     for c in r:
    #         if c == 0:
    #             c = "_"
    #         print(c, end= " ")

    #     print()
    for r in range(len(sudoku)):
        for c in range(len(sudoku[r])):
            if sudoku[r][c] == 0:
                cell = "_"
            else:
                cell = str(sudoku[r][c])
            print(cell, end=" ")
            if (c + 1) % 3 == 0:
                print(end = " ")  # Add space after each 3 elements in a row
        print()
        if (r + 1) % 3 == 0:
            print("")  # Add empty line after each 3 rows

    

def add_number(sudoku: list, row_no: int, col_no: int, number: int):
    sudoku[row_no][col_no] = number
    return sudoku


if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
