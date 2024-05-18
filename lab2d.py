#!/usr/bin/env python3
# Author: Micaira Mateo
# Author ID#: 103732228
# Author Email: mmateo2@myseneca.ca
# Date Created: May 17, 2024

import sys

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

name = str(sys.argv[1])
age = str(sys.argv[2])

print("Hi " + name + ", you are " + age + " years old.")
