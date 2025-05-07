import numpy as np

def main():
    file = np.loadtxt("perov.txt", delimiter='\t', skiprows=1)
    file_UI = file[:,0:2]
    file_UI_sorted = file_UI[file_UI[:,0].argsort()]
    file_P = (file_UI_sorted[:,0] * file_UI_sorted[:,1]).reshape(-1,1)
    file_UI_sorted = np.concatenate((file_UI_sorted, file_P), axis=1)
    file_UI_sorted[:,1] = file_UI_sorted[:,1] * 1000
    np.savetxt("perov_sorted.txt", file_UI_sorted, fmt='%8.4f', delimiter='\t', header="UmV\tIuA\tPuW", comments='')


if __name__ == '__main__':
    main()
