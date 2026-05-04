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
    square_with_mine_or_num.content.visible = True #invisible trait
    square_with_mine_or_num.flag = flag  # custom attribute flag which can be added on
    square_with_mine_or_num.flag.visible = False # invisible flag
    return square_with_mine_or_num # returns the value of what the squares "secret is"

# Mine Math - How many squares are around it
def initialize_numbers(): # changes -1 with the amount of mines around the given square
    neighbor_mines = 0 # starting value
    for row in range(rows): # kind of like the images that we did we need to go through the grid like this to find the exact distance between the mine and the spot chosen
        for col in range(cols):
            #inner rows and columns
            if row !=0 and row != rows -1 and col !=0 and col != cols -1:  
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
            elif row == 0 and col!=0 and col != cols-1: 
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
            elif row == 8 and col!=0 and col != cols-1: 
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
            elif row == rows-1 and col == cols-1:    
                if isinstance(board[row-1][col].content, Circle):
                   neighbor_mines += 1 
                if isinstance(board[row-1][col-1].content, Circle):
                   neighbor_mines += 1    
                if isinstance(board[row][col-1].content, Circle):
                   neighbor_mines += 1   
            #finish top-right corner                #COME BACK AND FINISH OFF!!!
            elif row ==0 and col == cols -1:
                if isinstance(board[row][col-1].content, Circle):
                    neighbor_mines += 1
                if isinstance(board[row+1][col-1].content, Circle):
                    neighbor_mines += 1
                if isinstance(board[row+1][col].content, Circle): 
                    neighbor_mines += 1
            # finish first column without corners 
            elif col == 0 and row !=0 and row != rows-1:
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
            
            # finish last column withou corners    
            elif col == cols-1 and row!=0 and row!= rows-1:
                if isinstance(board[row-1][col-1].content, Circle):
                    neighbor_mines += 1     
                if isinstance(board[row-1][col].content, Circle):
                    neighbor_mines += 1
                if isinstance(board[row][col-1].content, Circle):
                    neighbor_mines += 1
                if isinstance(board[row+1][col-1].content, Circle):
                    neighbor_mines += 1
                if isinstance(board[row+1][col].content, Circle):
                    neighbor_mines += 1

            board[row][col].content.value = neighbor_mines
            #print(neighbor_mines) 
            neighbor_mines = 0
            
      
    

def onMousePress(mouseX, mouseY, button):
    global first_click # needed it to be explicitly said to python
    global mine_count_label

    for row in range(rows): 
        for col in range(cols): 
            if board[row][col].hits(mouseX,mouseY):
                if (button == 0): # button is 0 means left click 
                    board[row][col].flag.visible = False # each square has an invisible flag so when clicked if double it will reveal
                    if isinstance(board[row][col].content,Circle) == True: # if it is a mine
                        if first_click == True:   #when first click is a mine
                            place_mine()
                            initialize_numbers()
                        else: # case for mine but not first click9
                            board[row][col].content.fill= 'red'  #end the game?
                            board[row][col].content.visible = True
                    else: # No mine there
                        board[row][col].content.visible = True

                else: # right click so button =1
                    first_click = False
                    if board[row][col].flag.visible == False:
                        board[row][col].flag.visible = True
                    else:
                        board[row][col].flag.visible = False
                        if isinstance(board[row][col].content,Circle) == True:
                            board[row][col].content.fill= 'green'  #end the game?
                            mine_count_label.value -=1
                        board[row][col].content.visible = True
                        
                       
def place_mine():
    # USE fisher-yates shuffle (shuffle index len rowxcol and pick first 10 to be mines)
    global number_of_mines
    global flat_list_of_squares
    global mine_count_label

    mine_count = 0 # starts at 0 

    random.shuffle(flat_list_of_squares) # shuffle the list
    first_n_random_values_of_list = flat_list_of_squares[:number_of_mines] # get the first number_of_mines position of numbers random
    first_n_random_values_of_list.sort() # sort the numbers to add the mines in grid order(cause that is the way you will traverse)

    
    for i in range(rows): 
        for j in range(cols):
            if mine_count < number_of_mines:
                random_mine = first_n_random_values_of_list[mine_count] # grabbing mine-count-th mine in that sorted list
            row = random_mine // cols
            column = random_mine % cols
        
            if mine_count < number_of_mines and row == i and j== column: #number of mines
                mine_count +=1 # adds to the mine count
                board[i][j] = draw_square(j* 30+ 70, i*30 + 70, 0) # draw square is the function I defined in the beginning - draws it @ specific coordinate and gives it a # square will have a 0 cause its a mine
            #when no mine
            else:
                board[i][j] = draw_square(j* 30+ 70, i*30 + 70, -1)    # -1 means number so no mine at the spot
    
    Label("Minecount: ",40,20)
    mine_count_label = Label(mine_count, 80,20)
    initialize_numbers() # how you find how many mines are around it and put in the label that was created in 

        
    eventLabel = Label('', 200, 150, size=40)
    buttonsLabel = Label('', 200, 250, size=40)
    

## game settings
size = int(input("How big do you want the minefield to be?[Enter a number between 8-12]: "))
number_of_mines = int(input("How many mines do you want to have?: "))
rows = size
cols = size
flat_list_of_squares = list(range(size * size))
first_click = True # initializing to true if its the first click when the came starts
#  Making the board - LIST OF LISTS!!! 
# for each row there will be a same number of columnts
board = [ ([0] * cols) for row in range(rows) ] 

place_mine()        
                   
cmu_graphics.run()

