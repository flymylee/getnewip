# Get my new Public IP

## What's this?

1. Uses [Requests](https://github.com/psf/requests) for retrieve the public IP address of the machine.
2. Modify selected batch file for updating a DNS record on AWS Route 53.

## How to use

0. First of all, **install python 3.x** on your computer.

1. If you don't know what to do, just type as following.

```
python getnewip.py --skeleton
```

2. Open your skeleton file, and modify it. But, the last key "Value" gets filled by this app.

```
{
  "HostedZoneId": "",
  "ChangeBatch": {
    "Comment": "",
    "Changes": {
      "Action": "[CREATE|DELETE|UPSERT]",
      "ResourceRecordSet": {
        "Name": "",
        "Type": "[A|TXT|MX]",
        "TTL": 0,
        "ResourceRecords": {
          "Value": ""
        }
      }
    }
  }
}
```

3. Alright. You can update your JSON file with your public IP address. Just type the following and return.

```
python getnewip.py --json YOUR-FILE.json
```

## Available Commands

- **--skeleton** makes a JSON template file like the above.
- **--json FILE** updates selected JSON file with the public IP address of the machine.

## Acknowledgements

- This application uses [requests](https://github.com/psf/requests).
- This application is for AWS Route 53 users.
- You can update your DNS record with your json file. However, This application only updates JSON file.

## License

1. [Requests](https://github.com/psf/requests/blob/master/LICENSE) is licensed under the apache license v2.0.
2. [Get my new public IP](https://github.com/flymylee/getnewip/blob/master/LICENSE) is also licensed under the WTFPL license.
