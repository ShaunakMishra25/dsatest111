
          Two Sum

          - Summary: This algorithm utilizes a hash map (dictionary in Python) to efficiently find two numbers within a list that add up to a target value. It iterates through the input list, calculating the complement needed to reach the target for each number. If the complement is found in the hash map, it means a pair has been identified, and their indices are returned. Otherwise, the current number and its index are added to the hash map for future checks.

          - Time Complexity: O(n) because the algorithm iterates through the input list once.  Hash map lookups are O(1) on average.
          - Space Complexity: O(n) because in the worst case, the hash map might store all the numbers from the input list.
          