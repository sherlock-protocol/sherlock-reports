import os
import urllib.parse

hash = "6227729ebc10421c6120301068c264abc262b156"

for item in os.listdir("."):
    if not item.endswith(".pdf"):
        continue

    file = urllib.parse.quote(item)

    url = f"https://github.com/sherlock-protocol/sherlock-reports/raw/{hash}/coverage-agreements/{file}"

    print(item, url)