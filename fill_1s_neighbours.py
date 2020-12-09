A = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]

def fillOnes(A):
    oneFound = False
    res = 0
    i = 0
    n = len(A)

    while i < n:

        if A[i] == 1:
            oneFound = True

        while i < n and A[i] == 1:
            i += 1

        count_zero = 0
        while i < n and A[i] == 0:
            count_zero += 1
            i += 1

        if oneFound == False and i == n:
            return -1

        curr_count = 0
        if i < n and oneFound == True:

            if count_zero%2 == 0:
                curr_count = count_zero/2
            else:
                curr_count = (count_zero+1)/2

        else:
            curr_count = count_zero

        count_zero = 0

        res = max(res, curr_count)

    return int(res)

print(fillOnes(A))