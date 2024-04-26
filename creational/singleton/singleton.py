# https://www.reddit.com/r/learnpython/comments/118a7d4/why_does_a_python_singleton_use_super/
# https://stackoverflow.com/questions/9056955/what-does-super-mean-in-new
# In Python, class variables (also known as class attributes)
# are shared across all instances of a class
# which means s1 = Singleton() and s2 = Singleton() will share _instance
# Every class is a subclass of the Object class
# In this case, super() == super(cur_class, 1st_args of the method)
# --> super(Single, cls)
# The first arg go upper on level of the class --> object (parent)
# cls == Singleton Class itself
# super() --> object.__new__(cls)
# rewrite __new__ --> new needs a return value
# hence we inherit from object and call __new__ of it
# super().__new__(cls) --> is only a empty cls class object, won't do anything (e.g., __new__)
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


"""
Anthor __new__ example

class ImmutablePoint:
	def __new__(cls, x, y):
		instance = super().__new__(cls)
		instance.x = x
		instance.y = y
		return instance

	def __setattr__(self, name, value):
		raise AttributeError("Cannot modify immutable object")

"""
