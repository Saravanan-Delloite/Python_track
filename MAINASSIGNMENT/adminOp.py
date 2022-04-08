import csv
import datetime

class adminOperation():
    def functions(self):
        while(True):
            print("---Select the operation you want to perform---")
            print("1. Add New Movie Info \n2. Edit Movie Info \n3. Delete Movies \n4.Logout ")
            choise = int(input("Enter the operation you want to perform : "))
            match choise:
                case 1:
                    print("Add new movie")
                    a = adminOperation()
                    a.addMovie()
                case 2:
                    print("Edit movie Details")
                    a = adminOperation()
                    a.editMovie()
                case 3:
                    a = adminOperation()
                    a.delMoive()
                case 4:
                    print("Successfully Logged Out")
                    break
    def login(self):
        print("----Welcome to Admin login page----")
        UserName=input("Enter USERNAME : ")
        PassWord=input("Enter PASSWORD : ")
        if UserName=="ADMIN" and PassWord=="123456":
            return True
        return False
    def addMovie(self):
        with open("hello.csv", "a", newline='') as csv_file:
            a = adminOperation()
            writer = csv.writer(csv_file)
            lst = []
            lst.append(input("Title : "))
            lst.append(input("Genre : "))
            lst.append(input("Length in HR:MIN format: "))
            lst.append(input("Cast : "))
            lst.append(input("Director : "))
            lst.append(input("Admin Rating : "))
            lst.append(input("Language : "))
            lst.append(int(input("Number of shows in a day : ")))
            lst.append(input("First show in HR:MIN format : "))
            lst.append(input("Interval show in HR:MIN format: "))
            lst.append(input("Gap Between Shows in HR:MIN format: "))
            lst.append(int(input("Capacity : ")))
            if a.movieTimings(lst):
                writer.writerow(lst)
                # a=adminOperation()
                # TotalMoiveLength=a.movieLen(lst)
                # FirstShow=a.firstShow(lst)
                # lst.append(float(FirstShow)/60)
                # num=a.showPossible(lst,TotalMoiveLength,FirstShow)
                # #print("num =",num)
                # if num!=0:
                #     for i in range(1,lst[7]):
                #         FirstShow+=TotalMoiveLength+lst[9]+lst[10]
                #         lst.append(float(FirstShow)/60)
                #     hell=FirstShow+TotalMoiveLength+lst[9]
                #     lst.append(float(hell)/60)

    def movieTimings(self,lst):
        MovieShowTimings = []
        MovieShowTimings.append(lst[0])
        LengthOfMovie = lst[2].split(':')
        NoOfShows = lst[7]
        FirstShow = lst[8].split(':')
        TimeInterval = lst[9].split(':')
        GapBetweenShows = lst[10].split(':')
        LengthOfMovie = datetime.timedelta(hours=int(LengthOfMovie[0]), minutes=int(LengthOfMovie[1]))
        TimeInterval = datetime.timedelta(hours=int(TimeInterval[0]), minutes=int(TimeInterval[1]))
        FirstShow = datetime.timedelta(hours=int(FirstShow[0]), minutes=int(FirstShow[1]))
        GapBetweenShows = datetime.timedelta(hours=int(GapBetweenShows[0]), minutes=int(GapBetweenShows[1]))
        check=datetime.timedelta(hours=int("23"), minutes=int("59"))
        for time in range(int(NoOfShows)):
            MovieShowTimings.append(str(FirstShow) + "-" + str(FirstShow + LengthOfMovie + TimeInterval))
            MovieShowTimings.append(lst[11])
            FirstShow = FirstShow + (GapBetweenShows + LengthOfMovie + TimeInterval)
            try:
                if FirstShow > check:
                    raise ValueError
            except:
                print("***cant perform all the shows within a day***")
                return False
        with open("showTime.csv", "a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(MovieShowTimings)
        return True

    def showPossible(self,lst,len,first):
        Interval = lst[9]
        ShowGap = lst[10]
        NumberOfShows = lst[7]
        sum = first
        TotalTimeForShow = len + Interval + ShowGap
        for i in range(NumberOfShows-1):
            sum = sum+TotalTimeForShow
        sum = sum+len+Interval
        if sum <= 1440:
            return len+Interval
        else:
            num = 0
            return num

    def firstShow(self,lst):
        Hr,Min = lst[8].split(":")
        Hours = int(Hr) * 60
        Min = int(Min)
        Total = Hours + Min
        return Total
    def movieLen(self,lst):
        MovieLength = lst[2].split(":")
        MovieLength1 = int(MovieLength[0]) * 60
        MovieLength2 = int(MovieLength[1])
        TotalMovieLength = MovieLength1 + MovieLength2
        return TotalMovieLength
    def editMovie(self):
        while(True):
            MovieName = input("Enter the movie name you want to edit or type EXIT if you don't want to edit : ")
            if(MovieName=="exit"):
                print("redirecting to operations menu")
                break
            location = int(input(
                "which field you want to edit :\n1.Titile \n2.Genre \n3.Length\n4.Cast\n5.Director\n6.Admin Rating\n7.Language\n8.Number of shows\n9.First show\n10.Interval Time\n11.Gap between shows\n12.Capcity\n:"))
            data = input("Enter the data you want to fill in that field : ")
            lines = list()
            with open('hello.csv', 'r', newline='') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == MovieName:
                            lst = row
                            lines.remove(row)
                            a = adminOperation()
                            lst = a.switch(lst, location, data)
                            lines.append(lst)
            with open('hello.csv', 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
    def delMoive(self):
        lines = list()
        members = input("Please enter a member's name to be deleted.")
        with open('hello.csv', 'r', newline='') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == members:
                        lines.remove(row)
        with open('hello.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    def switch(self,lst,choise,data):
        match choise:
            case 1:
                lst[0]=data
            case 2:
                lst[1] = data
            case 3:
                lst[2] = data
            case 4:
                lst[3] = data
            case 5:
                lst[4] = data
            case 6:
                lst[5] = data
            case 7:
                lst[6] = data
            case 8:
                lst[7] = data
            case 9:
                lst[8] = data
            case 10:
                lst[9] = data
            case 11:
                lst[10] = data
            case 12:
                lst[11] = data
        return lst
