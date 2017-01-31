""" Program for graph-search 
    Jhonatan da Silva 
    28/01/2017 """

""" Breadth-first-search uses FIFO
    First in first out """

def main():
    breadthFirstSearch('California', 'Washington')

def breadthFirstSearch(initState,goalState):
    frontier = search(initState, goalState)
    while not frontier.isEmpty():
        """ checks if state is equal to goal """ 
        if frontier.testGoal():
            break
        """ If not goal, gets the state to search """ 
        state = frontier.remove()
        """ add state to explored """ 
        frontier.addExplored(state)
        print("List of states  : {}".format(frontier.waiting()))
        for neighbors in StateNeighbors[state]:
            if neighbors not in (frontier.Explored()+frontier.waiting()):
                frontier.add(neighbors)
    
""" Using FIFO """ 
class Queue():
    """ Initialize the search with a state and stateGoal """
    def __init__(self, state,stateGoal):
        self.state = [state]
        self.goal = stateGoal

    """ Equeue := 
    """
    def dequeue(self,state):
        self.state.append(state)
    
    def waiting(self):
        return self.state

    """ Dequeue := 
    """
    def dequeue(self):
        temp = self.state[0]
        del self.state[0]
        return temp

    """ Tests for the first state on the 'waiting' list if is the goal or not """ 
    def testGoal(self):
        print("State : {}, Goal : {}".format(self.state[0],self.goal))
        if self.state[0] == self.goal:
            return True
        else:
            return False

    """ Returns true if list empty """ 
    def isEmpty(self):
        if len(self.state) == 0:
            return True
        else:
            return False

class Set():
    """ Initialize explored with empty list """
    def __init__(self):
        sefl.state = []
    """ Add new state to explored """ 
    def add(state):
        self.append(state)
    """ Returns list of explores states """
    def listStates():
        return self.state

""" dict with neighbors states I was lazy and just put some states""" 

StateNeighbors = {'California': ['Nevada','Arizona','Oregon'],
                  'Oregon':['Washington','Idaho','Nevada'],
                  'Nevada':['Utah','Idaho','Arizona'],
                  'Arizona':['New Mexico'],
                  'New Mexico':['Colorado'],
                  'Colorado':['Wyomming'],
                  'Wyomming':['Idaho','Montana'],
                  'Idaho':['Washington','Montana'],
                  'Montana':['Washington'],
                  'Utah':['Idaho']
                  }

""" runs function main """ 

if __name__ == '__main__':
    main()
