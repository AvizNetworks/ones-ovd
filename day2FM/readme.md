
# Day2 Operations example

This illustration demonstrates various day 2 operations such as backup&restore, compare config, image upgrade, reboot a device etc.
## Importing ONES Fabric Manager Agent

```py
from restclient.orchestration.client import FMClient
import json
```

## Setting Up connection
```py
conn = FMClient(url = "http://192.168.x.x:<port_number>") #usually <port_number> will be 8787
```

## Backup on Config
```py
payload = [{"ip":"192.168.x.x","label":"test_backup"}]
result = conn.backup_on_config(payload)
```

## Get all backups
```py
payload = ["192.168.x.1","192.168.x.2"]
result = conn.backups(payload)
```

## Restore Config
```py
payload = [
    {"ip":"192.168.x.1","timestamp":"USERINPUT"},
    {"ip":"192.168.x.2","timestamp":"USERINPUT"}
]
result = conn.restore_config(payload)
```

## Custom Image upgrade
To Trigger custom Image upgrade request
```py
payload_for_image_upgrade = [{"ip":"<ip address>","pathToImage":"<image path>"}]
## 'image path' example: http://192.168.0.2:8192/home/NOS.bin

result = conn.custom_image_upgrade(payload_for_image_upgrade)
```


## ZTP enable / Image Upgrade
To Trigger the ZTP, it take one or more device IPs as input
```py
payload = ["192.168.x.1", "192.168.x.2"] 
result = conn.ztp_enable(payload) # list of IPs
```


## Get Config Difference
To get the data to show in config diff in UI
```py
payload_for_config_diff = { "ip": "192.168.x.x"}
result = conn.get_config_diff(payload_for_config_diff)
```

## Get Controller version
```py
print("Controller Version ->")
result = conn.get_controller_version()
```

### Get management operation status of images
payload can be single IP, or list of IPs
```py
payload = ["192.168.x.x"]

status =  conn.get_image_mgmnt_status(payload)
print(json.dumps(status, indent= 4))
```


### Reboot a device
Only single ip should be pass at a time
```py
payload = ["192.168.x.x"]
result = conn.reboot(payload)
```

### Get controller / Fabric Manager version
```py
result = conn.controller_fm_version()
```

 ### Note - 
 The API calls  Day2FM are synchronous, meaning we have to wait for one API call to complete successfully or fail before proceeding. To ensure proper synchronization, it is advisable to call the **function get_image_mgmnt_status()** after each API call. This function will provide the values for the **device_action** field, which, in turn, will allow us to determine the status of an image based on the status field.

 - device_action = 0    **Failed**
 - device_action = 1    **Device is Free, can take any action**
 - device_action = 2    **image management operations in progress (custom/zip)**
 - device_action = 3    **reboot is in progress**

