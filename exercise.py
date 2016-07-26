import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of program')

def the_operations(arg):
  def the_operations(func):
    def decorator(*args, **kwargs):
      logging.info('Start..! executing method call %s...with name %s' % (func.__name__, arg))

      _ret = func(*args, **kwargs)
      logging.info('End... of method call %s with name %s!' % (func.__name__, arg))

      return _ret
    return decorator
  return the_operations

@the_operations('Division')
def division(arg1, arg2):
    logging.info('Division %r and %r: %r!'%(arg1, arg2, arg1/arg2))
    return arg1/arg2
@the_operations('Exponents')
def exponent(arg1, arg2):
    logging.info('Exponent %r to the power %r: %r!'%(arg1, arg2, arg1**arg2))
    return arg1**arg2
logging.info('End of program')
