from lib.arquivo import *

arq = 'grupos_teste.txt'

a = open(arq, 'r')

grupos = a.readlines()

print(grupos)