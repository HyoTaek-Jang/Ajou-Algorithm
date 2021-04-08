def solution(record):
    _dict = {}
    answer = []
    temp = []
    for i in record:
        recordList = i.split()
        
        if recordList[0] == "Enter":
            temp.append(('E',recordList[1]))            
            _dict[recordList[1]] = recordList[2]
        elif recordList[0] == "Leave":
            temp.append(('L',recordList[1]))
        else:
            _dict[recordList[1]] = recordList[2]
        
    for j in temp:
        if j[0] == "E":
            answer.append(_dict[j[1]]+"님이 들어왔습니다.")
        else:
            answer.append(_dict[j[1]]+"님이 나갔습니다.")
    
    return answer
