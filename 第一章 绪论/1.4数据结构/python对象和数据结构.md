## python对象和数据结构
1. python变量和对象
   1. 高级语言里的变量是内存及其地址的抽象。变量本身也需要在内存中安排位置，每个变量占用若干个存储单元。语言系统需要有一套系统化的安排方式处理这个问题。
   2. python程序中，可以通过初始化给变量约束一个值，还可以通过复制修改变量的值。这里的值就是对象，给变量约束一个对象，就是把该对象的标识存入该变量。从变量出发访问其值是常量时间，这是python里分析程序的时间代价基础
   3. python变量的值都是对象，可以是基本整数，浮点数等类型的对象，也可以是组合对象，如list等。程序中建立和使用的各种复杂对象，包括python函数等，都基于独立的存储块实现，通过链接相互关联。程序里的名字关联着作为其值的对象，这种关联可以用复制操作改变。
   4. python语言中变量的这种实现方式称为变量的引用语义，在变量里保存值的引用。采用这种方式，变量所需要的存储空间大小一致，因为其中只需要保存一个引用。有些语言采用的不知这种方式，他们把变量的值直接保存在变量的存储区里，称为值语义。这样一个整数类型的变量就需要保存一个整数所需的空间。
2. python对象表示
   1. 虽然再写python程序时可以不关系各种对象的具体表现方式。但对这方面情况有所了解，可以帮助人们更清晰的理解程序的行为，特别是与执行效率有关的行为。基于前面的讨论，现在对python的对象表示做一个概貌性的介绍。
   2. python语言实现基于一套精心设计的链接结构。变量与其值对象的关联通过链接的方式实现，对象之间的联系同样也通过链接。一个复杂的对象内部也可能包含几个字部份，相互之间通过链接建立关系。
   3. python里的组合对象可以具体有任意大的规模，每个对象需要的存储单元可能不同，还可能又复杂的内部结构。在这类复杂对象的创建和使用中，存储安排的挂历是比较麻烦的事情。python内部有一个存储管理系统，负责管理可用的内存，为各种对象安排存储，支持灵活有效的内存使用。程序中要求建立对象时，管理系统就会为其安排存储，某些对象不在游泳时则回收其占用的内存。存储管理系统屏蔽了具体的内存使用细节，大大减少了编程人员的负担。
3. python的几个标准数据类型
   1. list（列表）。list对象可以包含任意多个任意类型的元素，元素访问和修改都是常量时间操作。此外，list对象是可变对象，再对象的存在期间可以任意的加入或删除元素。因此，程序中经常需要从空列表开始，通过逐步添加元素的方法构造任意大的表。在后面一些数据结构的实现中，也是用这种技术。
   2. tuple（元组）。与list类似，但其对象是不变的，只能在创建时一下子构造出来，不能逐步构造。
   3. dict（字典）k,v形式，支持关键码的数据存储和检索。这里的关键码只能是不变对象。如果关键码是组合对象，其元素仍然必须是不变对象。在一个字典里可以容纳任意多个关键码/值关联，支持高效检索（平均时间为0(1)）。