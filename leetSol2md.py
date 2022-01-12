# @author: augu1sto
# blog: augu1sto.gitee.io

# 将leetcode的solution存为markdown
# 仅测试了官方题解


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

payload = {"operationName":"solutionDetailArticle",
"variables":{"slug":"","orderBy":"DEFAULT"},
"query":"query solutionDetailArticle($slug: String!, $orderBy: SolutionArticleOrderBy!) {\n  solutionArticle(slug: $slug, orderBy: $orderBy) {\n    ...solutionArticle\n    content\n    question {\n      questionTitleSlug\n      __typename\n    }\n    position\n    next {\n      slug\n      title\n      __typename\n    }\n    prev {\n      slug\n      title\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment solutionArticle on SolutionArticleNode {\n  rewardEnabled\n  canEditReward\n  uuid\n  title\n  slug\n  sunk\n  chargeType\n  status\n  identifier\n  canEdit\n  canSee\n  reactionType\n  reactionsV2 {\n    count\n    reactionType\n    __typename\n  }\n  tags {\n    name\n    nameTranslated\n    slug\n    tagType\n    __typename\n  }\n  createdAt\n  thumbnail\n  author {\n    username\n    profile {\n      userAvatar\n      userSlug\n      realName\n      __typename\n    }\n    __typename\n  }\n  summary\n  topic {\n    id\n    commentCount\n    viewCount\n    __typename\n  }\n  byLeetcode\n  isMyFavorite\n  isMostPopular\n  isEditorsPick\n  hitCount\n  videosInfo {\n    videoId\n    coverUrl\n    duration\n    __typename\n  }\n  __typename\n}\n"}


site_url = input("site_url: ")

U = site_url.split('/')
if U[-1]!='':
    sol_name = U[-1]
else:
    sol_name = U[-2]

cookie = input("cookie: ")


headers['referer']= site_url
payload['variables']['slug'] = sol_name
headers['cookie'] = cookie

response = requests.request("POST",url,headers=headers,data=json.dumps(payload))

a=response.content.decode()
b=json.loads(a)

mdtext = b["data"]["solutionArticle"]["content"]
mdtitle = b["data"]["solutionArticle"]["title"]

with open(mdtitle+'.md','w+',encoding='utf-8') as f:
    f.write("#"+mdtitle+"\n\n")
    f.write(mdtext)
