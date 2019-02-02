class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')
    def bar(self,message):
        print("%s from Parent" % message)

class FooChild(FooParent):
    def __init__(self):
        super().__init__()
        print('Child')

    def bar(self,message):
        super().bar(message)
        print('Child bar function')
        print(self.parent)

if __name__=='__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

class One(object):
    def method1(self):
        print('Method1, class one')
    def method2(self):
        print('Method2, class one')
    def method3(self):
        raise Exception('Empty method')
class Two(One):
    def method1(self):
        super(Two,self).method1()
        print("Method 1, class Two")
class Three(One):
    def method1(self):
        super(Three, self).method1()
        print('Method1, class Tree')
    def method2(self):
        super(Three,self).method2()
        print('Mehotd2, class Tree')
class Fourth(Three, Two):
    def method1(self):
        super(Fourth,self).method1()
        print('Method1, class Fourth')
    def method2(self):
        super(Fourth,self).method2()
        print('Method2, class Fourth')

fistObject = One()
secondObject = Two()
thirdObject = Three()
fourthObject = Fourth()

fourthObject.method2()
