### Python Code: password_checker.py

import re

def check_password_strength(password):
    strength_criteria = {
        "Length (8+ chars)": len(password) >= 8,
        "Uppercase Letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase Letter": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"\d", password)),
        "Special Character (@, #, $, %, etc.)": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }
    
    passed_criteria = sum(strength_criteria.values())
    total_criteria = len(strength_criteria)
    
    if passed_criteria == total_criteria:
        strength = "Strong ✅"
        feedback = "Your password is strong. Keep it safe!"
    elif passed_criteria >= 3:
        strength = "Moderate ⚠️"
        feedback = "Your password is okay, but consider adding more complexity."
    else:
        strength = "Weak ❌"
        feedback = "Your password is weak! Use a mix of letters, numbers, and special characters."
    
    return strength, feedback, strength_criteria

def main():
    print("____Password Complexity Checker____")
    password = input("Enter a password: ")

    strength, feedback, criteria = check_password_strength(password)
    
    print("\nPassword Strength: ", strength)
    print("Feedback: ", feedback)
    print("\nCriteria Breakdown:")
    for criterias, passed in criteria.items():
        print(f"✅ {criterias}" if passed else f"❌ {criterias}")

if __name__ == "__main__":
    main()
