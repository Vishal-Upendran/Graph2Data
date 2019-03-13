import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

'''
x-values of yax contains the x-location of the y-axis, and y-values of xax
contains the y-location of x-axis. With these values, we must then be able to
tell the coordinates of any given point on the graph by a simple subtraction.
'''
'''
Finding the points:
1. Take median of the x values to obtain the x-shift (of y-axis).
2. Take median of the y values to obtain the y-shift (of x-axis).
3. Since any point has a particular native pixel value, the value must be x
and y subtracted to get the final coordinate.
4. Sanity check: See if origin has (0,0).
'''

#Read image first
image=mpimg.imread("TestCase/Spectrum_id.png")
fig,ax=plt.subplots()
ax.imshow(image)
#Get y values helper
Npts=5

print "How many point approximation do you need for the axes?At least 2 are needed. "
Npts=int(raw_input())
print "Procedure: Decide upon %d points along the x and ya axis. You must select these points and also enter their values next."%(Npts)

print "Click %d consecutive (from bottom to top, preferrably the bottom-most and top-most) marked points along the y-axis for reconstruction."%(Npts)
yax=np.array(plt.ginput(Npts,timeout=0,show_clicks=True))
print "Enter the values of these %d points marked earlier."%(Npts)
lst=raw_input()
y_num = np.asarray(map(float,lst.split()))
y_max=image.shape[1]
print "-----------------------------------"

print "Click %d consecutive (from left to right, preferrably the left most and right most) marked points along the x-axis for reconstruction."%(Npts)
xax=np.array(plt.ginput(Npts,timeout=0,show_clicks=True))
print "Enter the values of these %d points marked earlier."%(Npts)
lst=raw_input()
x_num = np.asarray(map(float,lst.split()))
print "-------------------"
yscale=np.median((y_num[1:]-y_num[:-1])/(yax[1:,1]-yax[:-1,1]))
xscale=np.median((x_num[1:]-x_num[:-1])/(xax[1:,0]-xax[:-1,0]))

#Get the actual values at origin.
xmed=xax[0,0]
ymed=yax[0,1]
x0=x_num[0]
y0=y_num[0]
print "Select the points on the plot for which coordinates are needed."

coordx=[]
coordy=[]
def PutCoords(event):
    xpt=event.xdata
    ypt=event.ydata
    print "--------"
    print "Selected point pixel coordinates: (%0.2f,%0.2f)"%(xpt,ypt)
    xval=(xpt-xmed)*xscale+x0
    yval=(ypt-ymed)*yscale+y0
    coordx.append(xpt)
    coordy.append(ypt)
    plt.scatter(coordx,coordy)
    fig.canvas.draw()
    print "Actual values (x,y)=(%0.2f,%0.2f)"%(xval,yval)
fig.canvas.mpl_connect('button_press_event',PutCoords)
plt.show()
