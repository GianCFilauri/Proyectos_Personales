from requests_html import HTMLSession
import pandas as pd

urls = ['https://www.amazon.com/-/es/dp/1492093408/?coliid=I1IC6FL1P16ZWY&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1492061379/?coliid=I1ALPMHX5J9AJH&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/B097C9HGM8/?coliid=I2GM5BVQ2GWBXC&colid=M43A6JZRSMFP&psc=0&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/B0789WKTKJ/?coliid=IGOTF8M8TVT12&colid=M43A6JZRSMFP&psc=0&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/149209434X/?coliid=I2THWDG4EGRGNE&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/149191646X/?coliid=I2955Y328AW7ZY&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1491985577/?coliid=IKEQK7WUBQC55&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/183921418X/?coliid=I1OJLGAXCOL5G9&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1492091502/?coliid=I3G6EAGSR4SHSI&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1491963042/?coliid=I35TT6ZPW5LF94&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1449316549/?coliid=I1J11JHQETTAL8&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1492050040/?coliid=I1YHE3OEPDGRDW&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/B09982C9FX/?coliid=IZ35F414RYBOW&colid=M43A6JZRSMFP&psc=0&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1492073059/?coliid=I73CSGHP4PYBD&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1098104358/?coliid=I3RTKDLGYKWINK&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1492077445/?coliid=I1YNMIKQ1H0EV4&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1492081000/?coliid=I1IXG612HFHO3Y&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1492047686/?coliid=I3QK2V6XIJHCRZ&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1491957662/?coliid=I1T073EZYDCJHX&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/149208946X/?coliid=INLRTPP3OO2N8&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/1492032646/?coliid=IT1PGWFWSXF6T&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it',
        'https://www.amazon.com/-/es/dp/149207294X/?coliid=IIMHOI6K82LC2&colid=M43A6JZRSMFP&psc=1&ref_=lv_ov_lig_dp_it']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    try:
        product = {
            'url':url,
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': r.html.xpath('//*[@id="newBuyBoxPrice"]', first=True).text
        }
        print(product)
    except:
        product = {
            'url':url,
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': 'item unavailable'
        }
        print(product)
    return product

productsprices = []
for url in urls:
    productsprices.append(getPrice(url))

print(len(productsprices))

pricesdf = pd.DataFrame(productsprices)
pricesdf.to_excel('productsprices.xlsx', index=False)