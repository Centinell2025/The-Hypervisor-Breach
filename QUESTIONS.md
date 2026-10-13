# Investigation questions
Use exact values from the evidence. All timestamps are UTC.
1. Which hypervisor host recorded the suspicious successful login?
2. What account was used for that successful login?
3. What was the source IP address of the suspicious login?
4. At what exact UTC timestamp did that login succeed?
5. Which VM was affected by the subsequent snapshot activity?
6. What was the first snapshot-related action taken after the login?
7. At what exact UTC timestamp was the snapshot exported?
8. What was the final recorded authentication event for the suspicious source IP?

## Additional correlation questions — Very Easy extension

9. Which **API session ID** correlates the suspicious successful login with the creation and export actions on the affected VM? Answer format: `HVS-NNN`.
10. Which **API audit event ID** records the export of that VM's snapshot? Answer format: `API-NNN`.
11. Which **datastore** is identified for the correlated export action? Answer format: datastore name.
12. What is the status of the **change ticket** requesting an export on the affected VM during the relevant window? Answer format: exact status token.
13. Which **snapshot ID** appears in both create and export lifecycle records for that session? Answer format: snapshot ID.
14. How many seconds elapsed from the successful login at 09:15:03 UTC to the snapshot creation at 09:16:24 UTC? Answer format: integer seconds.
15. What was the management-network firewall decision for the suspicious source's TCP connection to port 443? Answer format: `allow` or `deny`.
16. Does this student evidence contain a verified export of the actual VM snapshot disk bytes? Answer format: `YES` or `NO` (this is separate from a successful API log status).

### Optional management conclusion (human reviewed)

Identify the actions actually *recorded* versus artifacts independently *acquired*, and recommend containment, preservation of a hypervisor console audit, approval-system reconciliation and restoration only after access review. A successful API operation does **not** prove compromise of the hypervisor kernel, a real person's identity or exfiltration to an external network.

**All hosts, identities, networks and events are fictional training records. Instructor answers are not part of the student ZIP.**
