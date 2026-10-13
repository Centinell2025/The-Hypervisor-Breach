# The Hypervisor Breach — forensic scope

**Publisher:** Beacon of the Eagle LLC · Centinell Suite Defense  
**Difficulty:** Very Easy, preserving the original scope.

This beginner-friendly Sherlock centers on a **fictional** virtualization host and one suspected login. The participant correlates authentication, VM action, API audit, snapshot lifecycle, authorization state and management-network access-control decisions.

## Safe, bounded claims

These are **synthetic CSV exports**, not actual hypervisor vCenter/ESXi logs, a memory/disk acquisition, VM snapshot bytes, a verified login identity, or authenticated independent collectors. The exported snapshot is represented by a **successful local management API log record** and lifecycle assertion; **there is no actual VM disk export artifact**. An exporter status field alone cannot prove an Internet transfer, account compromise or data theft.

The scenario is inspired by the conceptual EarthCentinell training theme, not a real EarthCentinell deployment or compromise. All addresses are from documentation-only ranges, and no offensive tools or live infrastructure are used. A tutor should review interpretation questions; the original eight remain single-value prompts.

## Student workflow

1. Verify SHA-256 inventory `evidence/SHA256SUMS.txt`.
2. Join the login at 09:15 with API session, VM action, snapshot inventory, and change authorization.
3. Resolve the network ACL for the source/destination/management port.
4. State what is observed and what remains unproved.
5. Complete the eight original questions and eight additional correlation tasks.

**Readiness:** automatic file integrity/answerability tests and student ZIP availability do not establish acceptance by HTB.
