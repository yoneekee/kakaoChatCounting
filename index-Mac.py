def kakaoChatsCount(path):
    list = []
    listv = {}
  
    sourcecode = open(path,"r+", encoding='utf-8')
    data=sourcecode.readlines()
    
    
    checkWord1 = "-"
    checkWord2 = ":"
    checkWord3 = "나갔습니다"
    checkWord4 = "들어왔습니다"
    checkWord5 = "채팅방 관리자가 메시지를 가렸습니다"
    checkWord6 = "초대했습니다"
    checkWord7 = "내보냈습니다"
    checkWord8 = ',"'
    checkWord9 = "방장이 되었습니다."
    
   
    for idata in data :
       if (   (checkWord1 in idata) & (checkWord2 in idata) &
        (checkWord3 not in idata) & (checkWord4 not in idata) & 
        (checkWord5 not in idata) & (checkWord6 not in idata) &
        (checkWord7 not in idata) & (checkWord8  in idata) &
        (checkWord9 not in idata)  ): 
            name = idata.split(',"')
            name = name[1][0:]
            name = name.split('"')
            name = name[0][0:]
            
            if name not in list:
                list.append(name)
                listv[name] = 1
            else :
                listv[name] = listv[name] +1

    listv = sorted(listv.items())
    #print(listv)

    listv= sorted(listv, key=lambda x : -x[1]) # 내림차순
    # listv= sorted(listv, key=lambda x : x[1]) # 올림차순

    rank = 1
    for item in listv :
        
        print (str(rank) + "위 - " + item[0] + "(" + str(item[1]) +"개)")
        rank += 1

# 함수 실행되는 부분
mylist = r"./testChat-Mac.txt"
kakaoChatsCount(mylist)