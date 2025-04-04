import numpy as np

def main():
    file_1 = np.loadtxt("barwnikowe_1.txt", delimiter='\t', skiprows=1)
    file_1_UI = file_1[:,0:2]
    file_1_UI_sorted = file_1_UI[file_1_UI[:,0].argsort()]
    file_1_P = (file_1_UI_sorted[:,0] * file_1_UI_sorted[:,1] * 1000).reshape(-1,1)
    file_1_UI_sorted = np.concatenate((file_1_UI_sorted, file_1_P), axis=1)
    file_1_UI_sorted[:,1] = file_1_UI_sorted[:,1] * 1000
    np.savetxt("barw_1_sorted.txt", file_1_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tIuA\tPnW", comments='')


    file_9 = np.loadtxt("barwnikowe_9.txt", delimiter='\t', skiprows=1)
    file_9_UI = file_9[:,0:2]
    file_9_UI_sorted = file_9_UI[file_9_UI[:,0].argsort()]
    file_9_P = (file_9_UI_sorted[:,0] * file_9_UI_sorted[:,1]).reshape(-1,1)
    file_9_UI_sorted = np.concatenate((file_9_UI_sorted, file_9_P), axis=1)
    file_9_UI_sorted[:,1] = file_9_UI_sorted[:,1] * 1000
    np.savetxt("barw_9_sorted.txt", file_9_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tIuA\tPuW", comments='')
    
    
    file_13 = np.loadtxt("barwnikowe_13.txt", delimiter='\t', skiprows=1)
    file_13_UI = file_13[:,0:2]
    file_13_UI_sorted = file_13_UI[file_13_UI[:,0].argsort()]
    file_13_P = (file_13_UI_sorted[:,0] * file_13_UI_sorted[:,1]).reshape(-1,1)
    file_13_UI_sorted = np.concatenate((file_13_UI_sorted, file_13_P), axis=1)
    file_13_UI_sorted[:,1] = file_13_UI_sorted[:,1] * 1000
    np.savetxt("barw_13_sorted.txt", file_13_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tIuA\tPuW", comments='')


    file_20 = np.loadtxt("barwnikowe_20.txt", delimiter='\t', skiprows=1)
    file_20_UI = file_20[:,0:2]
    file_20_UI_sorted = file_20_UI[file_20_UI[:,0].argsort()]
    file_20_P = (file_20_UI_sorted[:,0] * file_20_UI_sorted[:,1]).reshape(-1,1)
    file_20_UI_sorted = np.concatenate((file_20_UI_sorted, file_20_P), axis=1)
    file_20_UI_sorted[:,1] = file_20_UI_sorted[:,1] * 1000
    np.savetxt("barw_20_sorted.txt", file_20_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tIuA\tPuW", comments='')

if __name__ == '__main__':
    main()
