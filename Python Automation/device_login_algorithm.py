"""
Device login algorithm.

Scenario: As a security analyst, I developed an algorithm that connects users to
their assigned devices. It checks whether a user is approved on the system and
whether they brought the device assigned to them.

The two lists are synchronized: the user at index 0 in `approved_users` uses the
device at index 0 in `approved_devices`.
"""

# Approved usernames and the device IDs assigned to them (same order)
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]


def add_user(username, device_id):
    """Add a new approved user and their device to the end of both lists."""
    approved_users.append(username)
    approved_devices.append(device_id)


def remove_user(username):
    """Remove a user and their assigned device from both lists.

    The user's position is found once and used for both lists, so the two
    lists always stay synchronized.
    """
    ind = approved_users.index(username)
    approved_users.pop(ind)
    approved_devices.pop(ind)


def login(username, device_id):
    """Check a username and device ID against the approved lists."""
    # Outer conditional: is the username approved?
    if username in approved_users:
        print("The user", username, "is approved to access the system.")

        # Find the position of the username, then use that same position to
        # look up the device assigned to that user
        ind = approved_users.index(username)

        # Inner conditional: is this the user's assigned device?
        if device_id == approved_devices[ind]:
            print(device_id, "is the assigned device for", username)
        else:
            print(device_id, "is not their assigned device.")
    else:
        print("The user", username, "is not approved to access the system.")


if __name__ == "__main__":
    # A new employee joins the organization
    add_user("gesparza", "3rcv4w6")
    print(approved_users)
    print(approved_devices)

    # An employee leaves the team
    remove_user("tshah")
    print(approved_users)
    print(approved_devices)

    # Try different username and device ID combinations
    login("bmoreno", "hl0s5o1")   # approved user, correct device
    login("elarson", "r2s5r9g")   # approved user, wrong device
    login("abernard", "4n482ts")  # user is not approved
