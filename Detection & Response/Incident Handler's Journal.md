# Incident Handler's Journal

A record of incident response and network analysis exercises I completed as part of the Google Cybersecurity Certificate. Each entry documents the scenario, the tools I used, and what I learned.

**Scenario #1**

A small U.S. health care clinic specializing in delivering primary-care services experienced a security incident on a Tuesday morning, at approximately 9:00 a.m. Several employees reported that they were unable to use their computers to access files like medical records. Business operations shut down because employees were unable to access the files and software needed to do their job.

Additionally, employees also reported that a ransom note was displayed on their computers. The ransom note stated that all the company's files were encrypted by an organized group of unethical hackers who are known to target organizations in healthcare and transportation industries. In exchange for restoring access to the encrypted files, the ransom note demanded a large sum of money in exchange for the decryption key.

The attackers were able to gain access into the company's network by using targeted phishing emails, which were sent to several employees of the company. The phishing emails contained a malicious attachment that installed malware on the employee's computer once it was downloaded.

Once the attackers gained access, they deployed their ransomware, which encrypted critical files. The company was unable to access critical patient data, causing major disruptions in their business operations. The company was forced to shut down their computer systems and contact several organizations to report the incident and receive technical assistance.

| **Date:** October 10, 2026 | **Entry:**<br><br>#1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description                | Documenting a cybersecurity incident<br><br>This incident occurred in the two phases in the Detection and Analysis and in the Containment, Eradication, and Recovery:                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Tool(s) used               | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| The 5 W's                  | • **Who**: Group of unethical hackers<br>• **What**: ransomware security incident<br>• **Where**: At a health care company<br>• **When**: Tuesday 9:00 a.m.<br>• **Why**: The incident happened when the unethical hackers gained access the company's systems using a phishing attack. After an unsuspecting company employee downloaded malicious files containing malware on the emails, the attackers launched their ransomware on the company's systems by encrypting critical files. after that the attackers left a note demanding a large sum of money for the decryption key. |
| Additional notes           | 1\. How could the health care company prevent an incident like this from occurring again?<br>2\. Should the company pay the ransom to retrieve the decryption key?                                                                                                                                                                                                                                                                                                                                                                                                                     |

**Additional notes**

*How could the clinic prevent this from happening again?*
- Run regular security awareness training so employees can spot phishing emails.
- Use email filtering and attachment sandboxing to block malicious attachments.
- Deploy endpoint protection (EDR/antivirus) and keep systems patched.
- Require multi-factor authentication and limit user privileges.
- Keep tested, offline backups of patient data so files can be restored without paying.
- Segment the network so malware cannot spread easily, and maintain a written incident response plan.

*Should the company pay the ransom?*
Generally no. Paying does not guarantee the files will be restored, it funds criminal groups, and it can mark the clinic as a target for future attacks. Law enforcement agencies such as the FBI and CISA advise against paying. In a healthcare setting, patient safety could push leadership toward considering payment, so the decision should be made with legal counsel, law enforcement, and incident response experts. Good backups are the best way to avoid facing that choice.


**Scenario #2**

In this scenario, you're a security analyst investigating traffic to a website.

You'll analyze a network packet capture file that contains traffic data related to a user connecting to an internet site. The ability to filter network traffic using packet sniffers to gather relevant information is an essential skill as a security analyst.

You must filter the data in order to:

identify the source and destination IP addresses involved in this web browsing session,

examine the protocols that are used when the user makes the connection to the website, and

analyze some of the data packets to identify the type of information sent and received by the systems that connect to each other when the network data is captured.

| **Date:** October 18, 2026 | **Entry:<br>**#2                                                                                                                                                                                                                                                                               |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description                | Analyzing a packet capture file                                                                                                                                                                                                                                                                |
| Tool(s) used               | For this activity, I only used Wireshark to analyze a packet capture file. Wireshark is a network protocol analyzer that allows security analysts to capture and analyze network traffic and uses a graphical user interface. This can help in detecting and investigating malicious activity. |
| The 5 W's                  | • **Who**: N/A<br>• **What**: N/A<br>• **Where**: N/A<br>• **When**: N/A<br>• **Why**: N/A                                                                                                                                                                                                     |
| Additional notes           | N/A                                                                                                                                                                                                                                                                                            |

**Scenario #3**

As a security analyst, it's important to know how to capture and filter network traffic in a Linux environment. You'll also need to know the basic concepts associated with network interfaces.

In this lab activity, you'll perform tasks associated with using tcpdump to capture network traffic. You'll capture the data in a packet capture (p-cap) file and then examine the contents of the captured packet data to focus on specific types of traffic.

You're a network analyst who needs to use tcpdump to capture and analyze live network traffic from a Linux virtual machine.

| **Date:** October 18, 2026 | **Entry:**<br><br>#3                                                                                                                                                                                                                                                                                                  |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description                | Capturing my first packet                                                                                                                                                                                                                                                                                             |
| Tool(s) used               | For this activity, I used tcpdump to capture and analyze network traffic. Tcpdump is a network protocol analyzer that's accessible using the command-line interface. Similar to Wireshark, the value of tcpdump in cybersecurity is that it allows security analysts to capture, filter, and analyze network traffic. |
| The 5 W's                  | • **Who**: N/A<br>• **What**: N/A<br>• **Where**: N/A<br>• **When**: N/A<br>• **Why**: N/A                                                                                                                                                                                                                            |
| Additional notes           |                                                                                                                                                                                                                                                                                                                       |

**Scenario #4**

Review the following scenario. Then complete the step-by-step instructions.

You are a level one security operations center (SOC) analyst at a financial services company. You have received an alert about a suspicious file being downloaded on an employee's computer.

You investigate this alert and discover that the employee received an email containing an attachment. The attachment was a password-protected spreadsheet file. The spreadsheet's password was provided in the email. The employee downloaded the file, then entered the password to open the file. When the employee opened the file, a malicious payload was then executed on their computer.

You retrieve the malicious file and create a SHA256 hash of the file. You might recall from a previous course that a **hash function** is an algorithm that produces a code that can't be decrypted. Hashing is a cryptographic method used to uniquely identify malware, acting as the file's unique fingerprint.

Now that you have the file hash, you will use VirusTotal to uncover additional IoCs that are associated with the file.

| **Date:** October 18, 2026 | **Entry:**<br><br>#4                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description                | Investigate a suspicious file hash                                                                                                                                                                                                                                                                                                                                                                                  |
| Tool(s) used               | For this activity, I used VirusTotal an investigative tool that analyzes files and URLs for malicious content such as viruses, worms, trojans, and more.                                                                                                                                                                                                                                                            |
| The 5 W's                  | • **Who**: An unknown malicious actor<br>• **What**: An email sent to an employee contained a malicious file attachment with the SHA-256 file hash of 54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b<br>• **Where**: An employee's computer at a financial services company<br>• **When**: At 1:20 p.m.<br>• **Why**: An employee downloaded and executed a malicious file attachment via e-mail. |
| Additional notes           | How can this incident be prevented in the future?                                                                                                                                                                                                                                                                                                                                                                   |

*How can this incident be prevented in the future?*
- Train employees to be cautious with unexpected attachments, especially password-protected files with the password in the same email.
- Use an email gateway that scans or sandboxes attachments, and block risky file types and macros.
- Use endpoint detection and response (EDR) to catch and stop malicious payloads.
- Add known-bad file hashes and related IoCs to blocklists.
- Apply least privilege so a compromised account has limited reach.






