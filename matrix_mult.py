#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 11/25/25
#Description: Part 1 - dot_prod(): Calculates the dot product by multiplying corresponding elements and summing them up.
#             Part 2 - matrix_mult(): Takes two matrices and multiplies them by:
#             1: Checking that the dimensions are compatible (columns of A = rows of B)
#             2: For each cell in the result matrix, extracting the appropriate row from matrix A and column from matrix B
#             3: Calling dot_prod() to compute each cell value
#             4: Returning None if multiplication isn't possible

def dot_prod(vector_a, vector_b):
    """
    Calculate the dot product of two vectors

    The dot product is the sum of the products of corresponding elements
    from two vectors

    args:
    vector_a: A list of numeric values representing the first vector.
    vector_b: A list of numeric values representing the second vector.

    returns:
    The dot product as a number (int or float).
    """
    #initialize the result to 0
    result = 0

    #iterate through each index in the vectors
    for i in range(len(vector_a)):
        #multiply corresponding elements and add to the result
        result += vector_a[i] * vector_b[i]

    #return the final dot product
    return result


def matrix_mult(matrix_a, matrix_b):
    """
    Calculate the product of two 2D matrices (lists of lists).

    Multiplies two matrices together using the standard matrix multiplication
    method. Each element in the result matrix is the dot product of a row
    from matrix_a and a column from matrix_b. If the number of columns in
    matrix_a does not equal the number of rows in matrix_b, the function
    returns None as the matrices cannot be multiplied.

    args:
    matrix_a: A 2D list (list of lists) representing the first matrix
                with dimensions p x q (p rows and q columns).
    matrix_b: A 2D list (list of lists) representing the second matrix
                with dimensions q x r (q rows and r columns).

    returns:
    A 2D list representing the product matrix with dimensions p x r,
    or None if the matrices cannot be multiplied.
    """
    #get the dimensions of matrix_a
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])

    #bet the dimensions of matrix_b
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    #check if multiplication is possible: cols_a must equal rows_b
    if cols_a != rows_b:
        #return None if the matrices cannot be multiplied
        return None

    #initialize the result matrix with the correct dimensions (rows_a x cols_b)
    result = []

    #iterate through each row of matrix_a
    for i in range(rows_a):
        #create a new row in the result matrix
        new_row = []

        #iterate through each column of matrix_b
        for j in range(cols_b):
            #pull the current row from matrix_a
            row_a = matrix_a[i]

            #create a list for the current column of matrix_b
            col_b = []
            #iterate through each row of matrix_b to build the column
            for k in range(rows_b):
                #add the element at position j from row k of matrix_b
                col_b.append(matrix_b[k][j])

            #calculate the dot product of the row and column
            cell_value = dot_prod(row_a, col_b)

            #add the result to the current row
            new_row.append(cell_value)

        #add the completed row to the result matrix
        result.append(new_row)

    #return the completed result matrix
    return result