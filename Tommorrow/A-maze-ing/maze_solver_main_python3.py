#########################################
# Programmer: Mrs. G
# Date: 6.10.2014
# File Name: maze_solver-main.py
# Description: This program solves a maze of arbitrary size.
#   The program follows the algorithm described on the following website:
#       http://www.cs.bu.edu/teaching/alg/maze/
#   Input file must comply with the following guidelines:
#       - walls are one character thick and represented with "#"
#       - alleys are one character wide and represented with spaces
#       - each line, including the last, ends with 'new line' character
#   Module maze contains the following functions:
#       - load_maze(fname)
#       - random_coordinates_generator(maze)
#       - print_maze(maze)
#       - maze_solver(maze, x, y)
#   After importing the module, use help(function name), to understand how they work.
#   These functions exercise the following:
#       - reading from a file:
#       - nested lists (2D lists)
#       - string.join method:
#               L = ['i', 't', 'e', 'r', 'a', 'b', 'l', 'e']
#               print ''.join(L)
#       - list comprehension
#       - recursion
#########################################
import random
from maze import*
import maze_generator_python3
#---------------------------------------#        
# main program                          #
#---------------------------------------#        
fname = 'maze.txt'
maze = load_maze(fname)
# generate random start and goal locations
Sy,Sx = random_coordinates_generator(maze)
maze[Sy][Sx] = 'S'
Gy,Gx = random_coordinates_generator(maze)
maze[Gy][Gx] = 'G'
print ('\nHere is the maze with start and goal locations:')
print_maze(maze)

# now, find the path from S to G
maze_solver(maze, Sx, Sy)
maze[Sy][Sx] = 'S'
print ('\nHere is the maze with the path from start to goal:')
print_maze(maze)


