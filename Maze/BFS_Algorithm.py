from abc import ABC, abstractmethod
class Node(ABC):
  """
    This class used to represent a Node in the graph 
    It's important to implement this interface in order to make the class BFS more general
    and to use it for various problems
    ...


    Methods
    -------
    __eq__(self, other)
        Determines if two nodes are equal or not
    
    is_the_solution(self)
        Determines if the current node is the solution of the problem

    def is_the_solution(self)
        Extends the current node according to the rules of the problem
    
    __str__(self)
        Prints the node data
  """

  @abstractmethod
  def __eq__(self, other):
    pass

  @abstractmethod
  def is_the_solution(self, state):
    pass

  @abstractmethod
  def extend_node(self):
    pass

  @abstractmethod
  def __str__(self):
    pass
  
  

class BFS:
  """
    This class used to represent the  Breadth First Search algorithm (BFS)

    ...

    Attributes
    ----------
    start_state : Node
        represent the initial state of the problem 
    final_state : Node
        represent the final state (target) of the problem 
    frontier : List
        represents the stack and is initialized with the start node
    checked_nodes : List
        represents the list of nodes that have been visited throughout the algorithm execution
    number_of_steps : Integer
        Keep track of the algorithm's number of steps 
    path : List
        represents the steps from the initial state to the final state

    Methods
    -------
    insert_to_frontier(self, node)
        Insert a new node to the frontier. In this algorithm the frontier is a queue, so each new element is inserted to end of the data structure 
    
    remove_from_frontier(self)
        Remove the first element from the frontier, following the FIFO technic. The removed node is added to the checked_node list

    remove_from_frontier(self)
        check if the frontier is empty
    
    search(self)
        Implements the core of algorithm. This method searches, in the search space of the problem, a solution 
    """

  def __init__(self, start, final):
    self.start_state = start
    self.final_state = final
    self.frontier = [self.start_state]
    self.checked_nodes = []
    self.number_of_steps = 0
    self.path = []

  def insert_to_frontier(self, node):
    """
      Insert a node at the end of the frontier

      Parameters
      ----------
      node : Node
          The node of the problem that will be added to the frontier
    """
    self.frontier.append(node)
  

  def remove_from_frontier(self):
    """
      Remove a node from the beginning of the frontier
      Then add the removed node to the checked_nodes list

      Returns
      -------
      Node
        the first node of the frontier
    """
    first_node = self.frontier.pop(0)
    self.checked_nodes.append(first_node)
    return first_node


  def frontier_is_empty(self):
    """
      Check if the frontier id empty, so no solution found

      Returns
      -------
      Boolean
        True if the frontier is empty
        False if the frontier is not empty
    """
    if len(self.frontier) == 0:
      return True
    return False

  
  def search(self):
    """
      Is the main algorithm. Search for a solution in the solution space of the problem
      Stops if the frontier is empty, so no solution found or if find a solution. 
    """
    while True:

      self.number_of_steps += 1
      
      # print(f"Step: {self.number_of_steps}, Frontier Size: {len(self.frontier)} ")
      if self.frontier_is_empty():
        print(f"No Solution Found after {self.number_of_steps} steps!!!")
        break
        
      selected_node = self.remove_from_frontier()

      # check if the selected_node is the solution
      if selected_node.is_the_solution(self.final_state):
        print(f"Solution Found in {self.number_of_steps} steps")
        print(selected_node)
        break

      # extend the node
      new_nodes = selected_node.extend_node()

      # add the extended nodes in the frontier
      if len(new_nodes) > 0:
        for new_node in new_nodes:
          if new_node not in self.frontier and new_node not in self.checked_nodes:
            self.insert_to_frontier(new_node)


