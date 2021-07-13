class Parent:
    pass


class FirstChild(Parent):
    pass


class SecondChild(Parent):
    pass


class GrandChild(SecondChild, FirstChild):
    pass

print(GrandChild.mro())

'''
class GrandChild(SecondChild, FirstChild):
- търси в първия наследен клас първо SecondChild 

print(GrandChild.mro())
# [<class '__main__.GrandChild'>, <class '__main__.SecondChild'>, <class '__main__.FirstChild'>, 
<class '__main__.Parent'>, <class 'object'>]
- pokazwa posledowatelnostta na tyrsene
'''
