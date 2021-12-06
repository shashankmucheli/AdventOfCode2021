def measure_depth():
    with open('/Users/smucheli/repos/adventOfCode2021/day1/input.txt') as f:
       lines = f.readlines()
    f.close()

    data = []
    for line in lines:
        data.append(int(line))
    
    depthChange = 0
    for index in range(len(data)-3):
        A = data[index] + data[index+1] + data[index+2]
        B = data[index+1] + data[index+2] + data[index+3]
        # print("A - {} B - {}".format(str(A), str(B)))
        if A < B: 
            depthChange+=1
        pass
    print(depthChange)
    pass

if __name__ == "__main__":
    measure_depth()