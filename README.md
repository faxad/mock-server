# MockServer Recipes

### Mock Mode (with pre-defined mocks)

- define `expectioans` in `./mocks`
- refer to the `payments.json` and `transactions.json` examples


```bash
docker compose up -d
```

```bash
curl "http://localhost:1080/transactions?transactionRef=XVJ3KF9" | jq

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   132  100   132    0     0    425      0 --:--:-- --:--:-- --:--:--   425
{
  "transactionId": "945c47d1-203f-49ca-896a-5279d8075785",
  "transactionRef": "XVJ3KF9",
  "amount": 65000,
  "charges": 75
}


curl -X POST "http://localhost:1080/payments" -H 'Content-Type: application/json' -d '{"counterpartyIBAN": "CH8089144265645434356", "amount": 15000}' | jq

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   121  100    59  100    62   1401   1473 --:--:-- --:--:-- --:--:--  2880
{
  "status": "accepted",
  "transactionRef": "XVJ3KF9"
}
```

### Mock Mode (record via proxy)

#### Record (via proxy)

- enable proxy mode and start the `mockserver`
```yaml
mockserver:
    ...
    command: -logLevel DEBUG -serverPort 1080 -proxyRemotePort 80 -proxyRemoteHost integration
    ...
```

- build the mocks (proxy mode will record the `expectations`)

```bash
curl http://localhost:8089/ | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    73  100    73    0     0    160      0 --:--:-- --:--:-- --:--:--   159
{
  "source": "integration-service",
  "processed": "2024-08-18T10:39:39.655213"
}
```

#### Extract & Load Mocks

- extract and load the `expectations`
```bash
curl -v -X PUT "http://localhost:1080/mockserver/retrieve?type=RECORDED_EXPECTATIONS&format=JSON" -o ./mocks/recording.json
```

#### Mock

- disable the proxy mode and restart `mockserver`
```yaml
mockserver:
    ...
    # command: -logLevel DEBUG -serverPort 1080 -proxyRemotePort 80 -proxyRemoteHost integration
    ...
```
- bring down the `integration` service
- re-initate the same request (response will be by the mock, instead of `integration` service)

```bash
curl http://localhost:8089/ | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    73  100    73    0     0    229      0 --:--:-- --:--:-- --:--:--   229
{
  "source": "integration-service",
  "processed": "2024-08-18T10:39:39.655213"
}

date
Sun Aug 18 13:45:41 +03 2024
```

