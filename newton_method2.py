import numpy as np

def My_quadratic_form(x): # 방정식 정의
    quad = xT.dot(qq.dot(x)) - bT.dot(x) + c #(0.5)*x^T*Q*x - b^T*x + c
    return quad
    
def First_derivatives(x): # 1차 미분
    g = QQ.dot(x) - b # Q*x - b
    return g
    
def Second_derivatives(): # Hessian
    return QQ
    
def newton_method(a, iteration, My_equation, First_deri, Second_deri):
    iteration = iteration+1
    print("iteration: ", iteration)
    QQ_reverse = np.linalg.inv(QQ) #F^(-1)(x)
    grad = First_deri(a) # f'(x)
    a_next = QQ_reverse.dot(b) #x(k+1) = Q^(-1)*b
    print("Optimal x :".format(iteration-1), a_next)
    print("grad", grad)


n = int(input("행의 갯수를 입력하세요 : \n"))
Q = []
b = []
x = []


for i in range(n):
    number1 = list(map(int, input("Q 행렬의 {}번째 행의 원소를 입력하세요 : \n".format(i+1)).split()))
    Q.append(number1)
    if i == n-1:
        Q = np.array(Q)
    
for j in range(n):
    number2 = list(map(int, input("b 행렬의 {}번째 행의 원소를 입력하세요 : \n".format(j+1)).split()))
    b.append(number2)
    if j == n-1:
        b = np.array(b)
c = int(input("상수항 C를 입력하시오 :\n"))
for k in range(n):
    number3 = list(map(int, input("x 행렬의 {}번째 행의 원소를 입력하세요 : \n".format(k+1)).split()))
    x.append(number3)
    if k == n-1:
        x = np.array(x)

xT = np.transpose(x)
bT = np.transpose(b)
QT = np.transpose(Q)



qq = 0.5*(QT+Q)
QQ = 2*qq

newton_method(x, 0, My_quadratic_form, First_derivatives, Second_derivatives)