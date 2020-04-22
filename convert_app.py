#declaring variables
grade_f = 0      #temp. in F
grade_c = 0      #temp. in C
temperature = 0  #temp.from input

print("Converting temperature C/F")
print("C at the end for Celsius, F at end for Fahrenheit")
temperature = input("Enter temperature: ")

#converting
#f = c * 9/5 + 32
#c = 5/9 * (f-32)

#grade_f = float(temperature) * 9/5 + 32
#print(round(grade_f,3))

#grade_c = 5/9 * (float(temperature)-32)
#print(round(grade_c,3))

#print(float(temperature[:-1]) * 9/5 + 32 if temperature.endswith('c') else 5/9 * (float(temperature[:-1])-32))

#print(
#    float(temperature[:-1]) * 9/5 + 32
#    if temperature.endswith('c')
#    else 5/9 * (float(temperature[:-1])-32)
#    )

if temperature.endswith('c'):
   grade_f = float(temperature[:-1]) * 9/5 + 32
   print(grade_f)
elif temperature.endswith('f'):
   grade_c = 5/9 * (float(temperature[:-1])-32)
   print(grade_c)
else:
   print("Unknown conversion")

