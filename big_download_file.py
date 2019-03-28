# --coding:utf-8--
# File: big_download_file.py
# Author: dxj728
# Time: 2019年03月29日00时
# 说明：大文件下载请求测试

########**************************大文件下载*********************************

import requests
import urllib2
import datetime

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

start = datetime.datetime.now().replace(microsecond=0)
request_download_file(url, filename)
# urllib2_download_file(url, filename)
end = datetime.datetime.now().replace(microsecond=0)
print("用时: {0}".format(end - start))



######## **************************多线程下载*********************************

import sys
import requests
import threading
import datetime

def Handler(start, end, url, filename):
	headers = {'Range': 'bytes=%d-%d' % (start, end)}
	r = requests.get(url, headers=headers, stream=True)

	# 写入文件对应位置
	with open(filename, "r+b") as fp:
		fp.seek(start)
		var = fp.tell()
		fp.write(r.content)


def download_file(url, filename ,num_thread=5):
	r = requests.head(url)
	try:
		file_size = int(r.headers['content-length'])  # Content-Length获得文件主体的大小，当http服务器使用Connection:keep-alive时，不支持Content-Length
	except:
		print("检查URL，或不支持对线程下载")
		return

	#  创建一个和要下载文件一样大小的文件
	fp = open(filename, "wb")
	fp.truncate(file_size)
	fp.close()

	# 启动多线程写文件
	part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
	for i in range(num_thread):
		start = part * i
		if i == num_thread - 1:  # 最后一块
			end = file_size
		else:
			end = start + part

		t = threading.Thread(target=Handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': filename})
		t.setDaemon(True)
		t.start()

	# 等待所有线程下载完成
	main_thread = threading.current_thread()
	for t in threading.enumerate():
		if t is main_thread:
			continue
		t.join()
	print('%s 下载完成' % filename)


if __name__ == '__main__':
	url = r'http://cdnpatch.csonlinechina.com/CSOUpdateAll_OBT_CHN190325.exe'
	filename = r'D:\desktop\a'
	start = datetime.datetime.now().replace(microsecond=0)
	download_file(url, filename)
	end = datetime.datetime.now().replace(microsecond=0)
	print("用时: {0}".format(end - start))
