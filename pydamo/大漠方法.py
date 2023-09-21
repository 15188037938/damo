'''
#=================================
模块为了照顾英文不好的同学,特意全部按照中文格式编写
创建时间:2023.09.21
更新时间:2023.09.21
作者:暖君
#=================================
'''
#print('开头_name_为:',__name__)

# 这个魔术方法的作用就是 如果本py里运行则全部代码都会跑一遍
# 如果是非本py 其他py调用，则不会指定开头的顶级函数
# 这可以用于保护一些顶级函数不被外部访问
# if __name__ == '__main__':
#     print('if_name_为:',__name__)
    
from win32com.client import Dispatch
import ctypes , os
# 免注册 调用大漠
class 大漠初始化 :  #返回值为对象
	'''
	这个函数就是免注册调用大漠,只需要启动的时候调用一次即可
	'''
	def __init__(self) :
		self.dm = None
		self.dms = []  # 存放100个大漠对象
		self.注册码 = "sxy013dd3fa7adb88edd7ef5b4bea63ab2e4d"
		self.附加码 = "sxy52001"
		try :
			self.dm = Dispatch('dm.dmsoft')
			print('系统中已装大漠插件，版本为:' , self.dm.ver())
			
		
		except :
			print('正在初始化')
			#  通过调用DmReg.dll注册大漠 这样不会把dm.dll写到系统中，从而实现免注册
			dms = ctypes.windll.LoadLibrary(os.path.dirname(__file__) + './DmReg.dll')
			dms.SetDllPathW(os.path.dirname(__file__) + './dm.dll' , 0)
			self.dm = Dispatch('dm.dmsoft')  # 创建对象
			print('免注册调用初始化成功 版本号为:' , self.dm.ver())
		
		# 这里的range就是控制创建对象数量的
		a = 0
		for i in range(0) :
			self.dms.append(大漠初始化.CreateObject())
			#获取对象ID
			number = self.dms[a].GetID()
			#numbers = GetDmCount()
			#print(f'对象ID{number}')
			a += 1
	
	@classmethod
	def CreateObject(self) :
		return Dispatch('dm.dmsoft')
	
	#如果是使用收费版的 还需要注册VIP
	def reg(self , 注册码 , 附加码) :
		res = self.dm.diQiEPdS(注册码 , 附加码)
		dm_res = {
			-1 : "大漠无法连接网络" ,
			-2 : "进程没有以管理员方式运行" ,
			0 : "失败 (未知错误)" ,
			1 : "成功" ,
			2 : "余额不足" ,
			3 : "绑定了本机器，但是账户余额不足50元" ,
			4 : "注册码错误" ,
			5 : "你的机器或者IP在黑名单列表中或者不在白名单列表中" ,
			6 : "非法使用插件. 一般出现在定制插件时，使用了和绑定的用户名不同的注册码.  也有可能是系统的语言设置不是中文简体,也可能有这个错误" ,
			7 : "你的帐号因为非法使用被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac,否则可能会造成封号，或者封禁机器）" ,
			8 : "ver_info不在你设置的附加白名单中" ,
			77 : "机器码或者IP因为非法使用，而被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac,否则可能会造成封号，或者封禁机器）" ,
			777 : "同一个机器码注册次数超过了服务器限制,被暂时封禁. 请登录后台，插件今日详细消费记录里，相应的机器码是否有次数异常，并立刻优化解决.如果还有问题，可以联系我来解决." ,
			-8 : "版本附加信息长度超过了20" ,
			-9 : "版本附加信息里包含了非法字母.,可能是账号密码有中文" ,
		}
		if res == 1 :
			print("大漠vip注册成功")
			return self.dm
		else :
			print("大漠注册失败:" + dm_res[res])
			raise "大漠vip注册失败"

def 取创建的大漠对象总数 (对象) :
	'''
	:param 对象:
	:return: 返回所有的大漠对象个数
	'''
	return  对象.GetDmCount()
 


def 取大漠对象ID(对象) :
	'''
	:param 对象:
	:return: GetID返回当前大漠对象的ID值
	这个值对于每个对象是唯一存在的。可以用来判定两个大漠对象是否一致
	'''
	return 对象.GetID()
	

def 窗口_查找(对象 , 类名 = str , 标题 = str) :
	'''
	:param 对象: 必填
	:param 类名: 可空字符串
	:param 标题: 可空字符串
	:return: 返回窗口句柄
	'''
	return 对象.FindWindow(类名 , 标题)


def 绑定() :
	print('绑定窗口')


def 键盘() :
	print('测试键盘')


def 电脑() :
	print('测试系统')

def 游戏() :
	print('测试窗口')
