import one

print("Top level in TWO.PY")

one.func()

if __name__ == '__main__':
    print("TWO.Py is run directly")
else:
    print("TWO.Py is imported")