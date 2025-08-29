class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"Exception Type: {exc_type}")
            print(f"Exception Value: {exc_value}")
        return True  # suppress the exception

with MyContextManager() as cm:
    print("Inside the context")
    raise ValueError("An error occurred")