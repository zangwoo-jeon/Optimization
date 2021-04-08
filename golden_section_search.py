A = int(input("x^4의 계수 :\n"))
B = int(input("x^3의 계수 :\n"))
C = int(input("x^2의 계수 :\n"))
D = int(input("x^1의 계수 :\n"))
E = int(input("x^0의 계수 :\n"))

def My_Equation(x): # 방정식 정의
    return A*(x**4)+(B)*(x**3)+(C)*(x**2)+D*(x**1)+E

def golden_initial(a, b):
    if a < b: 
        x_l = a # x의 최소값
        x_h = b # x의 최대값
    else:
        x_l = b # x의 최소값
        x_h = a # x의 최대값

    x1 = x_h - 0.618 * (x_h - x_l) # a1
    x2 = x_l + 0.618 * (x_h - x_l) # b1
    return x1, x2, x_h, x_l

R = float(input("Threshold of the final range :\n")) # 종료 조건 범위

def golden_search(x1, x2, x_h, x_l, my_func, iteration):

    print("iteration:", str(iteration).ljust(3), "x_low:", str(x_l).ljust(25), "x1:", str(x1).ljust(25), "x2:", str(x2).ljust(25), "x_high:", str(x_h).ljust(25))
    iteration = iteration + 1
    
    if abs((0.618 ** iteration)*(x_h - x_l)) < R: # 종료 조건(b1-a1 < R보다 작을 때)
        print('Final case')
        print("iteration:", str(iteration).ljust(3), "x_low:", str(x_l).ljust(25), "x_high:", str(x_h).ljust(25), "x1:", str(x1).ljust(25), "x2:", str(x2).ljust(25))
        print("the optimal x:", str((x_l+x_h)/2).ljust(25), "minimum value: ", my_func((x_l+x_h)/2))
        print("Final uncertainty range: ", (0.618 ** iteration)*(x_h - x_l))
    else: # 종료 조건이 아닐 때
        if my_func(x1) > my_func(x2): # x1의 out값이 x2의 output값보다 클 때
            print("f(x1)", str(my_func(x1)).ljust(25),"f(x2)", str(my_func(x2)).ljust(25), "uncertainty range: ", (0.618 ** iteration)*(x_h - x_l))
            print("\n")
            x_l = x1
            x1 = x2
            x2 = x_l + 0.618 * (x_h - x_l)
            golden_search(x1, x2, x_h, x_l, my_func, iteration)
        elif my_func(x1) <= my_func(x2): # x1의 output값이 x2의 output값보다 작을 때
            print("f(x1)", str(my_func(x1)).ljust(25),"f(x2)", str(my_func(x2)).ljust(25), "uncertainty range: ", (0.618 ** iteration)*(x_h - x_l))
            print("\n")
            x_h = x2
            x2 = x1
            x1 = x_h - 0.618 * (x_h - x_l)

            golden_search(x1, x2, x_h, x_l, my_func, iteration)



X = int(input("시작점 :\n")) # 시작점(a0)
Y = int(input("끝점 :\n")) # 끝점(b0)

x1, x2, x_h, x_l = golden_initial(X, Y)
golden_search(x1, x2, x_h, x_l, My_Equation, 0)


