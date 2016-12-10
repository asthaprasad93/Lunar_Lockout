import argparse, numpy, openravepy, time
from BreadthFirstPlannerBoard import BreadthFirstPlannerBoard

def main(problemData):


    #Assign planner
    planner = BreadthFirstPlannerBoard()

    #Parse data into a board layout
    board = [['-' for i in range(5)] for j in range(5)]
    for i in range(len(problemData)):
        row = int(problemData[i][1])
        col = int(problemData[i][2])
        board[row][col] = problemData[i][0] 

    #Convert start position from board to string representation
    start_config = planner.BoardToRep(board)

    #Run planner
    plan = planner.Plan(start_config)

    #Print steps produced in the plaN
    for i in range(len(plan)):
        planner.PrintBoard(plan[i])
    print ("Number of states traversed : " + str(len(plan)))

    

if __name__ == "__main__":
    
    #Inputs
    parser = argparse.ArgumentParser(description='Lunar Lockout')
    parser.add_argument('-p', '--problem', type = str, default = 'problem1.txt');
    args = parser.parse_args()

    #Get Problem Data
    problemRaw = open(args.problem, 'rb')
    problemData = [row.strip().split('\t') for row in problemRaw]

    #Call main function
    main(problemData)