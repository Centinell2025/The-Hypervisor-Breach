<div align="center">
  <img src="https://raw.githubusercontent.com/Centinell2025/the-last-evidence-standing/main/branding/BEACON_SEAL.png" alt="Beacon of the Eagle LLC — logotipo corporativo" width="165" />
  <p><strong>BEACON OF THE EAGLE LLC</strong><br/><strong>CENTINELL SUITE DEFENSE</strong></p>
</div>

# The Hypervisor Breach

**Hack The Box Sherlock candidate | Very Easy | DFIR**

## EarthCentinell-inspired training case

A fictional infrastructure team detects a suspicious login on its virtualization host. Investigate the provided authentication and VM activity logs to determine which account, source, host and virtual machine were involved, and what snapshot actions followed.

**All organizations, assets, identities, IP addresses and events are synthetic.** EarthCentinell is the thematic inspiration; this challenge does not represent a real compromise of any product or organization. Documentation-only IP address ranges are used.

## Start here

1. Read [PLAYER-INSTRUCTIONS.md](PLAYER-INSTRUCTIONS.md).
2. Use the original [authentication](evidence/authentication.csv), [VM activity](evidence/vm_activity.csv) and [asset inventory](evidence/asset_inventory.csv) together with [API activity](evidence/hypervisor_api_audit.csv), [ticket state](evidence/change_tickets.csv), [snapshot lifecycle](evidence/snapshot_lifecycle.csv) and [network ACL](evidence/management_network_acl.csv).
3. Solve the **original eight questions plus eight correlation questions** in [QUESTIONS.md](QUESTIONS.md). See [forensic limitations](docs/FORENSIC_SCOPE.md). All timestamps are UTC.

No hypervisor, virtual machine, network access or offensive tooling is required. The private instructor writeup is not published here.

## Verified student ZIP

The student ZIP is generated and tested in [GitHub Actions](https://github.com/Centinell2025/The-Hypervisor-Breach/actions/workflows/validate.yml). After a successful run, download the `hypervisor-breach-student` artifact and extract `The-Hypervisor-Breach-STUDENT.zip`. It includes all eight CSV sources, the SHA-256 inventory, the 16 questions and onboarding documents.

Local QA (Python standard library only):

```bash
python3 tools/build_student_zip.py
python3 -m unittest discover -s tests -v
```

The student ZIP is **not password encrypted**; no encryption capability or reviewer password is claimed. Instructor answers must be delivered privately to HTB only after independent verification. GitHub Actions success does not establish accepted difficulty or payment.

## Scope

This is an entry-level log-correlation exercise, not an advanced hypervisor exploitation lab. No actual snapshot export image or authenticated production hypervisor telemetry is included. The added sources are simulated and explicitly marked unverified. The scenario is fictional and designed solely for defensive education.
