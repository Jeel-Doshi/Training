### Slice list into 3 equal chunks and reverse each 


Input : List of integers

Output : Reversed chunks list


| Input                               | Output                                    |
| ------                              | ------                                    |
| [11, 45, 8, 23, 14, 12, 78, 45, 89] | [[8, 45, 11], [12, 14, 23], [89, 45, 78]] |
| [1, 2, 3, 4, 5, 6]                  | [[3, 2, 1], [6, 5, 4]]                    |


### Count the occurrence of each element from a list


Input : List of integers

Output : dict with count of occurence


| Input                               | Output                               |
| ------                              | ------                               |
| [11, 45, 8, 23, 14, 12, 78, 45, 89] | {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}   |
| [1, 2, 3, 4, 5, 6, 2, 3, 1]         | {1: 2, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1} |


### Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.


Input : List of tuples

Output : Sorted list of tuples with sorting key as last element of tuple


| Input                                    | Output                                   |
| ------                                   | ------                                   |
| [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] | [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] |


### Find the intersection (common) of two sets and remove those elements from the first set


Input : Two different sets

Output : Intersection of two sets and first set with removed element of intersection


| Input         | Output       |
| ------        | ------       |
| {1,2,5,4,3,6} | {1, 4, 5, 6} | 
  {4,5,8,9,6,1} |              |
|               | {2, 3}       |


### Create a function to reverse the entire list without any function and also do not use any slicing shortcut


Input : List of integers

Output : Reversed list


| Input              | Output             |
| ------             | ------             |
| [1, 2, 3, 4, 5, 6] | [6, 5, 4, 3, 2, 1] | 


### Convert any lower case string to upper case without in-built python functions


Input : Any lower case string

Output : Same string with uppercase letters


| Input      | Output     |
| ------     | ------     |
| abcdef ghi | ABCDEF GHI |


### Return the sum of duplicates elements from the given List


Input : List of integers

Output : Sum pf duplicate elements


| Input                      | Output |
| ------                     | ------ |
| [3, 5, 6, 11, 12, 3, 5, 2] |   8    |


### Count the subsequence “AG” in the given string

Input : String

Output : Count of subsequence


| Input               | Output |
| ------              | ------ |
| BCAHGBNAJKGTYUALKWG | 6      |


### Find the max sum of subarray

Input : Array of integers

Output : Sum of any subarray


| Input                         | Output |
| ------                        | ------ |
| [-2, -3, 4, -1, -2, 1, 5, -3] | 7      |


### Sort given array of three random elements. 0,1 & 2. Without any sorting algorithm. Time complexity: O(n)


Input : Array of three random numbers

Output : Sorted array

| Input                             | Output |
| ------                            | ------ |
| [1, 0, 2, 2, 0, 1, 0, 1, 2, 0, 0] | [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2] |


### Return product of minimum of odd and maximum of even from a given list. do not use in-built min/max function


Input : List of integers

Output : Integer

| Input                             | Output |
| ------                            | ------ |
| [7, 5, 2, 3, 12, 9, 15, 24]       | 72     |


### Create a simulation program for the Hot Potato Game. You can develop with your ideas. Just take care of the following things:
###  At least one person must be removed from each round.
###  Display name in the console that the user has a hot potato.
###  Each user holds a potato for random seconds between 0.1 to 3.0.
###  Each round starts after 3 seconds of the previous elimination.
###  Each round stops at random seconds between 5 to 20.
###  Display the name of the winner.


Input : Name of players

Output : Winner of Hot Potato Game

| Input                                                              | Output                 |
| ------                                                             | ------                 |
| ['Tom', 'Jerry', 'Oggy', 'Bheem', 'Nobita', 'Shinchan', 'Doremon'] | Jerry won the Game...! |


### Return the array which contains the elements that are greater than from its right side elements


Input : Name of players

Output : Winner of Hot Potato Game

| Input            | Output     |
| ------           | ------     |
| [5, 17, 2, 6, 3] | [17, 6, 3] |
| [3, 14, 3, 7, 2] | [14, 7, 2] |


### Add 1 to the given list of elements. Do not use string conversion, number conversion


Input : List of integers

Output : List with one added 

| Input        | Output       |
| ------       | ------       |
| [1, 9, 9, 9] | [2, 0, 0, 0] |


### Calculate the sum of the major and minor diagonals of the given matrix


Input  : Matrix of size NxN

Output : Sum of major and minor diagnoals of giveb matrix 

| Input                              | Output       |
| ------                             | ------       |
| [ [2, 0, 7],[4, 1, 9],[8, 1, -1] ] | 2, 16        |



### Find the elements of the given list which are exactly the same as the entire product of the list except itself


Input  : List of integers

Output : Element from list which is product of entire list except itself 

| Input             | Output  |
| ------            | ------  |
| [1, 5, 1, 10, 50] | 50      |
| [1, 2, 4, 8, 1]   | 8       |


### Print reverse string using recursion


Input  : Input string

Output : Reversed string 

| Input           | Output       |
| ------          | ------       |
| helloworld      | dlrowolleh   |
| good morning    | gninrom doog |


### Find maximum sum of triplets in an array such than i < j < k and a[ i ] < a[ j ] < a[ k ]


Input  : List of integers

Output : Maximum sum of triplets with condition as i < j < k and a [ i ] < a[ j ] < a [ k ] 

| Input              | Output |
| ------             | ------ |
| [2, 5, 3, 1, 4, 9] | 16     |


### Find the majority element of the given list.
### Majority element: count of the element > N/2
### N = length of list

                    
Input  : List of integers

Output : Majority element count 

| Input                             | Output |
| --------------------------------- | ------ |
| [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5] | 5      |
