import os
import random
import math
import statistics
from tqdm import tqdm
from matplotlib import pyplot as plt
import argparse
from colorama import init,Fore, Back, Style

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
		
	def shuffle_list(self):
		random.shuffle(self.l)
		self.string = ' '.join([str(item) for item in self.l])
	
	def do_test(self):
		self.shuffle_list()
		self.status = os.popen(self.program +'"'+ self.string +'"'+ self.test + self.string).read()
		self.leaks = os.popen("valgrind "+self.program +'"'+ self.string +'"'+ self.test + self.string).read()
		self.cont = os.popen(self.program + self.string +"| wc -l").read()
		if (self.status[0] == "O"):
			self.resultados.append(int(self.cont))
			self.bien = self.bien + 1
		if (self.status[0] == "K"):
			print(l)
			self.final = "FAIL"
			self.mal = self.mal + 1
	
	def print_output(self):
		print(Fore.BLUE , end =" ")
		print(f'{len(self.l)} random number TEST:', end =" ")
		if (self.final == "OK"):
			print(Fore.GREEN + "OK", end =" ")
			print(f'[{self.bien}]', end =" ")
			print("\t ", end =" ")
			print(Fore.WHITE + "MOVEMENTS: AVG(",round(statistics.mean(self.resultados)), end ="")
			print(") MIN(", min(self.resultados), end ="")
			print(") MAX(", max(self.resultados), ")")
		else:
			print(Fore.GREEN + "FAIL")

parser = argparse.ArgumentParser(description='42 push_swap tester.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='number of test')
parser.add_argument('--size', type=int, default=0,
                    help='only check stacks of this size')


args = parser.parse_args()

if (args.size !=0):
	l = LISTA(-100, args.size-100, 1)
	x = TEST(args.size, l)
	for n in range(0,args.integers[0]):
		x.do_test()
	x.print_output()
else:
	test_valores = [2,3,5,10,15,20,25,30,35,40,45,50,60,70,80,90, 100,200,300,400,500]
	for up in test_valores:
		l = LISTA(-100, up-100, 1)
		x = TEST(up, l)
		for n in range(0,args.integers[0]):
			x.do_test()
		x.print_output()


print(x.string)	
print(x.leaks)
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