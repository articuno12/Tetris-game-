from block import *
from board import *
import  time, pygame, sys
import time
from pygame.locals import *


BOXSIZE = 15 # size of box height & width in pixels
GAPSIZE = 3 # size of gap between boxes in pixels
XMARGIN = 70
YMARGIN = 100
WINDOWWIDTH = board_width*(BOXSIZE+GAPSIZE) + 2*XMARGIN +50
WINDOWHEIGHT = board_height*(BOXSIZE+GAPSIZE) + 2*YMARGIN +50
FPS = 25
MoveDownFrequency = 0.3
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = GRAY


class gameplay(board,block) :


    def quit_game(self,score) :
        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        textSurfaceObj = BIGFONT.render("U LOOSE !!!", True, PURPLE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WINDOWWIDTH/2, YMARGIN/2)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = BIGFONT.render("Score : "+str(score), True, PURPLE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = BIGFONT.render("Press any Key to exit", True, PURPLE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WINDOWWIDTH/2, WINDOWHEIGHT - 1.5*YMARGIN)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        pygame.display.update()
        while True :
            for event in pygame.event.get(KEYDOWN) :
                pygame.quit()
                sys.exit()
        return None
    def PrintText(self,score,level) :
        LEVEL = "Level : " + str(level)
        textSurfaceObj = BASICFONT.render(LEVEL, True, PURPLE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WINDOWWIDTH/2, YMARGIN/2)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        SCORE = "Score : " + str(score)
        textSurfaceObj = BASICFONT.render(SCORE, True, RED)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WINDOWWIDTH/2, WINDOWHEIGHT - 1.4*YMARGIN)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return None
    def check_level(self,level,score,board,MoveDownFrequency):
        # if(score > 30):
        #     level=(level+1)
        #     score=0
        # if level==1:
            # MoveDownFrequency=0.3
            # return level,score,board,MoveDownFrequency
        if level==1 and score > 10000:
            MoveDownFrequency=0.06
            score=0
            level=2
            board=self.get_new_board()
        elif level==2 and score>20000:
            temp=[]
            for i in range(board_width) :
                for j in range(board_height) :
                    temp.append((i,j))
            random.shuffle(temp)
            level=3
            board=self.get_new_board()
            for i in range(10) :
                x,y=temp[i]
                board[x][y]=1
            MoveDownFrequency=0.07
        return level,score,board,MoveDownFrequency

    def update_score(self,row,board,score):
        if row==-1 :
            score = score +10
            return board,score
        score+=110
        for j in range(row,0,-1):
            for i in range(board_width):
                board[i][j]=board[i][j-1]
        for i in range(board_width):
            board[i][0]=0
        return board,score
    def Checkrowfull(self,board):
        for j in range(board_height):
            full=1
            for i in range(board_width):
                if(board[i][j]==0):
                    full=0
                    break
            if(full==1):
                return j+1
        if(full==0):
            return -1
    def board_copy(self,block_type,block_index,centre,board):
        #copy board here
        BOARD=[]
        for i in range(board_width):
            temp=[]
            for j in range(board_height):
                temp.append(board[i][j])
            BOARD.append(temp)
        if block_type == 0 :
            return BOARD
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
        return BOARD
    def leftTopCoordsOfBox(self,boxx, boxy):
        # Convert board coordinates to pixel coordinates
        left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
        top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
        return (left, top)

    def print_board(self,board) :
        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        cur_color=BGCOLOR
        for i in range(board_width) :
            for j in range(board_height) :
                left, top = self.leftTopCoordsOfBox(i,j)
                if board[i][j] == 0 :
                    cur_color=BLUE
                else :
                    cur_color=RED
                pygame.draw.rect(DISPLAYSURF, cur_color, (left, top , BOXSIZE , BOXSIZE ))

    def RUN(self):
        global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        BASICFONT = pygame.font.Font('freesansbold.ttf', 25)
        BIGFONT = pygame.font.Font('freesansbold.ttf', 40)
        pygame.display.set_caption('Building Blocks')
        LastDownTime=time.time()
        MoveDownFrequency=0.3
        block_type=index=0
        centre=(0,0)
        score=0
        level=1
        board=self.get_new_board()
        new_block=0
        while True:
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            board_temp=self.board_copy(block_type,index,centre,board)
            self.print_board(board_temp)
            self.PrintText(score,level)
            # print "block",new_block
            if new_block==0:
                block_type,index,centre=self.add_block()
                valid=self.checkPiecePos(block_type,index,centre,board)
                if valid==false:
                    self.quit_game(score)
                else:
                    new_block=1
                    #self.print_board(board_temp)

            for event in pygame.event.get(QUIT) :
                self.quit_game(score)
            for event in pygame.event.get(KEYUP) :
                if event.key==K_a or event.key==K_LEFT :
                    centre_temp=self.leftmove(centre)
                    if(self.checkPiecePos(block_type,index,centre_temp,board)==true):
                        centre=centre_temp
                elif event.key==K_d or event.key==K_RIGHT:
                    centre_temp=self.rightmove(centre)
                    if(self.checkPiecePos(block_type,index,centre_temp,board)==true):
                        centre=centre_temp
                elif event.key==K_s:
                    block_type,index_temp=self.rotate(block_type,index)
                    if(self.checkPiecePos(block_type,index_temp,centre,board)==true):
                        index=index_temp
                elif event.key == K_SPACE:
                    valid=self.checkPiecePos(block_type,index,centre_temp,board)
                    while valid==true:
                        centre_temp=self.down(centre)
                        valid=self.checkPiecePos(block_type,index,centre_temp,board)
                        centre=centre_temp
                    # print centre,block_type,index
                    if(self.checkPiecePos(block_type,index,centre_temp,board)==true):
                        centre=centre_temp
                    else:
                        t1,t2=centre_temp
                        t2=t2-1
                        centre=t1,t2
                    # break
            if time.time() - LastDownTime > MoveDownFrequency :
                centre_temp=self.down(centre)
                if(self.checkPiecePos(block_type,index,centre_temp,board)==true):
                    centre=centre_temp
                else:
                    self.fillPiecePos(block_type,index,centre,board)
                    new_block=0
                    row_full=self.Checkrowfull(board)
                    # print "row == ",row_full
                    board,score=self.update_score(row_full,board,score)
                    block_type=index=0
                    centre=(0,0)
                LastDownTime=time.time()
                level,score,board,MoveDownFrequency=self.check_level(level,score,board,MoveDownFrequency)
