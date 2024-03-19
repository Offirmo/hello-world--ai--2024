#!/usr/bin/python3
# coding: utf-8

#################################################
def solution(s):
    print(s)
    # Your code here


#################################################
# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
case_index = 0
has_failure = False
def test(got, expected):
    global case_index, has_failure
    case_index += 1
    if got == expected:
        print('#%s: OK got: "%s" as expected ✓' % (case_index, repr(got)))
    else:
        has_failure = True
        print('#%s: XXXXXXXXXXXX' % (case_index))
        print('expected: "%s"' % (repr(expected)))
        print('got     : "%s"' % (repr(got)))


#################################################
def fi(*args, **kwargs):
    for arg in args: print(arg)
    for k, v in kwargs.items(): print("%s = %s" % (k, v))
    return solution(*args, **kwargs)


#################################################
# Calls the above functions with interesting inputs.
def main():
    test(fi("abcd"), 3)
    test(fi(['', 'x', 'xy', 'xyx', 'xx']), 2)


if __name__ == '__main__':
    try:
        main()
        if has_failure:
            print('XXXXXXXX TEST FAILURES XXXXXX')
    except Exception as e:
        # to make exceptions more visible
        print('XXXXXXXXX EXCEPTION!!! XXXXXXXX')
        raise e
