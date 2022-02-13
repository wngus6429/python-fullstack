# 딕셔 = {"주현" : "good", "동영":"notbad"}
# print(딕셔["동영"])

# for index in range(1, 10):
#     for inde in range(1, 10):
#         if index*inde % 2 == 0:
#             print(index, "X", inde, index*inde) 
            
            
# dongs = ["6209동", "6208동", "6207동"]
# hos = ["101호", "102호", "103호", "104호"]
# for index in dongs:
#     for hoss in hos:
#         print(index, hoss)
        
# data = {'environment': 'ghksrud', 'company': 'ghltk', 'government': 'wjdqn, wjdcl', 'face': 'djfrnf'}
# for index in data:
#     print(data[index])
#     print("index",index)

data = {'environment': ['환경', 'X'], 'company': ['회사', 'O'], 'government': ['정부, 정치', 'X'], 'face': ['얼굴', 'X']}
for index in data:
    if data[index][1] == "X":
        print(index)
        
english = input()
if english in data.keys():
    data[english][1] = 'O'

for item in data.keys():
    data_list = data[item]
    if data_list[1] == 'X':
        print (item)