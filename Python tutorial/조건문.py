### if 
weather = input("how is the weather today? ") 
#  TODO input 문구안의 내용을 출력하고 입력을 기다린다.
if weather == "rainy" or weather == "blizzard":
    print("take an umbrella")
elif weather == "dusty":
    print("take a mask")
else:
    print("nothing needed")

temp = int(input("how about temperature? ")) # input 의 입력값을 int로 변경이 가능
if(temp > 30):
    print("too hot stay in home")
elif(10<=temp and temp<=30):
    print("it's fine")
elif(0<temp<10):
    print("take a coat")
else:
    print("too cold,, don't go outside")

## continue break
absent = [2, 5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("stop")
        break
    print("{} reades a book".format(student))