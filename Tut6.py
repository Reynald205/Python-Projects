while True:  # Exception handling
    if __name__ == '__main__':
        try:
            tuna = int(input("What is your favorite number?\n"))
            print(18/tuna)
            break
        except ValueError:
            print('Make sure to enter a number.')
        except ZeroDivisionError:
            print("Don't divide by zero.")
        except:
            break
        finally:  # Execute this code no matter what
            print("Loop Complete.")