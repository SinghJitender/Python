'''
Question :
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format
Print the runner-up score.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5
'''

n = int(input())
arr =  input().split(" ")
arr = [ int(i) for i in arr]
arr.sort(reverse=True)
for n in range(1,len(arr)):
    if(arr[n]==arr[n-1]):
        continue
    elif (arr[n] != arr[n-1]):
        print(arr[n])
        break
    if (n+1 == len(arr)-1):
        print(arr[n])