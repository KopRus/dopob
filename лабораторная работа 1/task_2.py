# TODO Найдите количество книг, которое можно разместить на дискете
from msvcrt import kbhit

print("Количество книг, помещающихся на дискету:", 3)

stinbook = 100
stronst = 50
symbinstr = 25
symb = 4

stra = symb * symbinstr
st = stra * stronst
book = st * stinbook
kb = book / 1024
mb = kb / 1024