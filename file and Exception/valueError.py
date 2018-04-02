
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("please input correct value")
    except Exception:
        print("exception not identified") #parent exception
    finally:
        print("resource haldled")