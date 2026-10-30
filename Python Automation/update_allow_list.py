"""
Update the allow list of IP addresses.

Scenario: I work as a security professional at a health care company. Access to
a restricted subnetwork is controlled by IP address. The file allow_list.txt
holds the IP addresses that are allowed to sign in. A separate remove list
contains the IP addresses that must no longer have access.

This script removes every IP address on the remove list from allow_list.txt.
"""


def update_allow_list(import_file, remove_list):
    """Remove the IP addresses in `remove_list` from the allow list file.

    Returns the list of IP addresses that were actually removed.
    """
    # Open the file in read mode. The `with` statement closes the file
    # automatically when the block ends.
    with open(import_file, "r") as file:
        # Read the whole file into a single string
        ip_addresses = file.read()

    # Convert the string into a list, because strings are immutable and a
    # list can be modified. split() separates the string on whitespace.
    ip_addresses = ip_addresses.split()

    removed = []

    # Loop through the remove list (not the allow list) so the list is never
    # modified while it is being iterated over.
    for element in remove_list:
        # `while` also removes any duplicate entries of the same address
        while element in ip_addresses:
            ip_addresses.remove(element)
            if element not in removed:
                removed.append(element)

    # Convert the list back into a string so it can be written to the file
    ip_addresses = " ".join(ip_addresses)

    # Open the file in write mode, which replaces the old contents
    with open(import_file, "w") as file:
        file.write(ip_addresses)

    return removed


if __name__ == "__main__":
    # The file that holds the allow list (in the same folder as this script)
    import_file = "allow_list.txt"

    # IP addresses that are no longer allowed to access restricted content
    remove_list = [
        "192.168.97.225",
        "192.168.158.170",
        "192.168.201.40",
        "192.168.58.57",
    ]

    try:
        removed = update_allow_list(import_file, remove_list)
    except FileNotFoundError:
        print(f"Could not find {import_file}. Run this script from the folder that contains it.")
    else:
        print("Removed from the allow list:", removed)
        with open(import_file, "r") as file:
            print("Updated allow list:", file.read().split())
