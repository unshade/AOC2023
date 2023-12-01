convert = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5,
           'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'zero' : 0}

def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

def combineToInt(arr):
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * 10**(len(arr)-i-1)
    return ans

def findFirst(arr):
    acc = ''
    for i in range(len(arr)):
        if arr[i].isdigit():
            return int(arr[i])
        else :
            acc += arr[i]
            for key in convert:
                if key in acc:
                    return convert[key]
    return -1

def findLast(arr):
    acc = ''
    for i in range(len(arr)-1, -1, -1):
        if arr[i].isdigit():
            return int(arr[i])
        else :
            acc = arr[i] + acc
            for key in convert:
                if key in acc:
                    return convert[key]
    return -1

def main():
    lines = parser()
    ans = []
    for i in range(len(lines)):
        ans.append((findFirst(lines[i]), findLast(lines[i])))

    for i in range(len(ans)):
        ans[i] = combineToInt(ans[i])

    return sum(ans)
      
    
print(main())