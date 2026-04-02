Matrix Diagonal Comparison
Given an integer matrix of size N x N, the program must print yes if all the elements of the left diagonal are present in the right diagonal and also all the elements of the right diagonal are present in the left diagonal. Otherwise, print no.
📥 Input Format
The first line contains N.
The next N lines contain the matrix elements.
📤 Output Format
The first line contains yes or no.
💡 Example Input/Output 1
Input:
text
3
12 34 56
78 90 29
12 68 56
Use code with caution.

Output:
text
yes

Explanation:
Left diagonal elements: {12, 90, 56}
Right diagonal elements: {56, 90, 12}
Since both sets contain the same elements, the output is yes.
💡 Example Input/Output 2
Input:
text
4
27 91 78 34
1 13 12 7
18 54 64 73
72 67 77 8

Output:
text
no

Explanation:
Left diagonal elements: {27, 13, 64, 8}
Right diagonal elements: {34, 12, 54, 72}
The elements do not match, so the output is no.
<img width="905" height="727" alt="Screenshot 2026-04-03 014527" src="https://github.com/user-attachments/assets/f4e28948-c60d-4f68-bda7-367eb7820784" />

