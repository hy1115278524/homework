# 第二章：构建对象的抽象 #
在第一章中，我们专注于计算过程，以及程序设计中函数的作用。在这一章中，我们将会专注于数据。

## 对象隐喻 ##

在这门课的开始，我们区分了函数和数据：函数执行操作，而数据被操作。当我们在数据中包含函数值时，我们承认数据也拥有行为。函数可以像数据一样被操作，但是也可以被调用来执行计算。对象既是信息也是过程，它们绑定在一起来展示复杂事物的属性、交互和行为。对象拥有属性，它们是带有名字的值，也是对象的一部分。Python 中，我们使用点运算符来访问对象属性：  
`<expression> . <name>`  
上面的<expression>求值为对象，<name>是对象的某个属性名称。

## 原始数据类型 ##

原始数据类型具有以下特性：  
1、原始表达式可以计算这些类型的对象，叫做字面值。  
2、内建的函数、运算符和方法可以操作这些对象。

## 数据抽象 ##

数据抽象类似于我们第一章所介绍的函数的抽象，数据抽象也忽略复合数据结构的实现细节，将数据的功能与实现分离开来。这样做就便于我们设计、维护和修改。具体来说，我们可以先假设我们有这样的数据结构，假设它会有这样的功能，最后再去考虑它的具体实现。

书中介绍了一个关于有理数的算术的具体的例子。

    >>> def add_rat(x, y):
            nx, dx = numer(x), denom(x)
                    ny, dy = numer(y), denom(y)
                            return make_rat(nx * dy + ny * dx, dx * dy)
                                >>> def mul_rat(x, y):
                                        return make_rat(numer(x) * numer(y), denom(x) * denom(y))
                                            >>> def eq_rat(x, y):
                                                    return numer(x) * denom(y) == numer(y) * denom(x)

                                                    make_rat(n, d)返回分子为n和分母为d的有理数。  
                                                    numer(x)返回有理数x的分子。  
                                                    denom(x)返回有理数x的分母。  
                                                    最后利用**元组**来实现数据抽象的具体层面。

## 抽象界限 ##

![](https://i.imgur.com/H0pk3cR.png)
每一层上，界限分离了使用数据抽象的函数（上面）和实现数据抽象的函数（下面）。使用有理数的程序仅仅通过算术函数来操作它们：add_rat、mul_rat和eq_rat，相应地,这些函数仅仅由构造器和选择器make_rat、numer和and denom来实现，它们本身由元组实现。  
抽象界限具有许多好处。一个好处就是，它们使程序更易于维护和修改。很少的函数依赖于特定的表现，当一个人希望修改表现时，不需要做很多修改。

## 序列 ##
接下来，我们看可以讨论利用python解决序列的问题。  
序列是数据值的顺序容器。不像偶对只有两个元素，序列可以拥有任意（但是有限）个有序元素。

序列有两个基本的属性：  
1、长度  
2、元素选择  

序列的迭代：python利用for语句来实现序列的迭代。  
**映射。**将一个元组变换为另一个元组的强大手段是在每个元素上调用函数，并收集结果。这一计算的常用形式叫做在序列上映射函数，对应内建函数map。map的结果是一个本身不是序列的对象，但是可以通过调用tuple来转换为序列。它是元组的构造器。

**范围**。range是另一种 Python 的内建序列类型，它表示一个整数范围。范围可以使用range函数来创建，它接受两个整数参数：所得范围的第一个数值和最后一个数值加一。


## 接口约定 ##

接口约定也是一种强大的处理数据结构的设计原则。例如，如果我们拥有多个函数，它们全部接受序列作为参数并且返回序列值，我们就可以把它们每一个用于上一个的输出上，并选择任意一种顺序。这样，我们就可以通过将函数链接成流水线，来创建一个复杂的过程，每个函数都是简单而专一的。   

考虑一个问题，对前n个斐波那契数中的偶数求和。我们可以设计出如下的步骤：  
 enumerate     map    filter  accumulate
 -----------    ---    ------  ----------
 naturals(n)    fib    iseven     sum

 每个函数的具体定义：  

     >>> def fib(k):
             ""Compute the kth Fibonacci number.""  
                     prev, curr = 1, 0  # curr is the first Fibonacci number.
                             for _ in range(k - 1):
                                             prev, curr = curr, prev + curr
                                                     return curr
                                                     
                                                         >>> def iseven(n):
                                                                 return n % 2 == 0
                                                                 
                                                                     >>> nums = (5, 6, -7, -8, 9)
                                                                     
                                                                         >>> def sum_even_fibs(n):
                                                                                 ""Sum the first n even Fibonacci numbers.""
                                                                                         return sum(filter(iseven, map(fib, range(1, n+1))))
                                                                                            >>> sum_even_fibs(20)
                                                                                                3382
                                                                                                
                                                                                                
                                                                                                上面的模式就是映射、过滤和累计，来组合序列的接口约定上的操作。  
                                                                                                在python中有一种更简洁明了的途径--**生成器表达式**。
                                                                                                
                                                                                                **生成器表达式**：
                                                                                                
                                                                                                    <map expression> for <name> in <sequence expression> if <filter expression>
                                                                                                    
                                                                                                    上面的问题就可以简化为：  
                                                                                                    
                                                                                                        >>> def sum_even_fibs(n):
                                                                                                                return sum(fib(k) for k in range(1, n+1) if fib(k) % 2 == 0)
                                                                                                                
                                                                                                                
                                                                                                                
## 可变数据 ##
                                                                                                                
                                                                                                                我们用于创建模块化程序的强大工具之一，是引入可能会随时间改变的新类型数据。这样，单个数据可以表示独立于其他程序演化的东西。对象行为的改变可能会由它的历史影响，就像世界中的实体那样。向数据添加状态是这一章最终目标：面向对象编程的要素。
                                                                                                                
                                                                                                                我们目前引入的原生数据类型 -- 数值、布尔值、元组、范围和字符串 -- 都是不可变类型的对象。虽然名称的绑定可以在执行过程中修改为环境中不同的值，但是这些值本身不会改变。这一章中，我们会介绍一组可变数据类型。可变对象可以在程序执行期间改变。
                                                                                                                
### 局部状态 ###
                                                                                                                
                                                                                                                局部状态是在程序执行期间会发生改变。
                                                                                                                
                                                                                                                    >>> def make_withdraw(balance):
                                                                                                                            ""Return a withdraw function that draws down balance with each call.""
                                                                                                                                    def withdraw(amount):
                                                                                                                                                nonlocal balance                 # Declare the name "balance" nonlocal
                                                                                                                                                            if amount > balance:
                                                                                                                                                                                return 'Insufficient funds'
                                                                                                                                                                                            balance = balance - amount       # Re-bind the existing balance name
                                                                                                                                                                                                        return balance
                                                                                                                                                                                                                return withdraw

                                                                                                                                                                                                                上面的例子看出我们每调用一次make_withdraw,就会创建一个新的局部栈帧，并且局部栈帧不会立即回收，nonlocal可以使得我们修改balance,使得局部状态发生变化。![](https://i.imgur.com/2JY1opu.png)

### 非局部赋值 ###

非局部赋值，使得对象彼此相互独立，各自管理自己的局部状态。![](https://i.imgur.com/lsE6udM.png)

如图中，我们将make_withdraw调用了两次，用wd和wd2分别绑定到两次的返回值上。这两个对象分别管理自己的状态。wd的局部状态的改变不会影响wd2的局部状态。

