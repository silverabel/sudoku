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
  sudok.eemaldaSudokustSuvaliseltNumbrid(sudoku, 45)

    
  context = {'sudoku': sudoku}
  return render(request, 'pages/index.html', context)