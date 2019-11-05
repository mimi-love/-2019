#!/usr/bin/env python
# coding: utf-8

# In[20]:
#只需将两个图片保存位置改成自己想要保存的图片位置即可，上下各一个都需要更改。

import requests
import re
from urllib.parse import urlencode
from hashlib import md5
import time
url=input('请输入你想要的下载的基本url：例如https://www.zhihu.com/question/267465811')
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36',
    'referer':'https://www.zhihu.com/question/63727821'}
response=requests.get(url,headers=headers)
#soup=BeautifulSoup(response.text,'html.parser')
img_url=re.findall('data-actualsrc="(.*?)"',response.text,re.S)
n=1
for i in img_url:
    pig= requests.get(i,timeout=20)
    dir = 'G://可爱小女孩//{}.gif'.format(n)
    f=open(dir,'wb')
    f.write(pig.content)
    print('第{}张图片下载完成'.format(n))
    n+=1
    time.sleep(1)
    f.close()

base_url=url
base_url=list(base_url.split('/'))
base_url.insert(3,'api')
base_url.insert(4,'v4')
base_url[5]='questions'
base_url.append('answers?')
base_url[0]='https:'
b=''
for i in range(len(base_url)):
    if i==0:
        b=b+base_url[i]+'//'
    elif  i>1:
        b=b+base_url[i]+'/'
update_url=b.strip('/')
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36',
    'referer':'https://www.zhihu.com/question/63727821'
}
n=n
for offset in range(5,200,5):
    params={
        'include':'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
        'limit':'5',
        'offset':offset,
        'platform':'desktop',
        'sort_by':'default'
        }
    url=update_url+urlencode(params)   #得到json数据的url
    response=requests.get(url,headers=headers)
    data=response.json() #将json模式的数据传给   字典模式
    images=data.get('data')   ##得到data里的数据，列表模式
    for image in images:  
        #print(image)    #字典模式
        img=image.get('content')
        #print(img)
        img_url=re.findall('data-actualsrc="(.*?)"',img)
        #print(img_url)
        for i in img_url:
            response=requests.get(i,headers=headers).content
            #name=md5(response).hexdigest()
            file_path='G://可爱小女孩//{}.gif'.format(n)
            with open(file_path,'wb') as f:
                f.write(response)
                print('第{}张图片下载完成'.format(n))
            time.sleep(1)
            n+=1
            


# In[ ]:





# In[ ]:




