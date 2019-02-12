import types
import sys


def recursive_reload(module, visited):
    if not module in visited:
        reload(module)
        print "reloading ", module.__name__
        visited[module] = None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                recursive_reload(attrobj, visited)


def reload_all(*args, **kwargs):
    visited = {}
    if args:
        for arg in args:
            if type(arg) == types.ModuleType:
                recursive_reload(arg, visited)
    if kwargs:
        print kwargs
        for arg in kwargs.values():
            if type(arg) == types.ModuleType:
                recursive_reload(arg, visited)


if __name__ == "__main__":
    import rldall
    reload_all(rldall)
else:
    reload_all(sys.modules)
