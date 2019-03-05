import types
import sys


def recursive_reload(module, visited):
    if module not in visited:
        for attrobj in module.__dict__.values():
            if isinstance(attrobj, types.ModuleType):
                print attrobj
                recursive_reload(attrobj, visited)
    visited.add(module)
    reload(module)
    print "reloading ", module.__name__


def reload_all(*args, **kwargs):
    visited = set()
    if args:
        for arg in args:
            if isinstance(arg, types.ModuleType):
                recursive_reload(arg, visited)
    if kwargs:
        print kwargs
        for arg in kwargs.values():
            if isinstance(arg, types.ModuleType):
                recursive_reload(arg, visited)


if __name__ == "__main__":
    import rldall
    reload_all(rldall)
else:
    reload_all(sys.modules)
