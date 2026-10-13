# The Hypervisor Breach — Player Instructions

**BEACON OF THE EAGLE LLC — CENTINELL SUITE DEFENSE**  
**Difficulty:** Very Easy, preserved from the original scenario.

Investigate a fictional EarthCentinell-inspired hypervisor, a suspicious successful login, subsequent snapshot creation/export records, and management API activity. All records are synthetic and use reserved IP ranges. No VM, live hypervisor or network access is necessary.

1. Download the `hypervisor-breach-student` artifact from the latest successful [GitHub Actions run](https://github.com/Centinell2025/The-Hypervisor-Breach/actions/workflows/validate.yml).
2. Extract the enclosed `The-Hypervisor-Breach-STUDENT.zip`.
3. Verify `evidence/SHA256SUMS.txt` using `sha256sum -c SHA256SUMS.txt` from inside the `evidence/` directory.
4. Read [the sixteen questions](QUESTIONS.md), beginning with the original eight. Work with any CSV viewer or Python 3.
5. Match authentication, VM actions, API session, snapshot lifecycle, change approvals and network ACL decisions by exact identifiers and UTC timestamps.
6. State whether an API log assertion is independently corroborated by acquired snapshot bytes. It is not: **no actual VM disk image is distributed**.

This case teaches defensible event correlation and source limitations. Do not infer a rootkit, compromised physical system, real client data theft, or a named malicious human from fictional CSV records.

The student ZIP excludes instructor solutions. Its generation and tests are in the public development repository; participants in a blind evaluation should receive **only the student ZIP**.
