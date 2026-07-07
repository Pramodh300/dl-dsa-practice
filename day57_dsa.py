#Number of Islands (DFS)
def numIslands(grid):

    rows = len(grid)
    cols = len(grid[0])


    def dfs(r, c):

        # boundary conditions
        if (
            r < 0 or
            c < 0 or
            r >= rows or
            c >= cols or
            grid[r][c] == "0"
        ):
            return


        # mark visited
        grid[r][c] = "0"


        # explore neighbours
        dfs(r + 1, c)   # down
        dfs(r - 1, c)   # up
        dfs(r, c + 1)   # right
        dfs(r, c - 1)   # left



    islands = 0


    for r in range(rows):

        for c in range(cols):

            if grid[r][c] == "1":

                islands += 1

                dfs(r,c)


    return islands



grid = [
 ["1","1","0"],
 ["1","0","0"],
 ["0","0","1"]
]


print(numIslands(grid))



#Rotting Oranges (Multi Source BFS)
from collections import deque


def orangesRotting(grid):


    rows = len(grid)
    cols = len(grid[0])


    queue = deque()


    fresh = 0



    # find rotten oranges

    for r in range(rows):

        for c in range(cols):


            if grid[r][c] == 2:

                queue.append((r,c))


            elif grid[r][c] == 1:

                fresh += 1




    directions = [

        (1,0),
        (-1,0),
        (0,1),
        (0,-1)

    ]



    minutes = 0



    while queue and fresh > 0:



        for i in range(len(queue)):


            r,c = queue.popleft()



            for dr,dc in directions:


                nr = r + dr

                nc = c + dc



                if (
                    nr>=0 and
                    nc>=0 and
                    nr<rows and
                    nc<cols and
                    grid[nr][nc]==1
                ):


                    grid[nr][nc]=2


                    fresh-=1


                    queue.append(
                        (nr,nc)
                    )


        minutes+=1




    if fresh==0:

        return minutes

    else:

        return -1





grid=[

[2,1,1],

[1,1,0],

[0,1,1]

]


print(orangesRotting(grid))



#Course Schedule (Cycle Detection)
def canFinish(numCourses, prerequisites):


    graph = {}


    for i in range(numCourses):

        graph[i]=[]



    for course,pre in prerequisites:

        graph[pre].append(course)



    visited=set()


    path=set()



    def dfs(course):


        if course in path:

            return False



        if course in visited:

            return True




        path.add(course)




        for nextCourse in graph[course]:


            if dfs(nextCourse)==False:

                return False



        path.remove(course)


        visited.add(course)



        return True




    for c in range(numCourses):


        if dfs(c)==False:

            return False



    return True





print(
    canFinish(
        2,
        [[1,0]]
    )
)



#Graph BFS Shortest Path
from collections import deque


def shortestPath(graph,start,target):


    queue=deque()


    queue.append(
        (start,0)
    )


    visited=set()


    visited.add(start)




    while queue:



        node,distance=queue.popleft()



        if node==target:

            return distance




        for neighbor in graph[node]:



            if neighbor not in visited:


                visited.add(neighbor)


                queue.append(

                    (
                    neighbor,
                    distance+1
                    )

                )



    return -1






graph={

0:[1,2],

1:[0,3],

2:[0,3],

3:[1,2]

}



print(
    shortestPath(
        graph,
        0,
        3
    )
)