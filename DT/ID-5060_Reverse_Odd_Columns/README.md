🔁 Reverse Odd Columns in Matrix
📌 Problem Statement

Given a matrix of size N × N, reverse the columns present in odd positions (1-based indexing) and print the resulting matrix.

🧠 Concept
Columns are considered odd-positioned using 1-based indexing:
1st column → reverse
3rd column → reverse
5th column → reverse
Even-positioned columns remain unchanged.
Reversing a column means swapping elements top to bottom.
📥 Input Format
First line: Integer N (size of matrix)
Next N lines: Matrix elements
📤 Output Format
Print the modified matrix after reversing odd columns
🔒 Constraints
1 ≤ N ≤ 100
🧪 Example 1
Input
3
123
456
789
Output
729
456
183
🧪 Example 2
Input
4
12 56 89 555
76 332 22 17
77 33 77 99
56 56 29 48
Output
56 56 29 555
77 332 77 17
76 33 22 99
12 56 89 48
