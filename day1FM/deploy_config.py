from client import FMClient

conn = FMClient(url = "http://192.168.0.1:8787")

file = "/home/aviz/ones-fm/yaml/IPCLOS-1-IPv4-SVI-AccessHosts.yaml"
result = conn.day1_intent_ovd_template(file)
