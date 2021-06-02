import pandas as pd

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

    acc = convert_timestemp(rawdatapth + "Accelerometer_raw.csv", rawdatapth + "Accelerometer_time.csv", timecol)
    acc.to_csv(rawdatapth + "Accelerometer.csv", index=False)

    gyr = convert_timestemp(rawdatapth + "Gyroscope_raw.csv", rawdatapth + "Gyroscope_time.csv", timecol)
    gyr.to_csv(rawdatapth + "Gyroscope.csv", index=False)

    lux = convert_timestemp(rawdatapth + "Light_raw.csv", rawdatapth + "Light_time.csv", timecol)
    lux.to_csv(rawdatapth + "Light.csv", index=False)

    loc = convert_timestemp(rawdatapth + "Location_raw.csv", rawdatapth + "Location_time.csv", timecol)
    loc.to_csv(rawdatapth + "Location.csv", index=False)

    mag = convert_timestemp(rawdatapth + "Magnetometer_raw.csv", rawdatapth + "Magnetometer_time.csv", timecol)
    mag.to_csv(rawdatapth + "Magnetometer.csv", index=False)



if __name__ == "__main__":
    main()

