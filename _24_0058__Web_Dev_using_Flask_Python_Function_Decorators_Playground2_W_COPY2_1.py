
import datetime

def outter_logging_decorator_function(main_function):
    def inner_wrapper_function_for_logging_actions():
        # gets the current date and time
        current_time = datetime.datetime.now()
        # formats the timestamp for the log
        timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')
        # prints the log message with the timestamp
        print(f"\nDate & Time: {timestamp}. \nName of the function being called: {main_function.__name__}")
        print(f"What the function is doing, processing-wise:")
        return main_function()

        # return main_function.__name__()
        # return main_function

    return inner_wrapper_function_for_logging_actions

@outter_logging_decorator_function
def start_process():
    print("Starting the program")    # these should contain the actual code you want to run, not the call to the decorator.

@outter_logging_decorator_function
def middle_process():
    print("Performing an action")

@outter_logging_decorator_function
def ending_process():
    print("Ending the program")

start_process()
middle_process()
ending_process()




# usage of the logging_decorator_function function:
# decorated_start_process = logging_decorator_function(start_process)   3 we don't use these because the decorator already applies this logic. That's what decorators do! :D
# decorated_middle_process = logging_decorator_function(middle_process)
# decorated_ending_process = logging_decorator_function(ending_process)

# decorated_start_process()
# decorated_middle_process()
# decorated_ending_process()




