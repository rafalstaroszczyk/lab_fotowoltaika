import numpy as np

def main():
    file_25 = np.loadtxt("temp_25.txt", delimiter='\t', skiprows=1)
    file_40 = np.loadtxt("temp_40.txt", delimiter='\t', skiprows=1)
    file_50 = np.loadtxt("temp_50.txt", delimiter='\t', skiprows=1)
    file_60 = np.loadtxt("temp_60.txt", delimiter='\t', skiprows=1)
    file_25_UI = file_25[:,0:2]
    file_40_UI = file_40[:,0:2]
    file_50_UI = file_50[:,0:2]
    file_60_UI = file_60[:,0:2]
    file_25_UI_sorted = file_25_UI[file_25_UI[:,0].argsort()]
    file_40_UI_sorted = file_40_UI[file_40_UI[:,0].argsort()]
    file_50_UI_sorted = file_50_UI[file_50_UI[:,0].argsort()]
    file_60_UI_sorted = file_60_UI[file_60_UI[:,0].argsort()]
    file_25_PU = file_25[:,[0,2]]
    file_40_PU = file_40[:,[0,2]]
    file_50_PU = file_50[:,[0,2]]
    file_60_PU = file_60[:,[0,2]]
    file_25_PU_sorted = file_25_PU[file_25_PU[:,0].argsort()][:-1,:]
    file_40_PU_sorted = file_40_PU[file_40_PU[:,0].argsort()][:-1,:]
    file_50_PU_sorted = file_50_PU[file_50_PU[:,0].argsort()][:-1,:]
    file_60_PU_sorted = file_60_PU[file_60_PU[:,0].argsort()][:-1,:]
    np.savetxt("temp_25_UI_sorted.txt", file_25_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tImA", comments='')
    np.savetxt("temp_40_UI_sorted.txt", file_40_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tImA", comments='')
    np.savetxt("temp_50_UI_sorted.txt", file_50_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tImA", comments='')
    np.savetxt("temp_60_UI_sorted.txt", file_60_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tImA", comments='')
    np.savetxt("temp_25_PU_sorted.txt", file_25_PU_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tPmW", comments='')
    np.savetxt("temp_40_PU_sorted.txt", file_40_PU_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tPmW", comments='')
    np.savetxt("temp_50_PU_sorted.txt", file_50_PU_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tPmW", comments='')
    np.savetxt("temp_60_PU_sorted.txt", file_60_PU_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tPmW", comments='')

if __name__ == '__main__':
    main()
