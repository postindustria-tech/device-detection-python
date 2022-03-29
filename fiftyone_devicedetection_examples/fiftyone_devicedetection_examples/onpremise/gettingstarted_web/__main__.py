import sys
from .app import main

# This file enables the example to be run without adding ".app" to the end of
# the module name
if __name__ == "__main__":
    main(sys.argv[1:])

