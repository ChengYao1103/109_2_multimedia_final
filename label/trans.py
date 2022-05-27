class_target = ['Car', 'Pedestrian', 'Tram']
for i in range(7481):
    if(i<10):
        f = open('./label_2_origin/00000'+str(i)+'.txt', 'r')
        f_new = open("./label_2/00000"+str(i)+'.txt', 'w')
    elif(i<100):
        f = open('./label_2_origin/0000'+str(i)+'.txt', 'r')
        f_new = open("./label_2/0000"+str(i)+'.txt', 'w')
    elif(i<1000):
        f = open('./label_2_origin/000'+str(i)+'.txt', 'r')
        f_new = open("./label_2/000"+str(i)+'.txt', 'w')
    else:
        f = open('./label_2_origin/00'+str(i)+'.txt', 'r')
        f_new = open("./label_2/00"+str(i)+'.txt', 'w')
    seq = []
    time = 1
    for lines in f.readlines():
        data = lines.split(' ')
        if(not(data[0] in class_target)):
            continue

        for classes in range(3):
            if(data[0] == class_target[classes]):
                class_type = classes
        x_min = float(data[4])
        y_min = float(data[5])
        x_max = float(data[6])
        y_max = float(data[7])
        img_width = 1242
        img_height = 375
        
        x = round(((x_min + (x_max-x_min)/2) * 1.0 / img_width), 6)
        y = round(((y_min + (y_max-y_min)/2) * 1.0 / img_height), 6)
        w = round(((x_max - x_min) * 1.0 / img_width), 6)
        h = round(((y_max - y_min) * 1.0 / img_height), 6)
        if(time == 1):
            seq.append(str(class_type) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h))
            time = 2
        else:
            seq.append('\n'+str(class_type) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h))

    f_new.writelines(seq)
    f_new.close()

    f.close()