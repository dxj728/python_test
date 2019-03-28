# --coding:utf-8--
# File: big_download_file.py
# Author: dxj728
# Time: 2019年03月29日00时
# 说明：大文件下载请求测试

import requests
import urllib2

# 当下载大的文件的时候，建议使用stream模式．
# 默认情况下是false，他会立即开始下载文件并存放到内存当中，倘若文件过大就会导致内存不足的情况．
# 当把get函数的stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载。需要注意一点：文件没有下载之前，它也需要保持连接。
# iter_content：一块一块的遍历要下载的内容
# iter_lines：一行一行的遍历要下载的内容
# 使用上面两个函数下载大文件可以防止占用过多的内存，因为每次只下载小部分数据。
def request_download_file(url, filename):
	# NOTE the stream=True parameter
	r = requests.get(url, stream=True)
	with open(filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024 * 1024):
			if chunk:		# filter out keep-alive new chunks
				f.write(chunk)
				f.flush()
	return filename

def urllib2_download_file(url, filename):
	file = urllib2.urlopen(url)
	with open(filename,'w') as f:
		while True:
			tmp = file.read(1024 * 1024)
			if not tmp:
				break
			f.write(tmp)

url = 'http://cdnpatch.csonlinechina.com/CSOUpdateAll_OBT_CHN190325.exe'
filename = r'D:\desktop\a'

request_download_file(url, filename)

# urllib2_download_file(url, filename)
