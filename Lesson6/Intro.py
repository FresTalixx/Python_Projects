import inspect
import requests
import sys

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.maxsize)
print(sys.argv)

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)
    
for _ in dir(__builtins__):
    print(_)
