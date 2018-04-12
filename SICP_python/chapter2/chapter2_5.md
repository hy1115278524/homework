## 面向对象编程 ##

在本节中，我们将介绍面向对象编程，其实在前面的章节中它的思想已经提到过，并且实现的技术细节也已经实现。在面向对象的编程语言中，一个class就把前面实现的方法隐藏起来，让用户感到更简洁方便。

面向对象编程（OOP）是一种用于组织程序的方法，它组合了这一章引入的许多概念。就像抽象数据类型那样，对象创建了数据使用和实现之间的抽象界限。类似消息传递中的分发字典，对象响应行为请求。就像可变的数据结构，对象拥有局部状态，并且不能直接从全局环境访问。Python 对象系统提供了新的语法，更易于为组织程序实现所有这些实用的技巧。这里就提到了三个需要实现的技术细节--抽象边界，消息传递及局部状态。

## 对象和类 ##

类可以用作所有类型为该类的对象的模板，对象是类的实例。
在python中，我们可以用如下的方法定义类：

    class <name>(<base class>):
            <suite>

## 方法 ##

对象方法也由class语句中的def语句定义。在类看来，这些在类里面定义的函数就是普通的函数，在实例对象看来这些函数就是方法，因为对象绑定到了第一个参数上。比如A是一个类，其实下面两种写法等效。
    
        a = A()
        a.fun()等效于A.fun(a)
        >>> type(Account.deposit)
        <class 'function'>
        >>> type(tom_account.deposit)
        <class 'method'>
                            从上面就可以看出什么时候类型是函数，什么时候类型是方法。

## 类属性 ##

类属性时关联到类本身，不是联系到某个特定的实例，因此类属性可以在对象之间共享。在类里面使用类属性时，我们可以写成:

    类名.属性
        self.__class__.属性

        类属性可以以通过任何实例属性进行访问，但是只有类可以修改它。

## 属性名称 ##

我们需要规定名称如何解析为特定的属性，毕竟我们可以轻易的拥有同名的类属性和实例属性。对于如下的表达式：

    <expression>.<name>

    我们对他的计算有如下四个步骤：

    1、求出点左边的<expression>，会产生点运算符的对象。  
    2、<name>会和对象的实例属性匹配；如果该名称的属性存在，会返回它的值。  
    3、如果<name>不存在于实例属性，那么会在类中查找<name>，这会产生类的属性值。  
    4、这个值会被返回，如果它是个函数，则会返回绑定方法。


## 对象的作用 ##

Python 对象系统为使数据抽象和消息传递更加便捷和灵活而设计。类、方法、继承和点运算符的特化语法都可以让我们在程序中形成对象隐喻，它能够提升我们组织大型程序的能力。对象可以在不同层面上进行分离。每个程序中的对象都封装和管理程序状态的一部分，每个类语句都定义了一些函数，它们实现了程序总体逻辑的一部分。抽象界限强制了大型程序不同层面之间的边界。