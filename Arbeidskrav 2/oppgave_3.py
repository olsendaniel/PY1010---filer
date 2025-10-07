# importere bibliotetet
import numpy as np

# hente input fra bruker
v_grad = float(input('Skriv inn gradtallet: '))

# regne om inndata
v_rad = v_grad * np.pi/180

# vise resultatet
print('Tallet', v_grad,'i grad er' ,v_rad, 'i radianer.')