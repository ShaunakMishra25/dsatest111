
          Two Sum

          - Summary: This algorithm utilizes a hash map (dictionary in Python) to efficiently find two numbers within a list that sum up to a specified target. It iterates through the input list, calculating the complement needed to reach the target for each number. If the complement is already present in the hash map, it means the pair has been found, and their indices are returned. Otherwise, the number and its index are added to the hash map for later lookup. This approach avoids nested loops, resulting in linear time complexity.

          - Time Complexity: O(n), where n is the length of the input list. This is because the algorithm iterates through the list once.  Hash map lookups (in and insertion) take constant time on average.
          - Space Complexity: O(n) in the worst case, where n is the length of the input list. This is because the hash map could potentially store all the numbers from the input list if no pair is found early on.
          