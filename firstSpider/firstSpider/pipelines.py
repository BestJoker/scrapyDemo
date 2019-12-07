# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import numpy as np
import pandas as pd

class FirstspiderPipeline(object):

    #爬虫开始就会触发这个方法
    def open_spider(self,spider):
        print('爬虫开始')

    def process_item(self, item, spider):
        df = pd.DataFrame()
        for i in range(0,len(item['city'])):
            np.array1 = [item['city'][i]]
            #拼接上地区
            #np.array1 = np.append(np.array1,item['city'][i])
            #拼接天气第一部分
            np.array1 = np.append(np.array1,item['dayDesc'][2*i])
            #拼接风力和温度
            np.array1 = np.append(np.array1,item['dayDesc1'][4*i:4*i+2])
            #拼接天气第二部分
            np.array1 = np.append(np.array1,item['dayDesc'][2*i+1])
            #拼接风力和温度2
            np.array1 = np.append(np.array1,item['dayDesc1'][4*i+2:4*i+4])
            #每次新添加一列
            df[i] = pd.Series(np.array1)
        #然后利用转至将期排列正确
        df = df.T
        #修改其列标题s
        df.columns = ['县/区','天气状况','风力方向','最高温度','天气状况','风力方向','最低温度']
        print (df)
        address = '/Users/fujinshi/Desktop/weibo.csv'
        print('------')
        df.to_csv(address)
        print ('成功csv格式')
        
        '''
        1.找出拼接的规律
        i=0 city[0] + dayDesc [0] + dayDesc1[0,1] + dayDesc[1] + dayDesc1[2,3]
        i=1 city[1] + dayDesc [2] + dayDesc1[4,5] + dayDesc[3] + dayDesc1[6,7]
        i=2 city[2] + dayDesc [4] + dayDesc1[8,9] + dayDesc[5] + dayDesc1[10,11]
        i=n city[n] + dayDesc [2n] + dayDesc1[4n,4n+1] + dayDesc[2n+1] + dayDesc1[4n+2,4n+3]
        实际右侧是开 所以右侧+1
        i=n city[n] + dayDesc [2n] + dayDesc1[4n,4n+2] + dayDesc[2n+1] + dayDesc1[4n+2,4n+4]

        2.构建对应list和dataFrame
        3.转至T一下
        '''

    #爬虫结束触发这个方法
    def close_spider(self,spider):
        print('爬虫结束')
