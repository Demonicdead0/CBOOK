from sympy import preview
import time

a = time.time()

preview(r'$$\int_0^1 e^x\,dx$$', viewer='file', filename='test.png', euler=False)

print(time.time() - a)