medical_course=input('did you complete medical course?? Y or N: ')
atten=int(input("enter student attendance"))
if medical_course=='y':
    print('you are allowed to attend the exam')
else:
    if atten>75:
        print('you are allowed to attend the exam')
    else:
        print('you are not allowed to attend the exam')

