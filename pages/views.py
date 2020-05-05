from django.shortcuts import render
from modules import sudok, edetabelFunktsioonid

def index(request):
  a = 0
  while not a:
    try:
      sudoku = sudok.ehitaSudoku()
      a = sudoku[8][8]
    except:
      pass

  try:
    eemaldatavateNumbriteArv = int(request.POST['eemaldatavateNumbriteArv'])
  except:
    eemaldatavateNumbriteArv = 36
  sudok.eemaldaSudokustSuvaliseltNumbrid(sudoku, eemaldatavateNumbriteArv)

  context = {'sudoku': sudoku, 'eemaldatavateNumbriteArv': eemaldatavateNumbriteArv}
  return render(request, 'pages/index.html', context)

def edetabel(request):
  edetabelFail = open('sudoku/pages/edetabel.txt', 'r')
  edetabel = edetabelFail.read().splitlines()
  edetabelFail.close()

  if request.POST:
    eemaldatavateNumbriteArv = int(request.POST['eemaldatavateNumbriteArv'])
    raskusaste = edetabelFunktsioonid.leiaRaskusaste(eemaldatavateNumbriteArv)

    if raskusaste:
      lahendajaNimi = request.POST['lahendajaNimi']
      lahendamisAeg = int(request.POST['lahendamisAeg'])

      edetabel = edetabelFunktsioonid.lisaEdetabelisse(edetabel, raskusaste, lahendajaNimi, lahendamisAeg)

  edetabel = edetabelFunktsioonid.vorminda(edetabel)

  edetabeliEsimenePool = edetabel[:23]
  edetabeliTeinePool = edetabel[24:]


  context = {'edetabeliEsimenePool': edetabeliEsimenePool, 'edetabeliTeinePool': edetabeliTeinePool}
  return render(request, 'pages/edetabel.html', context)

