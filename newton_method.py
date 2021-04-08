def My_Equation(x): # 방정식 정의
    return A*(x**4)+(B)*(x**3)+(C)*(x**2)+D*(x**1)+E

def First_derivatives(x): # 1차 미분
    return ((4*A)*(x**3))+((3*B)*(x**2))+((2*C)*(x**1))+D
    
def Second_derivatives(x): # 2차 미분
    return ((12*A)*(x**2))+((6*B)*(x**1))+(2*C)
    
def newton_method(a, iteration, My_func, first_deri, second_deri, R):
    iteration = iteration + 1 # 반복 횟수
    a_next = a-(first_deri(a)/second_deri(a)) # 다음 값
    if abs(1-(a/a_next)) < R: # 종료 조건
        print("Final case") 
        print("iteration: ", str(iteration).ljust(3), "Optimal x: ", str(a).ljust(25), "Range: ", a - a_next)
    else: # 종료 조건이 아닐 때 newton_method 계산
        a_next = a-(first_deri(a)/second_deri(a)) # 다음 값
        print("iteration:", str(iteration).ljust(3), "x{}: ".format(iteration), str(a).ljust(25), "x{}: ".format(iteration+1), str(a_next).ljust(25), "Range: ", a - a_next)
        newton_method(a_next, iteration, My_func, first_deri, second_deri, R) # 반복
        
            
A = int(input("x^4의 계수 :\n"))
B = int(input("x^3의 계수 :\n"))
C = int(input("x^2의 계수 :\n"))
D = int(input("x^1의 계수 :\n"))
E = int(input("x^0의 계수 :\n"))

R = float(input("Threshold of the final range :\n"))

X = float(input("초기값을 입력하세요.\n"))

newton_method(X, 0, My_Equation, First_derivatives, Second_derivatives, R)