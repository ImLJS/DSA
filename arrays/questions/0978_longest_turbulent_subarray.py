# Longest Turbulent Subarray - LeetCode 978 - Medium

# https://leetcode.com/problems/longest-turbulent-subarray/

# Used to find the length of the longest turbulent subarray in an array. A subarray is turbulent if the comparison sign between each pair of adjacent elements alternates. For example, [9,4,2,10,7] is turbulent because 9 > 4 < 2 < 10 > 7. The function uses a sliding window approach to keep track of the current turbulent subarray and updates the maximum length found so far. 

# Example:
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: The longest turbulent subarray is [4,2,10,7,8] of length 5.

# Time Complexity: O(n)
# Space Complexity: O(1)

def maxTurbulenceSize(arr):
    L, R = 0, 1 # Initialize left and right pointers
    res = 1 # Initialize result to 1
    prev = "" # Initialize previous comparison sign

    while R < len(arr):
        if arr[R-1] > arr[R] and prev != ">":
            res = max(res, R - L + 1)
            prev = ">"
            R += 1
        elif arr[R-1] < arr[R] and prev != "<":
            res = max(res, R - L + 1)
            prev = "<"
            R += 1
        else:
            R  = R + 1 if arr[R-1] == arr[R] else R
            L = R - 1
            prev = ""
    
    return res

# Example usage
if __name__ == "__main__":
    arr = [9,4,2,10,7,8,8,1,9]
    print(maxTurbulenceSize(arr))  # Output: 5
    arr = [4,8,12,16]
    print(maxTurbulenceSize(arr))  # Output: 2
    arr = [100]
    print(maxTurbulenceSize(arr))  # Output: 1

