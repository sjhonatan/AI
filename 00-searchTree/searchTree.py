""" Program for tree-search 
    Jhonatan da Silva 
    27/01/2017 """


def main():
    treeSearch('California', 'Washington')

def treeSearch(initState,goalState):
    path = []
    frontier = search(initState, goalState)

    while not frontier.isEmpty():
        """ checks if state is equal to goal """ 
        if frontier.testGoal():
            break
        """ If not goal, gets the state to search """ 
        state = frontier.remove()
        try:
            for neighbors in StateNeighbors[state]:
                frontier.add(neighbors)
        except Exception as e:
            print(e)
        

class search():
    """ Initialize the search with a state and stateGoal """
    def __init__(self, state,stateGoal):
        self.state = [state]
        self.goal = stateGoal
        self.root = []

        for states in StateNeighbors[state]:
            rootList = [self.state[0], states]
            self.root.append(rootList)

    """ Adds a new state to the list """ 
    def add(self,state):
        print("")
        print("Adding node : {}".format(state))
        print("")
        self.state.append(state)

    """ Remove the state waiting to be searched and return to the treeSearch """ 
    def remove(self):
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

    """ just for testing """  
    def print(self):
        for states in self.state:
            print(states) 

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
