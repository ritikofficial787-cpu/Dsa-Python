#Rotate Matrix-Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
import numpy as np

twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twoDArray)
print("******************")


def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # 1. Save top element
            top = matrix[first][i]

            # 2. Move left element to top
            matrix[first][i] = matrix[last - offset][first]

            # 3. Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # 4. Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]

            # 5. Move top element to right
            matrix[i][last] = top

    #  This must be indented outside the loops!
    return matrix


print(rotateMatrix(twoDArray))
    