import math
from PIL import Image, ImageDraw

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

width=(c[0]-a[0])*100
height=(c[1]-a[1])*100

im = Image.new("RGB", (width,height), "white")
draw = ImageDraw.Draw(im)

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
camAa1=[(math.cos(math.radians(angAa))*0.5)+22,(math.sin(math.radians(angAa))*0.5)]
camAb1=[(math.cos(math.radians(angAb))*0.5)+22,(math.sin(math.radians(angAb))*0.5)]

camBa=[0,0]
camBb=[0,0]
cambc=b
camBa1=[(math.cos(math.radians(angBa))*0.5),(math.sin(math.radians(angBa))*0.5)+20]
camBb1=[(math.cos(math.radians(angBb))*0.5),(math.sin(math.radians(angBb))*0.5)+20]

#finds where the two lines intersect and if it falls within the first line
def line(a1, b1, m1, a2, m2):
  sec=[0,0]
  sec[0]=((m1*a1[0])-(m2*a2[0])+a2[1]-(a1[0]))/(m1-m2)
  sec[1]=(m1*(sec[0]-a1[0]))+a1[1]
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
  tWACAMA,intWACAMA=vertline(AWa,AWb,camAc,camAa1)
else:
  tWACAMA,intWACAMA=line(AWa,AWb,AWm,camAc,AaCAMm)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDB == 1:
  tWBCAMA,intWBCAMA=vertline(BWa,BWb,camAc,camAa1)
else:
  tWBCAMA,intWBCAMA=line(BWa,BWb,BWm,camAc,AaCAMm)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDC == 1:
  tWCCAMA,intWCCAMA=vertline(CWa,CWb,camAc,camAa1)
else:
  tWCCAMA,intWCCAMA=line(CWa,CWb,CWm,camAc,AaCAMm)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDD == 1:
  tWDCAMA,intWDCAMA=vertline(DWa,DWb,camAc,camAa1)
else:
  tWDCAMA,intWDCAMA=line(DWa,DWb,DWm,camAc,AaCAMm)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDE == 1:
  tWECAMA,intWECAMA=vertline(EWa,EWb,camAc,camAa1)
else:
  tWECAMA,intWECAMA=line(EWa,EWb,EWm,camAc,AaCAMm)
  
  
#all camAb  

  
  
#all camBa  

  
  
#all camBb  

  
#finds the coverage if the camera view is on the same wall/wall plane


#finds the coverage is the camera view falls upon more than one wall plane


#checks that none of the camera side views lie on the same plane as a wall, and if they do, then includes that coverage


#sums the coverage of all three sides of the camera


#sums the coverage of both cameras


#divides sumative coverage by all surface on which paintings can be hung and multiplies by 100 to give percent



#image manipulation

#walls and doors
draw.line((a[0]*100, a[1]*100, b[0]*100, b[1]*100), width=10, fill="black")
draw.line((b[0]*100, b[1]*100, c[0]*100, c[1]*100), width=10, fill="black")
draw.line((c[0]*100, c[1]*100, d[0]*100, d[1]*100), width=10, fill="black")
draw.line((d[0]*100, d[1]*100, a[0]*100, a[1]*100), width=10, fill="black")

draw.line((AWa[0]*100, height-(AWa[1]*100), AWb[0]*100, height-(AWb[1]*100)), width=10, fill="green")
draw.line((BWa[0]*100, height-(BWa[1]*100), BWb[0]*100, height-(BWb[1]*100)), width=10, fill="green")
draw.line((CWa[0]*100, height-(CWa[1]*100), CWb[0]*100, height-(CWb[1]*100)), width=10, fill="green")
draw.line((DWa[0]*100, height-(DWa[1]*100), DWb[0]*100, height-(DWb[1]*100)), width=10, fill="green")
draw.line((EWa[0]*100, height-(EWa[1]*100), EWb[0]*100, height-(EWb[1]*100)), width=10, fill="green")




im.show()
