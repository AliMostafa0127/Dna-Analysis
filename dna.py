import csv
import sys


def main():
    # TODO: Check for command-line usage
    while len(sys.argv) != 3:
        print("Missing command lind argument")
        sys.exit(1)

    # TODO: Read database file into a variable
    data_base = []
    with open(sys.argv[1], "r") as csvfile:
        database_reader = csv.DictReader(csvfile)
        subsequences = database_reader.fieldnames[1:]
        for row in database_reader:
            data_base.append(row)

    # TODO: Read DNA sequence file into a variable
    txtfile = open(sys.argv[2], "r")
    dna = txtfile.read()

    # TODO: Find longest match of each STR in DNA sequence
    str_dna = {}
    for sub in subsequences:
        longest_run = longest_match(dna, sub)
        str_dna[sub] = longest_run
    # TODO: Check database for matching profiles
    for person in data_base:
        if match(subsequences, str_dna, person):
            print(person["name"])
            return
    print("No match")
    return


def match(subsequences, str_dna, person):
    for sub in subsequences:
        if str_dna[sub] != int(person[sub]):
            return False
    return True


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
