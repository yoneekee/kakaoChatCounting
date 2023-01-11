
################# TEST 1 ################
idata = '2022년 2월 24일 오전 12:19, 사람1 : 심심하네요'
# print (len(idata))



name = idata.split(', ')
name = name[1][0:]
name = name.split(':')
name = name[0][0:]
print(name)

idata2 = "2023년 1월 9일 오전 10:00"
print(len(idata2))

################# TEST 2 ################# 
import re
import traceback
import json


# 함수
def reading_source(path):
    list = []
    listv = {}
    sourcecode = open(path,"r+", encoding='utf-8')
    data=sourcecode.readlines()
    condition = 0
    checkWord1 = ":"
    checkWord2 = ","
    checkWord3 = "나갔습니다"
    checkWord4 = "들어왔습니다"
    checkWord5 = "채팅방 관리자가 메시지를 가렸습니다"
    checkWord6 = "초대했습니다"
    
   
    for idata in data :
        if (checkWord1 in idata) & (checkWord2 in idata) & (checkWord3 not in idata) & (checkWord4 not in idata) & (checkWord5 not in idata) & (checkWord6 not in idata): 
            name = idata.split(', ')
            name = name[1][0:]
            name = name.split(':')
            name = name[0][0:]
            # print(name)
            if name not in list:
                print(name + " 추가되었습니다.")
                list.append(name)
                listv[name]= 1
            else :
                listv[name] = listv[name] +1

    for i in listv :
        print(i + ": " + str(listv[i]))
    #print(listv)


# 함수 실행되는 부분
mylist = r".\chatPepper.txt"
reading_source(mylist)


## try - except로 함수 실행
# try :
#     reading_source(mylist)
# except :
#     print("오류가 발생했습니다.")
#     print(traceback.format_exc())
    
################# TEST 3 ################# 