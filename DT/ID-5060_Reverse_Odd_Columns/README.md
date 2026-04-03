# 🔁 Reverse Odd Columns in Matrix

## 📌 Problem Statement
Given a matrix of size **N × N**, reverse the columns present in **odd positions** (1-based indexing) and print the resulting matrix.

---

## 🧠 Concept
- Consider **1-based indexing**:
  - 1st column → reverse  
  - 3rd column → reverse  
  - 5th column → reverse  
- Even-positioned columns remain unchanged.
- Reversing a column means swapping elements from **top to bottom**.

---

## 📥 Input Format
- First line: Integer `N`
- Next `N` lines: Matrix elements

---

## 📤 Output Format
- Print the modified matrix

---

## 🔒 Constraints: 1 ≤ N ≤ 100

---

## 🧪 Example 1

### Input:
3
123
456
789


### Matrix Representation

1 2 3
4 5 6
7 8 9


### Output

729
456
183


---

## 🧪 Example 2 (Space-Separated Matrix)

### Input

4
12 56 89 555
76 332 22 17
77 33 77 99
56 56 29 48


### Output

56 56 29 555
77 332 77 17
76 33 22 99
12 56 89 48

##Intuition:
for every odd column, every matrix run i loop ply till half of the matrix len and for loop edge case handles index.
Then swap the row wise values.since the for loop runs only half the rows we wont repeat actions. 
