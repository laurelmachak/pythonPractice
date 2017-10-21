"""
BONUS QUESTION (20 pts)! - Chess board exercise
This question is optional extra credit.
You place a pawn at the top left corner of an n-by-n chess board, labeled (0,0). For each move, you have a choice: move the pawn down a single space, or move the pawn down one space and right one space. That is, if the pawn is at position (i,j), you can move the pawn to (i+1,j) or (i+1, j+1).
Ask the user for the size of a chessboard, n. Find the number of different paths the pawn could take to reach each position on the chess board. For example, there are two different paths the pawn can take to reach (2,1):
(0,0) -> (1,0) -> (2,1)
(0,0) -> (1,1) -> (2,1)
print the board with the number of ways to reach each square labeled as shown below.
Enter a size: 3
1 0 0
1 1 0
1 2 1
Below is the code to take in a board size input. Build your code from here.

[12:29] 
n = int(input(“Enter a board size: “))

"""

def coordinates(x,y):
    