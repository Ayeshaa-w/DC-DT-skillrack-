## 🧩 Find Numbers with Even Number of Digits

### 📘 Problem Statement  
Given an integer array `nums`, return all the numbers that contain an **even number of digits**.

---

### 🔹 Input  
- An integer array `nums`  
- `1 <= nums.length <= 500`  
- `-10^5 <= nums[i] <= 10^5`

---

### 🔹 Output  
- A list of integers from `nums` having an even number of digits  

---

### 🔹 Example  

**Input:**
```text
nums = [12, 345, 2, 6, 7896]
```

**Output:**
```text
[12, 7896]
```

---

### 🔹 Explanation  
- 12 → 2 digits ✅  
- 345 → 3 digits ❌  
- 2 → 1 digit ❌  
- 6 → 1 digit ❌  
- 7896 → 4 digits ✅  

---

### 🔹 Approach  
- Traverse each number in the array  
- Count digits (ignore sign for negative numbers)  
- If digit count is even → include in result  

---

---

### 🔹 Complexity Analysis  
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1) (excluding output list)

---

### 🔹 Follow-up  
- Solve the problem without converting numbers to strings  
