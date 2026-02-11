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

##
##board = [["1","2",".",".","9",".",".",".","."],
## ["2",".",".","5",".",".",".",".","."],
## [".","9","8",".",".",".",".",".","3"],
## ["3",".",".",".","6",".",".",".","1"],
## [".",".",".","8",".","3",".",".","5"],
## ["7",".",".",".","2",".",".",".","6"],
## [".",".",".",".",".",".","2",".","."],
## [".",".",".","4","1","9",".",".","8"],
## [".",".",".",".","8",".",".","9","7"]]
##
###print(board[2][1])
##
##def digit_check(l1):
##    arr = ['1','2','3','4','5','6','7','8','9','.']
##        for i in l1:
##            if i not in arr:
##                return False
##            else:
##                return True
##
###Duplicates present -> True else False
##def duplicates(l1):
##    counts = {}
##    flag = True
##    for i in l1:
##        if i not in counts.keys():
##            counts[i] = 1
##        else:
##            counts[i] = counts[i] + 1
##
##    if '.' in counts:
##        counts['.'] = 0
##        
##    #print(counts)
##    for j in counts.keys():
##        #print(j)
##        if counts[j] > 1:
##            flag = True
##            break
##        else:
##            flag = False
##    return flag
##
##
#####Row wise duplicates
###valid row -> No duplicate and valid char -> True else False
##row_flag = True
##for i in range(len(board)):
##    #print(board[i])
##    if (duplicates(board[i]) == True) or (digit_check(board[i]) == False):
##        row_flag = False
##        break
##    else:
##        row_flag = True
###print(row_flag)
##
#######Column wise duplicates
###valid column -> No duplicates -> True else False
##col_flag = True
##for i in range(len(board)):
##    l1 = []
##    for j in range(len(board)):
##        l1.append(board[j][i])
##    if duplicates(l1):
##        col_flag = False
##        break
##    else:
##        col_flag = True
###print(col_flag)
##
##
#####3X3 duplicates
##arr1 = []
##small_flag = True
##for i in [0,3,6]:
##    for j in [0,3,6]:
##        arr1.append([i,j])
##
##for i in arr1:
##    a = []
##    for k in range(i[0], i[0]+3):
##        for p in range(i[1], i[1]+3):
##            a.append(board[k][p])
##
##    if duplicates(a):
##        small_flag = False
##        #print(a)
##        break
##    else:
##        small_flag = True
##
###print(small_flag)
##valid_sudoku = False
##if (row_flag == True) and (col_flag == True) and (small_flag == True):
##    valid_sudoku = True
##else:
##    valid_sudoku = False
##
##print(valid_sudoku)
##
##
##
###Function to check if the sudoku is valid
##class Solution:
##    def isValidSudoku(self, board: List[List[str]]) -> bool:
##        #Row wise checking
##        row_flag = True
##        for i in range(len(board)):
##            #print(board[i])
##            #Duplicate checking
##            counts = {}
##            flag = True
##            for k in board[i]:
##                if k not in counts.keys():
##                    counts[k] = 1
##                else:
##                    counts[k] = counts[k] + 1
##
##            if '.' in counts:
##                counts['.'] = 0
##                
##            #print(counts)
##            for j in counts.keys():
##                #print(j)
##                if counts[j] > 1:
##                    flag = True
##                    break
##                else:
##                    flag = False
##            #Character checking
##            char_flag = True
##            arr = ['1','2','3','4','5','6','7','8','9','.']
##            for i in board[i]:
##                if i not in arr:
##                    char_flag = False
##                else:
##                    char_flag = True
##                       
##            if (flag == True) or (char_flag == False):
##                row_flag = False
##                break
##            else:
##                row_flag = True
##        
##        #Column wise checking
##        col_flag = True
##        for i in range(len(board)):
##            l1 = []
##            for j in range(len(board)):
##                l1.append(board[j][i])
##            
##            counts = {}
##            flag = True
##            for i in l1:
##                if i not in counts.keys():
##                    counts[i] = 1
##                else:
##                    counts[i] = counts[i] + 1
##
##            if '.' in counts:
##                counts['.'] = 0
##                
##            #print(counts)
##            for j in counts.keys():
##                #print(j)
##                if counts[j] > 1:
##                    flag = True
##                    break
##                else:
##                    flag = False
##            if flag:
##                col_flag = False
##                break
##            else:
##                col_flag = True
##        
##        #3x3 board checking
##        arr1 = []
##        small_flag = True
##        for i in [0,3,6]:
##            for j in [0,3,6]:
##                arr1.append([i,j])
##
##        for i in arr1:
##            a = []
##            for k in range(i[0], i[0]+3):
##                for p in range(i[1], i[1]+3):
##                    a.append(board[k][p])
##
##            counts = {}
##            flag = True
##            for i in a:
##                if i not in counts.keys():
##                    counts[i] = 1
##                else:
##                    counts[i] = counts[i] + 1
##
##            if '.' in counts:
##                counts['.'] = 0
##                
##            #print(counts)
##            for j in counts.keys():
##                #print(j)
##                if counts[j] > 1:
##                    flag = True
##                    break
##                else:
##                    flag = False
##
##            if flag:
##                small_flag = False
##                #print(a)
##                break
##            else:
##                small_flag = True
##
##        #Valid sudoku logic
##        valid_sudoku = False
##        if (row_flag == True) and (col_flag == True) and (small_flag == True):
##            valid_sudoku = True
##        else:
##            valid_sudoku = False
##        
##        return valid_sudoku
    

                
##nums = [1,2,3,3,3]                    
##count = {}
##for i in nums:
##    if i not in count:
##        count[i] = 1
##    else:
##        count[i] = count[i] + 1
##        
##for j in count:
##    if count[j] > 1:
##        print(True)
##    else:
##        print(False)

##strs = ["act","pots","tops","cat","stop","hat"]
###strs = ["x"]
##def valid_anagram(s, t):
##    if len(s) != len(t):
##        return False
##
##    s_d = {}
##    t_d = {}
##    for i in range(len(s)):
##        if s[i] not in s_d:
##            s_d[s[i]] = 1
##        else:
##            s_d[s[i]] = s_d[s[i]] + 1
##
##    for j in range(len(t)):
##        if t[j] not in t_d:
##            t_d[t[j]] = 1
##        else:
##            t_d[t[j]] = t_d[t[j]] + 1
##
##    if s_d == t_d:
##        return True
##    else:
##        return False
##
##seen = [False] * len(strs)
##op = []
##for i in range(len(strs)):
##    if seen[i]:
##        #print(seen[i])
##        continue
##
##    a = [strs[i]]
##    #print(a)
##    seen[i] = True
##
##    for j in range(i+1,len(strs)):
##         if not seen[j] and valid_anagram(strs[i],strs[j]):
##             #print(strs[j])
##             a.append(strs[j])
##             seen[j] = True
##    #print(a)
##
##    op.append(a)
##
##return op
##
##
##
##
##l = [10,8,7,5,2]
##
###Checking if the prices drop every day
##desc_flag = True
##for i in range(len(l)):
##    for j in range(i,len(l)):
##        if l[i] < l[j]:
##            desc_flag = False
##            break
##
##p_dict = {}
##max_profit = 0
##for i in range(len(l)):
##    for j in range(i,len(l)):
##        p_dict[(l[i],l[j])] = l[j] - l[i]
##
##if desc_flag == True:
##    max_profit = 0
##else:
##    for i in p_dict:
##        if p_dict[i] > max_profit:
##            max_profit = p_dict[i]
##
##print(max_profit)


s = "[(])"
dict = {'(':')', '[':']', '{':'}'}
rev = s[-1::-1]
seen = []
valid_s = True
for j in dict:
    for i in range(len(s)):
        print(s[i])
        print(rev[i])
        if (s[i] not in seen) and (s[i] == j and rev[i] != dict[j]):
            valid_s = False
            break
        else:
            valid_s = True


print(valid_s)
            
        

    
    

            
            

        
    
    
