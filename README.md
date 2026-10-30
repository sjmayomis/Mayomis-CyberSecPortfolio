# Mayomis Cybersecurity Portfolio

**Aspiring SOC Analyst** | BSIT (Network and Security) | Google Cybersecurity Certificate

I'm a BSIT graduate with a major in Network and Security, and I hold the Google Cybersecurity Certificate. I'm focused on starting a career in Security Operations. This portfolio collects the labs and projects I've completed to build my skills in detection, response, and security fundamentals. Each project has a write-up that explains what I did, the tools I used, and what I learned.

## Contact

- LinkedIn: [Stephen Joshua Mayomis](https://www.linkedin.com/in/stephen-joshua-mayomis-357805376/)
- Email: stephenjoshuamayomis@gmail.com

## Featured projects

- **[Vulnerability Assessment Report](Assets%2C%20Threats%20%26%20Vulnerabilities/Analyze%20a%20Vulnerable%20System%20For%20a%20Small%20Business.md):** assessed the risk of a publicly exposed database server, scored the threats, and recommended ten controls to secure it.
- **[Incident Handler's Journal](Detection%20%26%20Response/Incident%20Handler%27s%20Journal.md):** documented a ransomware incident, a packet capture analysis, and a malicious file investigation.
- **[Suricata Lab](Detection%20%26%20Response/Suricata%20Lab.md):** examined an IDS rule, triggered it with a sample capture, and analyzed the alerts in JSON logs.

## Skills and tools

| Area | Tools and concepts |
|---|---|
| Network analysis | Wireshark, tcpdump, packet capture and traffic analysis (IP, MAC, DNS, TCP, HTTP, ICMP) |
| Intrusion detection | Suricata rules and alerts, `eve.json` log analysis with `jq` |
| Incident response | Incident handler's journal, the incident response lifecycle, VirusTotal for file hash investigation |
| Frameworks and risk | NIST Cybersecurity Framework, NIST SP 800-30 risk assessment, vulnerability assessment, security audit |
| Linux | Command line, file permissions, `chmod` |
| SQL | MariaDB queries with `WHERE`, `AND`, `OR`, `NOT`, and `LIKE` |
| Python | File handling, lists and loops, conditionals, functions, security automation |

## Projects

| Project | What I did | Tools | Link |
|---|---|---|---|
| Company Security Audit | Completed a security audit of a fictional company, covering controls and compliance | NIST CSF, risk assessment | [BotiumToys_SecAudit.md](Conducting%20Company%20Security%20Audit/BotiumToys_SecAudit.md) |
| Assets, Threats & Vulnerabilities | Wrote a vulnerability assessment for an exposed database server, scored the risks, and explained the business impact | NIST SP 800-30, MySQL | [View report](Assets%2C%20Threats%20%26%20Vulnerabilities/Analyze%20a%20Vulnerable%20System%20For%20a%20Small%20Business.md) |
| Network and Security | Used the NIST Cybersecurity Framework to analyze a DoS (ICMP flood) incident and plan improvements | NIST CSF | [View analysis](Network%20and%20Security/NIST%20Cybersecurity%20Framework%20Analysis.md) |
| Linux & SQL | Filtered login and employee data with SQL, and fixed file and directory permissions with `chmod` | MariaDB, Linux | [View projects](Linux%20%26%20SQL/README.md) |
| Detection & Response | Analyzed network traffic, examined detection rules, and documented incidents | Wireshark, tcpdump, Suricata, VirusTotal | [View projects](Detection%20%26%20Response/README.md) |
| Python Automation | Built an algorithm that updates an IP allow list and one that verifies users and their devices | Python | [View projects](Python%20Automation/README.md) |

## Repository structure

```
Mayomis-CyberSecPortfolio/
├── Assets, Threats & Vulnerabilities/   Vulnerability assessment report
├── Conducting Company Security Audit/   Security audit
├── Detection & Response/                Incident journal, Wireshark, tcpdump, and Suricata labs
├── Linux & SQL/                         SQL filtering and Linux file permissions
├── Network and Security/                NIST Cybersecurity Framework analysis
├── Python Automation/                   Allow list and device login algorithms
├── LICENSE
└── README.md
```

## What I'm working on now

- Building a home lab to practice detection and response hands-on.

## Note on content

Projects are based on scenarios from the Google Cybersecurity Certificate. All data is fictional or from training environments. No real company data or credentials are included.
