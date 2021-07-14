from typing import get_args
from pycalil import Pycalil

apikey = "your apikey"
calil = Pycalil(apikey)

print(calil.library(pref="青森県", city="青森市"))
print(calil.library(systemid="Aomori_Pref"))
print(calil.library(geocode="136.7163027,35.390516"))
print(calil.library(pref="青森県", city="青森市", limit=2))

print(calil.check([4003400313], ["Tokyo_NDL"]))
