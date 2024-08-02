#pip install cowsay --> learn about pip - 3rd party libraries
import cowsay
import sys

if len (sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1]) #it's not print, cannot use comma comma
    cowsay.trex("Hello, " + sys.argv[1])
