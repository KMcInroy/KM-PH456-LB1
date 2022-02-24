#Initialise parameters and arrays
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import Generator,MT19937, PCG64

r=0
R=0
N=500 #Number of Particles initially in LHS of box
i=0
j=0
k=0
p=0.5 #Probability a particle moves to the RHS
prl=1-p #Probability a particle moves to the LHS
TotalTime=5000 #Total time of simulation
xarr=np.array([])
Parr=np.ones(N) #Initial state of all particles
Parr1=np.ones(N) #Initial state of all particles
Parr2=np.ones(N) #Initial state of all particles
NfArr=np.array(N) #Particles in LHS at each timestep
MfArr=np.array(0) #Particles in RHS at each timestep
NfArr1=np.array(N) #Particles in LHS at each timestep
MfArr1=np.array(0) #Particles in RHS at each timestep
NfArr2=np.array(N) #Particles in LHS at each timestep
MfArr2=np.array(0) #Particles in RHS at each timestep
t=np.arange(TotalTime)
MTarr=np.array([])
PCarr=np.array([])
rarr=np.array([])
#Assign a random value for every timestep
while r <= len(t)-2:
    x=np.random.rand()
    xarr=np.append(xarr,x)
    r+=1

#Generating arrays of random numbers by 2 different generators
while R <= 10000:
    MTgen=Generator(MT19937())
    PCgen=Generator(PCG64())
    MT=MTgen.random()
    PC=PCgen.random()
    MTarr=np.append(MTarr,MT)
    PCarr=np.append(PCarr,PC)
    rarr=np.append(rarr,r)
    
    R+=1

while i<=len(t)-2:
    #Pick a random particle
    a=np.random.randint(0,N)
   #use value for timestep probability to determine if particle
   #is moving left (>prl) or right (<prl).
   #If the particle is already on the side that it is told to move to
   #there is no movement in that timestep.
    if xarr[i]>=prl:
        if Parr[a] == 1:
            Parr[a] = 0
        elif Parr[a]==0:
            Parr[a]=0
    if xarr[i]<prl:
        if Parr[a] == 0:
            Parr[a] = 1
        elif Parr[a]==1:
            Parr[a]=1
            
    #Calculate number of particles on each side and record this.
    Nf=sum(Parr)
    Mf=N-sum(Parr)
    NfArr=np.append(NfArr,Nf) 
    MfArr=np.append(MfArr,Mf)
    i+=1

while j<=len(t)-2:
    #Pick a random particle
    b=np.random.randint(0,N)
   #use value for timestep probability to determine if particle
   #is moving left (>prl) or right (<prl).
   #If the particle is already on the side that it is told to move to
   #there is no movement in that timestep.
    if MTarr[j]>=prl:
        if Parr1[b] == 1:
            Parr1[b] = 0
        elif Parr1[b]==0:
            Parr1[b]=0
    if MTarr[j]<prl:
        if Parr1[b] == 0:
            Parr1[b] = 1
        elif Parr1[b]==1:
            Parr1[b]=1
            
    #Calculate number of particles on each side and record this.
    Nf1=sum(Parr1)
    Mf1=N-sum(Parr1)
    NfArr1=np.append(NfArr1,Nf1) 
    MfArr1=np.append(MfArr1,Mf1)
    j+=1

while k<=len(t)-2:
    #Pick a random particle
    c=np.random.randint(0,N)
   #use value for timestep probability to determine if particle
   #is moving left (>prl) or right (<prl).
   #If the particle is already on the side that it is told to move to
   #there is no movement in that timestep.
    if PCarr[k]>=prl:
        if Parr2[c] == 1:
            Parr2[c] = 0
        elif Parr2[c]==0:
            Parr2[c]=0
    if PCarr[k]<prl:
        if Parr2[c] == 0:
            Parr2[c] = 1
        elif Parr2[c]==1:
            Parr2[c]=1
            
    #Calculate number of particles on each side and record this.
    Nf2=sum(Parr2)
    Mf2=N-sum(Parr2)
    NfArr2=np.append(NfArr2,Nf2) 
    MfArr2=np.append(MfArr2,Mf2)
    k+=1
    
#Plot the evolution of the particle number on each side w.r.t time.
plt.plot(t,NfArr,label="LHS")
plt.plot(t,MfArr, label="RHS")
plt.yticks([0,100,200,300,400,500],fontsize="xx-small")
plt.xticks([0,1000,2000,3000,4000,5000], fontsize="xx-small")
plt.legend(loc="best",fontsize="xx-small")
plt.xlabel("Timestep")
plt.ylabel("Number of Particles")
plt.title("Simulation of Gas in Partitioned Box (np.random.rand) p=0.5",
          fontsize="x-small")
plt.show()

plt.plot(t,NfArr1,label="LHS")
plt.plot(t,MfArr1, label="RHS")
plt.yticks([0,100,200,300,400,500],fontsize="xx-small")
plt.xticks([0,1000,2000,3000,4000,5000], fontsize="xx-small")
plt.legend(loc="best",fontsize="xx-small")
plt.xlabel("Timestep")
plt.ylabel("Number of Particles")
plt.title("Simulation of Gas in Partitioned Box (MT19937) p=0.5",
          fontsize="x-small")
plt.show()

plt.plot(t,NfArr2,label="LHS")
plt.plot(t,MfArr2, label="RHS")
plt.yticks([0,100,200,300,400,500],fontsize="xx-small")
plt.xticks([0,1000,2000,3000,4000,5000], fontsize="xx-small")
plt.legend(loc="best",fontsize="xx-small")
plt.xlabel("Timestep")
plt.ylabel("Number of Particles")
plt.title("Simulation of Gas in Partitioned Box (PCG64) p=0.5",
          fontsize="x-small")
plt.show()

