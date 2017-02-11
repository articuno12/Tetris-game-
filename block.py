
import random
block1=[[(0,0),(0,1),(0,2),(0,3)],
        [(0,0),(1,0),(2,0),(3,0)]]
block2=[[(0,0),(0,1),(-1,0),(-1,1)]]
block3=[ [(0,0),(-1,0),(1,0),(0,-1)],
         [(0,0),(1,0),(0,-1),(0,1)] ,
         [(0,0),(1,0),(-1,0),(0,1)] ,
         [(0,0),(0,-1),(0,1),(-1,0)] ]
# Block type 4
block4=[ [(0,0),(1,0),(2,0),(0,-1)],
         [(0,0),(1,0),(0,-1),(0,-2)],
         [(0,0),(0,1),(-1,0),(-2,0)],
         [(0,0),(0,-1),(0,-2),(-1,0)] ]

class block:
    def new_blocktype(self):
        temp=[(1,0),(1,1),(2,0),(3,0),(3,1),(3,2),(3,3),(4,0),(4,1),(4,2),(4,3)] #it stores block type and index
        random.shuffle(temp)
        temp2=temp[0]
        x,y=temp2
        BLOCK=[]
        if x==1:
            BLOCK=block1[y]
        if x==2:
            BLOCK=block2[y]
        if x==3:
            BLOCK=block3[y]
        if x==4:
            BLOCK=block4[y]
        return BLOCK,x,y

    def cal_margin(self,BLOCK):
        ymin=5
        xmin=xmax=5
        #print "current Block is",BLOCK
        for point in BLOCK :
            x,y=point
            xmin=min(x,xmin)
            xmax=max(x,xmax)
            ymin=min(y,ymin)

        xmin=abs(xmin)
        ymin=abs(ymin)
        point=(xmin,ymin,xmax)
        return point

    def add_block(self):
        BLOCK,block_type,index=self.new_blocktype()
        a,b,c=self.cal_margin(BLOCK)
        temp3=[i for i in range(a,29-c)]
        random.shuffle(temp3)
        x=temp3[0]
        centre=x,b
        return block_type,index,centre

    def rotate(self,block_type,block_index):
        if block_type==1:
            block_index=(block_index+1)%len(block1)
        elif block_type==2:
            block_index=(block_index+1)%len(block2)
        elif block_type==3:
            block_index=(block_index+1)%len(block3)
        elif block_type==4:
            block_index=(block_index+1)%len(block4)
        return block_type,block_index

    def rightmove(self,centre):
        x,y=centre
        x=x+1
        centre=x,y
        return centre

    def leftmove(self,centre):
        x,y=centre
        x=x-1
        centre=x,y
        return centre

    def down(self,centre):
        x,y=centre
        y=y+1
        centre=x,y
        return centre
