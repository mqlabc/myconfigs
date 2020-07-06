import requests
from lxml import etree


def get_ip(url='https://githubusercontent.com.ipaddress.com/raw.githubusercontent.com'):
    r = requests.get(url)
    page = etree.HTML(r.text)
    n1 = page.xpath('//th[contains(text(),"IP Address")]/..')[0]
    return n1.xpath('./td/ul/li/text()')[0]


if __name__ == "__main__":
    print(get_ip())
