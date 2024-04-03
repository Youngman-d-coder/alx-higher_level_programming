#!/usr/bin/python3
import importlib.machinery

if __name__ == "__main__":
    loader = importlib.machinery.SourceFileLoader("a", "variable_load_5.py")
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    
    print(module.a)
