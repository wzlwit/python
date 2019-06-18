import os
import time

def main():
    content = 'Welcome! Create the World'
    while True:
        # clear the screen
        os.system('cls')  # os.system('clear')
        print(content)
        # sleep 200 ms
        time.sleep(0.2)
        content = content[1:] + content[0] #string manipulation


if __name__ == '__main__':
    main()