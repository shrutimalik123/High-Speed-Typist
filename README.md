# ⌨️ High-Speed Typist - Performance Metrics Sim

A professional-grade typing speed and accuracy tester. This project challenges players to replicate complex sentences under pressure, providing detailed post-run analytics including Words Per Minute (WPM), total time elapsed, and character-level accuracy.

This project focuses on teaching:
* **Real-Time Benchmarking:** Using the `time` module to calculate precise durations.
* **Metric Conversion:** Implementing standard typing industry formulas (e.g., 5 characters = 1 word).
* **String Comparison Algorithms:** Iterating through two strings to find character-level discrepancies.
* **Conditional Formatting:** Using f-strings to display clean, rounded float values for a polished UI.

---

## ✨ Features

* **Dynamic Text Bank:** Randomly selects from a library of sentences to keep the test fresh.
* **Standardized WPM:** Uses the universal typing formula: `(Characters / 5) / (Time in Minutes)`.
* **Character-Level Validation:** Tracks exactly how many characters were correct, even if the user typed more or fewer than required.
* **Instant Feedback:** Categorizes player performance into skill tiers (e.g., "Godlike Speed" vs. "Needs Practice").

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `typing_test.py`.
2.  **Open Terminal:** Navigate to the project folder.
3.  **Run the Script:**
    ```bash
    python typing_test.py
    ```

### 3. Gameplay Instructions
1.  **Get Ready:** A sentence will appear on the screen.
2.  **Start Typing:** As soon as you hit Enter to clear the prompt, the clock starts.
3.  **Finalize:** Type the sentence as fast and accurately as possible, then hit Enter to see your stats.



---

## 🧠 Code Structure Highlights

### Safe String Comparison
To avoid a `list index out of range` error, we use `min()` to compare the length of the target sentence and the user's input. This ensures the loop stops as soon as the shortest string ends.

```python
# Prevents crashing if the user types fewer characters than the target
for i in range(min(len(target), len(user_input))):
    if target[i] == user_input[i]:
        correct_chars += 1

