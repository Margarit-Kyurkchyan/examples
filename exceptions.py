def attempt_float(x):
    try:
        return float(x)
    except:
        return x


def attempt_float_v2(x):
    try:
        return float(x)
    except:
        return x
    else:
        print('Succeeded')
    finally:
        print('done')


def attempt_float_exception(x):
    try:
        return float(x)
    except ValueError:
        return x


def attempt_float_multiple_exception(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return x


print(attempt_float((1,2)))
print(attempt_float('454'))
print(attempt_float_v2('something'))
print(attempt_float_v2('963'))
print(attempt_float_exception('some text'))
print(attempt_float_multiple_exception((1,2)))
print(attempt_float_exception((1,2)))