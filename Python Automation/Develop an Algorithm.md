# Develop an Algorithm

**Date:** October 23, 2026

## Overview

An algorithm is a set of steps that solves a problem. As a security analyst, I developed an algorithm in Python that connects users to their assigned devices. It checks whether a user is approved on the system and whether they brought the device assigned to them.

**Tools:** Python 3, Jupyter Notebook

**Skills demonstrated:** lists and indexing, list methods (`.append()`, `.remove()`, `.index()`), conditionals, nested conditionals, functions

The algorithm uses two lists that are synchronized. The user at index 0 in `approved_users` uses the device at index 0 in `approved_devices`. This lets me check whether a username and a device ID belong together.

## Task 1: List indexing

I started by exploring how indices work in lists.

```python
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

print(approved_users[0])
print(approved_devices[0])
```

```
elarson
8rp2k75
```

**What I observed:** `approved_users[0]` returns the first username and `approved_devices[0]` returns the first device ID. Changing the index returns different elements from both lists. For example, index 2 returns the third username and the third device ID, because Python indexing starts at 0.

## Task 2: Add a new user

A new employee joined the organization. I used `.append()` to add their username and device ID to the end of each list.

```python
new_user = "gesparza"
new_device = "3rcv4w6"

approved_users.append(new_user)
approved_devices.append(new_device)

print(approved_users)
print(approved_devices)
```

```
['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab', 'gesparza']
['8rp2k75', 'hl0s5o1', '2ye3lzg', '4n482ts', 'a307vir', '3rcv4w6']
```

**What I observed:** the new username appears at the end of `approved_users`, and the new device ID appears at the end of `approved_devices`, so the two lists stay in step.

## Task 3: Remove a user

An employee left the team and should no longer have access. I used `.remove()` to delete their username and device ID.

```python
removed_user = "tshah"
removed_device = "2ye3lzg"

approved_users.remove(removed_user)
approved_devices.remove(removed_device)

print(approved_users)
print(approved_devices)
```

```
['elarson', 'bmoreno', 'sgilmore', 'eraab', 'gesparza']
['8rp2k75', 'hl0s5o1', '4n482ts', 'a307vir', '3rcv4w6']
```

**What I observed:** the username was deleted from `approved_users` and the matching device ID was deleted from `approved_devices`.

## Task 4: Check whether a user is approved

I wrote a conditional statement that checks whether a username is in the list of approved users and displays a message either way.

```python
username = "sgilmore"

if username in approved_users:
    print("The username", username, "is approved to access the system.")
else:
    print("The username", username, "is not approved to access the system.")
```

```
The username sgilmore is approved to access the system.
```

**What I observed:** for `"sgilmore"`, the system displays the approved message, because `"sgilmore"` is in `approved_users`.

## Task 5: Find an index with `.index()`

The `.index()` method returns the position of a value in a list. I used it to find where a username is in `approved_users`:

```python
ind = approved_users.index(username)
print(ind)
```

```
2
```

**What I observed:** `"sgilmore"` is at index 2, which makes it the third element, since indexing starts at 0.

## Task 6: Use one list's index to look up another list

Because the two lists are synchronized, I can find the index of a user in one list and use it to find their device in the other:

```python
ind = approved_users.index(username)
print(approved_devices[ind])
```

```
4n482ts
```

**What I observed:** the output is `4n482ts`, the device assigned to `sgilmore`. Both elements sit at index 2 in their own lists.

## Task 7: Check that the username and device match

Next I combined two conditions with the logical operator `and`. The user must be in `approved_users`, and the device at their index in `approved_devices` must match the device ID that was entered.

```python
username = "sgilmore"
device_id = "4n482ts"

ind = approved_users.index(username)

if username in approved_users and device_id == approved_devices[ind]:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)
```

```
The username sgilmore is approved to access the system.
4n482ts is the assigned device for sgilmore
```

**What I observed:** when both conditions are true, two messages are displayed. The first confirms the user is approved, and the second confirms that the device is assigned to that user.

## Task 8: Handle a wrong device with `elif`

I added an `elif` statement for the case when the user is approved but the device ID does not match.

```python
if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but",
          device_id, "is not their assigned device.")
```

```
The user sgilmore is approved to access the system.
4n482ts is the assigned device for sgilmore
```

**What I observed:** with the correct device, two lines are displayed. With a different device ID, the output says the user is approved but the device is not assigned to them.

**A limitation:** this version calls `.index()` before checking whether the username is approved. If the username is not in the list, `.index()` raises an error, and there is no branch that handles an unapproved user. Task 9 fixes both problems.

## Task 9: Put it all in a `login` function

To finish the algorithm, I defined a function named `login` that takes a `username` and a `device_id`. It uses a **nested conditional**:

- The **outer** conditional handles whether the username is approved.
- The **inner** conditional, which runs only for approved users, handles whether the device ID is correct.

```python
def login(username, device_id):
    # If `username` belongs to `approved_users`,
    if username in approved_users:
        print("The user", username, "is approved to access the system.")

        # find the index of `username`
        ind = approved_users.index(username)

        # If `device_id` matches the device at that index,
        if device_id == approved_devices[ind]:
            print(device_id, "is the assigned device for", username)
        # Otherwise,
        else:
            print(device_id, "is not their assigned device.")

    # Otherwise, the username is not approved
    else:
        print("The user", username, "is not approved to access the system.")
```

I called the function with different combinations to test it:

```python
login("bmoreno", "hl0s5o1")
login("elarson", "r2s5r9g")
login("abernard", "4n482ts")
```

```
The user bmoreno is approved to access the system.
hl0s5o1 is the assigned device for bmoreno
The user elarson is approved to access the system.
r2s5r9g is not their assigned device.
The user abernard is not approved to access the system.
```

**What I observed:** after Python enters the inner conditional, a correct `device_id` makes the `if` condition true, so a message confirms the device is assigned to the user. An incorrect `device_id` makes it false, so Python runs the `else` block and says the device does not belong to the user.

Because `.index()` only runs inside the outer `if`, an unapproved username like `"abernard"` no longer causes an error. The complete script is in [`device_login_algorithm.py`](device_login_algorithm.py).

## Key takeaways

- List indexing works like string indexing: the first element is at index 0.
- `.append()` adds a new element to the end of a list.
- `.remove()` deletes a specific element from a list.
- `.index()` returns the position of an element in a list (and it works with other sequence types, such as strings).
- When two lists hold related information in the same order, their elements can be matched using the same index.
- Functions help build algorithms by organizing instructions into reusable blocks, with parameters that define the inputs.

