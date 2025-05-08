def calculate_bmi(height, weight):
    print("Height=" + str(height))
    print("weight=" + str(weight))
    bmi = weight / (height * height)
    print ("BMI=" + str(bmi))

    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight") 
    elif 25 <= bmi < 29.9:
        print("Overweight")
    else:
        print("Obesity")




calculate_bmi(weight=57, height=1.73)   

