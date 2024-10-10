import logging
from functools import wraps

logging.basicConfig(
    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(message)s', # set the format for log entries
    datefmt="%x-%X",
    filename="timestamp.log",
    level=logging.DEBUG,
)


def logtimestamp(original_function):

    @wraps(original_function)
    def WRAPPER(*args, **kwargs):
        logging.debug("Calling %s", original_function.__name__)
        result = original_function(*args, **kwargs)
        return result

    return WRAPPER

@logtimestamp
def spam(x):
    print("SPAM", x)
# spam = logtimestamp(spam)

@logtimestamp
def ham(x, y):
    print("HAM", x * y)

spam(10)
ham(5, 8)
spam("wombat")
ham(5, "moose")
spam(-1)
