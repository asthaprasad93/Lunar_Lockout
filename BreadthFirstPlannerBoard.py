import time
import copy

class BreadthFirstPlannerBoard(object):
        
    def Plan(self, start_config):

        #Breadth first search algorithm

        Start_ID = start_config;
        Goal_ID = "r22"  

        plan = []
        queue = []
        parent = {}
        
        plan_ID = []

        queue.append(Start_ID)
        nNodes = 0

        while queue:
            successors = []
            ID = queue.pop(0)
            nNodes += 1
            if (Goal_ID in ID):
                plan_ID = [ID]
                break

            successors = self.GetSuccessors(ID)
            if len(successors) > 0:
                for i in range(len(successors)):
                    for k,v in parent.items():
                        if successors[i] == k or successors[i] == Start_ID:
                            successors[i] = []
                successors = filter(lambda a: a != [], successors)

            for s in successors:
                parent[s] = ID
        
            queue.extend(successors)  

        print 'Goal found'

        while plan_ID[-1] != Start_ID:
            plan_ID.append(parent[plan_ID[-1]])

        plan_ID.reverse()

        for i in range(len(plan_ID)):
            plan.append(self.RepToBoard(plan_ID[i]))
        return plan


    def PrintBoard(self, board):

        #Prints list of lists in a 2D matrix 

        for i in range(5):
            print "\n"
            for j in range(5):
                print (" " + str(board[i][j])),
        print ("\n\n---------------------")


    def GetSuccessors(self, rep):

        #Checks if a cell in the received current state is unoccupied
        #Returns all the states (boards) in which a rocket can legally move into a cell

        board = self.RepToBoard(rep)

        successors = []
        succRep = []

        for x in range(5):
            for y in range(5):
                if (board[x][y] == '-'):
                    nb = self.GetNeighbours(x, y, board)
                    self.MoveRockets(x, y, board, nb, successors)

        return successors



    def MoveRockets(self, r, c, board, nb, successors):

        # checks legal moves in the 4 directions of a cell and slides a rocket into the cell
        # if there is a legl move available
        # Appends all such resultant states to the list of successors

        if nb[0] != 0:
            for i in range(0, c+1):
                if board[r][c-i] != '-':
                    tempboard = [list(inner) for inner in board]
                    tempboard[r][c] = board[r][c-i]
                    tempboard[r][c-i] = '-'
                    successors.append(self.BoardToRep(tempboard))

        if nb[1] != 0:
            for i in range(0, 5-r):
                if board[r+i][c] != '-':
                    tempboard = [list(inner) for inner in board]
                    tempboard[r][c] = board[r+i][c]
                    tempboard[r+i][c] = '-'
                    successors.append(self.BoardToRep(tempboard))

        if nb[2] != 0:
            for i in range(0, 5-c):
                if board[r][c+i] != '-':
                    tempboard = [list(inner) for inner in board]
                    tempboard[r][c] = board[r][c+i]
                    tempboard[r][c+i] = '-'
                    successors.append(self.BoardToRep(tempboard))


        if nb[3] != 0:
            for i in range(0, r+1):
                if board[r-i][c] != '-':
                    tempboard = [list(inner) for inner in board]
                    tempboard[r][c] = board[r-i][c]
                    tempboard[r-i][c] = '-'
                    successors.append(self.BoardToRep(tempboard))

        return 


    def GetNeighbours(self, r, c, board):

        #r = cell row
        #c = cell column
        #board = current state

        # For a particular cell, returns a 4 element list representing 
        # whether or not a rocket can slide into the cell 
        # from each of the 4 directions [right up left down]

        nb = [0, 0, 0, 0]

        if c == 4:
            nb[0] = 0
        elif board[r][c+1] != '-':
            nb[0] = 1

        if r == 0:
            nb[1] = 0
        elif board[r-1][c] != '-':
            nb[1] = 1

        if c == 0:
            nb[2] = 0
        elif board[r][c-1] != '-':
            nb[2] = 1

        if r == 4:
            nb[3] = 0
        elif board[r+1][c] != '-':
            nb[3] = 1

        return nb


    def BoardToRep(self, board):

        #Converts board representation to a string (eg. "-00-01-02r04-10-11" etc)
        #each cell is represented by "ObjectRowColumn"
        #Length of returned string = 3*25 

        rep = ""
        for x in range(5):
            for y in range(5):
                rep += board[x][y]
                rep += str(x)
                rep += str(y)
        return rep


    def RepToBoard(self, rep):

        #Converts string back to board representation

        tempBoard = [['-' for i in range(5)] for j in range(5)]
        ind = 0
        for i in range(5):
            for j in range(5):
                x = int(rep[ind + 1])
                y = int(rep[ind + 2])
                tempBoard[x][y] = rep[ind]
                ind = ind + 3

        return tempBoard








        