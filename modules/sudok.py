from random import choice

def ehitaSudoku():
    read = [[] for _ in range(9)]

    #esimene rida
    arvud = [i for i in range(1, 10)]
    for _ in range(9):
        arv = choice(arvud)
        read[0].append(arv)
        arvud.remove(arv)

    #teine rida
    while len(read[1]) != 9:
        try:
            read[1] = []
            for j in range(3):
                arvud = []
                for k in range(1, 10):
                    if k not in read[1] and k not in read[0][:3]:
                        arvud.append(k)
                read[1].append(choice(arvud))
            for j in range(3, 6):
                arvud = []
                for k in range(1, 10):
                    if k not in read[1] and k not in read[0][3:6]:
                        arvud.append(k)
                read[1].append(choice(arvud))
            for j in range(6, 9):
                arvud = []
                for k in range(1, 10):
                    if k not in read[1] and k not in read[0][6:9]:
                        arvud.append(k)
                read[1].append(choice(arvud))
        except:
            pass

    #kolmas rida
    arvud = []
    for j in range(1, 10):
        if j not in read[0][:3] and j not in read[1][:3]:
            arvud.append(j)
    for j in range(3):
        arv = choice(arvud)
        read[2].append(arv)
        arvud.remove(arv)
    for j in range(1, 10):
        if j not in read[0][3:6] and j not in read[1][3:6]:
            arvud.append(j)
    for j in range(3):
        arv = choice(arvud)
        read[2].append(arv)
        arvud.remove(arv)
    for j in range(1, 10):
        if j not in read[0][6:9] and j not in read[1][6:9]:
            arvud.append(j)
    for j in range(3):
        arv = choice(arvud)
        read[2].append(arv)
        arvud.remove(arv)

    veerud = [[] for _ in range(9)]
    for j in range(3):
        for k in range(9):
            veerud[k].append(read[j][k])
    #neljas rida
    while len(read[3]) != 9:
        try:
            read[3] = []
            for j in range(9):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in read[3]:
                        arvud.append(k)
                read[3].append(choice(arvud))
        except:
            pass

    for j in range(9):
        veerud[j].append(read[3][j])
        
    #viies rida
    while len(read[4]) != 9:
        try:
            read[4] = []
            for j in range(3):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in read[4] and k not in read[3][:3]:
                        arvud.append(k)
                read[4].append(choice(arvud))
            for j in range(3, 6):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in read[4] and k not in read[3][3:6]:
                        arvud.append(k)
                read[4].append(choice(arvud))
            for j in range(6, 9):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in read[4] and k not in read[3][6:9]:
                        arvud.append(k)
                read[4].append(choice(arvud))
        except:
            pass
        
    for j in range(9):
        veerud[j].append(read[4][j])

    #kuues rida
    kolmene = []
    i = 0
    while len(kolmene) != 3:
        if i == 10:
            raise ValueError("Pekki 1")
        try:
            i += 1
            kolmene = []
            for j in range(3):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in kolmene and k not in read[3][:3] and k not in read[4][:3]:
                        arvud.append(k)
                kolmene.append(choice(arvud))
        except:
            pass
    read[5].extend(kolmene)
    kolmene = []
    i = 0
    while len(kolmene) != 3:
        if i == 10:
            raise ValueError("Pekki 2")
        try:
            i += 1
            kolmene = []
            for j in range(3, 6):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in kolmene and k not in read[3][3:6] and k not in read[4][3:6]:
                        arvud.append(k)
                kolmene.append(choice(arvud))
        except:
            pass
    read[5].extend(kolmene)
    kolmene = []
    i = 0
    while len(kolmene) != 3:
        if i == 10:
            raise ValueError("Pekki 3")
        try:
            i += 1
            kolmene = []
            for j in range(6, 9):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in kolmene and k not in read[3][6:9] and k not in read[4][6:9]:
                        arvud.append(k)
                kolmene.append(choice(arvud))
        except:
            pass
    read[5].extend(kolmene)
    
    for j in range(9):
        veerud[j].append(read[5][j])
    
    #seitsmes rida
    while len(read[6]) != 9:
        try:
            read[6] = []
            for j in range(9):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in read[6]:
                        arvud.append(k)
                read[6].append(choice(arvud))
        except:
            pass
    
    for j in range(9):
        veerud[j].append(read[6][j])
    
    #kaheksas rida
    while len(read[7]) != 9:
        try:
            read[7] = []
            for j in range(3):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in read[7] and k not in read[6][:3]:
                        arvud.append(k)
                read[7].append(choice(arvud))
            for j in range(3, 6):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in read[7] and k not in read[6][3:6]:
                        arvud.append(k)
                read[7].append(choice(arvud))
            for j in range(6, 9):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in read[7] and k not in read[6][6:9]:
                        arvud.append(k)
                read[7].append(choice(arvud))
        except:
            pass
    
    for j in range(9):
        veerud[j].append(read[7][j])
    
    #üheksas rida
    kolmene = []
    i = 0
    while len(kolmene) != 3:
        if i == 10:
            raise ValueError("Pekki 4")
        try:
            i += 1
            kolmene = []
            for j in range(3):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in kolmene and k not in read[6][:3] and k not in read[7][:3]:
                        arvud.append(k)
                kolmene.append(choice(arvud))
        except:
            pass
    read[8].extend(kolmene)
    kolmene = []
    i = 0
    while len(kolmene) != 3:
        if i == 10:
            raise ValueError("Pekki 5")
        try:
            i += 1
            kolmene = []
            for j in range(3, 6):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in kolmene and k not in read[6][3:6] and k not in read[7][3:6]:
                        arvud.append(k)
                kolmene.append(choice(arvud))
        except:
            pass
    read[8].extend(kolmene)
    kolmene = []
    i = 0
    while len(kolmene) != 3:
        if i == 10:
            raise ValueError("Pekki 6")
        try:
            i += 1
            kolmene = []
            for j in range(6, 9):
                arvud = []
                for k in range(1, 10):
                    if k not in veerud[j] and k not in kolmene and k not in read[6][6:9] and k not in read[7][6:9]:
                        arvud.append(k)
                kolmene.append(choice(arvud))
        except:
            pass
    read[8].extend(kolmene)
    return read

def eemaldaSudokustSuvaliseltNumbrid(sudoku, mituNumbritEemaldada):
    eemaldatavateNumbriteKohad = []
    kohad = [a for a in range(81)]
    for _ in range(mituNumbritEemaldada):
        koht = choice(kohad)
        eemaldatavateNumbriteKohad.append(koht)
        kohad.remove(koht)
    koht = 0
    for b in range(9):
        for c in range(9):
            if koht in eemaldatavateNumbriteKohad:
                sudoku[b][c] = ""
            koht += 1
    return sudoku