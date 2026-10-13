#!/usr/bin/env python3
"""Package the fictional Very Easy hypervisor Sherlock as a standalone student ZIP.

No simulator connectivity, image exploitation or customer data. The original
eight questions and original CSVs are kept intact; new exports are correlations.
"""
from __future__ import annotations
import csv
import hashlib
import sys
import zipfile
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"evidence"
OUTPUT=ROOT/"dist"/"The-Hypervisor-Breach-STUDENT.zip"
PAGES=("README.md","PLAYER-INSTRUCTIONS.md","QUESTIONS.md","docs/FORENSIC_SCOPE.md")
REQUIRED=("asset_inventory.csv","authentication.csv","vm_activity.csv","hypervisor_api_audit.csv","change_tickets.csv","snapshot_lifecycle.csv","management_network_acl.csv","acquisition_register.csv")

def rows(file):
    with (EVIDENCE/file).open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))

def require(ok,message):
    if not ok:raise ValueError(message)

def verify():
    auth=rows("authentication.csv")
    vm=rows("vm_activity.csv")
    api=rows("hypervisor_api_audit.csv")
    tickets=rows("change_tickets.csv")
    snaps=rows("snapshot_lifecycle.csv")
    acl=rows("management_network_acl.csv")
    acquisitions=rows("acquisition_register.csv")
    inventory=rows("asset_inventory.csv")
    login=[r for r in auth if r["source_ip"]=="198.51.100.77" and r["result"]=="success" and r["event"]=="login"]
    require(len(login)==1 and login[0]["username"]=="admin.ops" and login[0]["timestamp_utc"]=="2026-09-17T09:15:03Z","invalid unique suspicious login")
    key=[r for r in vm if r["username"]==login[0]["username"] and r["source_ip"]==login[0]["source_ip"] and r["vm_id"]=="EC-WEB-01"]
    require(len(key)==2 and {r["action"] for r in key}=={"create_snapshot","export_snapshot"},"unreproducible original VM questions")
    require(all(r["host"]==login[0]["host"] for r in key),"host mismatch")
    for action in ("create_snapshot","export_snapshot"):
        specific=[x for x in api if x["operation"]==action and x["session_id"]=="HVS-773" and
                  x["username"]==login[0]["username"] and x["source_ip"]==login[0]["source_ip"]]
        require(len(specific)==1,"API session/operation ambiguity: "+action)
        require(any(x["action"]==action and x["session_id"]=="HVS-773" and x["vm_id"]=="EC-WEB-01" and x["snapshot_id"]=="SNP-778" for x in snaps),
                "Snapshot lifecycle mismatch: "+action)
        require(specific[0]["timestamp_utc"]==next(x["timestamp_utc"] for x in key if x["action"]==action),"API original event UTC differs")
    require(any(x["ticket_id"]=="CHG-324" and x["status"]=="pending" and x["vm_id"]=="EC-WEB-01" for x in tickets),"Pending approval not evidenced")
    require(any(x["session_id"]=="HVS-773" and x["destination_port"]=="443" and x["decision"]=="allow" and x["source_ip"]=="198.51.100.77" for x in acl),"Firewall pivot ambiguous")
    require(any(x["host"]=="hv-earth-01" and x["asset_type"]=="hypervisor" for x in inventory),"Hypervisor inventory absent")
    require(len(acquisitions)==len(REQUIRED)-1 and all(r["original_system_authenticated"]=="no" for r in acquisitions),"Misrepresented independent hypervisor source authenticity")
    require(all(r["verified_artifact"]=="no" for r in snaps),"No real snapshot image is supplied or authenticated")
    elapsed=(datetime.fromisoformat("2026-09-17T09:16:24+00:00")-datetime.fromisoformat(login[0]["timestamp_utc"].replace("Z","+00:00"))).total_seconds()
    require(elapsed==81,"Unexpected login-to-snapshot interval")
    tasks=(ROOT/"QUESTIONS.md").read_text()
    for i in range(1,17):
        require(f"{i}." in tasks,"Missing question "+str(i))
    return dict(question_count=16,source_files=len(REQUIRED),origin="fictional-and-unverified")

def build():
    stats=verify()
    contents={name:(ROOT/name).read_bytes() for name in PAGES}
    for name in REQUIRED:contents["evidence/"+name]=(EVIDENCE/name).read_bytes()
    manifest="".join(f"{hashlib.sha256(contents['evidence/'+name]).hexdigest()}  {name}\n" for name in sorted(REQUIRED))
    contents["evidence/SHA256SUMS.txt"]=manifest.encode("utf-8")
    OUTPUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUTPUT,"w") as z:
        for name in sorted(contents):
            info=zipfile.ZipInfo(name,(2026,9,17,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o644<<16
            z.writestr(info,contents[name])
    with zipfile.ZipFile(OUTPUT) as z:
        require(z.testzip() is None,"damaged student ZIP")
        require(all(z.read(name)==content for name,content in contents.items()),"archive/content mismatch")
        require(not any("instructor" in n.lower() or "solution" in n.lower() or n.startswith(("tools/","tests/")) for n in z.namelist()),"private material present")
    print("PASS Hypervisor Very Easy:",stats,"student archive",OUTPUT)

if __name__=="__main__":
    try:build()
    except (ValueError,OSError,AssertionError,zipfile.BadZipFile) as e:
        print("FAIL:",e,file=sys.stderr)
        sys.exit(1)
