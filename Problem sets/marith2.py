class Matrix:
    def __init__(self, entries):
        # check all rows are the same length
        n = len(entries[0])
        for row in entries:
            if len(row) != n:
                raise Exception('all rows must be the same length')
                
        # n is now the number of columns
        if len(entries) > n:
            raise Exception('attempted to create a matrix with more rows than columns, marith2 supports only square matrices')
        if len(entries) < n:
            raise Exception('attempted to create a matrix with fewer rows than columns, marith2 supports only square matrices')
        
        self.entries = entries
        
    def size(self):
        return len(self.entries)
        
    def __add__(M, N):
        n = M.size()
        n2 = N.size()
        if n != n2:
            raise Exception('cannot add square matrices of different sizes (' + str(n) + ' and ' + str(n2) + ')')
        
        return Matrix([[M.entries[i][j] + N.entries[i][j] for j in range(n)] for i in range(n)])
    
    def __mul__(M, N):
        n = M.size()
        n2 = N.size()
        if n != n2:
            raise Exception('cannot multiply square matrices of different sizes (' + str(n) + ' and ' + str(n2) + ')')
        
        return Matrix([[sum([M.entries[i][k]*N.entries[k][j] for k in range(n)]) for j in range(n)] for i in range(n)])
    
    def scale(self, c):
        return Matrix([[c*x for x in row] for row in self.entries])
    
    def __str__(self):
        return str(self.entries)
    
    def __iter__(self):
        return Matrix_Iterator(self)
    
    def __getitem__(self, i):
        return self.entries[i]
    
    def determinant(self):
        n = self.size()
        
        if n == 1:
            return self.entries[0][0]
        
        # return the Laplace expansion along the first row
        return sum([(-1)**j*self.entries[0][j]*self.minor_matrix(0,j).determinant() for j in range(n)])
    
    # returns submatrix with row i and column j deleted
    def minor_matrix(self, s, t):
        n = self.size()
        
        return Matrix([[self.entries[i][j] for j in list(range(t))+list(range(t+1,n))] for i in list(range(s))+list(range(s+1,n))])
            
    
def identity(n):
    return Matrix([[int(i==j) for j in range(n)] for i in range(n)])

def zero(n):
    return Matrix([[0 for j in range(n)] for i in range(n)])

class Matrix_Iterator:
    row_counter = 0
    column_counter = -1 # must advance counter before returning entry
    
    def __init__(self, M):
        self.matrix = M
        
    def __next__(self):
        self.advance_counter()
        return self.matrix.entries[self.row_counter][self.column_counter]
    
    def advance_counter(self):
        n = self.matrix.size()
        if self.column_counter == n-1:
            if self.row_counter == n-1:
                raise StopIteration
            # advance row
            self.column_counter = 0
            self.row_counter += 1
        else:
            self.column_counter += 1