from client import FMClient
import json

conn = FMClient(url = "http://192.168.0.1:8787")
payload = ["192.168.0.xx", "192.168.0.xx"] 
result = conn.ztp_enable(payload) 
