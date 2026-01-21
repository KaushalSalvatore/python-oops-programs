'''
Finding the percentage

input:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

output :
26.50

'''

if __name__ == '__main__':
    n = int(input())
    sum = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for key, value in student_marks.items():
        if key == query_name:
            for i in value:
                sum += i
print("{:.2f}".format(sum / 3))
