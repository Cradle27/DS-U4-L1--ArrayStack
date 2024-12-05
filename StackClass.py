class ArrayStack:
  def __init__(self):
    self.__stack = []
    self.__size = self.__len__()

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out

  def push(self, e):
    """adds an item to stack"""
    self.__stack.append(e)

  def pop(self):
    """removes the top item from stack"""
    if self.__is_empty() == False:
      el = self.__stack[self.__len__() - 1]
      del self.__stack[self.__len__() - 1]
      return el

    else:
      raise ValueError("Stack has no elements")

  def top(self):
    """returns the top item from a stack"""
    if self.__is_empty() == False:
      return self.__stack[self.__len__() - 1]
    else:
      raise ValueError("Stack has no elements")

  def __is_empty(self):
    if self.__size <= 0:
      return True
    else:
      return False

  def __len__(self):
    """counts the items in stack and returns the numbers"""
    total = 0
    for i in self.__stack:
      total += 1
    self.__size = total
    return total
