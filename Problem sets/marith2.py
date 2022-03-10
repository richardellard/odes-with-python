class Matrix:
    def __init__(self, entries):
        self.entries = entries
        
    def size(self):
        return len(self.entries)
        
    def __add__(M, N):
        n = M.size()
        
        return Matrix([[M.entries[i][j] + N.entries[i][j] for j in range(n)] for i in range(n)])
    
    def __mul__(M, N):
        n = M.size()
        
        return Matrix([[sum([M.entries[i][k]*N.entries[k][j] for k in range(n)]) for j in range(n)] for i in range(n)])
    
    def scale(self, c):
        return Matrix([[c*x for x in row] for row in self.entries])
    
    def __str__(self):
        return str(self.entries)
    
    def __iter__(self):
        return Matrix_Iterator(self)
    
    def __getitem__(self, i):
        return self.entries[i]
    
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