from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a string length 2 made of its first 2 chars. If the //
## string length is less than 2, use  '@' for the missing chars.             //
##   ("hello") -> "he"                                                       //
##   ("hi") -> "hi"                                                          //
##   ("h") -> "h@"                                                           //
##/////////////////////////////////////////////////////////////////////////////


def first_two_chars(s):
    if len(s) >= 2:
        return s[:2]
    else:
        return s + "@"*(2-len(s))
