# python CommandLine3.py 11 21 Pune 89.90 Mumbai [10,20,30,40,50]
import sys

def main():
    print("Command line arguments are :")
    for i in range(len(sys.argv)):
        print(sys.argv[i])

if __name__ == "__main__":
    main()