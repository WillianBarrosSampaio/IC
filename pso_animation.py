# -*- coding: utf-8 -*-
"""
Created on Sun May 15 18:49:30 2022

@author: oscar
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:29:57 2021

@author: oscar
"""


import numpy as np
import random as rand
import matplotlib.pyplot as plt
from random import random,seed
import math

import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation, PillowWriter

import matplotlib.animation as animation
from IPython import display



def shubert(x):
    sum1=0
    sum2=0
    
    for i in range(1,6):
        sum1=sum1+i*np.cos((i+1)*x[0]+i)
        sum2=sum2+i*np.cos((i+1)*x[1]+i)

    res=sum1*sum2
    return res


def sphere(x):
  d=x.shape[0]
  sum=0
  for i in range(d):
    sum=sum+x[i]**2
  
  return sum

def rastrigin(x):
  d=x.shape[0]
  sum=0
  for i in range(d):
    sum=sum+x[i]**2-10*np.cos(2*np.pi*x[i])
  
  return 10*d+sum
'''
def Langermann(x):
    
  
  A=np.array([[3,5],[5,2],[2,1],[1,4],[7,9]])
  c=np.array([1,2,5,2,3])
  m=5
  d=x.shape[0]
  
  sum3=0
  for i in range(0,5):
      sum1=0
      for j in range(d):
          sum1=sum1+(x[j]-A[i,j])**2
          
      sum1=np.exp(-sum1/np.pi)
      
      sum2=0
      for j in range(d):
          sum2=sum2+(x[j]-A[i,j])**2     
      sum2=np.cos(np.pi*sum2)
      
      sum3=sum3+c[i]*sum1*sum2
      
  
  return sum3

def holder(x):
  c1=1-((x[0]**2+x[1]**2)**0.5)/np.pi
  c2=np.sin(x[0])*np.cos(x[1])
  c3=c2*np.exp(np.absolute(c1))
  res=-np.absolute(c3)
  return res
'''

num_variables=2
generation=2



#Sphere
x_max=10
x_min=-10

#shubert
x_max=5.12
x_min=-5.12



img = [] # some array of images
frames = [] # for storing the generated images



plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.grid(True)


# create data points
xx = np.linspace(x_min, x_max, 200)
yy = np.linspace(x_min, x_max, 200)
# create grid
x1, x2 = np.meshgrid(xx, yy)

l=[x1,x2]
arr = np.array(l)

z = rastrigin(arr)






it=1

c1=2.05
c2=2.05
ini_v=3

itmax = 100
wmax = 0.9
wmin=0.4
max_v = ini_v/3


w=wmax-it*(wmax-wmin)/itmax


#número de partículas
S=20 
#número de dimensões
d=2
# posição de cada partícula
x=np.zeros((S,d))
# velocidade de cada partícula
v=np.zeros((S,d))
# posição de melhor localização de cada partícula
Pbest=np.zeros((S,d))
# o custo da i-ésima partícula
fitness=np.zeros((S,1))
#O melhor fitness local visitado pela i-ésima partícula
Pbest_fitness=1e10*np.ones([S,1])
    

#Inicialização de x, v e Pbest
for i in range(S):
    for j in range(d):
        x[i,j]=x_min+ (x_max-x_min) * random()
        v[i,j]=ini_v
        
Pbest=np.copy(x)
        




fps = 10 # frame per sec
frn = itmax # frame number of the animation
zarray = np.zeros((S, d, itmax))
mycmap = plt.get_cmap('gist_earth')        
    
    
f=z 
    
#fig1=plt.figure()
#ax1=plt.axes(projection='3d')

#ax1.plot_surface(x1, x2, f,rstride=1,cstride=1,cmap=mycmap,edgecolor='none')
#plt.show()
    


#fig2 = plt.figure()
#ax2 = fig2.add_subplot(111, projection="3d")

#ax2.plot_surface(x1, x2, f, cmap=mycmap, lw=0.5, rstride=1, cstride=1)

#cset = ax2.contourf(x1, x2, f, offset=np.min(f), cmap='RdBu')


#plt.show()

    
    
while(it < itmax):
    #cp=ax.contourf(x1, x2, z, 20, cmap='viridis') 
    
    #Para cada partícula
    for i in range(S):
        #Avalie o fitness da função objetivo
        fitness[i,0]=rastrigin(x[i,:])
        #Encontra o melhor fitness e a posição         
        if fitness[i,0]<Pbest_fitness[i,0]:
            Pbest[i,:]=x[i,:]
            Pbest_fitness[i,0]=fitness[i,0]   
             
    
    #Encontra o melhor fitness da população
    bestfitness=np.amin(Pbest_fitness)
    result = np.where(Pbest_fitness == np.amin(Pbest_fitness))
    p=result[0]
    
    #Posição da melhor partícula
    Gbest=Pbest[p,:]
    
    
    #Para cada partícula
    for j in range(d):
        for i in range(S):      
            #Gera valores aleatórios para dar aleatoridade à busca
            r1=random()
            r2=random()
            
            #Atualiza a nova velocidade          
            v[i,j]=w*v[i,j] + c1*r1*(Pbest[i,j]-x[i,j]) + c2*r2*(Gbest[0,j]-x[i,j])
    
            #Limita a velocidade de cada partícula
            #Estabelecendo valor máximo e mínimo da velocidade
            if math.fabs(v[i,j])>max_v:
                if v[i,j]>0:
                    v[i,j] = max_v
                else:
                    v[i,j] = -max_v
                    
            #Atualiza a nova posição
            x[i,j]=x[i,j] + v[i,j]
            zarray[i,j,it]=x[i,j]
            
            #Limita a posição de cada partícula
            #Estabelecendo valor máximo e mínimo da posição            
            if x[i,j]>x_max:
                x[i,j]=x_max
                zarray[i,j,it]=x_max
 
            if x[i,j]<x_min:
                x[i,j]=x_min   
                zarray[i,j,it]=x_min
            
            
    #Calcula o fator de inercia 
    w=wmax-it*(wmax-wmin)/itmax    
    
    #Incremento da geração
    it=it+1
    
    
    
    print('Generacion: ' + str(it) + ' - - - Gbest: ' +str(Gbest[0,:]) + ' F(x)= '+str(bestfitness))
    
    
    #line1 = ax.plot(x[:,0], x[:,1], 'ro', linewidth=2, markersize=4)
    #line2 = ax.plot(Gbest[0,0],Gbest[0,1], 'o',color='orange', linewidth=2, markersize=4)    
    
    
    #ax.set_xlim(x_min, x_max)
    #ax.set_ylim(x_min, x_max)
   




    #fig.canvas.draw()
    #plt.pause(0.1)
    #ax.clear()
    #ax.grid(True)
    



def update_plot(frame_number, zarray, plot):
    ax.clear()
    cp=ax.contourf(x1, x2, z, 20, cmap=mycmap) 
    line1 = ax.plot(zarray[:,0,frame_number], zarray[:,1,frame_number], 'ro', linewidth=2, markersize=4)
    #line2 = ax.plot(Gbest[0,0],Gbest[0,1], 'o',color='orange', linewidth=2, markersize=4) 
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(x_min, x_max)
    ax.grid(True)
    return line1

cp=ax.contourf(x1, x2, z, 20, cmap=mycmap)   
ani = animation.FuncAnimation(fig, update_plot, frames=100, fargs=(zarray, cp), interval=1,blit = True)    
    



fn = 'plot_surface_animation_funcanimation'
#ani.save(fn+'.mp4',writer='ffmpeg',fps=fps)
#ani.save(fn+'.gif',writer='imagemagick',fps=fps)  

#anim = animation.FuncAnimation(fig, update_plot, frames=2, init_func=None,fargs=(zarray, cp),interval=1, blit=True)
#fig.suptitle('Sine wave plot', fontsize=14)
# converting to an html5 video
#video = anim.to_html5_video()
# embedding for the video
#html = display.HTML(video)
# draw the animation
#display.display(html)
#plt.close()









  
'''
cp=ax.contourf(x1, x2, z, 20, cmap='viridis')
line1 = ax.plot(x[:,0], x[:,1], 'ro', linewidth=2, markersize=4)
line2 = ax.plot(Gbest[0,0],Gbest[0,1], 'o',color='orange', linewidth=2, markersize=4) 
ax.set_xlim(x_min, x_max)
ax.set_ylim(x_min, x_max)
ax.grid(True)
'''
#ani = FuncAnimation(fig, animate, interval=40, blit=True, repeat=True, frames=20) 
#ani.save("TLI.gif", dpi=300, writer=PillowWriter(fps=25))