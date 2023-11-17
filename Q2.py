#2

x = int(input("Enter the number of classes held :"))
y = int(input("Enter the number of attended by a student :"))

Attended = y/x*100
print("your Attendence is ",Attended,"%")

if Attended >=80 :
    print("You can Attend for the Exam")
else:
    print("You cann't Attend for the Exam")
