# 📝 class Solution {  public:    vector<int> lcmAndGcd(int a, int b) {        // code here        int g = gcd (a,b);        return {(a*b)/g,g};    }        int gcd(int a , int b ){        if(a==0){            return b;        }                return gcd(b%a,a);    }};  very easy solution (GeeksforGeeks)

🔗 [Problem Link](https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1)

![Difficulty](https://img.shields.io/badge/Difficulty-Uncategorized-lightgrey) ![Language](https://img.shields.io/badge/Language-Python-blue)

### 💡 Tags
GFG Problem

### 🚀 Performance
- **Runtime:** Successfully Evaluated
- **Memory:** N/A

---

### 📜 Problem Description

Description not found