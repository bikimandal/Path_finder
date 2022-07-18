import curses
from curses import wrapper
import queue
import time

maze = [
    ["#","O","#","#","#","#","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#"," ","#","#"," ","#","#"," ","#"],
    ["#"," ","#"," "," "," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#","#","#","#","#","#","#","X","#"]
]

def print_maze(maze, stdscr, path = []):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i , row in enumerate(maze):
        for j , value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i*2, j*4, "X", RED)
            else:
                stdscr.addstr(i*2, j*4, value, BLUE)

                                #main_function_finding_path

def find_path  (maze,stdscr):

    start_symbol = "O"
    end_symbol = "X"
    
    GREEN = curses.color_pair(3)
    RED = curses.color_pair(2)

    start_position = find_start(maze, start_symbol)   
    q = queue.Queue()
    q.put((start_position, [start_position]))

    visited = set()

    while not q.empty() :
        current_pos , path = q.get()
        row, col = current_pos
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)                                 #TIME 
        stdscr.refresh()

        if maze [row] [col] == end_symbol :
            return_1 = path
        neighbours = find_neighbours(maze, row, col)

        for neighbour in neighbours:
            if neighbour in visited :
                continue
            r , c = neighbour

            if maze [r][c] == "#" :
                continue

            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)
        if find_end(maze, end_symbol) in path:
            succesfull = True
            stdscr.addstr("\n \n Succesfull!", GREEN)
        else:
            succesfull = False
            stdscr.addstr("\n \n Unsuccesfull!", RED)
        # stdscr.addstr("Succesfull!")
        # return succesfull

def find_neighbours (maze, row , col):
    neighbours = []
    if row > 0 :                    #UP
        neighbours.append((row - 1 , col))
    if row + 1 < len(maze):         #DOWN
        neighbours.append((row + 1 , col))
    if col > 0 :                    #LEFT
        neighbours.append((row , col - 1))
    if col + 1 < len(maze[0]) :     #RIGHT
        neighbours.append((row , col + 1))
    return neighbours


def find_start(maze, start):

        for i , row in enumerate(maze):
            for j , value in enumerate(row):
                if value == start :
                    return i , j
        return None

def find_end(maze, end_symbol):

    for i, row in enumerate(maze):
        for j , value in enumerate(row):
            if value == end_symbol:
                return i,j
    return None

def main (stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    
    # find_path(maze, stdscr)
    find_path(maze, stdscr)
    # if succesfull == True:
    #      print("Succesfull!")
    # else :
    #     print("Unsuccesfull!")
    stdscr.getch()

    
wrapper(main)


