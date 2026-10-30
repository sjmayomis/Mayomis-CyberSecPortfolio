# Detection & Response

This folder contains my hands-on labs and incident documentation for detecting, analyzing, and responding to security events. They are the core skills of a SOC analyst: reading network traffic, writing detection rules, investigating suspicious files, and documenting incidents.

All projects are based on scenarios from the Google Cybersecurity Certificate and use fictional data from training environments.

## Contents

| Project | What I did | Tools | Link |
|---|---|---|---|
| Incident Handler's Journal | Documented four security exercises: a ransomware attack on a health care clinic, a packet capture analysis, a live traffic capture, and an investigation of a suspicious file hash | Wireshark, tcpdump, VirusTotal | [Open](Incident%20Handler%27s%20Journal.md) |
| Wireshark Lab | Analyzed a packet capture and used display filters to examine IP, MAC, DNS, TCP, and HTTP traffic | Wireshark | [Open](Wireshark%20Lab.md) |
| tcpdump Lab | Captured live traffic from the command line, saved it to a pcap file, and filtered and inspected the saved packets | tcpdump, curl | [Open](TCPdump%20Lab.md) |
| Suricata Lab | Examined a custom IDS rule, triggered it with a sample capture, and analyzed the alerts in the `eve.json` log | Suricata, jq | [Open](Suricata%20Lab.md) |

## Skills demonstrated

- **Network traffic analysis:** capturing packets, reading protocol layers, and filtering by IP address, MAC address, port, and protocol
- **Intrusion detection:** understanding how Suricata rules are built (action, header, and options) and testing them against a packet capture
- **Log analysis:** reading JSON alert logs and extracting specific fields with `jq`
- **Incident documentation:** recording incidents with the 5 W's (who, what, where, when, why) and tying them to the incident response lifecycle
- **Threat investigation:** looking up file hashes in VirusTotal to find related indicators of compromise
- **Linux command line:** running and filtering capture tools in a Linux environment

## Suggested reading order

1. **Wireshark Lab** introduces packet analysis with a graphical tool.
2. **tcpdump Lab** covers the same ideas from the command line.
3. **Suricata Lab** moves from reading traffic to writing detection rules and reviewing alerts.
4. **Incident Handler's Journal** shows how these tools are used when documenting real incident scenarios.
