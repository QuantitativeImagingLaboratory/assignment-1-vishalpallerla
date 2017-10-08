import numpy as np
I = np.zeroes((200,200))
R = I.copy()

for i in range(255):
    for j in range(255):
        if I[i, j] == 1 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 0 and I[
                    i - 1, j + 1] == 0:
            R[i, j] = region_counter
            region_counter = region_counter + 1

        if I[i, j] == 1 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 0 and I[
                    i - 1, j + 1] == 1:
            R[i, j] = R[i - 1, j + 1]

        if I[i, j] == 1 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 1 and I[
                    i - 1, j + 1] == 0:
            R[i, j] = R[i - 1, j]

        if I[i, j] == 1 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 1 and I[i - 1, j] == 0 and I[
                    i - 1, j + 1] == 0:
            R[i, j] = R[i - 1, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 1 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 0 and I[
                    i - 1, j + 1] == 0:
            R[i, j] = R[i, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 1 and I[i - 1, j - 1] == 1 and I[i - 1, j] == 0 and I[
                    i - 1, j + 1] == 0:
            if R[i, j] == R[i, j - 1] == R[i - 1, j - 1]:
                R[i, j] = R[i - 1, j - 1]
            else:
                R[i, j - 1] = R[i - 1, j - 1]
                R[i, j] = R[i, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 1 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 1 and I[
                    i - 1, j + 1] == 0:
            if R[i, j] == R[i, j - 1] == R[i - 1, j]:
                R[i, j] = R[i, j - 1]
            else:
                R[i, j - 1] = R[i - 1, j]
                R[i, j] = R[i, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 1 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 0 and I[
                    i - 1, j + 1] == 1:
            if R[i, j] == R[i, j - 1] == R[i - 1, j + 1]:
                R[i, j] = R[i, j - 1]
            else:
                R[i, j - 1] = R[i - 1, j + 1]
                R[i, j] = R[i, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 1 and I[i - 1, j] == 1 and I[
                    i - 1, j + 1] == 0:
            if R[i, j] == R[i - 1, j - 1] == R[i - 1, j]:
                R[i, j] = R[i - 1, j]
        else:
            R[i - 1, j - 1] = R[i - 1, j]
            R[i, j] = R[i - 1, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 1 and I[i - 1, j] == 0 and I[
                    i - 1, j + 1] == 1:
            if R[i, j] == R[i - 1, j - 1] == R[i - 1, j + 1]:
                R[i, j] = R[i - 1, j - 1]
            else:
                R[i - 1, j - 1] = R[i - 1, j + 1]
                R[i, j] = R[i - 1, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 1 and I[
                    i - 1, j + 1] == 1:
            if R[i, j] == R[i - 1, j] == R[i - 1, j + 1]:
                R[i, j] = R[i - 1, j]
        else:
            R[i - 1, j] = R[i - 1, j + 1]
            R[i, j] = R[i - 1, j]

        if I[i, j] == 1 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 1 and I[i - 1, j] == 1 and I[
                    i - 1, j + 1] == 1:
            if R[i, j] == R[i - 1, j] == R[i - 1, j + 1] == R[i - 1, j - 1]:
                R[i, j] = R[i - 1, j]
        else:
            R[i - 1, j] = R[i - 1, j + 1]
            R[i - 1, j - 1] = R[i - 1, j]
            R[i, j] = R[i - 1, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 1 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 1 and I[
                    i - 1, j + 1] == 1:
            if R[i, j] == R[i - 1, j] == R[i - 1, j + 1] == R[i, j - 1]:
                R[i, j] = R[i - 1, j]
        else:
            R[i - 1, j] = R[i - 1, j + 1]
            R[i, j - 1] = R[i - 1, j]
            R[i, j] = R[i, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 1 and I[i - 1, j - 1] == 1 and I[i - 1, j] == 0 and I[
                    i - 1, j + 1] == 1:
            if R[i, j] == R[i, j - 1] == R[i - 1, j + 1] == R[i - 1, j - 1]:
                R[i, j] = R[i, j - 1]
        else:
            R[i - 1, j - 1] = R[i - 1, j + 1]
            R[i, j - 1] = R[i - 1, j - 1]
            R[i, j] = R[i, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 1 and I[i - 1, j - 1] == 1 and I[i - 1, j] == 1 and I[
                    i - 1, j + 1] == 0:
            if R[i, j] == R[i, j - 1] == R[i - 1, j] == R[i - 1, j - 1]:
                R[i, j] = R[i, j - 1]
        else:
            R[i - 1, j - 1] = R[i - 1, j]
            R[i, j - 1] = R[i - 1, j - 1]
            R[i, j] = R[i, j - 1]

        if I[i, j] == 1 and I[i, j - 1] == 1 and I[i - 1, j - 1] == 1 and I[i - 1, j] == 1 and I[
                    i - 1, j + 1] == 1:
            if R[i, j] == R[i, j - 1] == R[i - 1, j] == R[i - 1, j - 1]:
                R[i, j] = R[i, j - 1]
        else:
            R[i - 1, j] = R[i - 1, j + 1]
            R[i - 1, j - 1] = R[i - 1, j]
            R[i, j - 1] = R[i - 1, j - 1]
            R[i, j] = R[i, j - 1]



