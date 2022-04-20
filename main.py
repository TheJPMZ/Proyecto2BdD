import build.gui_controller
import os
import sys



def main():

    build.gui_controller.main()

if __name__ == "__main__":
    hashseed = os.getenv('PYTHONHASHSEED')
    if not hashseed:
        os.environ['PYTHONHASHSEED'] = '0'
        os.execv(sys.executable, [sys.executable] + sys.argv)
    main()