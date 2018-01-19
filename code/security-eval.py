import math

a=[0,0]
b=[0,20]
c=[22,20]
d=[22,0]
AWa=[0,14]
AWb=[5,14]
BWa=[5,14]
BWb=[10,14]
CWa=[7,6]
CWb=[12,6]
DWa=[12,6]
DWb=[17,6]
EWa=[17,6]
EWb=[22,6]

angAa=120
angAb=90

if angAa == 90 or angAa == 270:
  UNDEFINEDCAMAa=1
else:
  UNDEFINEDCAMAa=0
  AaCAMm=math.tan(math.radians(angAa))

if angAb == 90 or angAb == 270:
  UNDEFINEDCAMBb=1
else:
  UNDEFINEDCAMBb=0
  AbCAMm=math.tan(math.radians(angAb))

angBa=300
angBb=270


if angBa == 90 or angBa == 270:
  UNDEFINEDCAMBa=1
else:
  UNDEFINEDCAMBa=0
  BaCAMm=math.tan(math.radians(angBa))

if angBb == 90 or angBb == 270:
  UNDEFINEDCAMBb=1
else:
  UNDEFINEDCAMBb=0
  BbCAMm=math.tan(math.radians(angBb))


camAa=[0,0]

if UNDEFINEDCAMAa == 1:
  camAa1=[d[0], 0.5]
else:
  camAa1=[(d[0]+math.sin(math.radians(angAa))),(d[1]+math.sin(math.radians(angAa)))]
camAb=[0,0]

if UNDEFINEDCAMBb == 1:
  camAb1=[d[0], 0.5]
else:
  camAb1=[(d[0]+math.sin(math.radians(angAb))),(d[1]+math.sin(math.radians(angAb)))]

camAc=d

camBa=[0,0]

if UNDEFINEDCAMBa == 1:
  camAa1=[b[0], 19.5]
else:
  camAa1=[(b[0]+math.sin(math.radians(angBa))),(b[1]+math.sin(math.radians(angBa)))]

camBb=[0,0]

if UNDEFINEDCAMBb == 1:
  camAa1=[b[0], 19.5]
else:
  camAa1=[(b[0]+math.sin(math.radians(angBb))),(b[1]+math.sin(math.radians(angBb)))]

cambc=b

def line(a1, b1, m1, a2, b2, m2):
  int=[0,0]
  int[0]=((m1*a1[0])-a1[1]-(m2*a2[0])+a2[1])/(m1-m2)
  int[1]=(m1*(int[0]-a1[0]))+a1[1]
  if a1[0] >= b1[0]:
    if (b1[0] >= int[0]) and (int[0] >= a1[0]):
      t=1
    else:
      t=0
  elif a1[0] <= b1[0]:
    if (a1[0] >= int[0]) and (int[0] >= b1[0]):
      t=1
    else:
      t=0
  if t == 1:
    if a1[1] >= b1[1]:
      if (b1[1] >= int[1]) and (int[1] >= a1[1]):
        t=1
      else:
        t=0
    elif a1[1] <= b1[1]:
      if (a1[1] >= int[1]) and (int[1] >= b1[1]):
        t=1
      else:
        t=0
  return int,t

def vertline(a1, b1, a2, b2):
  if (a1[0]-b1[0]) == 0:
    int=[a1[0],0]
    m=(a2[1]-b2[1])/(a2[0]-b2[0])
    int[1]=(m*(a1[0]-a2[0]))+a2[1]
  else:
    int=[a2[0],0]
    m=(a1[1]-b1[1])/(a1[0]-b1[0])
    int[1]=(m*(a2[0]-a1[0]))+a1[1]
  if a1[0] >= b1[0]:
    if (b1[0] >= int[0]) and (int[0] >= a1[0]):
      t=1
    else:
      t=0
  elif a1[0] <= b1[0]:
    if (a1[0] >= int[0]) and (int[0] >= b1[0]):
      t=1
    else:
      t=0
  if t == 1:
    if a1[1] >= b1[1]:
      if (b1[1] >= int[1]) and (int[1] >= a1[1]):
        t=1
      else:
        t=0
    elif a1[1] <= b1[1]:
      if (a1[1] >= int[1]) and (int[1] >= b1[1]):
        t=1
      else:
        t=0
  return int,t
#finds the equations and limits for the moving walls
if (AWa[0]-AWb[0]) == 0:
  UNDEFINEDA=1
else:
  UNDEFINEDA=0
  AWm=(AWa[1]-AWb[1])/(AWa[0]-AWb[0])

if (BWa[0]-BWb[0]) == 0:
  UNDEFINEDC=1
else:
  UNDEFINEDB=0
  BWm=(BWa[1]-BWb[1])/(BWa[0]-BWb[0])

if (CWa[0]-CWb[0]) == 0:
  UNDEFINEDC=1
else:
  UNDEFINEDC=0
  CWm=(CWa[1]-CWb[1])/(CWa[0]-CWb[0])

if (DWa[0]-DWb[0]) == 0:
  UNDEFINEDD=1
else:
  UNDEFINEDD=0
  DWm=(DWa[1]-DWb[1])/(DWa[0]-DWb[0])
  
if (EWa[0]-EWb[0]) == 0:
  UNDEFINEDE=1
else:
  UNDEFINEDE=0
  EWm=(EWa[1]-EWb[1])/(EWa[0]-EWb[0])
#finds the intersection for camera views
if UNDEFINEDA == 0 or UNDEFINEDCAMAa == 1:
  intCAMAaA,tCAMAaA=vertline(AWa,AWb,camAc,camAa1)
else:
  intCAMAaA,tCAMAaA=line(AWa,AWb,AWm,camAc,AaCAMm)

#finds the coverage if the camera view is on the same wall/wall plane
print(camAa1,tCAMAaA,intCAMaA)

#finds the coverage is the camera view falls upon more than one wall plane


#checks that none of the camera side views lie on the same plane as a wall, and if they do, then includes that coverage


#sums the coverage of all three sides of the camera


#sums the coverage of both cameras


#divides sumative coverage by all surface on which paintings can be hung and multiplies by 100 to give percent

