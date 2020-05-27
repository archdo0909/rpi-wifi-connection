import os 

def turn_off_wifi():
    cmd = 'ifconfig wx down'
    os.system(cmd)

def turn_on_wifi():
    cmd = 'ifconfig wx up'
    os.system(cmd)

def generate_wpa(SSID, password):
  config_lines = [
    '\n',
    'network={',
    '\tssid="{}"'.format(SSID),
    '\tpsk="{}"'.format(password),
    '\tkey_mgmt=WPA-PSK',
    '}'
  ]

  config = '\n'.join(config_lines)
  print(config)

  with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a+") as wifi:
    wifi.write(config)

  print("Wifi config added")