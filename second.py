def calculate_grade():
    print("Welcome to the Student Grade Calculator!")
    
    
    num_subjects = int(input("Enter the number of subjects: "))
    total_marks = 0
    
    
    for i in range(1, num_subjects + 1):
        while True:
            try:
                marks = float(input(f"Enter marks obtained in Subject {i} (out of 100): "))
                if marks < 0 or marks > 100:
                    raise ValueError("Marks should be between 0 and 100.")
                total_marks += marks
                break
            except ValueError as e:
                print(e)
    
    
    average_percentage = (total_marks / (num_subjects * 100)) * 100
    
    
    def assign_grade(percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"
    
    
    grade = assign_grade(average_percentage)
    
    
    print("\n--- Results ---")
    print(f"Total Marks: {total_marks}")
    print(f"Average Percentage: {average_percentage:.2f}%")
    print(f"Grade: {grade}")


calculate_grade()
