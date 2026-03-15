import csv 

FILENAME= "data.csv" 



with open (FILENAME, "rt") as fp:     
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)     
    count = 0     
    total = 0     
    for line in reader:         
        total += line['age'] # Column 1 is the age and w want to calculate the average of the age that's why value is 1        
        count += 1          
    print (f"average is {total/(count)}") # before exit the for loop line count got increment by 1 that why it is -1 