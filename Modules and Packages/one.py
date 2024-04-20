def func():
    print("Func() in ONE.PY")

print("Top level in ONE.PY")

if __name__ == '__main__':
    print("ONE.Py is run directly")
else:
    print("ONE.PY has been imported")