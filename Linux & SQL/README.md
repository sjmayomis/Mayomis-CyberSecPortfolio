# Linux & SQL

This folder contains two hands-on projects using the Linux command line and SQL. Both are everyday tools for a security analyst: Linux for managing access and working on servers, and SQL for searching through log and employee data during an investigation.

All projects are based on scenarios from the Google Cybersecurity Certificate and use fictional data from training environments.

## Contents

| Project | What I did | Tools | Link |
|---|---|---|---|
| Apply Filters to SQL Queries | Investigated failed after-hours logins, activity on specific dates, and logins from outside Mexico, then located employee machines by department and office | SQL (MariaDB) | [Open](Apply%20Filters%20to%20SQL%20Queries.md) |
| File Permissions in Linux | Reviewed file and directory permissions, found those that broke the organization's rules, and fixed them with `chmod` | Linux (`ls`, `cd`, `chmod`) | [Open](File%20Permissions%20in%20Linux.md) |

## Skills demonstrated

- **SQL filtering:** `SELECT`, `FROM`, and `WHERE`, combined with `AND`, `OR`, and `NOT`
- **Pattern matching:** `LIKE` with the `%` wildcard to match countries and office locations
- **Log investigation:** narrowing login data by time, date, and location to find suspicious activity
- **Linux permissions:** reading permission strings (user, group, and others) and changing them with `chmod`
- **Least privilege:** removing unnecessary access to files and directories, including hidden files
- **Linux command line:** navigating directories and listing contents with `pwd`, `cd`, `ls -a`, and `ls -la`

## Suggested reading order

1. **File Permissions in Linux** covers the command line basics and how access control works on a file system.
2. **Apply Filters to SQL Queries** moves on to searching and filtering data to investigate security issues.
