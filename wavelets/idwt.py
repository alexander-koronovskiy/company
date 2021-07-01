# cA - approximation coefficient, cD - detail coefficient
import matplotlib.pyplot as plt
import pandas as pd
import pywt


def cd_builder(path, order):
    x = pd.read_csv(path)
    cA, cD = pywt.dwt(x, order)
    iwt = pywt.idwt(cA, cD, order)
    df = pd.DataFrame({"u": cD.transpose()[0]})
    return df


x = pd.read_csv("test_signal.txt")
x.columns = "u"
print(x.head())
