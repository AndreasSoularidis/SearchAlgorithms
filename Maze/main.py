from BFS_Algorithm import BFS
from maze import MazeNode


def main():
  # Representation of a graph as a dictionary
  graph = {
    "A": ['S'],
    "B": ['C', 'D','S'],
    "C": ['B', 'J'],
    "D": ['B', 'G', 'S'],
    "E": ['G', 'S'],
    "F": ['G', 'H'],
    "G": ['D', 'E', 'F', 'H', 'J'],
    "H": ['F', 'G', 'I'],
    "I": ['H', 'J'],
    "J": ['C', 'G', 'I'],
    "S": ['A', 'B', 'D', 'E']
  }

  mazes = MazeNode(graph, "S")
  bfs = BFS(mazes, "I")
  bfs.search()

if __name__ == '__main__':
  main()