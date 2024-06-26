#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        code = marshal.load(f)

    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)

    names = set()
    for name, value in module.__dict__.items():
        if not name.startswith("__"):
            names.add(name)

    for name in sorted(names):
        print(name)
