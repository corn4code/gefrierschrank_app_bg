from calendar import month
import re
import datetime
test_date = "31.07.2023"

# valid_date = re.search("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$",test_date)
# if valid_date:
#     day = int(re.split("\.", test_date)[0])
#     month = int(re.split("\.", test_date)[1])
#     year = int(re.split("\.", test_date)[2])
#     date = str(day)+"."+str(month)+"."+str(year)
#     if year>2000:
#         year -= 2000
#     comp_date = [year,month,day]

# print(date)
# print(year)


# current_day = str(datetime.date.today())
# day = re.split("[-]",current_day)[2]
# month = re.split("[-]",current_day)[1]
# year = re.split("[-]",current_day)[0]
# show_dof = day+"."+str(int(month))+"."+year
# compair_dof = [int(year[2:]), int(month),int(day)]
# print(show_dof, "\t",compair_dof)

for i in range(len(["d",1,1,1])):
    print(i)