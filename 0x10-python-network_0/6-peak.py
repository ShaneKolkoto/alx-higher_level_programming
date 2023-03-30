def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak in the list.
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Find the index of the middle element
    mid_index = len(list_of_integers) // 2

    # Compare the middle element with its adjacent elements
    if (mid_index == 0 or list_of_integers[mid_index - 1] <= list_of_integers[mid_index]) and (mid_index == len(list_of_integers) - 1 or list_of_integers[mid_index + 1] <= list_of_integers[mid_index]):
        # If the middle element is a peak, return it
        return list_of_integers[mid_index]
    elif mid_index > 0 and list_of_integers[mid_index - 1] > list_of_integers[mid_index]:
        # If the left adjacent element is greater than the middle element, search for a peak in the left half
        return find_peak(list_of_integers[:mid_index])
    else:
        # If the right adjacent element is greater than the middle element, search for a peak in the right half
        return find_peak(list_of_integers[mid_index + 1:])