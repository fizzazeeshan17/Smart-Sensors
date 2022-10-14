import sys
import pickle


def read_file(filename):
    try:
        with open(filename, 'rb') as dictioneries_file:
            loaded_dictionary = pickle.load(dictioneries_file)
    except (FileNotFoundError, IOError, IndexError):
        print('Error: The files given as arguments are not valid.')
        sys.exit()
    return loaded_dictionary


def map_to_int(measurements):
    new_dictionary = {key: int(value[:-1])
                      for key, value in measurements.items()}
    return new_dictionary


def find_faulty(primary, secondary, threshold):
    faulty_set = set()
    for key, value in primary.items():
        if (primary[key] - secondary[key] > threshold or
                secondary[key] - primary[key] > threshold):
            faulty_set.add(key)
    return faulty_set


def display_warnings(faulty_sensors):
    print('''Analyzis of the provided files is complete.
-------------------------------------------''')
    print()
    print('The following sensors differ more than 2°:')

    for location in faulty_sensors:
        print(location)


def main():
    primary_dictionary = read_file(sys.argv[1])
    secondary_dictionary = read_file(sys.argv[2])
    primary_dictionary = map_to_int(primary_dictionary)
    secondary_dictionary = map_to_int(secondary_dictionary)
    threshold = 2
    faulty_sensors = find_faulty(primary_dictionary, secondary_dictionary,
                                 threshold)
    display_warnings(faulty_sensors)


if __name__ == "__main__":
    main()
