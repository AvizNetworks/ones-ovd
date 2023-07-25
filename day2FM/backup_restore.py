from client import FMClient
import json

conn = FMClient(url = "http://192.168.0.1:8787")

# Taking Backup at config
payload = [{"ip":"192.168.0.xx","label":"test_backup"}]
result = conn.backup_on_config(payload)

# Get all backups
payload = ["192.168.0.xx.12","192.168.0.xx.11"]
result = conn.backups(payload)

# Restore any backup as per timestamp
payload = [
    {"ip":"192.168.0.xx","timestamp":"USERINPUT"},
    {"ip":"192.168.0.xx","timestamp":"USERINPUT"}
]
result = conn.restore_config(payload)
