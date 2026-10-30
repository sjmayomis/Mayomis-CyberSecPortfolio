# Vulnerability Assessment Report

**Date:** October 23, 2026

## Scenario

I am a newly hired cybersecurity analyst at an e-commerce company. The company stores its data on a remote database server because many employees work remotely from locations around the world. Employees regularly query the server to find potential customers. The database has been open to the public since the company launched three years ago, which is a serious vulnerability. This report explains the risk this server poses to business operations and how it can be secured.

## System Description

The server has a powerful CPU and 128 GB of memory. It runs the latest version of the Linux operating system and hosts a MySQL database management system. It has a stable network connection using IPv4 addresses and communicates with other servers on the network. Existing security measures include SSL/TLS encrypted connections.

## Scope

This assessment covers the current access controls of the system over a three-month period, from October 23, 2026 to January 2027. [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) was used to guide the risk analysis of the information system.

## Purpose

**How is the database server valuable to the business?**
The server stores the information employees use to find potential customers, so it directly supports sales and daily operations. Because the workforce is remote, it is also the central place where employees across the world get the data they need.

**Why is it important for the business to secure the data on the server?**
The data is sensitive and valuable. If it is stolen, altered, or deleted, the company could face financial loss, damaged customer trust, and possible legal consequences. The database has been open to the public for three years, so it should be assumed that attackers could already have found it.

**How might the server impact the business if it were disabled?**
Employees would not be able to access customer data, which would halt sales activity and slow or stop daily operations until the server is restored. The longer the outage, the greater the lost revenue and the harm to the company's reputation.

## Risk Assessment

Likelihood and severity are each scored from 1 (low) to 3 (high). Risk = likelihood × severity.

| Threat source | Threat event | Likelihood | Severity | Risk |
|---|---|:---:|:---:|:---:|
| Hacker | Obtain sensitive information via exfiltration | 3 | 3 | **9** |
| Employee | Disrupt critical operations and/or sell sensitive information | 2 | 3 | **6** |
| Customer | Alter or delete critical information | 1 | 3 | **3** |

## Risk Interpretation

A hacker with unauthorized access poses the highest risk, with a score of **9**. Because the database is publicly accessible, attackers can easily find the server and attempt to exploit it.

Employee-related risk scores **6** because employees have legitimate access to company resources and could misuse their privileges.

Customer-related risk scores **3**, the lowest of the three. It should still be addressed with appropriate access controls, because unauthorized modification or deletion of information could still affect business operations.

## Approach

The risks were selected and evaluated based on the database server's public exposure, its importance to daily operations, and the sensitivity of the information stored on it. A publicly accessible database gives external attackers more opportunity to gain unauthorized access, steal critical information, or disrupt operations.

**Likelihood** reflects how likely each threat source is to successfully exploit the identified vulnerability. Hackers were given the highest score because the server is reachable from the internet. Employees and customers were given lower scores because they are less likely to have the same level of access or opportunity.

**Severity** is based on the potential impact on the confidentiality, integrity, and availability of company data. A score of 3 is assigned to threats that could cause significant data loss, unauthorized disclosure, or disruption of critical business operations.

**Overall risk** is calculated by multiplying likelihood by severity.

**Limitations:** This assessment is based only on the information provided about the database. It does not include a full vulnerability scan, penetration testing, a source-code review, or a detailed review of existing security configurations (such as firewalls and IDS/IPS).

## Remediation Strategy

The most important recommendation is to remove direct public access to the database server. Only authorized employees and applications that need the database should be able to reach it.

1. **Restrict network access:** Configure firewall rules to block direct public access to the MySQL database. Allow connections only from approved applications, servers, VPNs, or trusted IP addresses.
2. **Use a VPN or secure access gateway:** Because most employees work remotely, they should be required to connect to the database through a company-approved VPN or secure access solution.
3. **Implement strong authentication:** Enforce a strong password policy and multi-factor authentication (MFA) for all employees.
4. **Apply least privilege:** Give employees only the access they need to do their jobs, and limit administrative privileges to authorized personnel.
5. **Encrypt sensitive information:** Continue using SSL/TLS for data in transit between clients and the database, and protect sensitive data stored in the database with encryption at rest.
6. **Segment the network:** Place the database on a separate network segment. If an attacker gets into the company network, it will be harder for them to reach the sensitive data.
7. **Keep systems updated:** Regularly update the Linux operating system, the MySQL database, and all other software to fix known vulnerabilities.
8. **Enable monitoring and logging:** Log database access, authentication attempts, and unusual queries. Review the logs regularly to catch possible unauthorized access.
9. **Perform regular backups:** Keep secure, tested backups of critical data so it can be restored if it is deleted, corrupted, or affected by a security incident.
10. **Conduct regular vulnerability assessments:** Run periodic vulnerability scans and security assessments to find new weaknesses and confirm that controls remain effective.

## Overall Improvement

Implementing these controls will significantly reduce the database server's exposure to external threats. Restricting public access, enforcing least privilege, monitoring activity, and maintaining secure backups will help protect the confidentiality, integrity, and availability of the company's data. These improvements will lower the likelihood of data breaches and service disruptions while still supporting the company's remote-work needs.
