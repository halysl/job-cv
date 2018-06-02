from django.test import TestCase

# Create your tests here.
edus = [
            {"id":1,
             "time":"2014-2018",
             "name":"铜陵学院",
             "href":"honor_1",
             "honors":["2017年“展航杯”安徽省大学生信息安全作品赛省二等奖",
                       "2017 年安徽省“易霖博杯”大学生网络攻防赛省三等奖",
                       "校长奖学金"]
            },
            {"id":2,
             "time":"2011-2013",
             "name":"安师大附中",
             "href":"honor_2",
             "honors":["优秀学生干部",
                       "三好学生"]
            },
           ]

for edu in edus:
    print(type(edu))
    for key,value in edu.items():
        print(key,":",value)
