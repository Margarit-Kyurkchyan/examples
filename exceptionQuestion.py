# What will the output be?

def bool_result():
    try:
        return True
    finally:
        return False

res = bool_result()
print(res)