
# anzahl maximum: zeit
Maxima_stange_1 = {1:3.138, 11:18.063, 20:32.935, 30:49.473, 40:66.058, 50:82.598, 60:99.190, 70:115.729, 79:130.651, 90:148.843, 101:167.079, 112:185.279}

for i in Maxima_stange_1:
    if i == 2: continue
    print((Maxima_stange_1[1] - Maxima_stange_1[i])/ (i-2))
