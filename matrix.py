class Matrix:
    def __init__(self, array):
        """ Vytvoreni matice """
        self.array = array

        if len(array[0]) != len(array[1]):
            raise ValueError("Matrices are not equal")

    @staticmethod
    def zero_matrix(height, width):
        """ Staticka metoda na vytovreni nulove matice """
        result = ""
        iterator = 1
        for x in range(height * width):
            result = result + str(0)
            if iterator % width == 0:
                result = result + "\n"
            iterator += 1
        return result

    @staticmethod
    def unit_matrix(side):
        """ Staticka metoda na vytvoreni jednotkove matice """
        result = ""
        iterator = 1
        for x in range(side):
            for y in range(side):
                if x == y:
                    result = result + str(1)
                else:
                    result = result + str(0)
                    if iterator % side == 0:
                        result = result + "\n"
                iterator += 1

        return result

    def __str__(self):
        iterator = 0
        result = ""
        for i in self.array:
            for a in i:
                iterator += 1
                result = result + " " + str(a)
                if iterator % len(self.array[0]) == 0:
                    result = result + "\n"
        return result

    def __setitem__(self, tup, new_value):
        """
        Overloading __setitem__ to set new value of element in matrix

        :parameter tup -- Tup is a position of element in matrix
        :parameter new_value -- new_value is value to set new value of element in matrix
        """
        
        array = self.array
        array[tup[0]][tup[1]] = new_value
        return array

    def __getitem__(self, tup):
        """
        Overloading __getitem__ to get element of matrix

        :parameter tup
        """

        x, y = tup
        print(self.array[x][y])

    def get_width(self):
        """ Print width of matrix """
        print(len(self.array[0]))

    def get_height(self):
        """
        Print height of matrix.
        """
        print(len(self.array))

    def transposition(self):
        """ Vrati novou matici, ktera je transpozici puvodni matice """
        array = self.array
        w, h = len(array), len(array[0])
        transposition = [[0 for x in range(w)] for y in range(h)]
        for i in range(len(array[0])):
            for j in range(len(array)):
                transposition[i][j] = array[j][i]

        return Matrix(transposition)

    def is_square(self):
        # This method check whether is matrix square or not
        array = self.array

        if len(array) == len(array[0]):
            return True

        return False

    def is_symmetric(self):
        """ This method prints whether matrix is symmetric or not and returns true or false """
        matrix = Matrix(self.array)
        if len(self.array) == len(self.array[0]) and matrix == matrix.transposition():
            print("Matrix is symmetric")
            return True
        else:
            print("Matrix is not symmetric")
            return False

    def __eq__(self, other_matrix):
        """
        Overloading operator ==

        :parameter other_matrix -- Other matrix for overloading == operator
        """
        if self.array == other_matrix:
            return True
        else:
            return False

    def __ne__(self, other_matrix):
        """
        Overloading operator !=

        :parameter other_matrix -- Other matrix for overloading != operator
        """

        if self.array != other_matrix:
            return True
        else:
            return False

    def __add__(self, other_matrix):
        """ Pretizeni operatoru + na scitani matic """
        first_matrix = self.array
        second_matrix = other_matrix
        print(second_matrix)
        #  if len(first_matrix) != len(second_matrix):
        #     raise ValueError("Matrices have not same size")

        # for i in range(len(first_matrix[0])):
        #  for j in range(len(first_matrix)):
        #      c = first_matrix[i][j] + second_matrix[i][j]
        # print(c)

    def __sub__(self, other_matrix):
        """ Pretizeni operatoru - na odecitani matic """
        pass

    def __mul__(self, other_matrix):
        """ Pretizeni operatoru * na nasobeni matic """
        pass

    def __rmul__(self, constant):
        """ Pretizeni operatoru * na nasobeni matice konstantou """
        pass


M = Matrix([[1, 2, 3], [4, 5, 6]])
A = Matrix([[1, 2, 3], [2, 5, 6]])
M + A


# Z = Matrix.zero_matrix(3, 2)
# print(M)
# print(Z)
