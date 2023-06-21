# Write your solution here
def column_correct(sudoku: list, col_no: int) -> bool:
    seen_val = []

    for row in sudoku:
        num = row[col_no]
        if num != 0:
            if num in seen_val:
                return False
            seen_val.append(num)
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
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
  ]
    
    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))

