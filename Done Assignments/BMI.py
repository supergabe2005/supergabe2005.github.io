def calculate_bmi(weight_kg, height_m):
    """
    Calculate the Body Mass Index (BMI) given weight and height.

    Takes two arguments: weight in kilograms (kg) and height in meters (m).
    The function returns the BMI of the weight and height as a float.

    Note: BMI is a general health metric. Different populations may have
    different healthy BMI ranges. Consider individual factors and consult
    health professionals for personalized assessment.

    Args:
    weight_kg: Weight in kilograms
    height_m: Height in meters

    Returns:
    float: The calculated BMI value
    """

    bmi = weight_kg / (height_m ** 2)

    return bmi

# Example usage
if __name__ == "__main__":
    bmi = calculate_bmi(55, 1.67)
    print(f"The BMI is: {bmi:.2f}")

