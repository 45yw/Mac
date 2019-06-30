def hex2dec(X, n):
    out = 0
    for i in range(1, len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

if __name__ == '__main__':
    s = input()
    n = hex2dec(s, 2)
    print(chr(n))
    
