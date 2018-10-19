import unittest

class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)


# 第一种运行测试用例方法
if __name__ == '__main__':
	unittest.main()

# 第一种方法运行结果
-----------------------------------
Ran 3 tests in 0.001s

OK



# 第二种运行测试用例的方法
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

# 第二种方法运行结果
test_isupper (__main__.TestStringMethods) ... ok
test_split (__main__.TestStringMethods) ... ok
test_upper (__main__.TestStringMethods) ... ok                                                      
-------------------------------------------------------
Ran 3 tests in 0.001s                                  
                                                       
OK   



	关键点：
	1、通过继承unittest.TestCase类来定义我们自己的测试用例，1个测试用例类下面可以有多个测试方法(test)或者叫做测试点
	2、记住这个套路：测试用例中方法名以test开头的方法才是测试方法，比如上面的例子里定义了3个以test开头的方法，分别是
           test_upper，test_isupper和test_split。非测试方法是不会被test runner执行的
	3、断言是测试用例的核心。我们使用assertEqual()来判断预期结果，用assertTrue()和assertFalse来做是非判断，
	   以及用assertRaises()来判断预期的异常是否有被抛出。这些unittest提供的以assert开头的方法就是断言，一般情况下,
	   每个测试方法里都必须有断言
	4、最后, unittest.main提供了最简单的运行用例的方式


