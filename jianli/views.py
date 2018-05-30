from django.shortcuts import render

# Create your views here.
def index(request):
    base_dir = "../../static/"
    avatar_dir = "images/avatar.jpg"
    one_sentence_introduction = "充满激情的Python工程师"
    email = "halysl0817@gmail.com"
    name = "刘志"
    phone = "15215626096"
    website = "http://demo.lightl.fun"

    edus = [
            {"time":"2014-2018",
             "name":"铜陵学院",
             "href":"honor_1",
             "honors":["2017年“展航杯”安徽省大学生信息安全作品赛省二等奖",
                       "2017 年安徽省“易霖博杯”大学生网络攻防赛省三等奖",
                       "校长奖学金"]
            },
            {"time":"2011-2013",
             "name":"安师大附中",
             "href":"honor_2",
             "honors":["优秀学生干部",
                       "三好学生"]
            },
           ]

    project_experience = [
                          {"id":1,
                           "class":"single",
                           "name":"利用Django开发个人博客",
                           "duty":"负责人",
                           "content":"根据教程，一步一步的完成个人博客的开发，了解了MVC设计模式，设计并实现了基本功能（分类、归档），添加对rss的支持，在linux的部署以及绑定域名",
                           "git_link":"https://github.com/halysl/blog-with-django",
                           "blog_link":None,
                           "full_content":["-->实现基本功能（发md格式博文，评论系统，分类，归档）",
                                           "-->添加对rss订阅的支持",
                                           "-->使用nginx+uwsgi完成部署，并将服务器ip绑定域名"]
                           },
                           {"id":2,
                           "class":"single",
                           "name":"利用scrapy爬取bilibili用户数据 ",
                           "duty":"项目负责人",
                           "content":"利用成熟的scrapy框架对https://space.bilibili.com/id/#/内的数据进行抓取并处理，并加入防ban策略，并将结果存入数据",
                           "git_link":"https://github.com/halysl/bilibili-user",
                           "blog_link":"https://blog.csdn.net/cloud_strife0/article/details/80249828",
                           "full_content":["-->根据目标网页，设计爬取内容，并针对获取内容进行处理",
                                           "-->使用docker+splash完成对js数据的获取，并连接mysql数据库进行存储",
                                           "-->通过设置“程序睡眠”，“设置user-agent”，“设置代理”等方法完成防ban策略"]
                           },
                          ]

    
    about_me = ["*全日制大学本科及以上学历",
                "*1年python开发经验/6月Django网页搭建经验",
                "*做过个人博客",
                "*善于应变，善于搜索与思考，能够快速解决开发问题"]

    skills = [{"name":"Python","score":"80","id":1},
              {"name":"MySQL","score":"70","id":2},
              {"name":"Linux","score":"50","id":3}
            ]
    dic = {'name':name,
           'base_dir':base_dir,
           'avatar_dir':avatar_dir,
           'one_sentence_introduction':one_sentence_introduction,
           'email':email,
           'phone':phone,
           'website':website,
           'about_me':about_me,

           'edus':edus,
           'skills':skills,
           'project_experience':project_experience,
           }
    return render(request, 'jianli/index.html', dic)