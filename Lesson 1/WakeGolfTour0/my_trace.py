from functools import wraps
import datetime
import logging

def get_logger():
        """Returns a logging object, if it doesn't exist create it, otherwise just return the existing one"""
        logger = logging.getLogger("trace_logger")

        # if the logger already has 'handlers' just return it.
        if logger.hasHandlers():
            return logger

        # set the logging level (Note we can pass this as a parm)
        logger.setLevel(logging.INFO)

        # create a logging file handler
        fh = logging.FileHandler("trace.log")

        # set the file handlers format
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)

        # add handler to logger object
        logger.addHandler(fh)
        return logger


# decorator function for functions
def trace_function(printArgs=False, printRes=False, log=True):
    def trace(function):
        @wraps(function)
        def do_trace(*args, **kwargs):
            logger = get_logger()
            if log:
                logger.info("Entering {}".format(function.__name__))
                if printArgs:
                    logger.info("<<< Arguments {}".format(args))
            else:
                print("\n[---TRACE---][{0}] Entering {1}".format(datetime.datetime.now(), function.__name__))
                if printArgs:
                    print("[---TRACE---][{0}] Arguments {1}".format(datetime.datetime.now(), args))

            # add a print statement for tracing the input arguments
            print("\n[---TRACE---] [{0}] Entering {1}".format(datetime.datetime.now(), function.__name__))
            print("\n[---TRACE---] [{0}] Arguments {1}".format(datetime.datetime.now(), args))

            # call the original function    
            res = function(*args, **kwargs)

            print("\n[---TRACE---] [{0}] Returning from {1}".format(datetime.datetime.now(), function.__name__))
            print("\n[---TRACE----] [{0}] Results {1}".format(datetime.datetime.now(), res))

            return res
            if printArgs:
                print("[---TRACE----] [{0}] Arguments {1}".format(datetime.datetime.now(), args))
            if printRes:
                print("[----TRACE---] [{0}] Results {1}".format(datetime.datetime.now(), res))
        return do_trace    
    return trace


# decorator function for class methods
# note the extra self argument passed to the do_trace function
def trace_class_method(printArgs=False,printRes=False, log=True):
    def trace(function):
        @wraps(function)
        def do_trace(self, *args, **kwargs):
            logger = get_logger()
            logger = get_logger()
            if log:
                logger.info("Entering {}".format(function.__name__))
                if printArgs:
                    logger.info("<<< Arguments {}".format(args))
            else:
                print("\n[---TRACE---][{0}] Entering {1}".format(datetime.datetime.now(), function.__name__))
                if printArgs:
                    print("[---TRACE---][{0}] Arguments {1}".format(datetime.datetime.now(), args))

            print("\n[---TRACE---][{0}] Entering {1}.{2}". format(datetime.datetime.now(),
                 self.__class__.__name__ ,function.__name__))

            if printArgs:
                print("[---TRACE---][{0}] Arguments {1}".format(datetime.datetime.now(), args))
            
            res = function(self, *args, **kwargs)

            print("\n[---TRACE---][{0}] Returning from {1}.{2}". format(datetime.datetime.now(),
                 self.__class__.__name__ ,function.__name__))

            return res
            if printRes:
                print("[---TRACE---][{0}] Results {1}".format(datetime.datetime.now(), res))
        return do_trace    
    return trace
