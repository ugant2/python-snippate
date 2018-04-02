# try:
#     a = 10 / 0
#     c = int("a")
#     b = "str" + 5
#
#
# except ZeroDivisionError:
#     print("Exception catched")
# except TypeError:
#     print("Exception caught in type")
# except Exception:
#     print("Exception not known")  # except all exception type
#
# finally:
#     print("resource handled")
#
#
#
# print ("new line")
#
# try:
#     a = 12/2
# except Exception:
#     print("error")
# else:
#     print("else")
# finally:
#     print("code not workng")



def compare(a,b):
    try:
        assert(a == b), "%d is not equal to %d"%(a,b)
        print("True")
    except AssertionError as error:
        print("error")

compare(6,6)