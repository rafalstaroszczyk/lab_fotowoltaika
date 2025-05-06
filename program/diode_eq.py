##https://pvlib-python.readthedocs.io/en/stable/auto_examples/plot_singlediode.html#sphx-glr-auto-examples-plot-singlediode-py

import pvlib
from numpy import linspace
import pvlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


V = linspace(-0.2, 1.2, 49)
name = "TEST"
light_intensity = 1000
n = 7.54599304;
I_L = 2.0057478
I_o = 0.010
R_s = 0.006
R_sh = 1000.04336672

def diode_eq(voltage, light_intensity, n, I_L, I_0, R_s, R_sh):
    # Example module parameters for the Canadian Solar CS5P-220M:
    k_B = 1.38064852E-23;
    T = 300;
    q = 1.602E-19
    
    tmp_single_J = [];
    for V in voltage:
        tmp_single_J.append( 
            pvlib.pvsystem.i_from_v(
                resistance_shunt=R_sh*1000/light_intensity, 
                resistance_series=R_s, 
                nNsVth=n*k_B*T/q,
                voltage=V,
                saturation_current=I_0,
                photocurrent=I_L*light_intensity/1000,
                method='lambertw')
            )
    # plug the parameters into the SDE and solve for IV curves:

    return tmp_single_J


J = diode_eq(V, light_intensity, n, I_L, I_o, R_s, R_sh)
P=V*J;
Vmp = V[np.argmax(P)];
Jmp = J[np.argmax(P)];
Jsc = np.interp(0, V[::-1], J[::-1]); #Inverted for interpolation only
Voc = np.interp(0, J[::-1], V[::-1]); #Inverted for interpolation only
FF = ((Vmp*Jmp) / (Voc*Jsc))*100;
PCE = np.absolute(Jsc*Voc*FF) / (100);

print("Jsc, Voc, FF, PCE")
print(Jsc, Voc, FF, PCE)

# plot the calculated curves:
plt.figure()
plt.plot(V, J)   
plt.xlabel('Voltage [V]')
plt.ylabel('Current [A]')
plt.title(name)
plt.show()
plt.gcf().set_tight_layout(True)

