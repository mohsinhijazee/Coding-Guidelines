"""Module docstring.
Should contain a high level summary of the module, why it exists, where to 
use.
"""

# General lining rules:
# 2 blank lines within classes
# 1 blank line within functions
# 79 characters per line
# 4 spaces indent (DO NOT USE TABS!)



# Your file should have following sections in order:
# 1. Info about module
# 1. Imports
# 2. Constants
# 3. Exception classes
# 4. Interface functions
# 5. Classes
# 6. Internal functions and classes

# List all the classes, functions, variables that you 
# prefer to be imported via import * OPTIONAL
__all__ = ["YourClassOne", "a_cute_function_for_outsiders"]

# Your verison. OPTIONAL
__version__ = "0.32"

# List of authors.
__authors = ["Mohsin Hijazee <mohsin@sovoia.com>",
             "Talib  Siddique <talib@sovoia.com>"]

# 1. Imports
# Should have following order:
# a. Pyhton standard library imports
# b. Third party imports
# c. Your own internal imports
# Each group should be separated by a blank line.

import os
import sys

from third.party import something
from third.gang import none

from your.own import another
from your.own import whatever


# Local and global variables are lowercase underscored.
server__config = {}

# If you use any global datastructures, do document them like this:
server_config.__doc__ = """This contains all the configs with keys as setting names 
in the following manner:
  web -- All web related settigs.
  db  -- All dataabase stuff
      host -- host for database
"""

# 2. Constants
# Use all uppercase separated with _
THIS_IS_A_GOOD_CONSTANT = 34


# 2.  Exception classes
# 2.1 Must be derived from Exception
# 2.2 Just like classes, must be TitleCased.

class VeryBadError(Exception):
    """All the classes should be documented.

    Provide one line summary above followed by blank line and then list further 
    details.
    """
    pass

# Interface functions
# The functions that are to be exported outside.
def function_for_outsiders(takes_something):
    """This function does nothing."""
    pass


# classes
class Person:
    """Class description here."""
    pass

# internal functions & classes
# All the functions and classes that you do not want to show the world.
def do_sum(a, b):
    """Sums the given numbers.

    Arguments:
        a -- First number
        b -- Second number

   Returns:
        Sum of a and b.
    """
    return a + b


def main(...):
    return 3


# Your main function in case the module is returend
if __name__ == '__main__':
    status = main()
    sys.exit(status)
