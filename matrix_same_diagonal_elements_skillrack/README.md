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
```text
3
12 34 56
78 90 29
12 68 56

yes
4
27 91 78 34
1 13 12 7
18 54 64 73
72 67 77 8
no

Explanation:
Left diagonal elements: {27, 13, 64, 8}
Right diagonal elements: {34, 12, 54, 72}
The elements do not match, so the output is no.
