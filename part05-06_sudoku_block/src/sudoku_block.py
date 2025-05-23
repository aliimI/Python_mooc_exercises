# Write your solution here
def block_correct(sudoku: list, row_no: int, col_no: int) -> bool:
    list_of_seen_val = []
    for row in range(row_no, row_no + 3):
        for element in range(col_no, col_no + 3):
            number = sudoku[row][element]
            if number > 0 and number in list_of_seen_val:
                return False
            list_of_seen_val.append(number)

    return True

if __name__ == "__main__":
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))
