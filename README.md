### driverreport:0.0.1

### Description
Driver report is a python utility for generating reports driver trip statistics.
It accepts an input file with commands to add drivers and their trips. It generates
a report of each driver, their totals miles driven, and their average speed in MPH, sorted
from the most miles driven to the least. It discards any trips that average a speed of less than
5mph or greater than 100mph.

### Approach
My approach to this solving this problem was to utilize TDD in Python in an object oriented manner. The most logical
implementation to me was to create a "Trip" class and a "Driver" class and have the "Driver" class contain
a "trips" attribute that stored "Trip" instances associated with that driver. It also
seemed logical to add trip statistic attributes (such as average speed and total driving distance)
to the driver and have them recalculated whenever a new, valid trip was added.

For running the app, I knew I wanted to implement a fully installable CLI rather than
just a simple script. I used the [Google Fire](https://github.com/google/python-fire) package
to implement this, as it is one of my favorite, lightweight cli packages that I use every day.

The project is structured as it is, so that it can be imported as a module OR run as a standalone cli.
This is a pattern I believe in and have used many times with Python where a CLI is applicable.

I hope you enjoy the project. Thank you!

### Installation
    # from the driverreport repository root directory

    pip install -e ./driverreport-pkg

### Input File
driverreport accepts an input text file to read driver and trip information from.
There are 2 commands: "Driver" and "Trip". "Driver" accepts the name of the driver as an argument and adds that driver to the app. Trip
accepts "driver name", "start time", "end time", and "miles". Time arguments should be in 24 hour HH:MM format.
Drivers MUST be added before they can have trips associated with them. Each command should be on a separate line of the file.

###### NOTE:
Any trips that average a speed of less than 5mph or greater than 100mph will be discarded.

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
Tests are located in the "driverreport-pkg/driverreport/tests" directory. To run tests:

    cd driverreport-pkg/

    # And then run using setup.py

    python setup.py test

    # OR using unittest discovery

    python -m unittest discover -v

##### Sample Test Output:
    Tests adding a single trip ... ok
    test_avg_speed (driverreport.tests.test_driver.TestDriver)
    Tests average speed calculation ... ok
    test_driver_exists (driverreport.tests.test_driver.TestDriver)
    Tests that  self.driver exists ... ok
    test_driver_name (driverreport.tests.test_driver.TestDriver)
    Tests that names can be correctly added ... ok
    test_invalid_avg_speed (driverreport.tests.test_driver.TestDriver)
    Tests trips are discarded that average less than 5mph or more than 100mph ... ok
    test_multiple_trips (driverreport.tests.test_driver.TestDriver)
    Tests adding multiple trips ... ok
    test_total_distance (driverreport.tests.test_driver.TestDriver)
    Tests total distance calculation ... ok
    test_total_time (driverreport.tests.test_driver.TestDriver)
    Tests total driving time calculation ... ok
    test_read_file (driverreport.tests.test_main.TestMain)
    Tests that files can be read ... ok
    test_report_from_input (driverreport.tests.test_main.TestMain)
    Tests that reports are generated as expected ... ok
    test_trip_atrrbutes (driverreport.tests.test_trip.TestTrip)
    Tests the setting of Trip attributes ... ok
    test_trip_exists (driverreport.tests.test_trip.TestTrip)
    Tests that the trip property exists ... ok


