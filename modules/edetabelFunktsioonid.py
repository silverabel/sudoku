def leiaRaskusaste(eemaldatavateNumbriteArv):
  if eemaldatavateNumbriteArv == 36:
    return 'Lihtne'
  elif eemaldatavateNumbriteArv == 42:
    return 'Keskmine'
  elif eemaldatavateNumbriteArv == 50:
    return 'Raske'
  elif eemaldatavateNumbriteArv == 55:
    return 'Ekspert'




def lisaRaskusastmeEdetabelisse(raskusastmeEdetabel, lahendajaNimi, lahendamisAeg):
  for i in range(len(raskusastmeEdetabel)):
    rida = raskusastmeEdetabel[i].split(" ")
    if rida == [""]:
      raskusastmeEdetabel.insert(i, lahendajaNimi + " " + str(lahendamisAeg))
      break
    reaSkoor = int(rida[1])
    if lahendamisAeg < reaSkoor:
      raskusastmeEdetabel.insert(i, lahendajaNimi + " " + str(lahendamisAeg))
      break

  if len(raskusastmeEdetabel) > 10:
    del raskusastmeEdetabel[10]


def lisaEdetabelisse(edetabel, raskusaste, lahendajaNimi, lahendamisAeg):
  raskusastmeNimeReanumber = edetabel.index(raskusaste)
  raskusastmeEdetabel = edetabel[raskusastmeNimeReanumber + 1: raskusastmeNimeReanumber + 11]
  lisaRaskusastmeEdetabelisse(raskusastmeEdetabel, lahendajaNimi, lahendamisAeg)

  del edetabel[raskusastmeNimeReanumber + 1: raskusastmeNimeReanumber + 11]
  edetabel[raskusastmeNimeReanumber + 1: raskusastmeNimeReanumber + 1] = raskusastmeEdetabel

  edetabelFail = open('sudoku/pages/edetabel.txt', 'w')
  edetabelFail.write('\n'.join(map(str, edetabel)))
  edetabelFail.close()

  return edetabel


def vorminda(edetabel):
  for i in range(len(edetabel) - 1):
    edetabel[i] += '<br>'

  edetabel[0] = '<h4>Lihtne</h4>'
  edetabel[12] = '<h4>Keskmine</h4>'
  edetabel[24] = '<h4>Raske</h4>'
  edetabel[36] = '<h4>Ekspert</h4>'
  del edetabel[47]

  return edetabel