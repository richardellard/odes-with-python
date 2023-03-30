class Matrix:
    def __init__(self, entries):
        m = len(entries)
        n = len(entries[0])
        for row in entries:
            if len(row) != n:
                raise Exception('all matrix rows must be of equal length')
        if m != n:
            raise Exception('cannot create the given ' + str(m) + ' x ' + str(n) + ' matrix - marith2 handles only square matrices')
        self.entries = entries
        
    def size(self):
        return len(self.entries)
    
    def __getitem__(self, i):
        return self.entries[i]
    
    def __setitem__(self, i, value):
        self.entries[i] = value
        
    def __add__(M, N):
        n = M.size()
        if N.size() != n:
            raise Exception('cannot add matrices of different size')
        
        return Matrix([[M[i][j]+N[i][j] for j in range(n)] for i in range(n)])
    
    def __mul__(M, N):
        n = M.size()
        if N.size() != n:
            raise Exception('cannot multiply square matrices of different size')
        
        def MN(i, j):# returns the (i, j)-entry of the matrix product MN
            return sum([M[i][k]*N[k][j] for k in range(n)])
        
        return Matrix([[MN(i, j) for j in range(n)] for i in range(n)])
    
    def scale(M, c):
        n = M.size()
        
        return Matrix([[c*M[i][j] for j in range(n)] for i in range(n)])
    
    def __iter__(self):
        return MatrixIterator(self)
        
    def __str__(self):
        return str(self.entries)
    
    # compute the determinant:
    
    def determinant(M):
        n = M.size()
        if n == 1:
            return M[0][0]
        
        return sum([M[0][j]*M.cofactor(0, j) for j in range(n)])# Laplace expansion along the first row
    
    def minor(M, i, j): # returns the (i, j)-minor of matrix M
        n = M.size()
        rows = list(range(n))
        cols = list(range(n))
        del rows[i]
        del cols[j]
        
        return Matrix([[M[i][j] for i in rows] for j in cols]).determinant()
    
    def cofactor(M, i, j): # returns the (i, j)-cofactor of matrix M
        return (-1)**(i+j)*M.minor(i, j)

class MatrixIterator:
    def __init__(self, M):
        self.M = M # stores the underlying Matrix object
        self.row = 0 # row placeholder
        self.col = -1 # column placeholder initially starts outside the matrix
        
    def advance_placeholder(self):
        n = self.M.size()
        if self.col == n - 1:
            if self.row == n - 1: # can't advance any further
                raise StopIteration
            self.col = 0
            self.row += 1
        else:
            self.col += 1
        
    def __next__(self):
        self.advance_placeholder()
        return self.M[self.row][self.col]
        
def diagonal_matrix(diagonal):
    n = len(diagonal)
    def M(i, j):
        if i == j:
            return diagonal[i]
        return 0
    
    return Matrix([[M(i, j) for j in range(n)] for i in range (n)])

def zero(n):
    return diagonal_matrix([0]*n)

def identity(n):
    return diagonal_matrix([1]*n)