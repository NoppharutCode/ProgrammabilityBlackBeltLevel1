Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
data = Sessions_Attended["sessions"].split(",")
count = len(data)
if len(data) > 0 and data[len(data)-1].strip() == "":
    count -= 1
    
print("I have attended {} sessions!!".format(count))
