import unittest             #imports the ability to run unittests

# Write a reverseList function and test it with at least 3 cases
def reverseList(a_list):
    for i in range(0, int(len(a_list)/2)):
        a_list[i], a_list[len(a_list)-1-i] = a_list[len(a_list)-1-i], a_list[i]
    return a_list

# Write an isPalindrome function and test it with at least 5 cases
def isPalindrome(a_string):
    for i in range(int(len(a_string))):
        if a_string[i] != a_string[len(a_string)-1-i]:
            return False
    return True

# Write a coins function and test it with at least 5 cases
def coins(num):
    quarters = 0
    nickles = 0 
    dimes = 0
    pennies = 0
    coin_list = []
    while num > 0:
        if num > 24:
            quarters += 1
            num -= 25
        elif num > 9:
            dimes += 1
            num -= 10
        elif num > 4:
            nickles +=1
            num -=5
        else:
            pennies +=1
            num -=1
    coin_list.append(quarters)
    coin_list.append(dimes)
    coin_list.append(nickles)
    coin_list.append(pennies)
    return coin_list

# BONUS: Write a recursive factorial function and test it with at least 3 cases
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

# BONUS: Write a recursive fibonacci function and test it with at least 3 cases
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-2) + fibonacci(n-1))


class reverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1, 2, 3]), [3, 2, 1])
    
    def testTwo(self):
        self.assertEqual(reverseList([5, 6, 7]), [7, 6, 5])
    
    def testThree(self):
        self.assertEqual(reverseList([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def setUp(self):
        print("running setUp for reverseList")

    def tearDown(self):
        print("running tearDown tasks for reverseList")


class isPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(isPalindrome("mom"), True)
    
    def testTwo(self):
        self.assertTrue(isPalindrome("dad"))
    
    def testThree(self):
        self.assertFalse(isPalindrome("yesterday"))
    
    def testFour(self):
        self.assertTrue(isPalindrome("racecar"))
    
    def testFive(self):
        self.assertFalse(isPalindrome("tomorrow"))


class coinsTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])
    
    def testTwo(self):
        self.assertEqual(coins(100), [4, 0, 0, 0])

    def testThree(self):
        self.assertEqual(coins(6), [0, 0, 1, 1])
    
    def testFour(self):
        self.assertEqual(coins(1), [0, 0, 0, 1])
    
    def testFive(self):
        self.assertEqual(coins(10), [0, 1, 0, 0])


class factorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5), 120)

    def testTwo(self):
        self.assertEqual(factorial(1), 1)
    
    def testThree(self):
        self.assertEqual(factorial(4), 24)


class fibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(1), 1)

    def testTwo(self):
        self.assertEqual(fibonacci(2), 1)

    def testThree(self):
        self.assertEqual(fibonacci(3), 2)

if __name__ == '__main__':
    unittest.main()             #this runs our tests       