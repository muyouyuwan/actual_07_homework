nu_li = [4,3,2,1]

for i in range(1,len(nu_li)):
    start = i
    end = 0
    step = -1
    for idx in range(start,end,step):
        if nu_li[idx] < nu_li[idx - 1]:
            nu_li[idx],nu_li[idx - 1] = nu_li[idx - 1],nu_li[idx]
        else:
            break
print nu_li
    
