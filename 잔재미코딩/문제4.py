# num_list = [0, -11, 31, 22, -11, 33, -44, -55]
# #양수만 추출하기
# num_answer = [];
# for index in num_list:
#     if index >= 0:
#         num_answer.append(index)
# print(num_answer)
#[31, 22, 33]


# list_data = ["fun-coding", "Dave", "Linux", "Python", "javascript", "front-end", "back-end", "dataengineering"]
# for indexf in list_data:
#     print(len(indexf))

# filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']
# for ii in filelist:
#     filename = ii.split(".")
#     print(filename[0])
    
filelist = ['exercise01.docx', 'exercise02.csv', 'exercise03.txt', 'exercise04.hwp']
for ii in filelist:
    filename = ii.split(".")
    if filename[1] == "txt":
        print(ii)