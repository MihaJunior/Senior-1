print("==============Base Exception===============")


print(f"name error = {type(NameError)} - {issubclass(NameError, BaseException)}")
try:
    print(hello)
except NameError:
    print("NameError")


try:
    print(5/0)
except ZeroDivisionError:
    print("ZeroDivisionError")


try:
    print("Hello World B***H!")
except:
    print("Something went wrong")
else:
    print("Else no problem")
finally:
    print("No promblem")