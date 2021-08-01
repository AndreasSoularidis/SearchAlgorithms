import os
from sudoku import Sudoku
from dfs_algorithm import DFS


def read_data(filename):
  """
    Reads the txt file and returns a list which containts the data of file 

    Parameters
    ----------
    filename : str
        The name of the file that user wants to read

    
    Raises
    ------
    FileNotFoundError
      If the filename does not exist

    Returns
    -------
    list
        a list of lists which contains the data of the file
  """
  try:
    data = []
    abs_path = os.path.abspath(f"puzzles/{filename}")
    with open(abs_path, "r", encoding="utf-8") as f:
      contents = f.readlines()
    for row in contents:
      new_row = [int(number.strip()) for number in row if number != '\n' and number != ' ']
      data.append(new_row)
    return data
  except FileNotFoundError:
     return None



def main():
  """
    Call the read_data function and then creates a new sudoku object.
    Finally creates an instance of DFS class, execute the algorithm
    and prints the resutls of the algorithm 
  """

  filename = input("Please enter the number of the text file: ")
  filename += ".txt"
  data = read_data(filename)

  if data is not None:
    sudoku = Sudoku(data)
    print("Depth First Search")
    dfs = DFS(sudoku)
    dfs.search()
  else:
    print("This file does not exit. Please enter another file name")


if __name__ == '__main__':
  main()