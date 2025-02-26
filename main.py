import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare the data and model
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
model.fit(x, y)

# Function to predict BMI
def predict_bmi():
    try:
        age = float(age_entry.get())
        weight = float(weight_entry.get())
        exercise_level = float(exercise_level_entry.get())
        diet = float(diet_entry.get())

        new_person = np.array([[age, weight, exercise_level, diet]])
        predict = model.predict(new_person)

        result_label.config(text=f"Predicted BMI: {predict[0]:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numerical values for all fields.")

# Create the main window
root = tk.Tk()
root.title("BMI Prediction")

# Create and place the widgets
age_label = tk.Label(root, text="Age:")
age_label.grid(row=0, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1, padx=10, pady=5)

weight_label = tk.Label(root, text="Weight:")
weight_label.grid(row=1, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

exercise_level_label = tk.Label(root, text="Exercise Level:")
exercise_level_label.grid(row=2, column=0, padx=10, pady=5)
exercise_level_entry = tk.Entry(root)
exercise_level_entry.grid(row=2, column=1, padx=10, pady=5)

diet_label = tk.Label(root, text="Diet (1-10):")
diet_label.grid(row=3, column=0, padx=10, pady=5)
diet_entry = tk.Entry(root)
diet_entry.grid(row=3, column=1, padx=10, pady=5)

predict_button = tk.Button(root, text="Predict BMI", command=predict_bmi)
predict_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Predicted BMI: ")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
root.mainloop()