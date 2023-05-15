from datetime import date, timedelta


index="DJI"
start="2020-01-01"
#end=date.today()-timedelta(days=1)
end='2020-02-21'

import data as da
#new_index,index=da.calc_index(index,start,end)

import diagram as dia
#dia.draw(new_index,index)

#da.technical_index(index)

import test as test
test
#test.technical_index(index)





