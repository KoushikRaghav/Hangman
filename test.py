import unittest
import hangman

class hangmanTest(unittest.TestCase):
	
	def testPrintLetters(self):
		print "\t\t\tTesting printLetters() method\n"
		result = hangman.printLetters('hello','')
		expected = 5
		self.assertEqual(expected,result) 		

	def testCheckForLose(self):
		print "\t\t\tTesting checkForLose() method\n"
		result = hangman.checkForLose('hai','h',3)
		expected = 3
		self.assertEqual(expected,result)
		
	def testCheckForWin(self):
		print "\t\t\tTesting checkForWin() method\n"
		result = hangman.checkForWin(0)
		expected = 1
		self.assertEqual(expected,result)

	def testGetValue(self):
		print "\t\t\tTesting getValue() method\n"
		result = hangman.getValue()
		expected = 'h'
		self.assertEqual(expected,result)

	def testGameFlow(self):
		print "\t\t\tTesting gameFlow() method\n"
		result = hangman.gameFlow(['hai','bye'],'hai',4,'')
		expected = 1
		self.assertEqual(expected,result)

	def testSelectOption(self):
		print "\t\t\tTesting selectOption() method\n"
		result = hangman.selectOption()
		expected = 1
		self.assertNotEqual(expected,result)
		
	def testStartGame(self):
		print "\t\t\tTesting startGame() method\n"
		result = hangman.startGame()
		expected = 0
		self.assertNotEqual(expected,result)

if __name__ == '__main__':
	unittest.main()