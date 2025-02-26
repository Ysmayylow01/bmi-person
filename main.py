from sklearn.linear_model import LinearRegression
import numpy as np

data = [
    {"age": 25, "weight": 70, "exercise_level": 7, "diet": 6, "bmi": 24.2},
    {"age": 30, "weight": 80, "exercise_level": 5, "diet": 7, "bmi": 27.0},
    {"age": 22, "weight": 60, "exercise_level": 8, "diet": 9, "bmi": 20.0},
    {"age": 40, "weight": 90, "exercise_level": 4, "diet": 5, "bmi": 29.0},
    {"age": 35, "weight": 75, "exercise_level": 6, "diet": 8, "bmi": 25.0},
    {"age": 50, "weight": 95, "exercise_level": 3, "diet": 4, "bmi": 31.0},
    {"age": 28, "weight": 72, "exercise_level": 6, "diet": 7, "bmi": 24.5},
    {"age": 32, "weight": 85, "exercise_level": 4, "diet": 6, "bmi": 27.5},
    {"age": 26, "weight": 68, "exercise_level": 7, "diet": 8, "bmi": 22.5},
    {"age": 45, "weight": 88, "exercise_level": 5, "diet": 7, "bmi": 28.0},
    {"age": 38, "weight": 80, "exercise_level": 6, "diet": 6, "bmi": 26.0},
    {"age": 23, "weight": 65, "exercise_level": 8, "diet": 9, "bmi": 21.5},
    {"age": 29, "weight": 77, "exercise_level": 5, "diet": 6, "bmi": 25.0},
    {"age": 33, "weight": 82, "exercise_level": 6, "diet": 7, "bmi": 26.5},
    {"age": 42, "weight": 93, "exercise_level": 4, "diet": 5, "bmi": 29.5},
    {"age": 36, "weight": 78, "exercise_level": 7, "diet": 7, "bmi": 24.0}
]

x = np.array([[entry["age"], entry["weight"], entry["exercise_level"], entry["diet"]] for entry in data])
y = np.array([entry["bmi"] for entry in data])

model = LinearRegression()
model.fit(x,y)

print("Maglumat giriz:")

age = float(input("age:"))
weight = float(input("weight:"))
exercise_level = float(input("exercise level:"))
diet = float(input("diet:"))

new_person = np.array([[age,weight,exercise_level,diet]])
predict = model.predict(new_person)

print(f"Predicted BMI for the person : {predict[0]:.2f}")