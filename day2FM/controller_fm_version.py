from client import FMClient

conn = FMClient(url = "http://192.168.0.1:8787")
result = conn.controller_fm_version()

