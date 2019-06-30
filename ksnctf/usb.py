flag = ""
for i in range(7):
    filename = "Liberty Leading the People.jpg:0" + str(i)
    with open(filename) as f:
        flag += f.read()
print(flag)
