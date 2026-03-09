## 🧠 Project Euler

Solutions to problems from **[Project Euler](https://projecteuler.net/)**.

Project Euler problems combine mathematics, algorithms, and programming, making them a great way to sharpen problem-solving skills. This repo acts as a small learning log where I share my approaches, methods, and things I learn while solving them.

---

### 📊 Recent Work

Here’s a concise entry that matches the style of the rest of your repo.

#### Problem 31 — *Coin Sums*

- The task is to determine **how many different ways £2 can be made using UK coins** (1p, 2p, 5p, 10p, 20p, 50p, £1, £2). 📄 [Problem Statement](problems/31/statement.md). 💻 [Solution](problems/31/solution.py)
- The approach taken uses a **recursive search over coin denominations**. At each step, the recursive function effectively "fixes" how many coins of the current denomination are used, and recursively solves the remaining value using the other coin types. 
- An initial idea was to generate all possible combinations of coin counts using a **cartesian product**. However, the number of candidate combinations grows extremely large, making this approach impractical.

#### Problem 23 — *Non-Abundant Sums*

- The task is to find the **sum of all positive integers which cannot be written as the sum of two abundant numbers**. 📄 [Problem Statement](problems/23/statement.md). 💻 [Solution](problems/23/solution.py)
- My approach consisted of three main steps:
  1. **Identify abundant numbers:** Compute all abundant numbers up to the known upper bound given in the problem ($28{,}123$). Above this limit, it is known that every integer can be written as the sum of two abundant numbers.
  2. **Generate abundant sums:** Using the list of abundant numbers, compute all pairwise sums that do not exceed the upper bound.
  3. **Take the complement:** Determine which integers up to the bound do **not** appear in the set of abundant sums; these are exactly the numbers that cannot be expressed as the sum of two abundant numbers.
- Before settling on this approach, the **On-Line Encyclopedia of Integer Sequences** entry for [odd abundant numbers](https://oeis.org/wiki/Odd_abundant_numbers#cite_note-1) was reviewed to see whether a method using arithmetic sequence could generate all abundant numbers directly. However, no sequence was found that captured all cases. As a result, the approach above turned out to be both straightforward and efficient, especially given the known upper bound in the problem.

#### Problem 11 — *Largest Product in a Grid*

- The challenge is to find the **largest product of four adjacent numbers** in a $20 \times 20$ grid (horizontal, vertical, diagonal, or anti-diagonal). 📄 [Problem Statement](problems/11/statement.md). 💻 [Solution](problems/11/solution.py)
- My approach was two simple steps:
  1. Extract all candidate 1D arrays (rows, columns, diagonals, anti-diagonals).
  2. Scan each array using a length-4 sliding window, compute each subarray product, and track the maximum.
- The solution runs in $\mathcal{O}(n^2)$ time. There are about $\mathcal{O}(n)$ candidate 1D arrays, and for each array we check $\mathcal{O}(n)$ length-4 subarrays, giving a total of $\mathcal{O}(n) \times \mathcal{O}(n) = \mathcal{O}(n^2)$.
- The approach was loosely inspired by the [maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem) (often solved with **Kadane's algorithm**). While this problem focuses on products rather than sums, the idea of scanning arrays and evaluating subarrays is conceptually similar.

---