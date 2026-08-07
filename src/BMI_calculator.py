"""
BMI Calculator Script
Calculates Body Mass Index based on user input for weight and height.
BMI = weight (kg) / height (m)^2
"""

class BMICalculator:
    def calculate_bmi(self, weight, height):
        if height <= 0:
            raise ValueError("Height must be greater than 0")
        if weight <= 0:
            raise ValueError("Weight must be greater than 0")

        bmi = weight / (height ** 2)
        return bmi

    def guidance(self):
        print("=" * 50)
        print("Welcome to the BMI Calculator!")
        print("=" * 50)

        try:
            weight = float(input("\nEnter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
            bmi = self.calculate_bmi(weight, height)


            # Display results using f-strings
            print("\n" + "=" * 50)
            print("BMI Calculation Results:")
            print("=" * 50)
            print(f"Weight: {weight} kg")
            print(f"Height: {height} m")
            print(f"Your BMI: {bmi:.2f}")
            print("=" * 50)

        except ValueError as e:
            print(f"\nError: {e}")
            print("Please enter valid positive numbers for weight and height.")


if __name__ == "__main__":
    calculator = BMICalculator()
    calculator.guidance()
