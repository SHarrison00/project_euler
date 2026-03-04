## 🧠 Project Euler

Solutions to problems from **[Project Euler](https://projecteuler.net/)**.

Project Euler problems combine mathematics, algorithms, and programming, making them a great way to sharpen problem-solving skills. This repo acts as a small learning log where I share my approaches, methods, and things I learn while solving them.

---

### 📊 Recent Work

#### Problem 11 — *Largest Product in a Grid*

- The challenge is to find the **largest product of four adjacent numbers** in a $20 \times 20$ grid (horizontal, vertical, diagonal, or anti-diagonal). 📄 [Problem Statement](problems/11/statement.md). 💻 [Solution](problems/11/solution.py)
- My approach was two simple steps:
  1. Extract all candidate 1D arrays (rows, columns, diagonals, anti-diagonals).
  2. Scan each array using a length-4 sliding window, compute each subarray product, and track the maximum.
- The solution runs in $\mathcal{O}(n^2)$ time. There are about $\mathcal{O}(n)$ candidate 1D arrays, and for each array we check $\mathcal{O}(n)$ length-4 subarrays, giving a total of $\mathcal{O}(n) \times \mathcal{O}(n) = \mathcal{O}(n^2)$.
- The approach was loosely inspired by the [maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem) (often solved with **Kadane's algorithm**). While this problem focuses on products rather than sums, the idea of scanning arrays and evaluating subarrays is conceptually similar.

---