# leet2md
将leetcode.cn上面的部分leetbook和solution题解保存为markdown文件

## requirements
- python 3
- - requests
- - json

## notice
- leetbook2md仅适用于leetbook本身就是用markdown编写的情况，同时也无法保存LC类型的题目
- - 例如《图解算法数据结构》
- leetSol2md目前测试了官方题解

## usage
```bash
python xxxx.py
```
- site_url：填写网址，例 https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/phn3m1/
- （仅leetbook2md）page_id：填写页码，例 phn3m1
- cookie：你的浏览器cookie
- - F12-网络-XHR-请求标头
- - ![image](https://user-images.githubusercontent.com/38211047/149122917-6739425c-6a19-4e4f-9fe6-4d284afed955.png)
