import pandas as pd
import os
import ssl
import json
import urllib.request

endUri = 'https://fxendpoint.westeurope.inference.ml.azure.com/score'
endKey = 'hisDMwA19iORNOSbd93hhgIDZ3A2A3Vw'
endHeaders = {
    'Authorization': f'Bearer {endKey}',
    'Content-Type':'application/json',
    'azureml-model-deployment': 'fxmodel-4'
}
endData = [{
    "GBPCHF": 2.2959,
    "EURCHF": 1.4680083333333334,
    "USDCHF": 1.50264,
    "GBPUSD": 1.5270187499999999,
    "EURGBP": 0.63975,
    "EURUSD": 0.9767
  }]
endBody = str.encode(json.dumps(endData))

req = urllib.request.Request(endUri, endBody, endHeaders)
ret = urllib.request.urlopen(req)
res1 = json.load(ret)
res2 = json.loads(res1)

dfRes = pd.DataFrame(res2)
valOrg = dfRes.result[0][-2]
valCal = dfRes.result[0][-1]

print(valOrg, valCal)