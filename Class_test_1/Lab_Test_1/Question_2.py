# /c:/Users/Madhu/OneDrive/Pictures/Desktop/AIAP/Class_test_1/Lab_Test_1/Question_2.py

def main():
    students = {"Madhu": 67, "Nethaji": 89, "Shiva kiran": 45, "Suganth": 76}
    marks = list(students.values())
    mean_mark = sum(marks) / len(marks)

    print(f"Mean mark: {mean_mark:.2f}\n")
    print("Students who scored above the mean:")
    for name, mark in students.items():
        if mark > mean_mark:
            print(f"{name}: {mark}")

if __name__ == "__main__":
    main()