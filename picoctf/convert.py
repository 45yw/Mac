def main():
    key = 'thisisalilkey'
    c = 'llkjmlmpadkkc'
    ans = []
    for i in range(13):
        key_ascii = ord(key[i]) - 97
        orgin_ascii = ord(c[i]) - 97
        for j in range(26):
            if(key_ascii + j) % 26 == orgin_ascii:
                ans.append(chr(97+j))
                break
    print(','.join(ans))


if __name__ == '__main__':
    main()
