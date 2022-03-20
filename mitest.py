import os
import random
import math
import statistics
from tqdm import tqdm
from matplotlib import pyplot as plt
import argparse
from colorama import init,Fore, Back, Style
import random
from xml.dom import minidom

class LISTA:
	def __init__(self, start, end, step):
		self.l = list(range(start, end, 1))

class TEST:
	def __init__(self, size, lista):
		self.size = size
		self.l = lista.l
		self.program = "./push_swap "
		self.arg = "3 2 1"
		self.test = "| ./checker_LINUX "
		self.resultados = []
		self.final = "OK"
		self.bien = 0
		self.mal = 0
		self.n_leaks = 0
		
	def shuffle_list(self):
		random.shuffle(self.l)
		self.string = ' '.join([str(item) for item in self.l])
	
	def do_test(self):
		self.shuffle_list()
		if random.choice([True, False]):
			self.status = os.popen(self.program +'"'+ self.string +'"'+ self.test + self.string).read()
		else:
			self.status = os.popen(self.program +self.string + self.test + self.string).read()
		self.cont = os.popen(self.program + self.string +"| wc -l").read()
		if (self.status[0] == "O"):
			self.resultados.append(int(self.cont))
			self.bien = self.bien + 1
		if (self.status[0] == "K"):
			self.final = "FAIL"
			self.mal = self.mal + 1
	
	def check_leaks(self):
		self.leaks = os.popen("valgrind --xml=yes --xml-file=log.xml "+self.program +'"'+ self.string +'"'+ self.test + self.string).read()
		self.compute_leaks()
		self.leaks = os.popen("valgrind --xml=yes --xml-file=log.xml "+self.program + self.string + self.test + self.string).read()
		self.compute_leaks()

	def compute_leaks(self):
		self.mydoc = minidom.parse('log.xml')
		self.items = self.mydoc.getElementsByTagName('count')
		try:
			self.items[0].firstChild.data
			self.n_leaks = self.n_leaks + 1
		except:
			self.n_leaks = self.n_leaks
		
	def print_output(self):
		print(Fore.BLUE , end =" ")
		print(f'{len(self.l):>5} random number TEST:', end =" ")
		if (self.final == "OK"):
			print(Fore.GREEN + "OK", end =" ")
			print(f'[{self.bien}]', end =" ")
			print("\t ", end =" ")
			print(Fore.WHITE + "MOVEMENTS: avg:"+ f'{round(statistics.mean(self.resultados)):<5}', end ="")
			print("   min:"+ f'{min(self.resultados):<5}' + "   max:"+ f'{max(self.resultados):<5}', end ="")
		else:
			print(Fore.GREEN + "FAIL")

	def print_leaks(self):
		if (self.n_leaks == 0):
			print(Fore.GREEN, end =" ")
			print("NO LEAKS FOUND!!")
		else:
			print(Fore.RED, end =" ")
			print("LEAKS FOUND!!")
			
	def points(self):
		if self.size == 5:
			if max(self.resultados) > 2:
				print(Fore.RED+" FAIL!! MAXIMUM 12 movs ALLOWED")
parser = argparse.ArgumentParser(description='42 push_swap tester.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='number of test')
parser.add_argument('--size', type=int, default=0,
                    help='only check stacks of this size')				
parser.add_argument("--leaks", default=False, action="store_true",
                    help="check leaks with valgrind")
args = parser.parse_args()


if (args.size !=0):
	l = LISTA(-100, args.size-100, 1)
	x = TEST(args.size, l)
	for n in range(0,args.integers[0]):
		x.do_test()
	x.print_output()
	if args.leaks == True:
		x.check_leaks()
		x.print_leaks()
	else:
		print("")
	x.points()
else:
	test_valores = [2,3,5,10,15,20,25,30,35,40,45,50,60,70,80,90, 100,200,300,400,500]
	for up in test_valores:
		l = LISTA(-100, up-100, 1)
		x = TEST(up, l)
		for n in range(0,args.integers[0]):
			x.do_test()
		x.print_output()
		if args.leaks == True:
			x.check_leaks()
			x.print_leaks()
		else:
			print("")
		x.points()


resultados =[]
medias = []
limitx=[1,3,5, 100, 500]
limity=[1,2,12,1500, 11500]


"""
test_n = 1
if (args.size ==0):
	for up in test_valores:
		resultados =[]
		print(Fore.BLUE + 'TEST-', test_n)
		for n in tqdm(range(0,args.integers[0])):
			l = list(range(-100, up-100, 1))
			
			random.shuffle(l)
		
			string = ' '.join([str(item) for item in l])
			f = os.popen(program + string + test + string).read()
			cont = os.popen(program + string +"| wc -l").read()
			if (f[0] == "O"):
				resultados.append(int(cont))
			if (f[0] == "K"):
				print(l)
		print("--------------------------------------------------")
		print("RESULTADOS CON ", up," NUMEROS ALEATORIOS")
		print("NUMERO MOV PROMEDIO", statistics.mean(resultados))
		medias.append(statistics.mean(resultados))
		
		print("NUMERO MOV MIN", min(resultados))
		print("NUMERO MOV MAX", max(resultados))

print(medias)
plt.plot(test_valores, medias)
#plt.plot(test_valores, ncuadrado)
#plt.plot(limitx, limity)
plt.ylabel('Iterations Average')
plt.xlabel('N Random Numbers')
plt.savefig('Results.png')
"""