# Python Automation

This folder contains two Python projects that automate everyday security tasks: keeping an access list up to date, and checking whether a user brought the device assigned to them. Both use core Python skills a security analyst relies on, including working with files, lists, loops, conditionals, and functions.

Both projects are based on scenarios from the Google Cybersecurity Certificate and use fictional data.

## Contents

| File | What it does | Concepts |
|---|---|---|
| [`update_allow_list.py`](update_allow_list.py) | Removes IP addresses on a remove list from the allow list file | File handling, strings and lists, loops, conditionals, functions |
| [`allow_list.txt`](allow_list.txt) | Sample allow list (fictional IP addresses) for running the script | |
| [`device_login_algorithm.py`](device_login_algorithm.py) | Checks whether a user is approved and whether they have their assigned device | Lists, indexing, `.append()`, `.remove()`, `.index()`, nested conditionals, functions |

## How to run

You need Python 3. From this folder:

```bash
python3 update_allow_list.py
python3 device_login_algorithm.py
```

> `update_allow_list.py` rewrites `allow_list.txt` in place. To run it again, restore the original file first.

## Project 1: Update an allow list

### Scenario

I am a security professional at a health care company. Access to a restricted subnetwork is limited by IP address. The IP addresses allowed to sign in are stored in `allow_list.txt`, and a separate remove list holds the addresses of employees who must no longer have access. The goal is to automate removing those addresses from the file.

### How the algorithm works

1. **Open the file** with a `with` statement in read mode (`"r"`). `with` closes the file automatically when the block ends.
2. **Read the contents** into one string with `.read()`.
3. **Convert the string to a list** with `.split()`. Strings are immutable, so a list is needed to change the contents.
4. **Loop through the remove list.** For each address that is in the allow list, remove it with `.remove()`.
5. **Convert the list back to a string** with `" ".join(...)`.
6. **Write the result back** to the file with a second `with` statement in write mode (`"w"`).

### Example

Running it removes the four addresses on the remove list:

```
Removed from the allow list: ['192.168.97.225', '192.168.158.170', '192.168.201.40', '192.168.58.57']
Updated allow list: ['192.168.25.60', '192.168.205.12', '192.168.6.9', ... ]
```

### Design notes

- **The loop runs over the remove list, not the allow list.** An earlier version looped over the allow list and removed items from it at the same time. Changing a list while looping over it can cause Python to skip items, for example when two addresses in a row are both on the remove list.
- **`while` handles duplicates.** `.remove()` only deletes the first match, so a `while` loop makes sure every copy of an address is removed.
- **The logic is in a function** (`update_allow_list`), so it can be reused with any file and any remove list.
- **The script handles a missing file.** It prints a clear message if `allow_list.txt` is not found.

## Project 2: Device login algorithm

### Scenario

I am a security analyst who developed an algorithm that connects users to their assigned devices. It checks that a user is approved on the system and that they brought the device assigned to them.

### How it works

The two lists are synchronized: the user at index 0 in `approved_users` uses the device at index 0 in `approved_devices`. That lets the algorithm use one index to look up both.

| Step | Technique |
|---|---|
| Access elements | List indexing (starts at 0) |
| Add a new user and device | `.append()` |
| Remove a user and device | `.remove()` / `.pop()` |
| Find where a user is in the list | `.index()` |
| Check the user and the device | A nested conditional inside a `login()` function |

The `login(username, device_id)` function works like this:

- **Outer condition:** is the username in `approved_users`? If not, the user is not approved.
- **Inner condition:** if the user is approved, does `device_id` match the device at the same index in `approved_devices`?

### Example output

```
login("bmoreno", "hl0s5o1")
The user bmoreno is approved to access the system.
hl0s5o1 is the assigned device for bmoreno

login("elarson", "r2s5r9g")
The user elarson is approved to access the system.
r2s5r9g is not their assigned device.

login("abernard", "4n482ts")
The user abernard is not approved to access the system.
```

### Design notes

- **The index lookup happens inside the `if`.** `.index()` raises an error if the value is not in the list, so it is only called after checking that the username is approved.
- **`remove_user()` finds the position once and removes from both lists.** That keeps the two lists synchronized, which the algorithm depends on.

## Skills demonstrated

- **Python file handling:** reading and writing text files with `with open(...)`
- **Data structures:** converting between strings and lists, and using list methods
- **Control flow:** `for` and `while` loops, `if`/`elif`/`else`, and nested conditionals
- **Functions:** organizing code into reusable blocks with parameters
- **Security automation:** automating access list maintenance and device verification
- **Debugging and safe coding:** avoiding changes to a list while looping over it, and checking values before looking them up
