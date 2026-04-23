import requests
import pandas as pd
import os

def fetch_szse_data():
    url = "https://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=SGT_GGTBDTZ&loading=first"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://www.szse.cn/"
    }
    
    response = requests.get(url, headers=headers)
    json_data = response.json()
    raw_list = json_data[0]['data']
    
    df = pd.DataFrame(raw_list)
    df = df[['zqdm', 'zqjc', 'tznr', 'sxrq']]
    df.columns = ['Code', 'Name', 'Action', 'Date']
    
    # 儲存成檔案
    df.to_csv("data.csv", index=False, encoding="utf_8_sig")
    print("Data saved successfully.")

if __name__ == "__main__":
    fetch_szse_data()