#sandwhiches = ['old biden','dingzhen','longer','trump']
#finished_sandwhiches=[]
#while sandwhiches:
#    new_sandwhiches = sandwhiches.pop(0)
#    print(f"{new_sandwhiches} is ready")
#    finished_sandwhiches.append(new_sandwhiches)
#    print(finished_sandwhiches)
#print(f"sandwhhiches below are ready{finished_sandwhiches}")



      
#sandwhiches = ['laoda','kobe','laoda','kobe','longer','longer','kobe','weihiyuan','litingzhang']
#print("kobe has been sold out")
#while 'kobe' in sandwhiches:
#    sandwhiches.remove('kobe')
#print(sandwhiches)
#while 'longer' in sandwhhiches:
#print(sandwhiches)
   










#famous_people = ['dingzhen','xiucai','caixukun','liyifeng','wuyifan','liyundi','guohaifeng','weizhiyuan','weizhiyuan','weizhiyuan','kobe','caixukun']
#a = 0
#b = 0
#for people in famous_people:
#    if people =='caixukun':
#       a =a+1
#    if people == 'weizhiyuan':
#      b = b+1
#print(a) 
#print(b)









#def add(x,y):
#    return x**y
#z = add(2,6)
#print(z)

     



#def display_message(topic):
#    print(f"the topic of this artical is {topic.title()}")
#display_message("war")
    







#def favorite_book(title):
 #   print(f"one of my favorite book is {title.title()}")


#favorite_book('journey to the west')
  
#def make_shirt(word,number):
#    print(f"the size of the shirt is {number}")
#    print(f"the word on this shirt is {word}")
#make_shirt('Nike',"190")
#make_shirt(word='I love python',number = 'Medium')
#make_shirt(word = 'Adidas',number = 'Large')





#def describle_city(city,country):
#    print(f"{city} is in {country}")
#describle_city('Paris','Germany')










#def  city_country(city,country):
#    position = f"{city},{country}"
#    return position.title()
#z =  city_country('Paris','Germany')
#print（z)





#a = []
#def perfect(i):
#    for num in list(range(1,i+1,1)):
#     if i%num ==0:
#         a.append(num)
#         b = sum(a)
#         if b == i:
#            return i 
#        
#c=int(input("please enter your number:"))
#if c == perfect(c):
#   print("恭喜你得到了一个perfect number")



#以下为8.8课堂作业：


#向函数传递列表：
#def add(list_one):
#  sum(list_one)
#  return(sum(list_one))

#num = list(range(1,10))
#z = add(num)
#print(z)
   

#set 函数
#def eliminator(list1):
#    list0 = list(set(list1))
#    return list0
#a = [1,2,3,3,3,3,3,4,4,5,5,5]
#print(eliminator(a))
###查找的资料。。。。




#def send_messages(infos):
    #for info in infos:
    ##    mess = f"{info}"
     #   print(mess) 
#list = [0,1,2,3,4,5,6,7]
#send_messages(list) 
#sent_messages = []
#for a in list:
#    sent_messages.append(f"{a}")
#print(list)
#print(sent_messages)
     

#class Restaurant:
#    def __int__(self,name,cuisine,favor,number_served):
#        self.name = name
#        self.cuisine = cuisine
#        self.favor = favor
#        self.number_served = number_served
#    
#    def get_info(self):
#        return f"name:{self.name},famous_cuisine:{self.cuisine},famous_favor:{self.favor},num :{self.number_served}"###
#longer = Restaurant("ruike","litangdingzhen","smoke",100)
#print(longer.get_info())
#print(longer.number_served)
#longer.number_served = 200
    
    


#class Order:
#    def __init__(self,buyer_name,product,email,phone):
#        self.buyer_name = buyer_name
#        self.product = product
#        self.email = email
#        self.phone = phone
#    def deliver_mail(self):
#        mess = f"""\nto {self.phone}
#              Dear{self.buyer_name}
#              Your purchased product:{self.product}is delivered
#               Thanks for your choosing"""
#        print(mess)
    
    
#orders = [
#{"buyer_name": "Pony","product": "MacBook","email": "pony@qq.com","phone": 13812341234},
#{"buyer_name": "Bill","product": "AirPods","email": "bill@ms.com","phone": 13812341235},
#{"buyer_name": "Hank","product": "iPhone","email": "hank@xyz.com","phone": 13812341239},
#]
#for  order_info in orders:
#        order = Order(order_info["buyer_name"], order_info["product"], order_info["email"], order_info["phone"])
#order.deliver_mail()    
#    


'''import math

class Circle:


    
    def __init__(self):
        pass
    def SetCenter(self,x,y):
        self.x=x
        self.y=y
    def SetRadius(self,r):
        self.r = r
    def GetArea(self):
        return math.pi*r**2
if __name__=='__main__':
    x=eval(input()) #输入圆心的x坐标
    y=eval(input()) #输入圆心的y坐标
    r=eval(input()) #输入半径
    c=Circle() #创建Cirle对象
    c.SetCenter(x,y) #设置圆心
    c.SetRadius(r) #设置半径
    print('center:(%.2f,%.2f),radius:%.2f'%(c.x,c.y,c.r)) #输出圆心和半径
    print('area:%.2f'%c.GetArea()) #输出面积'''












'''class Restaurant:
    def __init__(self,name,cuisine,number_served):
        self.name = name
        self.cuisine = cuisine
    
        self.number_served = number_served
    
    def get_info(self):
        return f"name:{self.name},famous_cuisine:{self.cuisine},num :{self.number_served}"
      class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine ,number_served,flavors):
       super().__init__(name,cuisine,number_served)
       self.flavors = flavors

    def get_info(self):
        return f"name:{self.name},famous_cuisine:{self.cuisine},num :{self.number_served},flavor:{self.flavors}"
    
longer_likes = IceCreamStand('litingzhang','shit','91','pineapple')
print(longer_likes.get_info())'''
   








"""class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def  info(self):
        return f"Hello {self.first_name} {self.last_name},you are now {self.age} years old"
class Privileges(User):
    def __init__(self,first_name,last_name,age,favors):
        super().__init__(first_name,last_name,age)
        self.favors = favors
    def info(self):
        return f"Hello {self.first_name} {self.last_name},you are now {self.age} years old,your favors is/are {self.favors}"
    


a = input("please enter your first_name:")
b  = input("pleases enter your last name:")
c = input("please enter you real age:")
d = input("pleases enter your favorite sports:")
mess = Privileges(f'{a}',f'{b}',f'{c}',f'{d}')
print(mess.info())"""
















#读取数据模版
'''from pathlib import Path
  
path = Path("longer.txt")
contence = path.read_text()
print(contence)'''






"""from pathlib import Path
path = Path("./new_files/longer.txt")

contents = path.read_text()
print(contents)"""

 




'''from pathlib import Path
path = Path("pi_million_digits.txt")

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''


for line in lines:
    pi_string +=line


print(f"{pi_string[:100]}...")
print(len(pi_string))
'''
  

'''from pathlib import Path
path = Path("longer.txt")
contents = path.read_text()


print(contents)
contents=contents.replace('pirson','jail')

print(contents)'''


'''from pathlib import Path
contents = "caixukun loves basketball.\n"
contents += "weizhiyuan loves little sister.\n"
contents += "dingzhen loves ruike.\n"

path = Path('guest.txt')
path.write_text(contents)
print("your text has been saved")'''
   



'''from pathlib import Path
while True:
    name = input("pleases enter your name:")
    if name =="quit":
        break
    else:
        favor = input("please enter his/hers favoritw:")

dic = {}
dic['name'] = f"{name}"
dic["favor"] = f"{favor}"
print(dic)

for name, favor in dic.items():
    contents = f"{name} loves {favor}"
print(contents)
path = Path('guest.txt')
path.write_text(contents)'''

 
'''while True:
     number_one = input ("please enter your first number: ")
     if number_one.lower() == "quit":
        break
     
     number_two = input("please enter your second_number:")
     if number_two.lower() == "quit":
        break
     try:
        result = float(number_one) + float(number_two)
     except ValueError:
        print("Cannot type text")
     else:
        print(result)'''

#写入数据
'''from pathlib import Path
import json
number = [1,2,3,4,5]
path = Path("numbers.json")
contence = json.dumps(number)


path.write_text(contence)'''

#导出数据
'''from pathlib import Path
import json
path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)'''
 



'''

a = input("please enter the number you prefered:")
name = input("please enter your name in English:")

from pathlib import Path
import json
path = Path('numbers.json')
content = {}
content["name"] =f"{name}"
content["number"] = f"{int(a)}"
print(content)
contents = json.dumps(content)

path.write_text(contents)




path = Path('numbers.json')
mess = path.read_text()
num = json.loads(mess)
print(type(num))
print(num)
'''



'''from pathlib import Path
import json
path = Path('numbers.json')
if path.exists():
    contents = path.read_text()
    num = json.loads(contents)
    print(f"welcome back your favorite number is {num}")
else:
    num = input("pleases enter your favorite number:")
    contents = json.dumps(num)
    path.write_text(contents)
    print(f"we will remember your favorite number {num}")
'''





















































































































































































































































































































































































































































































































































































