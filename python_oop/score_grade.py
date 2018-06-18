import random

def verify_score(score):
    if score < 69:
        result = "D"
    elif score < 79:
        result = "C"
    elif score < 89:
        result = "B"
    else:
        result =  "A"
    return "Score :%s;Your grade is %s" %(score, result)

for i in range(8):
    print(verify_score(random.randint(60,100)))

