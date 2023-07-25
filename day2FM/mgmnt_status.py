from client import FMClient
import json

conn = FMClient(url = "http://192.168.0.1:8787")

payload = ["192.168.0.xx"]
status =  conn.get_image_mgmnt_status(payload)
print(json.dumps(status, indent= 4))