### driverreport:0.0.1

### Description
Driver report is a python utility for generating reports driver trip statistics.
It accepts an input file with commands to add drivers and their trips. It generates
a report of each driver, their totals miles driven, and their average speed in MPH.

### Installation
    ## from the root driverreport repository directory
    pip install -e ./driverreport-pkg

### Input File
driverreport accepts an input text file to read driver and trip information from.
There are 2 commands: "Driver" and "Trip". "Driver" accepts the name of the driver as an argument and adds that driver to the app. Trip
accepts "driver name", "start time", "end time", and "miles". Time arguments should be in 24 hour HH:MM format.
Drivers MUST be added before they can have trips associated with them. Each command should be on a separate line of the file.

##### Sample Input:
    Driver Dan
    Driver Alex
    Driver Bob
    Trip Dan 07:15 07:45 17.3
    Trip Dan 06:12 06:32 21.8
    Trip Alex 12:01 13:16 42.0

### Usage
    driverreport run path/to/input/file.txt

##### Sample Output
    Alex: 42 miles @ 34 mph
    Dan: 39 miles @ 47 mph
    Bob: 0 miles


### Tests
Tests are located in the "driver-report-pkg/driver-report/tests" directory. To run tests:

    cd driver-report-pkg/
    python setup.py test

    #OR


