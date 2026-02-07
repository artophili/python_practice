##def twoSum(nums, target):
##    sum = 0
##    l1 = []
##    for i in range(0, len(nums)):
##        for j in range(i+1, len(nums)):
##            if nums[i] + nums[j] == target:
##                l1.append(i)
##                l1.append(j)
##    return l1
##
##nums = [3,3]
##l1 = twoSum(nums, 6)
##print(l1)
##
##
##
##def twoSum(nums, target):
##    seen = {}
##    for i, num in enumerate(nums):
##        complement = target - num
##        if complement in seen:
##            return [seen[complement], i]
##        seen[num] = i


##def palindrome(num):
##    x = str(num)
##    if x[0] == '-':
##        return False
##    else:
##        rev_x = x[-1::-1]
##        print(rev_x)
##        if x == rev_x:
##            return True
##        return False
##
##x = 10
##palindrome(x)


board = [["1","2",".",".","3",".",".",".","."],
 ["2",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","1"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","9","7"]]

#print(board[2][1])

def digit_check(l1):
    arr = ['1','2','3','4','5','6','7','8','9']
    for i in l1:
        if i not in arr:
            return False
        else:
            return True

def duplicates(l1):
    counts = {}
    flag = True
    for i in l1:
        if i not in counts.keys():
            counts[i] = 1
        else:
            counts[i] = counts[i] + 1
    try:
        del counts['.']
    except keyError:
        print("'.' not found in sudoku")
    #print(counts)
    for j in counts.keys():
        #print(j)
        if counts[j] > 1:
            flag = True
            break
        else:
            flag = False
    return flag

arr = ['1','2','3','4','5','6','7','8','9']
###Row wise duplicates
##flag = True
##for i in range(len(board)):
##    #print(board[i])
##    if duplicates(board[i]):
##        flag = True
##        break
##    else:
##        flag = False

###Digit checker
##flag = True
##for i in range(len(board)):
##    for j in range(len(board)):
##        if board[i][j] == '.':
##            flag = False
##        elif board[i][j] not in arr:
##            flag = True
##            break
##        else:
##            flag = False
##print(flag)
        

###Column wise duplicates
##flag = True
##for i in range(len(board)):
##    l1 = []
##    for j in range(len(board)):
##        l1.append(board[j][i])
##    if duplicates(l1):
##        flag = True
##        break
##    else:
##        flag = False
##print(flag)



        
    
    
