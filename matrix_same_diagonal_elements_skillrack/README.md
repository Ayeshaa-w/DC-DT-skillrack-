# 🔍 Matrix Diagonal Comparison

Given an integer matrix of size **N x N**, print **`yes`** if all the elements of the left diagonal are present in the right diagonal **and** all the elements of the right diagonal are present in the left diagonal. Otherwise, print **`no`**.

---

## ⚙️ Boundary Condition(s)
* N ≥ 1 (matrix is square)

---

## 📥 Input Format
1. The first line contains **N**.  
2. The next **N** lines contain the matrix elements, space-separated.

---

## 📤 Output Format
- The first line contains **`yes`** or **`no`**.

---

## 💡 Example Input/Output 1

**Input:**
3
12 34 56
78 90 29
12 68 56

**Output:**

**Explanation:**  
Left diagonal elements: `{12, 90, 56}`  
Right diagonal elements: `{56, 90, 12}`  
Since both sets contain the same elements, the output is **`yes`**.

---

## 💡 Example Input/Output 2

**Input:**
<img width="905" height="727" alt="Screenshot 2026-04-03 014527" src="https://github.com/user-attachments/assets/f4e28948-c60d-4f68-bda7-367eb7820784" />

