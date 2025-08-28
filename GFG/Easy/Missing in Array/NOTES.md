
          Missing in Array

          - Summary: The code uses an integer array to store input numbers. It leverages the bitwise XOR operation. First, it XORs all numbers from 1 to n (where n is the expected array length including the missing number). Then, it XORs all the elements present in the input array with the previously calculated XOR value. The final XOR result gives the missing number because XORing a number with itself results in 0, leaving only the missing number.

          - Time Complexity: O(n) because the code iterates through the array of size n once and then iterates from 1 to n once, resulting in a total of 2n iterations. The XOR operation is considered O(1).
          - Space Complexity: O(1) because the code uses a constant amount of extra space to store variables like n and xor, irrespective of the input array's size.
          