# @author: augu1sto
# blog: augu1sto.gitee.io

# 将leetbook存为markdown（仅适用于源网页是markdown类型的书籍）
# 例 图解算法数据结构 https://leetcode-cn.com/leetbook/read/illustration-of-algorithm

import requests
import json


url = "https://leetcode-cn.com/graphql/"


headers = {

'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN',
'content-type': 'application/json',
'cookie': '',
'origin': 'https://leetcode-cn.com',
'referer': '',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',


}

payload = {"operationName":"leetbookPageDetail",
"variables":{"pageId":""},
"query":"query leetbookPageDetail($pageId: ID!) {\n  leetbookPage(pageId: $pageId) {\n    title\n    subtitle\n    id\n    pageType\n    blocks {\n      type\n      value\n      __typename\n    }\n    commonTags {\n      nameTranslated\n      name\n      slug\n      __typename\n    }\n    qaQuestionUuid\n    ...leetbookQuestionPageNode\n    __typename\n  }\n}\n\nfragment leetbookQuestionPageNode on LeetbookQuestionPage {\n  question {\n    questionId\n    envInfo\n    judgeType\n    metaData\n    enableRunCode\n    sampleTestCase\n    judgerAvailable\n    langToValidPlayground\n    questionFrontendId\n    style\n    content\n    translatedContent\n    questionType\n    questionTitleSlug\n    editorType\n    mysqlSchemas\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    topicTags {\n      slug\n      name\n      translatedName\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"}


site_url = input("site_url: ")
page_id = input("page_id: ")
cookie = input("cookie: ")


headers['referer']= site_url
payload['variables']['pageId'] = page_id
headers['cookie'] = cookie

response = requests.request("POST",url,headers=headers,data=json.dumps(payload))

a=response.content.decode()
b=json.loads(a)

if b["data"]["leetbookPage"]["blocks"][0]["type"]!='MARKDOWN':
    print("非markdown类型\n")
else:
    mdtext = b["data"]["leetbookPage"]["blocks"][0]["value"]
    mdtitle = b["data"]["leetbookPage"]["title"]

    with open(mdtitle+'.md','w+',encoding='utf-8') as f:
        f.write("#"+mdtitle+"\n\n")
        f.write(mdtext)
