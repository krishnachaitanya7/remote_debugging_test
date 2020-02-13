"""
Remote debugging setup
Reference: https://stackoverflow.com/questions/6989965/how-do-i-start-up-remote-debugging-with-pycharm
"""
import math
import pydevd_pycharm
pydevd_pycharm.settrace('10.201.16.206', port=4444, stdoutToServer=True, stderrToServer=True)

if __name__ == "__main__":
    x = 0
    print("Wantedly testing remote exception to see if it works or not")
    y = 2/x
    print("Yayy!!!")