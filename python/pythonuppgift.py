
import csv
print("Hej och välkommen kontakt information")
        
Val = True
Val1 = 0

while Val:
    Val1 = input('''
      Förname  [0]
      Eftername  [1]
      Gmail        [2]
      Mobilnummet    [3] 
      Födesldag         [4]
      Välj en av talet !''')
    if Val1 >= "5":
        print("Välj ett tal mellan 0 till 5")

    if Val1 == "0":  
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[0])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False

    elif Val1 == "1":  
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[1])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False


    elif Val1 == "2":  
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[2])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False

    elif Val1 == "3":  
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[3])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False

    elif Val1 == "4":  
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[4])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False
