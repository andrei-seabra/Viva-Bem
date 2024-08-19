def bmiCalculator(weight: str, height: str):
    """
        Calculates the bmi of the user based on their information.
    """

    # References
    formatedMagnitudes = []
    
    acceptableCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "."]
    magnitudes = [weight, height]

    # Avoids other characters in magnitudes which aren't related to numbers
    for magnitude in magnitudes:
        for char in magnitude:
            if not char in acceptableCharacters:
                ...
                return
            
    # Treat the information
    for magnitude in magnitudes:
        if "," in magnitude:
            formatedMagnitude = float(magnitude.replace(",","."))
            formatedMagnitudes.append(formatedMagnitude)
        else:
            formatedMagnitude = float(magnitude)
            formatedMagnitudes.append(formatedMagnitude)

    # Calculation
    bmi = formatedMagnitudes[0] / formatedMagnitudes[1] ** 2
    
    result = ""

    if bmi < 18.5:
        result = "Você está abaixo do peso ideal."
    elif bmi < 25:
        result = "Você está no peso ideal."
    elif bmi < 30:
        result = "Você está sobrepeso."
    elif bmi < 40:
        result = "Você está com obesidade."
    else:
        result = "Você está com obesidade mórbida."
    
    return result