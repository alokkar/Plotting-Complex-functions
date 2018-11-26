from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm,colors
from scipy import linspace, meshgrid, arange, empty, concatenate, newaxis, shape

u = np.linspace(-5,5, 1000)
v = np.linspace(-5,5, 1000)

xline = 10 * (np.cos(u))
yline = 10 * (np.sin(u))
X,Y=np.meshgrid(u,v)
zline = np.sin(2*X)/(np.cos(2*X)+np.cosh(2*Y))
# print(zline)
# zline=np.append(zline,(-1)*zline,axis=0)
# print(zline)
fig = plt.figure()
ax1=fig.add_subplot(1,2,1,projection='3d')
ax2=fig.add_subplot(1,2,2,projection='3d')
# ax=plt.axes()
Z=np.sinh(2*Y)/(np.cos(2*X)+np.cosh(2*Y))


color_dimension = Z # change to desired fourth dimension
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



surf1=ax1.plot_surface(X,Y,zline,facecolors=fcolors,linewidth=0)
# surf2=ax1.plot_surface(X,Y,(-1)*zline,facecolors=fcolors1,linewidth=0)
surf3=ax2.plot_surface(X,Y,Z,facecolors=fcolors2,linewidth=0)
# surf4=ax2.plot_surface(X,Y,(-1)*Z,facecolors=fcolors3,linewidth=0)
# fig.colorbar(surf)
# ax.plot3D(xline,yline,zline)
# ax.plot(xline,yline)
plt.show()

