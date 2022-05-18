weight = input("enter your weight digit \n")
height = input("enter your height digit \n")

bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)

bmi_as_floor = round(bmi_as_int)

print(f"your body mass index is {bmi_as_floor} ")