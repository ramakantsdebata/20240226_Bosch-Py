
# https://docs.python.org/3/library/exceptions.html

def Divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("A divisor can NOT be zero.")
    return dividend / divisor

def Test1():
    a = 10
    b = 2
    try:
        res = Divide(a, b)
        print(res)
        # Open a connection
        # Operate
        # Close Connection {1} args -> ###, ___

    except ZeroDivisionError:
        print("Division failed")
    except ValueError as ex:
        print("Exception:", ex)
    except Exception as ex:
        print(ex)
    # except Exception as ex:
    #     print(ex)
    #     # Close Connection {2} args -> ___, ___
    finally:
        # Close Connection
        pass

    print("Resuming other activities")

########################################################
def Baz(data):
    if data == 10:
        raise ValueError("Invalid Input")

def Bar(data):
    try:
        Baz(data)
    except ValueError:
        print("Performing cleanu up & Saving context")
        print("Log data point")
        raise

def GetUserInput():
    return 10

def Foo():
    try:
        data = GetUserInput()
        Bar(data)
    except ValueError as ex:
        print("Notify User that input is incorrect")
        print("Attempt to accept fresh input for reattempt")

def Test2():
    Foo()

if __name__ =="__main__":
    # Test1()
    Test2()