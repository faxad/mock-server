# mock-server
MockServer Recipes

```bash
docker compose up -d


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


