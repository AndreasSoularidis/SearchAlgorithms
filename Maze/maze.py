from BFS_Algorithm import Node 
class MazeNode(Node):
  """
    This class used to represent the node of a maze
    ...
    Attributes
    ----------
    graph : Dictionary
        represent the graph  
    value : String
        represents the id of the vertex
    parent : MazeNode
        represents the parent of the current node
  
    Methods
    -------
    __eq__(self, other)
        Determines if the current node is the same with the other 
    is_the_solution(self, final_state)
        Checks if the current node is the solution
    extend_node(self)
        Extends the current node, creating a new instance of MazeNode for each edge starts from current node 
    _find_path(self)
        Find the path (all verticies and edges from the intitial state to the final state)
    __str__(self)
        Returns the solution of the maze, the whole path vertex by vertex in order to be printed properly.
  """

  def __init__(self, graph, value):
    self.graph = graph
    self.value = value
    self.parent = None

  
  def __eq__(self, other):
    """
      Check if the current node is equal with the other node.
      Parameters
      ----------
      Other : MazeNode
          The other vertex of the graph
      Returns
      -------
      Boolean
        True: if both verticies are the same
        False: If verticies are different
    """ 
    if isinstance(other, MazeNode):
      return self.value == other.value
    return self.value == other

  
  def is_the_solution(self, final_state):
    """
      Checks if the current node is the solution
      Parameters
      ----------
      final_state : MazeNode
          The target vertex (final state) of the graph
      Returns
      -------
      Boolean
        True: if both verticies are the same, so solution has been found
        False: If verticies are different, so solution has not been found
    """
    return self.value == final_state

  
  def extend_node(self):
    """
      Extends the current node, creating a new instance of MazeNode for each edge starts from the current node
      Returns
      -------
      List
        List with all valid new nodes
    """
    children = [MazeNode(self.graph, child) for child in self.graph[self.value]]
    for child in children:
      child.parent = self
    return children

  def _find_path(self):
    """
      Find the path, all verticies and edges from the intitial state to the final state
      Returns
      -------
      List
        List with all nodes fron start to end in a row
    """
    path = []
    current_node = self
    while current_node.parent is not None:
      path.insert(0, current_node.value)
      current_node = current_node.parent
    path.insert(0, current_node.value)
    return path

  def __str__(self):
    """
      Returns the solution of the maze, the whole path vertex by vertex as well as the path lenght, in order to be printed properly.
      Returns
      -------
      str
        the solution of the problem
    """
    total_path = self._find_path()
    path = ""
    for index in range(len(total_path)):
      if index == len(total_path) - 1:
        path += f"{total_path[index]} "
      else:
        path += f"{total_path[index]} -> "


    return path + f"\nPath lenght: {len(total_path)-1}"