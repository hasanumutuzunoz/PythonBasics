#bmi (body mass index) = weight in kg / (height * height in meters)
def calculateBMI(height, weight):
    heightInMeters = height * 0.4536
    bmi = weight / (heightInMeters * heightInMeters)
    return bmi

print("BMI : ", calculateBMI(6.2, 85))