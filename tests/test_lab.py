"""Exact student archive, hypervisor source relationships and privacy checks."""
import csv,hashlib,subprocess,sys,unittest,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class HypervisorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable,str(ROOT/"tools/build_student_zip.py")],check=True)
    def test_player_zip_contains_original_and_new_sources(self):
        with zipfile.ZipFile(ROOT/"dist/The-Hypervisor-Breach-STUDENT.zip") as z:
            self.assertIsNone(z.testzip())
            for name in ("authentication.csv","vm_activity.csv","asset_inventory.csv","hypervisor_api_audit.csv","change_tickets.csv","snapshot_lifecycle.csv","management_network_acl.csv","acquisition_register.csv"):
                self.assertIn("evidence/"+name,z.namelist())
    def test_hash_manifest_matches_zip_evidence(self):
        with zipfile.ZipFile(ROOT/"dist/The-Hypervisor-Breach-STUDENT.zip") as z:
            for line in z.read("evidence/SHA256SUMS.txt").decode().splitlines():
                sha,name=line.split("  ",1)
                self.assertEqual(sha,hashlib.sha256(z.read("evidence/"+name)).hexdigest())
    def test_student_archive_no_private_solutions(self):
        with zipfile.ZipFile(ROOT/"dist/The-Hypervisor-Breach-STUDENT.zip") as z:
            self.assertFalse(any("solution" in n.lower() or "instructor" in n.lower() or n.startswith(("tools/","tests/")) for n in z.namelist()))
    def test_original_eight_still_present(self):
        text=(ROOT/"QUESTIONS.md").read_text()
        original=[
            "Which hypervisor host recorded the suspicious successful login?",
            "What account was used for that successful login?",
            "What was the source IP address of the suspicious login?",
            "At what exact UTC timestamp did that login succeed?",
            "Which VM was affected by the subsequent snapshot activity?",
            "What was the first snapshot-related action taken after the login?",
            "At what exact UTC timestamp was the snapshot exported?",
            "What was the final recorded authentication event for the suspicious source IP?",
        ]
        for q in original:self.assertIn(q,text)
        for i in range(9,17):self.assertIn(f"{i}.",text)
    def test_scope_excludes_real_disk_images(self):
        with (ROOT/"evidence/acquisition_register.csv").open(newline="") as f:
            self.assertTrue(all(x["original_system_authenticated"]=="no" for x in csv.DictReader(f)))
if __name__=="__main__":unittest.main()
