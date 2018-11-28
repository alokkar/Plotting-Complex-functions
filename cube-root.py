from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm,colors
from scipy import linspace, meshgrid, arange, empty, concatenate, newaxis, shape

u = np.linspace(-10,10, 1000)
v = np.linspace(-10,10, 1000)

xline = 10 * (np.cos(u))
yline = 10 * (np.sin(u))
X,Y=np.meshgrid(u,v)
mod=np.sqrt(X**2+Y**2)
theta=np.arccos(X/np.sqrt(X**2+Y**2))
zline1 = mod*np.cos(theta/3)
zline2 = mod*np.cos((theta+2*np.pi)/3)
zline3 = mod*np.cos((theta+4*np.pi)/3)
# print(zline)
# zline=np.append(zline,(-1)*zline,axis=0)
# print(zline)
fig = plt.figure()
ax1=fig.add_subplot(1,1,1,projection='3d')
# ax2=fig.add_subplot(1,2,2,projection='3d')
# ax=plt.axes()
Z1 = mod*np.sin((theta)/3)
Z2 = mod*np.sin((theta+2*np.pi)/3)
Z3 = mod*np.sin((theta+4*np.pi)/3)

color_dimension = Z1 # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
m.set_array([])
fcolors = m.to_rgba(color_dimension)


color_dimension1 = Z2 # change to desired fourth dimension
minn1, maxx1 = color_dimension1.min(), color_dimension1.max()
norm1 = colors.Normalize(minn1, maxx1)
m1 = plt.cm.ScalarMappable(norm=norm1, cmap='jet')
m1.set_array([])
fcolors1 = m1.to_rgba(color_dimension1)

color_dimension2 = Z3 # change to desired fourth dimension
minn2, maxx2 = color_dimension2.min(), color_dimension2.max()
norm2 = colors.Normalize(minn2, maxx2)
m2 = plt.cm.ScalarMappable(norm=norm2, cmap='jet')
m2.set_array([])
fcolors2 = m2.to_rgba(color_dimension2)

color_dimension3 = zline1 # change to desired fourth dimension
minn3, maxx3 = color_dimension3.min(), color_dimension3.max()
norm3 = colors.Normalize(minn3, maxx3)
m3 = plt.cm.ScalarMappable(norm=norm3, cmap='jet')
m3.set_array([])
fcolors3 = m1.to_rgba(color_dimension3)

color_dimension4 = zline2 # change to desired fourth dimension
minn4, maxx4 = color_dimension4.min(), color_dimension4.max()
norm4 = colors.Normalize(minn4, maxx4)
m4 = plt.cm.ScalarMappable(norm=norm4, cmap='jet')
m4.set_array([])
fcolors4 = m4.to_rgba(color_dimension4)

color_dimension5 = zline3 # change to desired fourth dimension
minn5, maxx5 = color_dimension5.min(), color_dimension5.max()
norm5 = colors.Normalize(minn5, maxx5)
m5 = plt.cm.ScalarMappable(norm=norm5, cmap='jet')
m5.set_array([])
fcolors5 = m5.to_rgba(color_dimension5)



surf1=ax1.plot_surface(X,Y,zline1,facecolors=fcolors,linewidth=0)
surf2=ax1.plot_surface(X,Y,zline2,facecolors=fcolors1,linewidth=0)
surf3=ax1.plot_surface(X,Y,zline3,facecolors=fcolors2,linewidth=0)
# surf4=ax2.plot_surface(X,Y,Z1,facecolors=fcolors3,linewidth=0)
# surf5=ax2.plot_surface(X,Y,Z2,facecolors=fcolors4,linewidth=0)
# surf6=ax2.plot_surface(X,Y,Z3,facecolors=fcolors5,linewidth=0)
# fig.colorbar(surf)
# ax.plot3D(xline,yline,zline)
# ax.plot(xline,yline)
plt.show()

