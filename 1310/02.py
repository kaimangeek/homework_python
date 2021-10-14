class Matrix:
    def __init__(self, mat):
        self.mat = mat
        min = len(mat[0])
        a = True
        for i in range(len(mat)):
            if len(mat[i]) != min:
                a = False
        if not a:
            print("._.")

    def transpone(self):
        mat1 = []
        i = 0
        for i in range(len(self.mat[i])):
            x = []
            for j in range(len(self.mat)):
                x.append(self.mat[j][i])
            mat1.append(x)
        return mat1


matrix = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1], [1, 2, 3]])
print(matrix.transpone())
