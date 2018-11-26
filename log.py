from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm,colors
from scipy import linspace, meshgrid, arange, empty, concatenate, newaxis, shape

u = np.linspace(0,10, 1000)
v = np.linspace(0,10, 1000)
w = np.linspace(-10,0, 1000)
x = np.linspace(-10,0, 1000)

xline = 10 * (np.cos(u))
yline = 10 * (np.sin(u))
X,Y=np.meshgrid(u,v)
NX,NY=np.meshgrid(np.linspace(-10,10,1000),np.linspace(-10,10,1000))
XN,YN=np.meshgrid(w,x)
XNN,YNN=np.meshgrid(u,w)
XNNN,YNNN=np.meshgrid(w,u)
zline = np.log(np.sqrt(X**2 + Y**2))
# print(zline)
# zline=np.append(zline,(-1)*zline,axis=0)
# print(zline)
fig = plt.figure()
ax1=fig.add_subplot(1,2,1,projection='3d')
ax2=fig.add_subplot(1,2,2,projection='3d')
# ax=plt.axes()
Z=np.arcsin(Y/np.sqrt(X**2 + Y**2))

color_dimension = np.arcsin(NY/np.sqrt(NX**2+NY**2)) # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
m.set_array([])
fcolors = m.to_rgba(color_dimension)


color_dimension1 = (-1)*Z # change to desired fourth dimension
minn1, maxx1 = color_dimension1.min(), color_dimension1.max()
norm1 = colors.Normalize(minn1, maxx1)
m1 = plt.cm.ScalarMappable(norm=norm1, cmap='jet')
m1.set_array([])
fcolors1 = m1.to_rgba(color_dimension1)

color_dimension2 = zline # change to desired fourth dimension
minn2, maxx2 = color_dimension2.min(), color_dimension2.max()
norm2 = colors.Normalize(minn2, maxx2)
m2 = plt.cm.ScalarMappable(norm=norm2, cmap='jet')
m2.set_array([])
fcolors2 = m2.to_rgba(color_dimension2)

color_dimension3 = (-1)*zline # change to desired fourth dimension
minn3, maxx3 = color_dimension3.min(), color_dimension3.max()
norm3 = colors.Normalize(minn3, maxx3)
m3 = plt.cm.ScalarMappable(norm=norm3, cmap='jet')
m3.set_array([])
fcolors3 = m3.to_rgba(color_dimension3)



surf1=ax1.plot_surface(NX,NY,np.log(np.sqrt(NX**2+NY**2)),facecolors=fcolors,linewidth=0)
# surf2=ax1.plot_surface(X,Y,(-1)*zline,facecolors=fcolors1,linewidth=0)
surf3=ax2.plot_surface(X,Y,Z,cmap='jet',linewidth=0)
surf4=ax2.plot_surface(XNN,YNN,np.arcsin(YNN/np.sqrt(YNN**2 + XNN**2)),cmap='jet',linewidth=0)
surf5=ax2.plot_surface(XN,YN,(-1)*np.arcsin(YN/np.sqrt(YN**2 + XN**2))-np.pi, cmap='jet', linewidth=0)
surf6=ax2.plot_surface(XNNN,YNNN,(-1)*np.arcsin(YNNN/np.sqrt(YNNN**2 + XNNN**2))+np.pi, cmap='jet', linewidth=0)
# surf5=ax2.plot_surface(X,Y,(-1)*Z,facecolors=fcolors3,linewidth=0)1
# fig.colorbar(surf)
# ax.plot3D(xline,yline,zline)
# ax.plot(xline,yline)
plt.show()




