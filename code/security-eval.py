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

angBb=300
angBb=270

camAa=d
camAb=[0,0]
camAc=[0,0]

camBa=b
camBb=[0,0]
cambc=[0,0]

def line(a1, b1, m1, a2, b2, m2):
  int=[0,0]
  int[0]=((m1*a1[0])-a1[1]-(m2*a2[0])+a2[1])/(m1-m2)
  int[1]=(m1*(int[0]-a1[0]))+a1[1]
  if a1[0] >= b1[0]:
    if (b1[0] >= int[0]) and (int[0] >= a1[0]):
      t=true
    else:
      t=false
  elif a1[0] <= b1[0]:
    if (a1[0] >= int[0]) and (int[0] >= b1[0]):
      t=true
    else:
      t=false
  if t == true:
    if a1[1] >= b1[1]:
      if (b1[1] >= int[1]) and (int[1] >= a1[1]):
        t=true
      else:
        t=false
    elif a1[1] <= b1[1]:
      if (a1[1] >= int[1]) and (int[1] >= b1[1]):
        t=true
      else:
        t=false
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
      t=true
    else:
      t=false
  elif a1[0] <= b1[0]:
    if (a1[0] >= int[0]) and (int[0] >= b1[0]):
      t=true
    else:
      t=false
  if t == true:
    if a1[1] >= b1[1]:
      if (b1[1] >= int[1]) and (int[1] >= a1[1]):
        t=true
      else:
        t=false
    elif a1[1] <= b1[1]:
      if (a1[1] >= int[1]) and (int[1] >= b1[1]):
        t=true
      else:
        t=false
  return int,t
#finds the equations and limits for the moving walls
if (AWa[0]-AWb[0]) == 0:
  UNDEFINEDA=true
else:
  AWm=(AWa[1]-AWb[1])/(AWa[0]-AWb[0])

#finds the intersection for camera views


#finds the coverage if the camera view is on the same wall/wall plane


#finds the coverage is the camera view falls upon more than one wall plane


#checks that none of the camera side views lie on the same plane as a wall, and if they do, then includes that coverage


#sums the coverage of all three sides of the camera


#sums the coverage of both cameras


#divides sumative coverage by all surface on which paintings can be hung and multiplies by 100 to give percent

