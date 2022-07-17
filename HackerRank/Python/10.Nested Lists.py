if __name__ == '__main__':
    student=[]
    for _ in range(0,int(input())):
        student.append([input(), float(input())])
    second_highest = sorted(list(set([marks for name, marks in student])))[1]
    for a,b in sorted(student):
        if b==second_highest:
            print(a)