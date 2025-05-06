import lmfit
import pandas as pd
import numpy as np
from lmfit import Minimizer, Parameters, report_fit
from numpy import exp, pi, sqrt, linspace, random, interp


#### LOAD EXPERIMENTAL DATA ####

df = pd.read_csv('per_suns.csv')
df.head()
V_applied = df.V
J_exp = np.array([])
light_intensity_array = []

for index in range(1, df.shape[1]): # except V_applied
    columnSeriesObj = df.iloc[: , index] # Select column by index position using iloc[]

    light_intensity_array.append(
        np.interp(0, V_applied, columnSeriesObj.values)/np.interp(0, V_applied, df.iloc[: , 1])
        ) #Jsc_[i]/J_sc[1] - light intensity [0,1]
    J_exp = np.concatenate([J_exp, columnSeriesObj.values], axis=0)


#### DIODE EQUATION - LATER DRIFT-DIFFUSION ####

import pvlib
from scipy.stats import chisquare

#def diode_eq(voltage, light_intensity, n, I_L, I_0, R_s, R_sh):
def diode_eq(params, light_intensity, V_exp, J_exp):
    k_B = 1.38064852E-23;
    T = 300;
    q = 1.602E-19
    
    n = params['n']
    I_L = params['I_L']
    I_0 = params['I_0']
    R_s = params['R_s']
    R_sh = params['R_sh']
    
    tmp_J = [];
    for tmp_light_intensity in light_intensity:
        for V in V_exp:
            tmp_J.append( 
                pvlib.pvsystem.i_from_v(
                    resistance_shunt=R_sh*1/tmp_light_intensity, 
                    resistance_series=R_s, 
                    nNsVth=n*k_B*T/q,
                    voltage=V,
                    saturation_current=I_0,
                    photocurrent=I_L*tmp_light_intensity,
                    method='lambertw')
                )
    # Here it needs to have the same V_exp and V_sim
    # test = np.interp(V_exp, V_sim, J_sim)
    #print(sum((tmp_J-J_exp)**2))
    
    return tmp_J-J_exp



#### FITTING PROCESS ####


# create a set of parameters to be fitted
params = Parameters()


params.add('n', value=1.70, vary=True, min=0.8, max=6)
params.add('I_L', value=46.5, vary=True, min=0.0001, max=50)
params.add('I_0', value=8.063e-06, vary=True, min=1E-12, max=1E-1)
params.add('R_s', value=0.00432, vary=True, min=1E-4, max=1E-1)
params.add('R_sh', value=4.629, vary=True, min=1E-2, max=1E5)

# do fit, here with the default leastsq algorithm
minner = Minimizer(diode_eq, params, fcn_args=(light_intensity_array, V_applied, J_exp), max_nfev=99999)

result = minner.minimize(method='leastsq')


#Takes 20 times more iterations!
#ci = lmfit.conf_interval(minner, result, sigmas=[1, 2], trace=True, verbose=False)
#lmfit.printfuncs.report_ci(ci)

# calculate final result
J_res = result.residual
J_sim = J_exp + J_res

# write error report
report_fit(result)


# try to plot results
try:
    J_exp_light_intensity = np.split(J_exp, len(light_intensity_array))
    J_sim_light_intensity = np.split(J_sim, len(light_intensity_array))
    J_res_light_intensity = np.split(J_res, len(light_intensity_array))
    
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    
    for i in range(0, len(light_intensity_array)):
        plt.plot(V_applied, J_exp_light_intensity[i], 'or', color='red')
        plt.plot(V_applied, J_sim_light_intensity[i], '-', color='black')
    
        plt.fill_between(V_applied, J_sim_light_intensity[i] - J_res_light_intensity[i], 
                         J_sim_light_intensity[i] + J_res_light_intensity[i],
                     color='gray', alpha=0.2)
        plt_exp = mpatches.Patch(color='red', label='Experiment')
        plt_sim = mpatches.Patch(color='black', label='Simulation')
        plt_res = mpatches.Patch(color='gray', label='Uncertainty')
    
    plt.legend(handles=[plt_exp,plt_sim,plt_res])

    plt.show()
except ImportError:
    pass