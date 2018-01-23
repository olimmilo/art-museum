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
camAb=[0,0]
camAc=d
camAa1=[(math.cos(math.radians(angAa))*0.5),(math.sin(math.radians(angAa))*0.5)]
camAb1=[(math.cos(math.radians(angAb))*0.5),(math.sin(math.radians(angAb))*0.5)]

camBa=[0,0]
camBb=[0,0]
cambc=b
camBa1=[(math.cos(math.radians(angBa))*0.5),(math.sin(math.radians(angBa))*0.5)]
camBb1=[(math.cos(math.radians(angBb))*0.5),(math.sin(math.radians(angBb))*0.5)]

#finds where the two lines intersect and if it falls within the first line
def line(a1, b1, m1, a2, m2):
  sec=[0,0]
  sec[0]=((m1*a1[0])-a1[1]-(m2*a2[0])+a2[1])/(m1-m2)
  sec[1]=(m1*(int[0]-a1[0]))+a1[1]
  if a1[0] >= b1[0]:
    if (b1[0] >= sec[0]) and (sec[0] >= a1[0]):
      t=1
    else:
      t=0
  elif a1[0] <= b1[0]:
    if (a1[0] >= sec[0]) and (sec[0] >= b1[0]):
      t=1
    else:
      t=0
  if t == 1:
    if a1[1] >= b1[1]:
      if (b1[1] >= sec[1]) and (sec[1] >= a1[1]):
        t=1
      else:
        t=0
    elif a1[1] <= b1[1]:
      if (a1[1] >= sec[1]) and (sec[1] >= b1[1]):
        t=1
      else:
        t=0
  return sec,t

#finds where the two lines (one verticle) intersect, and if it fals within the first one
def vertline(a1, b1, a2, b2):
  if (a1[0]-b1[0]) == 0:
    sec=[a1[0],0]
    m=(a2[1]-b2[1])/(a2[0]-b2[0])
    sec[1]=(m*(a1[0]-a2[0]))+a2[1]
  else:
    sec=[a2[0],0]
    m=(a1[1]-b1[1])/(a1[0]-b1[0])
    sec[1]=(m*(a2[0]-a1[0]))+a1[1]
  if a1[0] >= b1[0]:
    if (b1[0] >= sec[0]) and (sec[0] >= a1[0]):
      t=1
    else:
      t=0
  elif a1[0] <= b1[0]:
    if (a1[0] >= sec[0]) and (sec[0] >= b1[0]):
      t=1
    else:
      t=0
  if t == 1:
    if a1[1] >= b1[1]:
      if (b1[1] >= sec[1]) and (sec[1] >= a1[1]):
        t=1
      else:
        t=0
    elif a1[1] <= b1[1]:
      if (a1[1] >= sec[1]) and (sec[1] >= b1[1]):
        t=1
      else:
        t=0
  return sec,t
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
#all camAa
if UNDEFINEDCAMAa == 1 or UNDEFINEDA == 1:
  tWACAMA,intWACAMA=vertline(AWa,AWb,camAa,camAa1)
else:
  tWACAMA,intWACAMA=line(AWa,AWb,AWm,camAa,camAa1)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDB == 1:
  tWBCAMA,intWBCAMA=vertline(BWa,BWb,camAa,camAa1)
else:
  tWBCAMA,intWBCAMA=line(BWa,BWb,BWm,camAa,camAa1)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDC == 1:
  tWCCAMA,intWCCAMA=vertline(CWa,CWb,camAa,camAa1)
else:
  tWCCAMA,intWCCAMA=line(CWa,CWb,CWm,camAa,camAa1)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDD == 1:
  tWDCAMA,intWDCAMA=vertline(DWa,DWb,camAa,camAa1)
else:
  tWDCAMA,intWDCAMA=line(DWa,DWb,DWm,camAa,camAa1)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDE == 1:
  tWECAMA,intWECAMA=vertline(EWa,EWb,camAa,camAa1)
else:
  tWECAMA,intWECAMA=line(EWa,EWb,EWm,camAa,camAa1)
  
  
#all camAb  

  
  
#all camBa  

  
  
#all camBb  

  
#finds the coverage if the camera view is on the same wall/wall plane


#finds the coverage is the camera view falls upon more than one wall plane


#checks that none of the camera side views lie on the same plane as a wall, and if they do, then includes that coverage


#sums the coverage of all three sides of the camera


#sums the coverage of both cameras


#divides sumative coverage by all surface on which paintings can be hung and multiplies by 100 to give percent

