# Botium Toys: Controls and Compliance Assessment

*Case study based on a fictional company, completed as part of the Google Cybersecurity Certificate.*

## Executive Summary

Botium Toys has a risk score of **8 out of 10**. Only **5 of 14** security controls are in place, and only **4 of 12** compliance best practices are met (PCI DSS 0/4, GDPR 2/4, SOC 2/4).

The most urgent gaps are that every employee can access cardholder data and customer PII/SPII, and that credit card information is not encrypted. Together these expose the company to a data breach and to penalties under PCI DSS and GDPR.

This report recommends 10 actions, starting with **least privilege, separation of duties, and encryption**.

## Scenario

Botium Toys is a small U.S. toy business with a single physical location (office, storefront, and warehouse) and a growing online presence in the U.S. and abroad. The IT manager is concerned about maintaining compliance and business operations as the company grows, and wants to understand the risks and possible fines caused by its current security posture. The company accepts online payments and serves customers in the European Union, so PCI DSS and GDPR both apply.

**My task:** review the IT manager's scope, goals, and risk assessment, then complete a controls and compliance checklist and make recommendations.

**Scope:** the entire security program at Botium Toys, including all assets, internal processes, and procedures.

**Goal:** determine which controls and compliance best practices need to be implemented to improve the company's security posture.

**Framework:** NIST Cybersecurity Framework (NIST CSF).

## Key Findings from the Risk Assessment

- **Risk score:** 8/10. The impact of losing an asset is rated medium because IT does not know which assets are at risk. The risk of fines is high.
- All employees can access internally stored data, including cardholder data and customer PII/SPII.
- Credit card information is accepted, processed, transmitted, and stored internally **without encryption**.
- Least privilege and separation of duties are not implemented.
- There is no IDS, no disaster recovery plan, and no backups of critical data.
- A password policy exists, but its requirements are weak and there is no centralized password management system.
- Legacy systems are monitored, but not on a regular schedule, and intervention methods are unclear.
- Strengths: a properly configured firewall, regularly monitored antivirus, a 72-hour breach notification plan for E.U. customers, enforced privacy policies, and good physical security (locks, CCTV, fire detection).

## Controls Assessment

Does Botium Toys currently have this control in place?

| Control | Category | Type | In place? | Evidence |
|---|---|---|---|---|
| Least privilege | Administrative | Preventative | ❌ No | All employees have access to internally stored data. |
| Disaster recovery plans | Administrative | Corrective | ❌ No | No disaster recovery plans exist. |
| Password policies | Administrative | Preventative | ❌ No | A policy exists, but its requirements are too weak and do not meet minimum complexity standards. |
| Separation of duties | Administrative | Preventative | ❌ No | Not implemented. |
| Firewall | Technical | Preventative | ✅ Yes | Blocks traffic according to an appropriately defined set of security rules. |
| Intrusion detection system (IDS) | Technical | Detective | ❌ No | No IDS is installed. |
| Backups | Technical | Corrective | ❌ No | No backups of critical company data. |
| Antivirus software | Technical | Corrective | ✅ Yes | Installed and regularly monitored by IT. |
| Manual monitoring, maintenance, and intervention for legacy systems | Technical | Preventative | ❌ No | Legacy systems are monitored, but there is no regular schedule and intervention methods are unclear. |
| Encryption | Technical | Deterrent | ❌ No | Credit card information is accepted, processed, transmitted, and stored without encryption. |
| Password management system | Technical | Preventative | ❌ No | No centralized system enforces the password policy. |
| Locks (offices, storefront, warehouse) | Physical | Deterrent / Preventative | ✅ Yes | Sufficient locks at the physical location. |
| Closed-circuit television (CCTV) | Physical | Preventative / Detective | ✅ Yes | Up-to-date CCTV surveillance. |
| Fire detection and prevention | Physical | Detective / Preventative | ✅ Yes | Functioning fire detection and prevention systems. |

**Result: 5 of 14 controls in place.**

## Compliance Assessment

### Payment Card Industry Data Security Standard (PCI DSS)

| Best practice | In place? | Evidence |
|---|---|---|
| Only authorized users have access to customers' credit card information. | ❌ No | All employees can access internally stored data, including cardholder data. |
| Credit card information is stored, accepted, processed, and transmitted in a secure environment. | ❌ No | Credit card information is stored internally without encryption. |
| Implement data encryption procedures to secure credit card transaction touchpoints and data. | ❌ No | Encryption is not used for customers' credit card information. |
| Adopt secure password management policies. | ❌ No | The password policy has weak requirements and there is no centralized password management system. |

**Result: 0 of 4.**

### General Data Protection Regulation (GDPR)

| Best practice | In place? | Evidence |
|---|---|---|
| E.U. customers' data is kept private and secured. | ❌ No | All employees can access internally stored data, and necessary controls to protect critical data are missing. |
| There is a plan to notify E.U. customers within 72 hours of a breach. | ✅ Yes | The company has an established plan. |
| Data is properly classified and inventoried. | ❌ No | The risk assessment states that asset management is inadequate and assets need to be identified and classified. |
| Privacy policies, procedures, and processes are enforced to properly document and maintain data. | ✅ Yes | Policies are developed and enforced. |

**Result: 2 of 4.**

### System and Organization Controls (SOC type 1, SOC type 2)

| Best practice | In place? | Evidence |
|---|---|---|
| User access policies are established. | ❌ No | Least privilege and separation of duties are not implemented, and access controls are inadequate. |
| Sensitive data (PII/SPII) is confidential and private. | ❌ No | Employees can access internally stored data, including PII/SPII. |
| Data integrity ensures data is consistent, complete, accurate, and validated. | ✅ Yes | IT has implemented controls to ensure data integrity. |
| Data is available to individuals authorized to access it. | ✅ Yes | IT ensures data availability. Note: because every employee has access, the set of "authorized" individuals is not clearly defined. |

**Result: 2 of 4.**

## Recommendations

Botium Toys should prioritize controls that protect sensitive customer information, reduce unauthorized access, and improve business continuity.

| Priority | Recommendation | NIST CSF function | Why |
|---|---|---|---|
| Critical | Implement least privilege | Protect | Restrict access to internal data based on job responsibilities. This greatly reduces the risk of unauthorized access to critical data. |
| Critical | Implement separation of duties | Protect | Ensures no single employee has excessive control over sensitive processes, reducing the risk of fraud, errors, and malicious activity. |
| Critical | Encrypt sensitive customer data | Protect | The company accepts, processes, transmits, and stores credit card information internally, so encryption is essential for PCI DSS and GDPR. |
| High | Strengthen the password policy | Protect | Require a minimum length and a combination of letters, numbers, and special characters, and enforce it consistently. |
| High | Implement a centralized password management system | Protect | Enforces password requirements for all employees and makes account recovery and resets more efficient. |
| High | Implement regular backups and a disaster recovery plan | Recover | Allows the company to recover from security incidents, system failures, or other events that disrupt operations. |
| High | Implement an intrusion detection system | Detect | Monitors for suspicious or anomalous network activity so incidents can be identified sooner. |
| Medium | Improve asset management and classification | Identify | Identify, inventory, and classify assets and determine which systems and data are most critical, so security resources can be allocated appropriately. Also supports GDPR. |
| Medium | Schedule monitoring and maintenance for legacy systems | Protect | Establish a regular schedule and document clear intervention procedures so outdated systems are managed consistently. |
| Ongoing | Prioritize PCI DSS and GDPR compliance | All | Since the company processes payments and does business in the E.U., maintain and improve access restrictions, encryption, data classification, privacy controls, and breach notification procedures. |

## Conclusion

Botium Toys has solid physical security, a working firewall and antivirus, and a breach notification plan, but its handling of sensitive customer data is the main weakness. Fixing access control and encryption first would close the largest gaps in PCI DSS and GDPR compliance and substantially reduce the risk of a damaging breach.
