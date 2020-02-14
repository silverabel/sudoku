from django.shortcuts import render
from modules import sudok

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
    eemaldatavateNumbriteArv = 45
  sudok.eemaldaSudokustSuvaliseltNumbrid(sudoku, eemaldatavateNumbriteArv)

  context = {'sudoku': sudoku, 'eemaldatavateNumbriteArv': eemaldatavateNumbriteArv}
  return render(request, 'pages/index.html', context)

