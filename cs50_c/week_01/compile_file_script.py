import sys
import subprocess
import re

def compile_process(arr):
    print("Compilation successful!")
    if check_file(r"^.+\.c$", arr[0]):
        subprocess.run(["g++", arr[0]])
    else:
        subprocess.run(arr)
    execute_process()

def execute_process():
    print("Running program...\n")
    subprocess.run("./a.out")

def check_file(conditional, argument):
    res = False
    if re.match(conditional, argument):
        res = True
    return res

def main():
    sys.argv = sys.argv[1:]
    if len(sys.argv) > 0:
        compile_process(sys.argv)
    else:
        print("Too few arguments!")
        print(sys.argv)

if __name__ == "__main__":
    main()
