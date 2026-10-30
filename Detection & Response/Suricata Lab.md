# Suricata Lab: Writing and Triggering a Custom Rule

## Overview

As a security analyst monitoring an employer's network, I configured Suricata (an open-source network intrusion detection system) to raise alerts on suspicious traffic. I examined a custom rule, ran Suricata against a sample packet capture to trigger it, and reviewed the results in Suricata's log files.

**Tools:** Suricata 7.0.10, `jq`, Linux command line

**Skills demonstrated:** reading IDS rule syntax, replaying packet captures through an IDS, analyzing alert logs in JSON

## Files used

| File | Purpose |
|---|---|
| `sample.pcap` | A packet capture with example network traffic, used to test the rules repeatably |
| `custom.rules` | The Suricata rules file that I examined and ran |
| `fast.log` | A quick, one-line-per-alert log (in `/var/log/suricata`). It is a deprecated format, so it is fine for quick checks but not for incident response or threat hunting |
| `eve.json` | Suricata's main log (in `/var/log/suricata`). It holds detailed alert data and other network events in JSON |

## Task 1: Examine a custom rule

I displayed the rule with `cat`:

```bash
cat custom.rules
```

![Contents of custom.rules](images/suricata-01-custom-rules.jpg)

```
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"GET on wire"; flow:established,to_server; content:"GET"; http_method; sid:12345; rev:3;)
```

A Suricata rule has three parts: the action, the header, and the rule options.

### Action

The action is the first word and sets what Suricata does when a packet matches. The common actions are:

- `alert`: generate an alert (the action used in this rule)
- `drop`: drop the traffic and generate an alert. This only works when Suricata runs in IPS mode
- `pass`: allow the traffic through. It can be used to make an exception to another rule
- `reject`: block the traffic and send a TCP reset packet

### Header

The header defines which traffic the rule applies to: protocol, source and destination addresses and ports, and direction.

![Rule header highlighted](images/suricata-02-rule-header.jpg)

- `http`: the rule applies only to HTTP traffic
- `$HOME_NET any -> $EXTERNAL_NET any`: traffic going from the home network (any port) to external networks (any port). The arrow shows the direction. `$HOME_NET` is a variable defined in `/etc/suricata/suricata.yaml` that stands for the organization's local network

### Rule options

The options, written in parentheses and separated by semicolons, narrow down exactly what to match.

![Rule options highlighted](images/suricata-03-rule-options.jpg)

| Option | Meaning |
|---|---|
| `msg:"GET on wire"` | The text shown in the alert |
| `flow:established,to_server` | Match only packets going from client to server in an established connection |
| `content:"GET"; http_method;` | Look for the text `GET` in the HTTP method of the packet |
| `sid:12345` | A unique ID for the signature |
| `rev:3` | The revision (version) of the signature |

**In summary:** this rule raises an alert whenever Suricata sees an HTTP GET request going from the home network to the outside.

## Task 2: Trigger the custom rule

I ran Suricata against the sample capture:

```bash
sudo suricata -r sample.pcap -S custom.rules -k none
```

![Running Suricata](images/suricata-04-run-suricata.jpg)

| Option | Meaning |
|---|---|
| `-r sample.pcap` | Read packets from a capture file instead of live traffic |
| `-S custom.rules` | Load only the rules in `custom.rules` |
| `-k none` | Disable checksum checks |

Suricata read 1 file containing 200 packets (54,238 bytes) and wrote its alerts to the log files.

## Task 3: Examine the `eve.json` output

`eve.json` holds much more detail than `fast.log`, and because it is JSON, other tools can process it easily. Displaying it with `cat` returns the raw, hard-to-read text:

```bash
cat /var/log/suricata/eve.json
```

![Raw eve.json output](images/suricata-05-eve-json-raw.jpg)

To make it readable I used `jq`:

```bash
jq . /var/log/suricata/eve.json | less
```

![eve.json formatted with jq](images/suricata-06-eve-json-jq.jpg)

`jq` can also pull out specific fields. This command returns only the timestamp, flow ID, alert signature, protocol, and destination IP:

```bash
jq -c "[.timestamp,.flow_id,.alert.signature,.proto,.dest_ip]" /var/log/suricata/eve.json
```

![Extracting specific fields with jq](images/suricata-07-jq-extract-fields.jpg)

## Findings

The rule triggered two alerts, both with the signature "GET on wire":

| Detail | Alert 1 | Alert 2 |
|---|---|---|
| Source IP | 172.21.224.2 | 172.21.224.2 |
| Destination IP | 142.250.1.139 | 142.250.1.102 |
| Destination port | 80 | 80 |
| Protocol | TCP (HTTP/1.1) | TCP (HTTP/1.1) |
| HTTP method / host | GET / `opensource.google.com` | GET / `opensource.google.com` |
| User agent | curl/7.74.0 | curl/7.74.0 |
| Response | 301 redirect to `https://opensource.google/` | 301 redirect to `https://opensource.google/` |
| Alert action | allowed | allowed |

The `alert` action only logs the traffic and does not block it, which is why `eve.json` shows the action as `allowed`.

## What I learned

- How a Suricata rule is built from an action, a header, and options
- How to replay a packet capture through Suricata to test rules safely and repeatably
- Why `eve.json` is better than `fast.log` for investigations, and how to use `jq` to read and filter it
