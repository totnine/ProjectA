# modules in Anaconda
import urllib as ulb


def data_fetching():
	"""
		Description:
			Fetching the stock data for sina.com;
			one example url is
			"http://hq.sinajs.cn/list=sh601006"
		return:
			pandas
	"""
	urlnow = ulb.request.urlopen('http://hq.sinajs.cn/list=sh601006')
	urldata = urlnow.read()
	urldata = urldata.decode(encoding='gb2312')
	print(urldata,'\n')
