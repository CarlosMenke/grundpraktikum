
# anzahl maximum: zeit
Maxima_stange_1 = {1:3.138, 11:18.063, 20:32.935, 30:49.473, 40:66.058, 50:82.598, 60:99.190, 70:115.729, 79:130.651, 90:148.843, 101:167.079, 112:185.279}
Maxima_stange_2 = {1:1.455, 10:16.382, 20:32.944, 29:47.857, 39:64.411, 50:82.628, 60:99.192, 69:114.075, 80:132.288, 90:148.857, 100:165.417, 111:183.626}
Maxima_stange_3 = {1:1.528, 11:18.088, 20:33.022, 29:47.909, 39:64.471, 51:84.347, 60:99.269, 69:114.162, 79:130.7, 90:148.936, 101:167.164, 111:183.715}

for i in Maxima_stange_1:
    if i == 2: continue
    #print((Maxima_stange_1[1] - Maxima_stange_1[i])/ (i-2))

for i in Maxima_stange_2:
    if i == 1: continue
    #print((Maxima_stange_2[1] - Maxima_stange_2[i])/ (i-1))

for i in Maxima_stange_3:
    if i == 1: continue
    print((Maxima_stange_3[1] - Maxima_stange_3[i])/ (i-1))
