from astar_siddhav import astar
from math import sqrt
from math import exp
grid = [[0 for x in range(20)] for y in range(20)]
#heuristic = [[0 for x in range(20)] for y in range(20)]
obs = [[2,2,2,3],[7,9,3,2],[4,4,3,3],[18,7,2,1]] #[x,y,r,c]
gstart = [6,16] #there is a function to calculate this in the astar_siddhav.py code but not being used currently
#currently only a set value is  being used for ghost. Its position can also  be passed as a parameter in the function
start = [4, 3, 2] #[grid row, grid col, direction]
goal = [6, 18]
points,plan = astar(start,grid,obs,goal)
print("Printing from test file")
for pr in range(len(plan)):
    print(plan[pr])
print(points)
#adding code for ghost
'''
#sensing distance
sens = 3
#Parameters for force
kpar = 1.5
mpar = 2
t0par = 3
epspar = 0
pos = gstart
vel = [0,0]
goal = [5,6] #this will be the current position of the snake
gvel = goal-pos
gvel = gvel/(sqrt(gvel.dot(gvel)))*prefspeed
ghost = [pos,vel,gvel,goal,radius,prefspeed,maxspeed]'''
