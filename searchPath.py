import sys, pprint, json

print("Is 'sys' builtin?", 'sys' in sys.builtin_module_names)

print("\nTop of sys.path (searched first):")
print(sys.path[0])

print("\nWhere did 'json' come from?")
print(getattr(json, '__file__', 'builtin'))

print("\nFull sys.path:")
pprint.pp(sys.path)