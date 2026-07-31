# 📝 Equal Sum (GeeksforGeeks)

🔗 [Problem Link](https://www.geeksforgeeks.org/problems/equal-sum0810/1)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange) ![Language](https://img.shields.io/badge/Language-Python-blue)

### 💡 Tags
Arrays

### 🚀 Performance
- **Runtime:** Successfully Evaluated
- **Memory:** N/A

---

### 📜 Problem Description

Given an array  **a**  **rr** . Determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right.

If there are no elements to the left/right, then the sum is considered to be zero.

**Examples:**

```
Input: arr[] = [1, 2, 3, 3]
Output: true
Explanation: Consider 1-based indexing i = 3, for [1, 2] sum is 3 and for [3] sum is also 3.

```

```
Input: arr[] = [1, 5]
Output: false
Explanation: No such index present.

```

**Constraints:** 
1 ≤ arr.size() ≤ 105 
1 ≤ arr[i] ≤ 106