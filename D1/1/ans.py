def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

def combineToInt(arr):
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * 10**(len(arr)-i-1)
    return ans

def main():
    lines = parser()
    ans = []
    for i in range(len(lines)):
        buff = []
        for char in lines[i]:
            if char.isdigit():
                buff.append(int(char))
        buff = (buff[0], buff[len(buff)-1])
        ans.append(combineToInt(buff))
    return sum(ans)

print(main())