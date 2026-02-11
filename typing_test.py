import time
import random

def typing_game():
    # 1. Game Content
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is an interpreted high-level programming language.",
        "Complexity is the enemy of execution.",
        "Code is like humor. When you have to explain it, it’s bad.",
        "Stay hungry, stay foolish."
    ]
    
    target = random.choice(sentences)
    
    print("--- ⌨️ HIGH-SPEED TYPIST ⌨️ ---")
    print("Type the following sentence exactly as it appears.")
    print("The timer starts as soon as you hit ENTER!")
    input("\nREADY? (Press Enter to start)")

    # 2. Timing the Input
    start_time = time.time()
    user_input = input(f"\nTARGET: {target}\nINPUT : ").strip()
    end_time = time.time()

    # 3. Calculations
    total_time = round(end_time - start_time, 2)
    
    # Calculate Accuracy
    correct_chars = 0
    for i in range(min(len(target), len(user_input))):
        if target[i] == user_input[i]:
            correct_chars += 1
    
    accuracy = (correct_chars / len(target)) * 100
    
    # Calculate WPM (Standard: 5 characters = 1 word)
    wpm = (len(user_input) / 5) / (total_time / 60)

    # 4. Results
    print(f"\n{'-'*30}")
    print(f"⏱️  Time: {total_time} seconds")
    print(f"🎯 Accuracy: {accuracy:.1f}%")
    print(f"🚀 Speed: {round(wpm, 1)} WPM")
    print(f"{'-'*30}")

    if accuracy == 100 and wpm > 60:
        print("🔥 GODLIKE SPEED! You're a pro.")
    elif accuracy > 90:
        print("✨ Great job! Very accurate.")
    else:
        print("⚠️  Keep practicing! Focus on accuracy first.")

typing_game()
