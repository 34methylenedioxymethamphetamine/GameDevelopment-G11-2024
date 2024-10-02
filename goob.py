import os

try:
    while True:
        try:
            cmd = input("C:\\>").strip()
            if cmd == "_exit":
                print("Quitting...")
                exit()
            os.system(cmd)
        except KeyboardInterrupt:
            print("Caught ^C (Command Executor)")
            exit()
except KeyboardInterrupt:
    print("Caught ^C")
    exit()
except Exception as ex:
    print("Caught Exception")
    print(ex)
    exit()