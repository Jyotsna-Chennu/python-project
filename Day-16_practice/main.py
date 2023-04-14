from prettytable import PrettyTable

add_col = PrettyTable()
# add_col.align("c")
add_col.add_column('Place', ['Vindavan', 'Kedarnath', 'Rameswaram'])
add_col.add_column('Gods', ['RadhaKrishna', 'Shuva', 'Shiva'])
#print(add_col)
add_col.add_row(['Shirid', 'SaiBaba'])
add_col.align = 'c'
print(add_col)
