from block import *
board_height=30
board_width=32
false="false"
true="true"
class board:

    def get_new_board(self):
        # BOARD = [[0 for i in range(board_height)] for j in range(board_width)]
        BOARD=[]
        for j in range(board_width) :
            temp=[]
            for i in range(board_height) :
                temp.append(0)
            BOARD.append(temp)
        return BOARD
    def checkPiecePos(self,block_type,block_index,centre,BOARD):
        #print "block index is",block_index
        if block_type==1:
            a,b=centre
            for point in block1[block_index]:
                x,y=point
                x=x+a
                y=y+b
                if(x<(board_width) and x>=0 and y>=0 and y<(board_height)):
                    if BOARD[x][y]!=0:
                        return false
                else:
                    return false

        elif block_type==2:
            for point in block2[block_index]:
                x,y=point
                a,b=centre
                x=x+a
                y=y+b
                if(x<(board_width) and x>=0 and y>=0 and y<(board_height)):
                    if BOARD[x][y]!=0:
                        return false
                else:
                    return false
        elif block_type==3:
            #print "error may be",block3[block_index]
            for point in block3[block_index]:
                x,y=point
                a,b=centre
                x=x+a
                y=y+b
                if(x<(board_width) and x>=0 and y>=0 and y<(board_height)):
                    if BOARD[x][y]!=0:
                        return false
                else:
                    return false
        elif block_type==4:
            for point in block4[block_index]:
                x,y=point
                a,b=centre
                x=x+a
                y=y+b
                if(x<(board_width) and x>=0 and y>=0 and y<(board_height)):
                    if BOARD[x][y]!=0:
                        return false
                else:
                    return false
        return true

    def fillPiecePos(self,block_type,block_index,centre,BOARD):
        a,b=centre
        if(block_type==1):
            for point in block1[block_index]:
                x,y=point
                x=x+a
                y=y+b
                BOARD[x][y]=1
        elif(block_type==2):
            for point in block2[block_index]:
                x,y=point
                x=x+a
                y=y+b
                BOARD[x][y]=1
        elif(block_type==3):
            for point in block3[block_index]:
                x,y=point
                x=x+a
                y=y+b
                BOARD[x][y]=1
        elif(block_type==4):
            for point in block4[block_index]:
                x,y=point
                x=x+a
                y=y+b
                BOARD[x][y]=1
