import csv
import numpy as np

with open(r'.\22Jun2020_BIHAR.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    stn_no = []
    rain = []
    
    # Creating Station No. List
    for row in csv_reader:
        rain.append(row['RAIN (mm)'])
        if (row['STATION_NUMBER'] != ''):
            stn_no.append(row['STATION_NUMBER'])
            stn_no.append(row['STATION_NUMBER'])
            stn_no.append(row['STATION_NUMBER'])
     
     # Creating Rain List       
    final_rain = []
    for i in range(0, 5034, 2):
        test = float(rain[i]) + float(rain[i+1])
        final_rain.append(test)

    # Creating Time List
    final_date = []
    date = ['23JUN2020', '24JUN2020', '25JUN2020']
    for i in range(839):
        final_date.append(date)
        
    final_time = np.concatenate(final_date, axis=0)
    
    # Creating the csv file   
    with open("out.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file) 
        
        for i in range(0, 839, 1):
            final_csv = [stn_no[i], final_time[i], final_rain[i]]
            csv_writer.writerow(final_csv)
        
    
        