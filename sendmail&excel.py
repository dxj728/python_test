# --coding:utf-8--
# File: sendmail&excel.py
# Author: dxj728
# Time: 2019年07月10日22时
# 说明：

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

filename = r'D:\desktop\test1.xls' #附件地址

def send_mail(to_list,sub,context,filename):
	mail_host="smtp.163.com"
	mail_user="dxj728@163.com"
	mail_pass="DONGxiaojie1994@"
	mail_postfix="163.com"
	me="服务器"+"<"+ mail_user +"@"+mail_postfix+">"
	msg = MIMEMultipart() #给定msg类型
	msg['Subject'] = sub #邮件主题
	msg['From'] = me
	msg['To'] = ";".join(mailto_list)
	msg.attach(context)
	#构造附件1
	att1 = MIMEText(open(filename, 'rb').read(), 'xls', 'gb2312')
	att1["Content-Type"] = 'application/octet-stream'
	att1["Content-Disposition"] = 'attachment;filename='+filename[-6:] #这里的filename可以任意写，写什么名字，邮件中显示什么名字，filename[-6:]指的是之前附件地址的后6位
	msg.attach(att1)
	try:
		s = smtplib.SMTP()
		s.connect(mail_host) #连接smtp服务器
		s.login(mail_user,mail_pass)  #登陆服务器
		s.sendmail(me, mailto_list, msg.as_string()) #发送邮件
		s.close()
		return True
	except Exception:
		return False


if __name__ == '__main__':
	mailto_list=["dxj728@163.com"]
	a=pd.DataFrame({'数列1':(1,1,1,1),'数列2':(2,2,2,2),'数列3':(3,3,3,3),'数列4':(4,4,4,4)})
	a.index={'行1','行2','行3','行4'} #这里dataframe类型a就是要输出的表格
	sub="test"
	d='' #表格内容
	for i in range(len(a)):
		d=d+"""
	        <tr>
	 		  <td width="80">""" + str(a.index[i]) + """</td>
	          <td width="80">""" + str(a.index[i]) + """</td>
	          <td width="80">""" + str(a.iloc[i][0]) + """</td>
	          <td width="80" align="center">""" + str(a.iloc[i][1]) + """</td>
	          <td width="80">""" + str(a.iloc[i][2]) + """</td>
	          <td width="80">""" + str(a.iloc[i][3]) + """</td>
	        </tr>"""
		html = """\
		<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<body>
		<div id="container">
		<p><strong>测试程序邮件发送:</strong></p>
		<div id="content">
		 <table width="30%" border="2" bordercolor="black" cellspacing="0" cellpadding="0">
		<tr>
		  <td colspan="2" width="80"><strong>统计</strong></td>
		  <td width="80"><strong>数列1</strong></td>
		  <td width="80" align="center"><strong>数列2</strong></td>
		  <td width="80"><strong>数列3</strong></td>
		  <td width="80"><strong>数列4</strong></td>
		</tr>"""+d+"""
		</table>
		</div>
		</div>
		</div>
		</body>
		</html>
		      """
	context = MIMEText(html,_subtype='html',_charset='utf-8') #解决乱码
	if send_mail(mailto_list,sub,context,filename):
		print ("发送成功")
	else:
		print("发送失败")
