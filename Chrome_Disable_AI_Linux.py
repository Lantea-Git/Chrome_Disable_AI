import json
import os
import time



policy_dir = "/etc/opt/chrome/policies/managed"
policy_file = os.path.join(policy_dir, "chrome_policies.json")

policies = {
    "LensOverlaySettings": 1,
    "SearchContentSharingSettings": 1,
    "AIModeSettings": 1
}
content = json.dumps(policies, indent=2)

os.system(f"sudo mkdir -p {policy_dir}")
os.system(f"echo '{content}' | sudo tee {policy_file}")

print(f"Politiques écrites dans {policy_file}")
time.sleep(1)
