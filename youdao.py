import urllib.request
import urllib.parse
import josn
import time

while True:
    content = input('请输入您要翻译的内容：')
    if content == 'q!':
            break
    else:
        url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

        head = {}
        head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

        data = {
        'i': '安静''灰''崔默涵',
        'from':'zh-CHS',
        'to':'ja',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'1542355065481',
        'sign':'32780efd4fa6af55e47371ea8ee03118',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTION',
        'typoResult':'false'
        }
        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url,data)
        respones = urllib.request.urlopen(req)
        html = respones.read().decode()
        target = json.loads(html)
        print('翻译的结果为：%s' % target[])
        time.sleep(5)
