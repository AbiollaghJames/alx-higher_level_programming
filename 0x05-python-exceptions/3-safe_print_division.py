#!/usr/bin/python3

def safe_print_division(a, b):
    """Divie two numbers and catch
    zeroDivisionError"""
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
