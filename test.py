from astar_siddhav import astarold
from math import sqrt
from math import exp
import time
import functools
inf = float("inf")
def dotp(x,y):
    z = x[0]*y[0] + x[1]*y[1]
    return z

def sensrad(ghost,obstacles):
    obsvar = []
    for ob in obstacles:
        dist = sqrt((ghost[0][0]-ob[0])**2 + (ghost[0][1]-ob[1])**2)
        if(dist < sens):
            obsvar.append(ob)
    return obsvar


def ttciso(x,agent):
    tr = agent[4] * 2
    tw = [-x[0] + agent[0][0],-x[1] + agent[0][1]]
    c = dotp(tw,tw) - tr*tr
    if (c < 0):
        return(0)
    tv = [agent[1][0],agent[1][1]]
    a = dotp(tv,tv) - epspar**2
    b = dotp(tw,tv) - epspar*tr
    #print("b = %s" %b)
    if (b > 0):
        return(inf)
    discr = b*b - a*c
    if (discr <= 0):
        return(inf)
    tau = c/(-b + sqrt(discr))
    if(tau < 0):
        return(inf)
    return tau

def mg(a):
    return sqrt(a[0]*a[0] + a[1]*a[1])

def computeisoforce(ob,nagent,tc):
    #find relative displacement
    disc = 0
    fce = []
    disp = [nagent[0][0] - ob[0],nagent[0][1]-ob[1]]
    #print("displacement %s" %disp)
    relvel = [nagent[3][0],nagent[3][1]]
    #print("V = %s" %relvel)
    r = mg([disp[0]+relvel[0]*tc,disp[1]+relvel[1]*tc])
    #print("r %s" %r)
    disc = (dotp(disp,relvel) - r*epspar)**2 - ((mg(relvel)**2) - epspar**2)*(mg(disp)**2 - r**2)
    #print("discriminant %s" %disc)
    fce = [(disp[0] + relvel[0]*tc)/sqrt(disc),(disp[1] + relvel[1]*tc)/sqrt(disc)]
    cal = ((kpar*exp(-tc/t0par))/tc**(mpar+1))*(mpar + tc/t0par)
    fce[0] = fce[0]*cal
    fce[1] = fce[1]*cal
    print("fce = %s" %fce)
    return fce

def updatePos(dt):
    #print("entered update sim")
    fg = [(ghost[2][0] - ghost[1][0])/0.5,(ghost[2][1] - ghost[1][1])/0.5]
    #find obstacles within a sensing radius
    obs = sensrad(ghost,obstacles)
    if not ghost[-1]:
        for o in obs:
            tc = ttciso(o,ghost)
            #print("tc = %s"%tc)
            if tc > 0 and tc < 2:
                fce = computeisoforce(o,ghost,tc)
                #print("fce = %s" %fce)
                fg = [fg[0]+fce[0],fg[1],fce[1]]
                #print("fg=%s" %fg)
        force = fg
        if mg(force)>8:
            par = 8/mg(force)
            print("capping to max force")
        force *= par
        global reachedgoal
        reachedgoal = True #this is to find if ghost has caught snake
        ghost[1] = [(ghost[1][0]+force[0])*dt,(ghost[1][1]+force[1])*dt]
        #cap it to max speed
        mg = sqrt(dotp(ghost[1],ghost[1]))
        if mg > ghost[6]:
            ghost[1] = [ghost[6]*ghost[1][0]/mg,ghost[6]*ghost[1][1]/mg]
        #update position
        ghost[0] = [ghost[0][0]+ghost[1][0]*dt,ghost[0][1]+ghost[1][1]*dt]
        print(ghost[0])
        #find goal vel for next step
        gv = [ghost[3][0]-ghost[0][0],ghost[3][1]-ghost[0][1]]
        distToGoal = dotp(gv,gv)
        if(distToGoal < adist):
            ghost[-1] = True
            print("ghost reached goal!")
        else:
            gv = [ghost[5]*gv[0]/sqrt(distToGoal),ghost[5]*gv[1]/sqrt(distToGoal)]
            ghost[2] = gv
            #print(ghost[0])
            reachedgoal = False
'''
pygame.init()
screen = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption('Ghost')
white = 255, 255, 255
black = 20, 20, 40
screen.fill(white)
blue=(0,0,255)
dobs = [[90,45,10,10]]
'''
def ghostPlan(gstart,goal,obstacles):
    #gstart = [5,13]
    dt = 0.1
    #sensing distance
    sens = 2
    #Parameters for force
    kpar = 1.5
    mpar = 2
    t0par = 3
    epspar = 0.2
    radius = 0.5
    prefspeed = 2
    maxspeed = 2.5
    pos = gstart
    vel = [0,0]
    #goal = [5,6] #this will be the current position of the snake
    gvel = [goal[0]-pos[0],goal[1]-pos[1]]
    gvel = [gvel[0]/(sqrt(dotp(gvel,gvel)))*prefspeed,gvel[1]/(sqrt(dotp(gvel,gvel)))*prefspeed]
    reachedgoal = False
    ghost = [pos,vel,gvel,goal,radius,prefspeed,maxspeed,reachedgoal]
    #obstacles = [[5,10]]
    adist = 1
    updatePos(dt)
    return ghost[0]
if __name__ = __main__:
    print("hello")
