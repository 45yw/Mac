#coding:utf8
import random

def is_prime3(q, k):
    q = abs(q)
    #計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q&1 == 0: return False   #アンドは論理積

    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    #判定をk回繰り返す
    for i in range(k):
        a = random.randint(1, q-1)
        t = d
        y = pow(a, t, q)
        #[0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            print("ゴミ")
            return False
    print("神")
    return True

if __name__ == '__main__':
    #n = 12345
    #l = [int(x) for x in list(str(n))]
    is_prime3(345829343, 50);
