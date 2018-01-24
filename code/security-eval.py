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

angAa=90
angAb=120

if angAa == 90 or angAa == 270:
  UNDEFINEDCAMAa=1
else:
  UNDEFINEDCAMAa=0
  AaCAMm=math.tan(math.radians(angAa))

if angAb == 90 or angAb == 270:
  UNDEFINEDCAMAb=1
else:
  UNDEFINEDCAMAb=0
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
  if a1[0] <= b1[0]:
    if (a1[0] <= sec[0]) and (b1[0] >= sec[0]):
      t=1
    else:
      t=0
  elif a1[0] >= b1[0]:
    if (a1[0] >= sec[0]) and (b1[0] <= sec[0]):
      t=1
    else:
      t=0
  return t,sec

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
  if a1[0] <= b1[0]:
    if (a1[0] <= sec[0]) and (b1[0] >= sec[0]):
      t=1
    else:
      t=0
  elif a1[0] >= b1[0]:
    if (a1[0] >= sec[0]) and (b1[0] <= sec[0]):
      t=1
    else:
      t=0
  return t,sec
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
  tWACAMAa,secWACAMAa=vertline(AWa,AWb,camAc,camAa1)
else:
  tWACAMAa,secWACAMAa=line(AWa,AWb,AWm,camAc,AaCAMm)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDB == 1:
  tWBCAMAa,secWBCAMAa=vertline(BWa,BWb,camAc,camAa1)
else:
  tWBCAMAa,secWBCAMAa=line(BWa,BWb,BWm,camAc,AaCAMm)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDC == 1:
  tWCCAMAa,secWCCAMAa=vertline(CWa,CWb,camAc,camAa1)
else:
  tWCCAMAa,secWCCAMAa=line(CWa,CWb,CWm,camAc,AaCAMm)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDD == 1:
  tWDCAMAa,secWDCAMAa=vertline(DWa,DWb,camAc,camAa1)
else:
  tWDCAMAa,secWDCAMAa=line(DWa,DWb,DWm,camAc,AaCAMm)
  
if UNDEFINEDCAMAa == 1 or UNDEFINEDE == 1:
  tWECAMAa,secWECAMAa=vertline(EWa,EWb,camAc,camAa1)
else:
  tWECAMAa,secWECAMAa=line(EWa,EWb,EWm,camAc,AaCAMm)
  
#all camAb
if UNDEFINEDCAMAb == 1 or UNDEFINEDA == 1:
  tWACAMAb,secWACAMAb=vertline(AWa,AWb,camAc,camAb1)
else:
  tWACAMAb,secWACAMAb=line(AWa,AWb,AWm,camAc,AbCAMm)
  
if UNDEFINEDCAMAb == 1 or UNDEFINEDB == 1:
  tWBCAMAb,secWBCAMAb=vertline(BWa,BWb,camAc,camAb1)
else:
  tWBCAMAb,secWBCAMAb=line(BWa,BWb,BWm,camAc,AbCAMm)
  
if UNDEFINEDCAMAb == 1 or UNDEFINEDC == 1:
  tWCCAMAb,secWCCAMAb=vertline(CWa,CWb,camAc,camAb1)
else:
  tWCCAMAb,secWCCAMAb=line(CWa,CWb,CWm,camAc,AbCAMm)
  
if UNDEFINEDCAMAb == 1 or UNDEFINEDD == 1:
  tWDCAMAb,secWDCAMAb=vertline(DWa,DWb,camAc,camAb1)
else:
  tWDCAMAb,secWDCAMAb=line(DWa,DWb,DWm,camAc,AbCAMm)
  
if UNDEFINEDCAMAb == 1 or UNDEFINEDE == 1:
  tWECAMAb,secWECAMAb=vertline(EWa,EWb,camAc,camAb1)
else:
  tWECAMAb,secWECAMAb=line(EWa,EWb,EWm,camAc,AbCAMm)

  
#all camBa
if UNDEFINEDCAMBa == 1 or UNDEFINEDA == 1:
  tWACAMBa,secWACAMBa=vertline(AWa,AWb,camBc,camBa1)
else:
  tWACAMBa,secWACAMBa=line(AWa,AWb,AWm,camBc,BaCAMm)
  
if UNDEFINEDCAMBa == 1 or UNDEFINEDB == 1:
  tWBCAMBa,secWBCAMBa=vertline(BWa,BWb,camBc,camBa1)
else:
  tWBCAMBa,secWBCAMBa=line(BWa,BWb,BWm,camBc,BaCAMm)
  
if UNDEFINEDCAMBa == 1 or UNDEFINEDC == 1:
  tWCCAMBa,secWCCAMBa=vertline(CWa,CWb,camBc,camBa1)
else:
  tWCCAMBa,secWCCAMBa=line(CWa,CWb,CWm,camBc,BaCAMm)
  
if UNDEFINEDCAMBa == 1 or UNDEFINEDD == 1:
  tWDCAMBa,secWDCAMBa=vertline(DWa,DWb,camBc,camBa1)
else:
  tWDCAMBa,secWDCAMBa=line(DWa,DWb,DWm,camBc,BaCAMm)
  
if UNDEFINEDCAMBa == 1 or UNDEFINEDE == 1:
  tWECAMBa,secWECAMBa=vertline(EWa,EWb,camBc,camBa1)
else:
  tWECAMBa,secWECAMBa=line(EWa,EWb,EWm,camBc,BaCAMm)
    
#all camBb
if UNDEFINEDCAMBb == 1 or UNDEFINEDA == 1:
  tWACAMBb,secWACAMBb=vertline(AWa,AWb,camBc,camBb1)
else:
  tWACAMBb,secWACAMBb=line(AWa,AWb,AWm,camBc,BbCAMm)
  
if UNDEFINEDCAMBb == 1 or UNDEFINEDB == 1:
  tWBCAMBb,secWBCAMBb=vertline(BWa,BWb,camBc,camBb1)
else:
  tWBCAMBb,secWBCAMBb=line(BWa,BWb,BWm,camBc,BbCAMm)
  
if UNDEFINEDCAMBb == 1 or UNDEFINEDC == 1:
  tWCCAMBb,secWCCAMBb=vertline(CWa,CWb,camBc,camBb1)
else:
  tWCCAMBb,secWCCAMBb=line(CWa,CWb,CWm,camBc,BbCAMm)
  
if UNDEFINEDCAMBb == 1 or UNDEFINEDD == 1:
  tWDCAMBb,secWDCAMBb=vertline(DWa,DWb,camBc,camBb1)
else:
  tWDCAMBb,secWDCAMBb=line(DWa,DWb,DWm,camBc,BbCAMm)
  
if UNDEFINEDCAMBb == 1 or UNDEFINEDE == 1:
  tWECAMBb,secWECAMBb=vertline(EWa,EWb,camBc,camBb1)
else:
  tWECAMBb,secWECAMBb=line(EWa,EWb,EWm,camBc,BbCAMm)
  
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




#walls, doors, and camera locations
draw.line((AWa[0]*100, height-(AWa[1]*100), AWb[0]*100, height-(AWb[1]*100)), width=10, fill="purple")
draw.line((BWa[0]*100, height-(BWa[1]*100), BWb[0]*100, height-(BWb[1]*100)), width=10, fill="purple")
draw.line((CWa[0]*100, height-(CWa[1]*100), CWb[0]*100, height-(CWb[1]*100)), width=10, fill="purple")
draw.line((DWa[0]*100, height-(DWa[1]*100), DWb[0]*100, height-(DWb[1]*100)), width=10, fill="purple")
draw.line((EWa[0]*100, height-(EWa[1]*100), EWb[0]*100, height-(EWb[1]*100)), width=10, fill="purple")

draw.line((a[0]*100, a[1]*100, b[0]*100, b[1]*100), width=20, fill="black")
draw.line((b[0]*100, b[1]*100, c[0]*100, c[1]*100), width=20, fill="black")
draw.line((c[0]*100, c[1]*100, d[0]*100, d[1]*100), width=20, fill="black")
draw.line((d[0]*100, d[1]*100, a[0]*100, a[1]*100), width=20, fill="black")

draw.line((a[0]*100, height-(a[1]*100), (a[0]+2)*100, height-(a[1]*100)), width=40, fill="green")
draw.line((c[0]*100, height-(c[1]*100), (c[0]-2)*100, height-(c[1]*100)), width=40, fill="green")

#CAMAa potentials
if tWACAMAa == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWACAMAa[0]*100, height-(secWACAMAa[1]*100)), width=10, fill="red")

if tWBCAMAa == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWBCAMAa[0]*100, height-(secWBCAMAa[1]*100)), width=10, fill="red")

if tWCCAMAa == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWCCAMAa[0]*100, height-(secWCCAMAa[1]*100)), width=10, fill="red")

if tWDCAMAa == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWDCAMAa[0]*100, height-(secWDCAMAa[1]*100)), width=10, fill="red")

if tWECAMAa == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWECAMAa[0]*100, height-(secWECAMAa[1]*100)), width=10, fill="red")
  
#CAMAb potentials
if tWACAMAb == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWACAMAb[0]*100, height-(secWACAMAb[1]*100)), width=10, fill="red")

if tWBCAMAb == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWBCAMAb[0]*100, height-(secWBCAMAb[1]*100)), width=10, fill="red")

if tWCCAMAb == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWCCAMAb[0]*100, height-(secWCCAMAb[1]*100)), width=10, fill="red")

if tWDCAMAb == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWDCAMAb[0]*100, height-(secWDCAMAb[1]*100)), width=10, fill="red")

if tWECAMAb == 1:
  draw.line((camAc[0]*100, height-(camAc[1]*100),secWECAMAb[0]*100, height-(secWECAMAb[1]*100)), width=10, fill="red")

#CAMBa potentials
if tWACAMBa == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWACAMBa[0]*100, height-(secWACAMBa[1]*100)), width=10, fill="red")

if tWBCAMBa == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWBCAMBa[0]*100, height-(secWBCAMBa[1]*100)), width=10, fill="red")

if tWCCAMBa == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWCCAMBa[0]*100, height-(secWCCAMBa[1]*100)), width=10, fill="red")

if tWDCAMBa == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWDCAMBa[0]*100, height-(secWDCAMBa[1]*100)), width=10, fill="red")

if tWECAMBa == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWECAMBa[0]*100, height-(secWECAMBa[1]*100)), width=10, fill="red")
  
#CAMBa potentials
if tWACAMBb == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWACAMBb[0]*100, height-(secWACAMBb[1]*100)), width=10, fill="red")

if tWBCAMBb == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWBCAMBb[0]*100, height-(secWBCAMBb[1]*100)), width=10, fill="red")

if tWCCAMBb == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWCCAMBb[0]*100, height-(secWCCAMBb[1]*100)), width=10, fill="red")

if tWDCAMBb == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWDCAMBb[0]*100, height-(secWDCAMBb[1]*100)), width=10, fill="red")

if tWECAMBb == 1:
  draw.line((camBc[0]*100, height-(camBc[1]*100),secWECAMBb[0]*100, height-(secWECAMBb[1]*100)), width=10, fill="red")
#image saving and testing
im.show()
