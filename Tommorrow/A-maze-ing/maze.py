##By: Benji Saltz
##Date: 02/04/18
#Description: This maze solving recursive algorithm works due to many pieces: 1) to run the program, you must run from main, all this program does is find the path on the already generated maze what is the quickest route to from the start to the goal. 
import random
def load_maze(fname):
    maze = []
    file_in = open(fname,'r')# readlines()
    lines = file_in.readlines()   # 
    for i in range(len(lines)):   #
        lines[i]=lines[i][0:-1]   # Newline characters are removed before printing
        maze.append(lines[i])  
        maze[i]= list(maze[i])
    return maze
    
def random_coordinates_generator(maze):
    chosen=False
    while chosen==False:
        x = random.randint(1,len(maze)-2) #Coordinates which start and finish will spawn on which does not include walls
        y = random.randint(1,len(maze[0])-2)
        if maze[x][y]==' ':
            chosen = True
    return(x,y)
        
    
def print_maze(maze):
    for a in range(len(maze)):
        print (''.join(maze[a]))
        
def maze_solver(maze, sx, sy):
    if maze[sy][sx]=='G':
        return True
    elif maze[sy][sx]=='#':
        return False
    elif maze[sy][sx]=='+':
        return False
    else:
        maze[sy][sx]='+'
        if maze_solver(maze,sx,sy+1):
            return True
        if maze_solver(maze,sx+1,sy):
            return True
        if maze_solver(maze,sx,sy-1):
            return True
        if maze_solver(maze,sx-1,sy):
            return True
        maze[sy][sx]=' '
        return False
