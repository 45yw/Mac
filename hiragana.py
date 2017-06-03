# -*- coding:utf-8 -*-
import sys
import json
BYTE_SIZE = 8

# 文字列textをバイナリの文字列に変換する
def str2bin(s):
    binStr = ""
    for c in s:
        for i in range(BYTE_SIZE):
            binStr += str((ord(c) >> (BYTE_SIZE - (i + 1))) & 1)
    return binStr

# 文字列sを文字数nで分割したリストを返す
def split(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

# 文字列sを文字数nで分割した時に足りない部分を文字cで埋める
def fillInBlank(s, n, c):
    mod = len(s) % n
    if mod == 0: return s
    margin = n - mod
    return s + c * margin

def main():
    argvs = sys.argv
    argc = len(argvs)
    if argc != 2:
        print "Usage:\n$ python %s CONVERT_STRING" % argvs[0]
        quit()
    binStr = str2bin(argvs[1])
    s = split(binStr, 6)
    s[-1] = fillInBlank(s[-1], 6, "0")
    tableFile = open("base64_table.json", "r")
    base64Dict = json.loads(tableFile.read())
    result = ""
    for i in s:
        result += base64Dict[i]
    print result
    print fillInBlank(result, 4, "=")

if __name__ == '__main__':
    main()
