import re
import datetime

class Item:
    def __init__(self, name, mhd, kategorie):
        self.name = name
        self.kategorie = kategorie
        # getting dof
        current_day = str(datetime.date.today())
        day = re.split("[-]",current_day)[2]
        month = re.split("[-]",current_day)[1]
        year = re.split("[-]",current_day)[0]
        self.dof = day+"."+str(int(month))+"."+year
        self.compair_dof = [int(year[2:]), int(month),int(day)]

        # checking + getting mhd
        date = mhd
        valid_date = re.search("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$",date)
        if valid_date:
            mhd_day = int(re.split("\.", date)[0])
            mhd_month = int(re.split("\.", date)[1])
            mhd_year = int(re.split("\.", date)[2])
            if mhd_year < 2000:
                mhd_year += 2000
            self.mhd = str(mhd_day)+"."+str(mhd_month)+"."+str(mhd_year)
            mhd_year -= 2000
            self.compair_mhd = [mhd_year, mhd_month, mhd_day]
        else:
            self.mhd = "N/A"
            self.compair_mhd = "N/A"
            return "ungültiges Mindesthaltbarkeitsdatum, sie können dieses jedoch nachträglich hinzufügen bzw. ändern"
        
    def change_mhd(self, mhd):
        date = mhd
        valid_date = re.search("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$",date)
        if valid_date:
            mhd_day = int(re.split("\.", date)[0])
            mhd_month = int(re.split("\.", date)[1])
            mhd_year = int(re.split("\.", date)[2])
            if mhd_year < 2000:
                mhd_year += 2000
            self.mhd = str(mhd_day)+"."+str(mhd_month)+"."+str(mhd_year)
            mhd_year -= 2000
            self.compair_mhd = [mhd_year, mhd_month, mhd_day]
        else:
            return "ungültiges Mindesthaltbarkeitsdatum"
            

    