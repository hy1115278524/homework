## 服务器处理HTTP请求流程 ##
![](https://i.imgur.com/YEQSdwi.png)

从这张图，我们可以看出，当一个HTTP请求从客户端发过来时，首先web server接收请求，在其中web server会解析HTTP请求头部，比如说请求方法、请求路径等等，我们要知道web server不能自主的产生数据来传输。所以说当我们需要动态的产生数据时，就需要借助User Script序。但是web server和User Script之间无法直接交流，需借助CGI来帮助两者交流。对于python作为后台编程语言，常见的Web Server、CGI和User script都在图中有说明。



## 其他 ##

在利用Apache配合CGI做完一次请求实验后，我觉得这样的方式有些地方值得改进。  
1、如果利用CGI调用User script，我需要在URL中显示的说明我需要执行哪一个脚本文件（比如`http://server.com/cgi-bin/first.pl`）。但这对于用户来说不够友好，那么对于这点来说，我觉得需要根据用户的路径，服务器内部自动的根据路径来进行不同的处理。  
2、如果我们按`http://server.com/cgi-bin/first.pl`这种方式去访问资源，那么这个文件无法进行额外的动作(比如打开一个文件，往里面插入点数据)，它只能创造一个请求头，然后紧跟html代码。所以说，如果我们需要服务器动态的为我们提供数据，那么在还需要其他的脚本文件来做这件事情。
