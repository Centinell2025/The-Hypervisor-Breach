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
2. Open [evidence/authentication.csv](evidence/authentication.csv), [evidence/vm_activity.csv](evidence/vm_activity.csv), and [evidence/asset_inventory.csv](evidence/asset_inventory.csv).
3. Solve the eight questions in [QUESTIONS.md](QUESTIONS.md). All timestamps are UTC.

No hypervisor, virtual machine, network access or offensive tooling is required. The private instructor writeup is not published here.

## Packaging for HTB

The player ZIP is prepared separately with password `hackthebox`. The ZIP must be hosted at a downloadable URL before completing the HTB submission form. Instructor solutions must be shared privately with HTB, not committed to this public repository.

## Scope

This is an entry-level log-correlation exercise, not an advanced hypervisor exploitation lab. The scenario is fictional and designed solely for defensive education.
