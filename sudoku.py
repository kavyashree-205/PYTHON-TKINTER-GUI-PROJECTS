from tkinter import *

root=Tk()
root.geometry("700x800")
root.title("Sudoku Solver")
root.configure(bg="#344861")
grid=[]

def possible(row,col,num):
    for ele in range(9):
        if grid[row][ele]==num:
            return False
        if grid[ele][col]==num:
            return False
    row1=(row//3)*3
    col1=(col//3)*3
    for ele1 in range(row1,(row1+3)):
        for ele2 in range(col1,(col1+3)):
            if grid[ele1][ele2]==num:
                return False
    return True

def solve_puzzle(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                for num in range(1,10):
                    if possible(row,col,num):
                        grid[row][col]=num
                        solve_puzzle(grid)
                        grid[row][col]=0       
                return
    for r in range(9):
        for c in range(9):
            d=box[r][c].get()
            if d=="":
                e=str(grid[r][c])
                box[r][c].insert(END,e)
 
def gather():
    for i in range(9):
        row=[]
        for j in range(9):
            val=box[i][j].get()
            if val == "":
                val="0"
            row.append(int(val))
        grid.append(row)
    solve_puzzle(grid)
    
heading=Label(root,text="Sudoku Solver",font=("COMIC SANS MS",30),padx=217,pady=4,bg="#344861",fg="#F3F6FA").grid(row=0,column=0)
main_frame=LabelFrame(root,bd=10,relief=GROOVE,bg="#344861")
main_frame.place(x=90,y=75)
box=[["0" for x in range(9)] for y in range(9)]
for i in range(9):
    for j in range(9):
        box[i][j]=Entry(main_frame,width=2,font=("COMIC SANS MS",33),bg="#F3F6FA",fg="#344861")
        box[i][j].grid(row=i,column=j)    
solve=Button(root,text="Solve",width=10,font=("COMIC SANS MS",18),command=lambda:gather(),bg="#F3F6FA",fg="#344861",activebackground="#F3F6FA")
solve.place(x=280,y=700)
  
root.mainloop()

