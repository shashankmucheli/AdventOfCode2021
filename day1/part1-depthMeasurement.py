def measure_depth():
    with open('/Users/smucheli/repos/adventOfCode2021/day1/input.txt') as f:
       lines = f.readlines()
    f.close()

    data = []
    for line in lines:
        data.append(int(line))
    
    depthChange = 0
    for index in range(len(data)-1):
        if data[index] < data[index+1]:
            depthChange+=1
    print(depthChange)
    pass

if __name__ == "__main__":
    measure_depth()