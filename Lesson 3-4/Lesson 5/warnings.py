import _warnings
from sys import excepthook

try:
    _warnings.warn("Text for warning is deprecated", DeprecationWarning)
except:
        print("Warning for deprecation warning")


print("Code end")