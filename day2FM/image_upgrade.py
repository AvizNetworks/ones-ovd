from client import FMClient

conn = FMClient(url = "http://192.168.0.1:8787")
payload_for_image_upgrade = [{"ip":"192.168.0.xx","pathToImage":"http://192.168.0.xx:8192/path_of_file/filename.bin"}]
result = conn.custom_image_upgrade(payload_for_image_upgrade)
