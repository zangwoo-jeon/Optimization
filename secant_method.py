def My_Equation(x): # 방정식 정의
    return A*(x**4)+(B)*(x**3)+(C)*(x**2)+D*(x**1)+E

def First_derivatives(x): # 1차 미분
    return ((4*A)*(x**3))+((3*B)*(x**2))+((2*C)*(x**1))+D
    
def Secant_method(a, b, iteration, My_func, first_deri, R): #a = x^0, b = x^(-1), iteration 반복 횟수, My_func 방정식, first_deri 1차 미분, R 종료 조건
    iteration = iteration + 1 # 반복 횟수
    a_next = a-((a-b)/(first_deri(a)-first_deri(b))*first_deri(a)) # 다음 값
    if abs(1-(a/a_next)) < R: # 종료 조건
        print("Final case") 
        print("iteration: ", str(iteration).ljust(3), "Optimal x: ", str(a).ljust(25), "Range: ", a - a_next)
    else: # 종료 조건이 아닐 때 newton_method 계산
        a_next = a-((a-b)/(first_deri(a)-first_deri(b))*first_deri(a)) # 다음 값
        print("iteration:", str(iteration).ljust(3), "x{}: ".format(iteration), str(a).ljust(25), "x{}: ".format(iteration+1), str(a_next).ljust(25), "Range: ", a - a_next)
        Secant_method(a_next, a, iteration, My_func, first_deri, R) # 반복
        
            
A = int(input("x^4의 계수 :\n"))
B = int(input("x^3의 계수 :\n"))
C = int(input("x^2의 계수 :\n"))
D = int(input("x^1의 계수 :\n"))
E = int(input("x^0의 계수 :\n"))

R = float(input("Threshold of the final range :\n")) # 종료 조건

X = float(input("초기값 x^-1를 입력하세요.\n")) # x^(-1) 입력
X2 = float(input("초기값 x^0를 입력하세요.\n"))# x^0 입력

Secant_method(X2, X, 0, My_Equation, First_derivatives, R)