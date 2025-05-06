import numpy as np

def main():
    file_25 = np.loadtxt("temp_25_UI_sorted.txt", delimiter='\t', skiprows=1)
    file_40 = np.loadtxt("temp_40_UI_sorted.txt", delimiter='\t', skiprows=1)
    file_50 = np.loadtxt("temp_50_UI_sorted.txt", delimiter='\t', skiprows=1)
    file_60 = np.loadtxt("temp_60_UI_sorted.txt", delimiter='\t', skiprows=1)


if __name__ == '__main__':
    main()

