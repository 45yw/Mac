#入力値 P(x_1, y_1), y = x^3 + ax + b
#出力値 2P(x_3, y_3)
# x_3 = λ^2 - 2x_1
#y_3 = λ(x_1 - x_3) - y_1
#λ = (3 * (x_1)^3 - a) / 2 * y_1

def calc_double(x, y, a):
    slope = (3 * x ** 3 - a) / (2 * y)
    new_x = slope ** 2 - 2 * x
    new_y = slope * (x - new_x) - y
    return new_x, new_y

def main():
    a = int(input())
    P = [int(i) for i in input().split()]
    new_P = calc_double(P[0], P[1], a)
    print(new_P[0])
    print(new_P[1]) 

if __name__ == '__main__':
    main()
