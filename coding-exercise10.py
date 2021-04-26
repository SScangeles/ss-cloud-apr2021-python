
'''
The simple measure of body constitution was proposed at the middle of XIX century.
It depends only on the height and weight of a person - and is called Body Mass Index or BMI.
Create a function to calculate grades for several people.
'''

def bmiCalc(info):
    weight = info[0]
    height = info[1]
    bmi =  weight/(height**2)
    if bmi < 18.5:
        return "under"
    elif bmi >= 18.5 and bmi < 25.0:
        return "normal"
    elif bmi >= 25.0 and bmi < 30.0:
        return "over"
    else:
        return "obese"


inputList = [(80, 1.73), (55, 1.58), (49, 1.91), [100, 1]]
print(inputList)

try:
    outputList = list(map(bmiCalc, inputList))
    print(outputList)
except TypeError as ex:
    print("TypeError:", ex)
    print("Input must be a list, consisting of weight and height pair items")
except:
    print("Something went wrong")
