import bs4 as bs
import pandas as pd
import re
import requests
from requests.exceptions import HTTPError
from urllib.request import urlopen
import matplotlib.pyplot as plt
from main import root_path
import inspect

whitelist = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def info(symbols):

    weights = pd.read_csv(root_path + '/Daily Data/Portfolio/Portfolio Weights.csv', index_col=0)
    sector_info = pd.DataFrame()
    industry_info = pd.DataFrame()

    for symbol in symbols:
        symbol = symbol.replace('_', '/')
        s_data = []

        url = 'https://eresearch.fidelity.com/eresearch/goto/evaluate/snapshot.jhtml?symbols=' + symbol

        #Web Page
        try:
            r = requests.get(url)
            r.raise_for_status()
        except HTTPError:
            print ('Could not download page')
        else:
            html = r.text

        #Elements
        try:
            sector = html.split('<a href="http://eresearch.fidelity.com/eresearch/markets_sectors/sectors/sectors_in_market.jhtml?tab=learn&sector=')[1].split('</a>')[0]
            sector = ''.join(filter(whitelist.__contains__, sector))
        except IndexError:
            print ('Element not found for:'+symbol)

        try:
            industry = html.split('<a href="http://eresearch.fidelity.com/eresearch/markets_sectors/sectors/industries.jhtml?tab=learn&industry=')[1].split('</a>')[0]
            industry = ''.join(filter(whitelist.__contains__, industry))
        except IndexError:
            print ('Element not found for:' + symbol)

        sector_info = sector_info.append({'Sector': sector, 'Symbol': symbol}, ignore_index=True)
        industry_info = industry_info.append({'Industry': industry, 'Symbol': symbol}, ignore_index=True)

    sector_info.set_index('Symbol', inplace=True)
    industry_info.set_index('Symbol', inplace=True)

    dat1 = pd.concat([sector_info, weights], axis=1)
    dat1.columns = ["Sector", "Weight"]
    t = dat1.groupby(["Sector"]).sum()

    t.to_csv(root_path+'/Daily Data/Portfolio/Sectoral Weights.csv', index=True)

    plt.pie(
        t["Weight"],
        labels=t.index,
        shadow=False,
        startangle=90,
        autopct='%1.1f%%',
    )

    plt.axis('equal')
    plt.suptitle('Sectoral Weights')

    plt.savefig(root_path + '/Figures/sec_ind.png')

    call_name = inspect.stack()[1][3]

    if call_name != "diversification":
        plt.show()

    rpdf = pd.concat([sector_info, industry_info], axis=1)
    rpdf.to_csv(root_path+'/Daily Data/Portfolio/Asset Exposure.csv',index=True)

