import pandas as pd
from datetime import datetime

def UTC_to_wall_time(datapth, timecol):
    # Obtain the data from the file
    data = pd.read_csv(datapth)

    dt = datetime.fromtimestamp(data[timecol].astype(int) // 1000000000)
    s = dt.strftime('%d/%m/%Y %H:%M:%S %p')
    data[timecol] = s
    
    return data


def convert_timestemp(datapth, timepth, timecol):
    
    # Obtain the data from the file
    data = pd.read_csv(datapth) 
    time = pd.read_csv(timepth) 
    
    # Obtain the starting time for the recording
    start_time = time["system time"][0] 

    # Convert the time from s to ns
    data[timecol] = (data[timecol] + start_time) * 1e+9 
    
    return data

def main():

    rawdatapth = "data/raw/"
    outputpth = "data/intermediate/"
    timecol = "Time (s)"

    acc = convert_timestemp(rawdatapth + "Accelerometer_raw.csv", rawdatapth + "time.csv", timecol)
    acc.to_csv(rawdatapth + "Accelerometer.csv", index=False)

    gyr = convert_timestemp(rawdatapth + "Gyroscope_raw.csv", rawdatapth + "time.csv", timecol)
    gyr.to_csv(rawdatapth + "Gyroscope.csv", index=False)

    lux = convert_timestemp(rawdatapth + "Light_raw.csv", rawdatapth + "time.csv", timecol)
    lux.to_csv(rawdatapth + "Light.csv", index=False)

    loc = convert_timestemp(rawdatapth + "Location_raw.csv", rawdatapth + "time.csv", timecol)
    loc.to_csv(rawdatapth + "Location.csv", index=False)

    mag = convert_timestemp(rawdatapth + "Magnetometer_raw.csv", rawdatapth + "time.csv", timecol)
    mag.to_csv(rawdatapth + "Magnetometer.csv", index=False)


def main2():
    rawdatapth = "data/raw/"
    outputpth = "data/intermediate/"
    timecol = "Time (s)"

    acc = UTC_to_wall_time(rawdatapth + "Accelerometer_index.csv", timecol)
    acc.to_csv(rawdatapth + "Accelerometer_UTC.csv", index=True)

if __name__ == "__main__":
    main()

