# -*- coding: utf-8 -*-

"""
Drawing playing board with for loops
 | | | | | |
-------------
 | | | | | |
-------------
 | | | | | |
-------------
 | | | | | |
printing the above shapes with specified number of rows and columns
"""

def draw_board(rows, columns):  
    if columns <= 72 and rows <= 13:
        verticals = columns*2 # real number of elements that define the column
        horizontals = rows*2 # real number of elements that define the row
        for row in range(horizontals-1):
            if row%2 == 0:
                for column in range(1, verticals):
                    if column % 2 == 1:
                        if column != verticals-1:
                            print(" ", end = "")
                        else:
                            print(" ")
                    else:
                        print("|", end = "")
            else:
                print("-"*(verticals-1))
        return True
    else:
        return False

print(draw_board(5, 72))
