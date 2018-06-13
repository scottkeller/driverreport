import os
import sys
import codecs
from .driver import Driver

def driver_report(path):
    """Takes an input text file with commands to add drivers and trips and generates a report
    with name, total distance and average speed"""

    # Using dict with driver name as key
    drivers = {}
    data = read_file(path).readlines()
    # Loop through the arguments in the file separating
    # the first arg as the command and the rest as params
    for ln in data:
        args = ln.strip().split(' ')
        command = args.pop(0)

        # add a driver
        if command == 'Driver':
            name = str(args[0])
            # ensure we haven't already added this driver
            if name not in drivers:
                drivers[name] = Driver(name)

        # add a trip
        if command == 'Trip':
            name = str(args[0])
            start_time = str(args[1])
            end_time = str(args[2])
            distance = float(args[3])

            # find the driver in the drivers dict and add a trip
            try:
                driver = drivers[name]
                driver.add_trip(start_time, end_time, distance)

            # throw an error if the driver
            except KeyError:
                print(drivers)
                print(name)
                print('Error: Driver not found!')
                sys.exit(-1)

    # Convert drivers from drivers dict and sort by total distance
    added_drivers = [drivers[d] for d in drivers]
    added_drivers.sort(key=lambda x: x.total_distance, reverse=True)

    report = ""
    # # Build the report string and print it for each driver
    for i, d in enumerate(added_drivers):
        report_line = '{}: {} miles'.format(d.name, d.total_distance)
        if d.avg_speed > 0:
            report_line = '{} @ {} mph'.format(report_line, d.avg_speed)
        # Add new line only if this is not the last driver
        if i < len(added_drivers) -1:
            report_line += '\n'
        report += report_line

    return report



def read_file(path):
    """Reads a file from a given path"""
    return codecs.open(filename=resolve_path(path), mode='r', encoding='utf-8')

def resolve_path(path):
    """Resolves relative paths and returns the absolute path"""
    if path.startswith('~'):
        path = os.path.expanduser(path)

    elif os.path.isabs(path) is False:
        path = os.path.join(os.path.abspath(os.getcwd()), path)

    return os.path.realpath(path)



if __name__ == "__main__":
    print(driver_report(sys.argv[1]))