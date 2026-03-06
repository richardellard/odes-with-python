class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def __add__(M, N):
        a = M.a + N.a
        b = M.b + N.b
        c = M.c + N.c
        d = M.d + N.d
        
        return Matrix(a, b, c, d)
    
    def __mul__(M, N):
        a = M.a*N.a + M.b*N.c
        b = M.a*N.b + M.b*N.d
        c = M.c*N.a + M.d*N.c
        d = M.c*N.b + M.d*N.d
        
        return Matrix(a, b, c, d)
    
    def scale(self, x):
        a = x*self.a
        b = x*self.b
        c = x*self.c
        d = x*self.d
        
        return Matrix(a, b, c, d)
    
    def __str__(self):
        return '(' + str(self.a) + ', ' + str(self.b) + ', ' + str(self.c) + ', ' + str(self.d) + ')'
    
identity = Matrix(1, 0, 0 ,1)
zero = Matrix(0, 0, 0 ,0)