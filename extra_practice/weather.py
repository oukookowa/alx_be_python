try:
    import requests
    print("The package is installed")
except ImportError as error:
    print(error)