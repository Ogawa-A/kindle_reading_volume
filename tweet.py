from calendar import month
from locale import currency
import tweepy
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import date
import pandas.tseries.offsets as offsets
from dateutil.relativedelta import relativedelta
import settings

def main():
    kindle_data = get_kindle_list()

    last_month_first = (date.today() - relativedelta(months=1)).replace(day=1)
    last_month_last = date.today().replace(day=1) - relativedelta(days=1)
    book_num = get_purchace_book_num(kindle_data, last_month_first, last_month_last)

    text = '{0} ~ {1} までの間に {2}冊の本をKindleで購入しました'.format(last_month_first, last_month_last, book_num)

    tweet(text)


# kindlePCのキャッシュを取得
def get_kindle_list():
    input_file_str = "C:/Users/uncle/AppData/Local/Amazon/Kindle/Cache/KindleSyncMetadataCache.xml"

    header = ["ASIN", "title", "authors", "publishers",
           "publication_date", "purchase_date",
           "textbook_type", "cde_contenttype",
           "content_type"]
    nary = [header]
    tree = ET.parse(input_file_str)
    root = tree.getroot()

    for book_info in root[2]:
        ary = []
        for info in book_info:
            #authers publishers are nested
            if len(info) == 0:
                ary.append(info.text)
            else:
                info_list = [ s.text for s in info ]
                ary.append(';'.join(info_list))
        nary.append(ary)

    data = pd.DataFrame(nary[1:], columns = nary[0])
    data['jst_time'] = (pd.to_datetime(data['purchase_date']) + offsets.Hour(9)).dt.date

    return data

# 前月に購入した冊数を取得
def get_purchace_book_num(kindle_data, last_month_first, last_month_last):


    last_month_data = kindle_data[(kindle_data['jst_time'] >= last_month_first) & (kindle_data['jst_time'] <= last_month_last)]

    return len(last_month_data)

def tweet(text):
      # Twitterオブジェクトの生成
    client = tweepy.Client(None, settings.api_key, settings.api_secret, settings.access_token, settings.access_token_secret)
    client.create_tweet(text = text)
  
if __name__ == "__main__":  
    main()
