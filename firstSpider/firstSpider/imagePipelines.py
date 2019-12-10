# coding:utf-8

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class SpDownimagePipeline(ImagesPipeline):
    #自定义图片下载类
    '''
    get_media_requests(item, info)
    pipeline会获取image的urls从item下载它，
    因此我们可以重写get_media_requests方法并且返回每一个url的request：
    这些请求将由pipeline处理,当完成下载时结果将会以2-元素的元组形式被发送到item_completed方法，
    每个元组将包含（success， file_info_or_error）类似下面这种形式：

    success：布尔值，如果下载图片成功，返回True,如果下载图片失败，返回False。file_info_or_error：返回的是一个字典，
    其中包括，url、path和checksum,如果出现问题返回Twisted Failure。
    url代表文件从哪里下载的，这是从get_media_requests返回的request的url
    path代表文件存储路径
    checksum代表图像内容的MD5 hash

    '''

    def get_media_requests(self, item, info):
        print('+++++++')
        title_list = item['images']
        url_list = item['image_urls']
        print(url_list)
        #如果没有标题则取消下载item
        if (len(title_list)):
            # 从item中获取图片url并发送请求，image_urls就是items.py中定义的字段
            for url in url_list:
                # meta作用就是可以将item的值传给下一个函数使用，类似于先缓存起来
                yield scrapy.Request(url,meta={'item': item})
        else:
            raise DropItem('Missing title in %s' % item)


    '''
    item_completed(results, item, info)
    当一个单独项目中所有图片请求完成时（下载完成或者下载失败），此方法将会被调用，
    其中results参数为get_media_requests下载完成后返回的结果，item_completed必须返回输出发送到下一个阶段的pipeline。
    所以你必须返回或删除item，和之前其它pipeline操作一样。
    下面的一个示例，我们将下载的文件路径(在results中传递)存储在file_path item字段中，如果不包含任何文件，则删除该项目。
    '''
    def item_completed(self, results, item, info):
        """
        此处没有做修改，只是把ImagesPipeline的方法拿过来用，必须返回item
        """
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        """
        file_path为ImagePipeline自带的方法，这里我们重写这个方法，
        为了能够自定义图片的名称，如果不重写，SHA1 hash格式，类似full/63bbfea82b8880ed33cdb762aa11fab722a90a24.jpg
        """
        # 获取item，从get_media_requests的Request中获取
        item = request.meta['item']
        # 图片名称，一般用split（‘/’）分割后取最后一个值也就是-1，这里没用-1是因为图片最后一个字段不是随机数
        # 是长乘以宽如：452x340c.jpg，容易重名，所以用的-2，倒数第二个字段
        image_guid = request.url.split('/')[-2]+'.jpg'
        fullname = 'full/%s/%s' % (item['images'][0],image_guid)
        print('图片的名字是%s' % fullname)
        return fullname
