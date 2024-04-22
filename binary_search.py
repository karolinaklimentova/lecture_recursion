import os
import json

cwd_path = os.getcwd()
file_path = "files"


def read_data(file_name, key="ordered_numbers"):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, str), sequential data
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), mode="r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]


def recursive_binary_search(seq, number, left, right):
    """
    Recursive binary search.
    :param seq: (list), ordered list of numbers
    :param number: (int), number to search for
    :param left: (int), index of the left boundary of the search interval
    :param right: (int), index of the right boundary of the search interval
    :return: (int), index of the found number, or None if not found
    """
    if left <= right:
        mid = (left + right) // 2

        if seq[mid] == number:
            return mid
        elif seq[mid] < number:
            return recursive_binary_search(seq, number, mid + 1, right)
        else:
            return recursive_binary_search(seq, number, left, mid - 1)
    else:
        return None


def main(file_name, number):
    sequence = read_data(file_name=file_name, key="ordered_numbers")

    # Recursive binary search
    index = recursive_binary_search(sequence, number, 0, len(sequence) - 1)

    if index is not None:
        print(f"Number {number} found at index {index}.")
    else:
        print(f"Number {number} not found in the sequence.")


if __name__ == "__main__":
    my_file = "sequential.json"
    my_number = 90
    main(my_file, my_number)

