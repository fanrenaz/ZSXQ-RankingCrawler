import requests
import csv
import codecs
#追加用a+，新写入用w+
#创建一个csv文件输入路径
f = codecs.open('//path', 'w+', 'utf_8_sig')
writer = csv.writer(f)
#如果是追加的话可以把下面一行注释掉
writer.writerow(['gid','圈子名','作者','创建时间','付费类型','简介','领域','话题数','问答数','精华数','成员数','好评','差评','定价'])
#可以用Charles复制header
headers = {

}
requests.packages.urllib3.disable_warnings()
response = requests.get('https://api.zsxq.com/v1.10/groups/ranking_list',headers=headers,verify=False)
content=response.json()['resp_data']['groups']
n=0
for i in content:
    n+=1
    group_id = i['group_id']
    name = i['name']
    author = i['owner']['name']
    time = i['create_time']
    time1 = time[:10]
    pay = i['type']
    intro = i['description']
    category = i['category']['title']
    tpc = i['statistics']['topics']['topics_count']
    answer = i['statistics']['topics']['answers_count']
    digest = i['statistics']['topics']['digests_count']
    member = i['statistics']['members']['count']
    try:
        good = i['statistics']['ratings']['satisfied_count']
        bad = i['statistics']['ratings']['regretted_count']
    except:
        good = bad = 'N/A'        
    try:
        price = i['policies']['payment']['amount']
    except:
        price = 0
    print(f'第{n}名：{name}')
    writer.writerow([group_id,name,author,time1,pay,intro,category,tpc,answer,digest,member,good,bad,price])
 
