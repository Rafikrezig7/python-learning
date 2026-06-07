# 📘 Day 13 — NumPy (Numeric Python)

> **"NumPy array is a list, pro max."**

This notebook covers the core building blocks of NumPy — Python's most powerful library for numerical computing. By the end of this day, you should be comfortable creating, manipulating, and analyzing n-dimensional arrays.

---

## 🧠 What is NumPy?

**NumPy** (Numeric Python) provides the `ndarray` — an **n-dimensional array** that is faster, more memory-efficient, and far more feature-rich than a regular Python list.

---

## 📚 Topics Covered

### 1. 🔨 Array Creation
| Method | Description |
|---|---|
| `np.array([...])` | Create array from a list |
| `np.arange(start, stop, step)` | Range-based array |
| `np.zeros((rows, cols))` | Array filled with 0s |
| `np.full((rows, cols), value)` | Array filled with a constant |

### 2. 🧭 Array Properties
- `.shape` — dimensions of the array (like `len()` but for N-D)
- `.ndim` — number of dimensions

### 3. ✂️ Slicing & Indexing
```python
array[start:end:step]        # 1D slicing
array[row_start:, col_start:] # 2D slicing
array[1, 2, 2]               # 3D indexing
```

### 4. ➕ Arithmetic
- **Scalar arithmetic** — `+`, `-`, `*`, `/`, `**`, `%` applied element-wise
- **Element-wise arithmetic** — operations between two same-shaped arrays
- **Vectorized functions** — `np.sqrt()`, `np.round()`, `np.pi`
- **Comparison operators** — returns boolean arrays (e.g. `array > 2`)

### 5. 📡 Broadcasting
NumPy can multiply arrays of different shapes by "stretching" the smaller one:
```python
array1.shape  # (1, 10)
array2.shape  # (10, 1)
array1 * array2  # → (10, 10) multiplication table!
```

### 6. 📊 Aggregation Functions
| Function | Description |
|---|---|
| `np.sum(a, axis=...)` | Sum (axis=0: columns, axis=1: rows) |
| `np.mean(a)` | Average |
| `np.std(a)` | Standard deviation |
| `np.var(a)` | Variance |
| `np.min(a)` / `np.max(a)` | Min / Max value |
| `np.argmin(a)` / `np.argmax(a)` | Index of min / max |

### 7. 🎯 Boolean Indexing
```python
array[array < 18]           # flattens and filters — fast but loses shape
np.where(array >= 18, array, 0)  # ✅ preserves shape, replaces non-matches with 0
```

### 8. 🎲 Random Numbers
```python
rng = np.random.default_rng(seed=1)       # reproducible randomness
rng.integers(low=1, high=101, size=3)     # 3 random integers between 1–100
```

---

## 💡 Key Takeaways

- Use `np.where()` instead of boolean indexing when you want to **preserve array shape**.
- Broadcasting lets you do math on arrays with different shapes — think multiplication tables in one line.
- `axis=0` → operates **down columns**, `axis=1` → operates **across rows**.
- Always set a `seed` when using random numbers for reproducibility.

---

*Day 13 of the Python learning journey 🚀*