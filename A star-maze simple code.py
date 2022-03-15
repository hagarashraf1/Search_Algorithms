
# A* search algorithm is used to find the shortest path between the source and destination on image that represents a map or a maze.


from pyamaze import maze,agent,textLabel
from queue import PriorityQueue


 # Heuristic function


def h (cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1-x2) + abs(y1-y2)


# A* function


def aStar(m):
    start = (m.rows , m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start] = h( start , (1,2))

    opened = PriorityQueue()
    opened.put(( h(start,(1,2)) , h(start,(1,2)) , start ))
    aPath = {}
    
    while not opened.empty():
        currCell = opened.get()[2]
        if currCell == (1,2):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = ( currCell[0] , currCell[1]+1 )
                if d=='W':
                    childCell = ( currCell[0] , currCell[1]-1 )
                if d=='N':
                    childCell = ( currCell[0]-1 , currCell[1] )
                if d=='S':
                    childCell = ( currCell[0]+1 , currCell[1] )

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell , (1,2) )

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    opened.put(( temp_f_score , h(childCell,(1,2)) , childCell ))
                    aPath[childCell] = currCell
    
    fwdPath = {}
    cell = (1,2)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath


# Executing source code module

if __name__ == '__main__':
    m = maze(20,20)
    m.CreateMaze(1,2, loopPercent=100 , theme="light",pattern='v') 
    path = aStar(m)

    a = agent( m, footprints=True)
    m.tracePath({a:path})
    l = textLabel( m , 'A Star Path Length' , len(path)+1)

    m.run()







# In[5]:


print(m.maze_map)
#print(m.grid)


# In[ ]:




