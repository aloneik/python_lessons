import types


def recursive_reload(module, visited):
    if not module in visited:
        reload(module)
        print "reloading ", module.__name__
        visited[module] = None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                recursive_reload(attrobj, visited)


def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            recursive_reload(arg, visited)


if __name__ == "__main__":
    import rldall
    reload_all(rldall)
