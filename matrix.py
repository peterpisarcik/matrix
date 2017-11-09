class Matrix:
    def __init__(self, array):
        # Get matrix access to object
        self.array = array

        # Check if rows have same width
        for i in range(0, len(array)):
            if len(array[0]) != len(array[i]):
                raise ValueError("Rows are not equal")

    @staticmethod
    def zero_matrix(height, width):
        """
        Create whole matrix with zeros

        :parameter height
        :parameter width
        :return Matrix
        """
        result = [[0 for x in range(width)] for y in range(height)]

        for x in range(width):
            for y in range(height):
                result[y][x] = 0

        return Matrix(result)

    @staticmethod
    def unit_matrix(side):
        """
        Static method to create matrix with zeroes and ones

        :parameter side
        :return Matrix
        """
        result = [[0 for x in range(side)] for y in range(side)]

        for x in range(side):
            for y in range(side):
                if x == y:
                    result[x][y] = 1
                else:
                    result[x][y] = 0

        return Matrix(result)

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
        """ Print height of matrix.  """
        print(len(self.array))

    def transposition(self):
        """
        Return transpose of matrix

        :return Matrix
        """
        array = self.array
        w, h = len(array), len(array[0])

        transposition = [[0 for x in range(w)] for y in range(h)]

        for i in range(len(array[0])):
            for j in range(len(array)):
                transposition[i][j] = array[j][i]

        return Matrix(transposition)

    def is_square(self):
        # This method check whether is matrix square or not.
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
        :return boolean
        """
        if self.array == other_matrix:
            return True
        else:
            return False

    def __ne__(self, other_matrix):
        """
        Overloading operator !=

        :parameter other_matrix -- Other matrix for overloading != operator
        :return boolean
        """

        if self.array != other_matrix:
            return True
        else:
            return False

    def __add__(self, other_matrix):
        """
        Overloading operator +

        :parameter other_matrix -- Other matrix for overloading + operator
        :return Matrix -- Return sum of two matrices
        """
        first_matrix = self.array
        second_matrix = other_matrix.array

        if len(first_matrix) != len(second_matrix):
            raise ValueError("Matrices have not same size")

        w, h = len(first_matrix), len(first_matrix[0])
        result = [[0 for x in range(h)] for y in range(w)]

        for i in range(len(first_matrix[0])):
            for j in range(len(first_matrix)):
                result[j][i] = first_matrix[j][i] + second_matrix[j][i]

        return Matrix(result)

    def __sub__(self, other_matrix):
        """
       Overloading operator -

       :parameter other_matrix -- Other matrix for overloading - operator
       :return Matrix -- Return subtraction of two matrices
       """
        first_matrix = self.array
        second_matrix = other_matrix.array

        if len(first_matrix) != len(second_matrix):
            raise ValueError("Matrices have not same size")

        w, h = len(first_matrix), len(first_matrix[0])
        result = [[0 for x in range(h)] for y in range(w)]

        for i in range(len(first_matrix[0])):
            for j in range(len(first_matrix)):
                result[j][i] = first_matrix[j][i] - second_matrix[j][i]

        return Matrix(result)

    def __mul__(self, other_matrix):
        """
       Overloading operator *

       :parameter other_matrix -- Other matrix for overloading * operator
       :return Matrix -- Return subtraction of two matrices
       """
        first_matrix = self.array
        second_matrix = other_matrix.array

        if len(first_matrix[0]) != len(second_matrix):
            raise ValueError("Rows of first matrix must be equal to second matrix columns")

        w, h = len(second_matrix[0]), len(first_matrix)
        result = [[0 for x in range(w)] for y in range(h)]

        for i in range(len(first_matrix)):
            for j in range(len(first_matrix[0])):
                result[i][j] = first_matrix[i][j] * second_matrix[j][i]

        return Matrix(result)

    def __rmul__(self, constant):
        """
        Overloading operator * by constant

        :parameter constant
        :return Matrix
        """
        first_matrix = self.array

        w, h = len(first_matrix), len(first_matrix[0])
        result = [[0 for x in range(h)] for y in range(w)]

        for i in range(len(first_matrix[0])):
            for j in range(len(first_matrix)):
                result[j][i] = constant * first_matrix[j][i]

        return Matrix(result)


M = Matrix([[1, 2, 3], [4, 5, 6]])
A = Matrix([[-1, 3, -3, 1], [2, 0, 0, 5], [1, 5, 7, -10]])

C = M * A
print(C)





# Z = Matrix.zero_matrix(3, 2)
# print(M)
# print(Z)
