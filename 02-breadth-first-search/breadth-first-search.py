"""
Jhonatan da Silva
Last Updated version :
Fri Feb 10 12:15:05 2017
Number of code lines: 
111
"""

""" 
Algorithms in Artificial Inteligence 

Breadth First Search 

"""

def main():
    ''' creates a new frontier with initial state and goal state ''' 
    frontier = Queue('California','Washington')
    ''' creates a set of explored states ''' 
    explored = Set() 
    ''' adds initial state to explored ''' 
    explored.add(frontier.listStates()[0])
    ''' while the list is not empty,
        if list is empty then there's no solution '''
    while not frontier.isEmpty():
        ''' dequeue from list, gets the last element '''
        state = frontier.dequeue()
        ''' tests if reaches the goal '''
        if frontier.testGoal(state):
            ''' breaks when reaches goal ''' 
            break
        else:
            ''' add node in explored ''' 
            explored.add(state)
            ''' for every neighboors of current state adds 
                in the states if the state is not in the explored 
                list and not in the frontier, that is, the wait list
                for explore ''' 
            for new in neighboors[state]:
                if new not in explored.listStates() + frontier.listStates():
                    frontier.enqueue(new)
    

""" Using FIFO """ 
class Queue():

    """ Queue --> FIFO : First In First Out """ 

    def __init__(self, state,stateGoal):
        """ Initialize the search with a state and stateGoal """
        self.state = [state]
        self.goal = stateGoal

    def enqueue(self,state):
        """ Enqueue = add elements to the init of list
            while the current elements goes to the end
            of the list """  
        temp = []
        temp.append(state)
        temp.extend(self.state)
        self.state = temp[:]
        del temp[:]
    
    def dequeue(self):
        """ Dequeue = remove from last element """  
        temp = self.state[-1]
        del self.state[-1]
        return temp

    def testGoal(self,state):
        """ Tests for the first state on the 'waiting' list if is the goal or not """ 
        print("State : {}, Goal : {}".format(state,self.goal))
        if state == self.goal:
            return True
        else:
            return False

    def isEmpty(self):
        """ Returns true if list empty """ 
        if len(self.state) == 0:
            return True
        else:
            return False

    def listStates(self):
        return self.state

class Set():
    """ Explored elements """ 

    def __init__(self):
        """ Initialize explored with empty list """
        self.state = []
    def add(self,state):
        """ Add new state to explored """ 
        self.state.append(state)
    def listStates(self):
        """ Returns list of explores states """
        return self.state

""" dict with neighbors states I was lazy and just put some states""" 

neighboors = {'California': ['Nevada','Arizona','Oregon'],
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
