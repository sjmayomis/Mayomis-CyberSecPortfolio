# Incident Handler's Journal

A record of incident response and network analysis exercises I completed as part of the Google Cybersecurity Certificate. Each entry documents the scenario, the tools I used, and what I learned.

| Entry | Date | Topic | Tool |
|---|---|---|---|
| [#1](#entry-1-ransomware-attack-on-a-health-care-clinic) | October 10, 2026 | Ransomware incident | None (documentation) |
| [#2](#entry-2-analyzing-a-packet-capture-file) | October 18, 2026 | Packet capture analysis | Wireshark |
| [#3](#entry-3-capturing-my-first-packet) | October 18, 2026 | Live traffic capture | tcpdump |
| [#4](#entry-4-investigating-a-suspicious-file-hash) | October 18, 2026 | Malware investigation | VirusTotal |

---

## Entry #1: Ransomware attack on a health care clinic

**Date:** October 10, 2026

**Scenario:** A small U.S. primary-care clinic was hit by a ransomware attack on a Tuesday morning at about 9:00 a.m. Employees could not open files such as medical records, and a ransom note appeared on their computers. It said an organized hacking group that targets healthcare and transportation had encrypted the company's files and demanded payment for the decryption key. The attackers got in through phishing emails with a malicious attachment, which installed malware when an employee opened it. Operations shut down, and the clinic had to take its systems offline and contact outside organizations for help.

**Description:** Documenting a ransomware incident. It covers two phases of the incident response lifecycle:

- **Detection and Analysis:** Employees reported that they could not access files and that a ransom note was displayed. The ransomware was identified, and the phishing email was traced as the point of entry.
- **Containment, Eradication, and Recovery:** The clinic shut down its computer systems to stop the spread and contacted external organizations for technical help and to report the incident.

**Tool(s) used:** None.

**The 5 W's**

- **Who:** An organized group of hackers known to target healthcare and transportation organizations
- **What:** A ransomware attack that encrypted critical files and demanded payment
- **Where:** A small primary-care clinic in the U.S.
- **When:** Tuesday at approximately 9:00 a.m.
- **Why:** An employee opened a malicious attachment in a phishing email, which gave the attackers access. They then deployed ransomware, encrypted critical patient files, and left a ransom note demanding money for the decryption key.

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

---

## Entry #2: Analyzing a packet capture file

**Date:** October 18, 2026

**Scenario:** As a security analyst investigating traffic to a website, I analyzed a packet capture file of a user connecting to an internet site. The goal was to identify the source and destination IP addresses, examine the protocols used, and analyze some packets to see what information was sent and received.

**Description:** Analyzing a packet capture file.

**Tool(s) used:** Wireshark, a network protocol analyzer with a graphical interface. It lets security analysts capture and analyze network traffic, which helps in detecting and investigating malicious activity.

**What I did**

[TODO: Describe your steps, for example which filters you applied.]

**What I found**

- **Source and destination IP addresses:** [TODO]
- **Protocols observed:** [TODO]
- **Type of data sent and received:** [TODO]

**Takeaway:** [TODO: One or two sentences on what this shows about analyzing traffic.]

---

## Entry #3: Capturing my first packet

**Date:** October 18, 2026

**Scenario:** As a network analyst, I used tcpdump on a Linux virtual machine to capture live network traffic, save it to a packet capture (pcap) file, and examine the contents to focus on specific types of traffic.

**Description:** Capturing network traffic from the command line.

**Tool(s) used:** tcpdump, a command-line network protocol analyzer. Like Wireshark, it lets analysts capture, filter, and analyze network traffic.

**What I did**

[TODO: List the commands you used, for example identifying the network interface, capturing packets, saving to a file, and filtering.]

**What I found**

[TODO: Describe the traffic you saw and what the filters showed.]

**Takeaway:** [TODO: One or two sentences on when you would use tcpdump versus Wireshark.]

---

## Entry #4: Investigating a suspicious file hash

**Date:** October 18, 2026

**Scenario:** As a level-one SOC analyst at a financial services company, I received an alert about a suspicious file downloaded on an employee's computer. An employee received an email with a password-protected spreadsheet and the password in the body of the email. After opening it, a malicious payload ran on their computer. I created a SHA-256 hash of the file and used VirusTotal to find related indicators of compromise (IoCs).

**Description:** Investigating a suspicious file hash.

**Tool(s) used:** VirusTotal, an investigative tool that analyzes files and URLs for malicious content such as viruses, worms, and trojans.

**The 5 W's**

- **Who:** An unknown malicious actor
- **What:** An email sent to an employee contained a malicious attachment with the SHA-256 hash `54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b`
- **Where:** An employee's computer at a financial services company
- **When:** 1:20 p.m.
- **Why:** An employee downloaded and opened a malicious attachment from an email, which executed a malicious payload.

**What I found in VirusTotal**

- **Detection ratio:** [TODO: for example, how many security vendors flagged the file]
- **Related IoCs:** [TODO: domains, IP addresses, or file names associated with the hash]
- **Malware family or behavior:** [TODO]

**Additional notes**

*How can this incident be prevented in the future?*
- Train employees to be cautious with unexpected attachments, especially password-protected files with the password in the same email.
- Use an email gateway that scans or sandboxes attachments, and block risky file types and macros.
- Use endpoint detection and response (EDR) to catch and stop malicious payloads.
- Add known-bad file hashes and related IoCs to blocklists.
- Apply least privilege so a compromised account has limited reach.
