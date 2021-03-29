def solution(cacheSize, cities):
    answer = 0
    d = []
    if cacheSize == 0:
        return 5*len(cities)
    for i in cities:
        escape = False
        if len(d):
            for j in range(len(d)):             # cache hit
                if d[j].upper() == i.upper():
                    answer += 1
                    if len(d) == cacheSize:
                        d.pop(j)
                    d.append(i)
                    escape = True
                    break
            if escape:
                continue
            else:                              # cache miss
                answer += 5
                if len(d) == cacheSize:
                    d.pop(0)
                d.append(i)
                    
        else:
            d.append(i)
            answer += 5

    return answer