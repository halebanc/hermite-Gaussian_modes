from scipy import special
from pylab import figure, cm
import matplotlib.pyplot as plt
import numpy as np
taille=60

def hermitian(x, y, xn=0, yn=0):
    return special.hermite(xn)(y*np.sqrt(2))*special.hermite(yn)(x*np.sqrt(2))*np.exp(-x**2)*np.exp(-y**2)
fig = plt.figure(figsize=(4, 4))
tab_num=[(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (1, 2), (2, 1)]
tableau=np.zeros((taille, taille))
col=2
ligne=4
compte=1
for num1, num2 in tab_num:
    for xi, yi in np.ndindex(tableau.shape):
        tableau[xi, yi]=hermitian((xi/10)-3, (yi/10)-3, xn=num1, yn=num2) 
    fig.add_subplot(col, ligne, compte)
    plt.imshow(np.absolute(tableau), cmap='gray', origin='lower')
    plt.axis('off')
    plt.title(str(num1)+","+str(num2))
    compte+=1
#plt.colorbar()
plt.savefig("hermitian.pdf")
plt.show()
