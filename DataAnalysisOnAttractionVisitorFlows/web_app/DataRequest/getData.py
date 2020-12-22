import json
import urllib.request
import re

# return data[{}{}{}]字典.
def getDataList():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    urls = 'http://61.152.117.25/SqlHelper/passenger/PassengerInfo.asmx/QueryRealtimeInfo?callback=jQuery17209489305473286322_1604326222192&username=dfw&password=eastday&district=0&_=1604326224091'
    request = urllib.request.Request(url=urls, method='GET', headers=headers)
    response = urllib.request.urlopen(request).read()
    list_data = response.decode('utf8')
    data = re.findall('.*?msg:"(.*?)"}\)', list_data)
    # data[0]为字典数据
    content = data[0].replace("'", '"')
    text = json.loads(content)  # 将json字符串转换为字典类型
    line_data = text.get('Rows', 'None')  # 获取内部数据
    TotalRowCount = text.get('TotalRowCount')
    return {'line_data':line_data,'TotalRowCount': TotalRowCount}