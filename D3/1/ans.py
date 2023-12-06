def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

def combineToInt(arr):
    ans = 0
    for i in range(len(arr)):
        ans += int(arr[i]) * 10**(len(arr)-i-1)
    return ans



def isCandidateValid(columnIndex, lineIndex, candidateLen, lines):
    for i in range(candidateLen):

        neighbours8 = [None] * 8

        try:
            neighbours8[0] = lines[lineIndex-1][columnIndex+i]
        except:
            pass
        try:
            neighbours8[1] = lines[lineIndex-1][columnIndex+i+1]
        except:
            pass
        try:
            neighbours8[2] = lines[lineIndex][columnIndex+i+1]
        except:
            pass
        try:
            neighbours8[3] = lines[lineIndex+1][columnIndex+i+1]
        except:
            pass
        try:
            neighbours8[4] = lines[lineIndex+1][columnIndex+i]
        except:
            pass
        try:
            neighbours8[5] = lines[lineIndex+1][columnIndex+i-1]
        except:
            pass
        try:
            neighbours8[6] = lines[lineIndex][columnIndex+i-1]
        except:
            pass
        try:
            neighbours8[7] = lines[lineIndex-1][columnIndex+i-1]
        except:
            pass

        for j in range(8):
            if neighbours8[j] == None:
                continue
            if not neighbours8[j].isdigit() and not neighbours8[j] == '.' and not neighbours8[j] == ' ' and not neighbours8[j] == '\n':
                return True

class Candidate:
    def __init__(self, value, lineIndex, columnIndex, candidateLen):
        self.value = value
        self.lineIndex = lineIndex
        self.columnIndex = columnIndex
        self.candidateLen = candidateLen

def main():
    lines = parser()
    candidates = []
    for i in range(len(lines[0]) - 1):
        j = 0
        while j < len(lines[i]):
            if lines[i][j].isdigit():
                candidateLen = 1
                while j+candidateLen < len(lines[i]) and lines[i][j+candidateLen].isdigit():
                    candidateLen += 1
                candidates.append(Candidate(combineToInt(lines[i][j:j+candidateLen]), i, j, candidateLen))
                j += candidateLen
            j += 1

    ans = 0
    for candidate in candidates:
        isValid = isCandidateValid(candidate.columnIndex, candidate.lineIndex, candidate.candidateLen, lines)
        print(candidate.value)
        if isValid:
            
            print('valid')
            
            ans += candidate.value
        print('---')
    return ans

            

        

print(main())