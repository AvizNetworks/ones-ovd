from client import FMClient

conn = FMClient(url = "http://192.168.0.1:8787")

payload_for_config_diff = { "ip": "192.168.0.xx"}
result = conn.get_config_diff(payload_for_config_diff)