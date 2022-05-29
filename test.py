# TEST
from methods.transportation import *

s1 = [110,160,150]
d1 = [140,200,80]
c1 = [[5,10,10],[20,30,20],[10,20,30]]
print('north west corner method:', north_west_corner(s1,d1,c1), sep='\n')
print('row minimum method:', row_min(s1,d1,c1), sep='\n')
print('column minimum method:', col_min(s1,d1,c1), sep='\n')
print('least cost method:', least_cost(s1,d1,c1), sep='\n')
print('vogel method:', vogel(s1,d1,c1), sep='\n')

s2 = [15,25,5]
d2 = [5,15,15,10]
c2 = [[10,0,20,11],[12,7,9,20],[0,14,16,18]]
print('north west corner method:', north_west_corner(s2,d2,c2), sep='\n')
print('row minimum method:', row_min(s2,d2,c2), sep='\n')
print('column minimum method:', col_min(s2,d2,c2), sep='\n')
print('least cost method:',least_cost(s2,d2,c2), sep='\n')
print('vogel method:', vogel(s2,d2,c2), sep='\n')

s3 = [80,120,180]
d3 = [100,120,180]
c3 = [[10,15,25],[8,10,15],[16,7,10]]
print('north west corner method:', north_west_corner(s3,d3,c3), sep='\n')
print('row minimum method:', row_min(s3,d3,c3), sep='\n')
print('column minimum method:', col_min(s3,d3,c3), sep='\n')
print('least cost method:', least_cost(s3,d3,c3), sep='\n')
print('vogel method:', vogel(s3,d3,c3), sep='\n')
