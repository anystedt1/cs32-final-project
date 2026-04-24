from cmu_graphics import * # helps me actually makes the shapes
import random # need to randomly place the mines
### Your code goes here; if it contains a call to
### runApp(), use the "CPCS Mode" starter code instead.

# think about the matrix of the game a list of lists

def draw_square(x, y, number): # make a bunch of squares
    
    square = Rect(x, y,25,25, fill = 'blue') # square specs
  
    if number == -1: # creating labels (remember -1 or mine)
       num_or_mine = Label(number,square.centerX, square.centerY, fill="white", bold=True) # make text white for number away essentially
    
    else:
        num_or_mine = Circle(square.centerX,square.centerY,5, fill='red')
    flag = Polygon(square.centerX-5,square.centerY-5,square.centerX+7,square.centerY-2, square.centerX-5,square.centerY+5, fill='yellow') # if there is no number then its either a mine or you can double click for a flag
    
    square_with_mine_or_num = Group (
            square,
            num_or_mine,
            flag
    )   
    square_with_mine_or_num.content = num_or_mine  # custom attribute content
    square_with_mine_or_num.content.visible = False
    square_with_mine_or_num.flag = flag  # custom attribute flag which can be added on
    square_with_mine_or_num.flag.visible = False # invisible flag
    return square_with_mine_or_num # returns the value of what the squares "secret is"

# Mine Math - How many squares are around it
def initialize_numbers(): # changes -1 with the amount of mines around the given square
    neighbor_mines = 0 # starting value
    for row in range(rows): # kind of like the images that we did we need to go through the grid like this to find the exact distance between the mine and the spot chosen
        for col in range(cols):
            #inner rows and columns
            if row !=0 and row !=8 and col !=0 and col !=8:  
                if isinstance(board[row-1][col-1].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row-1][col].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row-1][col+1].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row][col+1].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row+1][col+1].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row+1][col].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row+1][col-1].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row][col-1].content, Circle):
                    neighbor_mines += 1

                #top-left corner    
            elif row == 0 and col==0: 
                if isinstance(board[row][col+1].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row+1][col+1].content, Circle):
                   neighbor_mines += 1    
                if isinstance(board[row+1][col].content, Circle):
                   neighbor_mines += 1 
            #firts row without the corners
            elif row == 0 and col!=0 and col <8: 
                if isinstance(board[row][col+1].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row+1][col+1].content, Circle):
                   neighbor_mines += 1    
                if isinstance(board[row+1][col].content, Circle):
                   neighbor_mines += 1  
                if isinstance(board[row+1][col-1].content, Circle):
                   neighbor_mines += 1  
                if isinstance(board[row][col-1].content, Circle):
                   neighbor_mines += 1    
            #bottom-left corner       
            elif row == 8 and col == 0:    
                if isinstance(board[row-1][col].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row-1][col+1].content, Circle):
                   neighbor_mines += 1    
                if isinstance(board[row][col+1].content, Circle):
                   neighbor_mines += 1         
            #last row without the corners
            elif row == 8 and col!=0 and col <8: 
                if isinstance(board[row][col-1].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row-1][col-1].content, Circle):
                   neighbor_mines += 1    
                if isinstance(board[row-1][col].content, Circle):
                   neighbor_mines += 1  
                if isinstance(board[row-1][col+1].content, Circle):
                   neighbor_mines += 1  
                if isinstance(board[row][col+1].content, Circle):
                   neighbor_mines += 1 
            #bottom-right corner   
            elif row == 8 and col == 8:    
                if isinstance(board[row-1][col].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row-1][col-1].content, Circle):
                   neighbor_mines += 1    
                if isinstance(board[row][col-1].content, Circle):
                   neighbor_mines += 1   
            #finish top-right corner                #COME BACK AND FINISH OFF!!!
            # finish first column without corners 
            # finish last column withou corners    

            board[row][col].content.value = neighbor_mines
            print(neighbor_mines) 
            neighbor_mines = 0
            
      

rows = 9
cols = 9
#  Making the board - LIST OF LISTS!!! 
# for each row there will be a same number of columnts
board = [ ([0] * cols) for row in range(rows) ] 

mine_count = 0 # starts at 0 cause need to randomly pla
for i in range(rows):
    for j in range(cols):
        random_mine = random.randint(0,4) # placing the mines when randomly generates a 0 it will put a mine on the map
        if random_mine == 0 and mine_count<10: # 10 mines
            mine_count +=1 # adds to the mine count
            board[i][j] = draw_square(j* 30+ 70, i*30 + 70, 0) # draw square is the function I defined in the beginning - draws it @ specific coordinate and gives it a # square will have a 0 cause its a mine
        #when no mine
        else:
            board[i][j] = draw_square(j* 30+ 70, i*30 + 70, -1)    # -1 means number so no mine at the spot
Label("Minecount: ",40,30)
mine_count_label = Label(mine_count, 80,30)
initialize_numbers() # how you find how many mines are around it and put in the label that was created in 

     
eventLabel = Label('', 200, 150, size=40)
buttonsLabel = Label('', 200, 250, size=40)



    
# PLAYING Mouse clickes
def onMousePress(mouseX, mouseY, button):
    for row in range(rows): 
        for col in range(cols): 
            if board[row][col].hits(mouseX,mouseY):
                if (button == 0): # button is 0 means left click 
                    board[row][col].flag.visible = False # each square has an invisible flag so when clicked if double it will reveal
                    if isinstance(board[row][col].content,Circle) == True:
                        
                        board[row][col].content.fill= 'red'  #end the game?
                        board[row][col].content.visible = True
                    else: # button is 1 will be right click
                        board[row][col].content.visible = True

                else:
                    if board[row][col].flag.visible == False:
                        board[row][col].flag.visible = True
                    else:
                        board[row][col].flag.visible = False
                        if isinstance(board[row][col].content,Circle) == True:
                            board[row][col].content.fill= 'green'  #end the game?
                            mine_count_label.value -=1
                        board[row][col].content.visible = True
                        
                       
                     
                   
cmu_graphics.run() # make it good

