class A:
    def __init__(self):
        print("A: Constructor")
    
    def __del__(self):
        print("A: Destructor")

def main():
    print ("Main: start")
    try:
        a = A()
        raise Exception
    except:
        exit(1)
    print ("Main: end")

if __name__ == "__main__":
    main()
    