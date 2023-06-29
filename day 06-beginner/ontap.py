# print(1 == 2) # False
# print(1 == 1) # True

# data = ["a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "e"]
# index= len(data) - 1
# print("index of 'e' is: ", index)



# Viết chương trình quản lí học sinh gồm các chức năng sau: (List)
  # 1. Nhập tên. MSHS
  # 2. Lớp
  # 3. Nhập điểm từng môn
  # 4. Tính điểm. Xếp loại học lực. ( Syntax: Tam đạt học lực Giỏi)



names = []
id = []
class_student = []
math = []
english = []
literature = []
average_score = []
score = []
rank = []

nums = int(input("Enter the number of students: "))
for i in range(nums):
    name = input("Enter name: ")
    enter_id = int(input("Enter ID:"))
    class_name = int(input("Enter Class: "))
    math_score = float(input("Enter Math Score: "))
    english_score = float(input("Enter Math Score: "))
    literature_score = float(input("Enter Math Score: "))
    names.append(name)
    id.append(enter_id)
    class_student.append(class_name)
    math.append(math_score)
    english.append(english_score)
    literature.append(literature_score)

print("\nName\t\t\tID\t\t\tClass\t\t\tAverage Score\n")
for i in range(nums):
    ave_scr = (math[i] + literature[i] + english[i]) / 3
    str_ave = str(ave_scr)
    average_score.append(str_ave)
    
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], id[i], class_student[i], average_score[i]))




