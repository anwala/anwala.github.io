import matplotlib.pyplot as plt
import numpy as np


def add_arrow(line, position=None, direction='right', size=15, color=None):
    """
    add an arrow to a line.

    line:       Line2D object
    position:   x-position of the arrow. If None, mean of xdata is taken
    direction:  'left' or 'right'
    size:       size of the arrow in fontsize points
    color:      if None, line color is taken.
    """
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if position is None:
        position = xdata.mean()
    # find closest index
    start_ind = np.argmin(np.absolute(xdata - position))
    if direction == 'right':
        end_ind = start_ind + 1
    else:
        end_ind = start_ind - 1

    line.axes.annotate('',
        xytext=(xdata[start_ind], ydata[start_ind]),
        xy=(xdata[end_ind], ydata[end_ind]),
        arrowprops=dict(arrowstyle="->", color=color),
        size=size
    )


n=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'] 
a=[ 2 , 3 , 4 , 7 , 5 , 6 , 4 , 7 , 0 , 0 , 1 , 0 , .5, .5, 0 , 0]
b=[ 3 , 2 , 2,  2,  0 , 0 , 3 , 3 , 5 , 0,  5,  1,  2 , 1 , 2 , 3]

fig, ax = plt.subplots()
ax.scatter(a, b)



for i, txt in enumerate(n):
    ax.annotate(txt, (a[i],b[i]))

#ax = plt.axes()
#ax.arrow(1, 1, 0, 1, head_width=0.05, head_length=0.1, fc='k', ec='k')
#plt.show()

#    A --> B 
x= [2,3]
y= [3,2]
plt.plot(x,y, label="A --> B")[0]
#  B --> C
x2 = [3,4]
y2 = [2,2]
plt.plot(x2, y2, label="B --> C")[0]
#    C --> D
x3 = [4,7]
y3 = [2,2]
plt.plot(x3, y3, label="C --> D")
#    C --> A  
x4 = [4,2]
y4 = [2,3]
plt.plot(x4, y4, label="C --> A")
#    C --> G
x5 = [4,4]
y5 = [2,3]
plt.plot(x5, y5, label="C --> G")
#    E --> F
x6 = [5,6]
y6 = [0,0]
plt.plot(x6, y6, label="E --> F")
#    G --> C
x7 = [4,4]
y7 = [3,2]
plt.plot(x7, y7, label="G --> C")
#    G --> H
x8 = [4,7]
y8 = [3,3]
plt.plot(x8, y8, label="G --> H")
#    I --> H
x9 = [0,7]
y9 = [5,3]
plt.plot(x9, y9, label="I --> H")
#    I --> K
x10 = [0,1]
y10 = [5,5]
plt.plot(x10, y10, label="I --> K")
#    L --> D
x11 = [0,7]
y11 = [1,2]
plt.plot(x11, y11, label="L --> D")
#    M --> A
x12 = [.5,2]
y12 = [2,3]
plt.plot(x12, y12, label="M --> A")
#    M --> N
x13 = [.5,.5]
y13 = [2,1]
plt.plot(x13, y13, label="M --> N")
#    N --> D
x14 = [.5,7]
y14 = [1,2]
plt.plot(x14, y14, label="N --> D")
#    O --> A
x15 = [0,2]
y15 = [2,3]
plt.plot(x15, y15, label="O --> A")
#    P --> G 
x16 = [0,4]
y16 = [3,3]
plt.plot(x16, y16, label="P --> G")

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Determining Bow Tie for Points')
plt.legend()
plt.show()

