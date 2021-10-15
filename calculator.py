import re

#github: PetronioN
#Autor: Petronio Nascimento

print("Digite 'sair' para sair do programa.\n")

previous = 0
run = True

def performMath():
	global run
	global previous
	
	equation = ""
	
	#Entrada do usuário
	if previous == 0:
		equation = input("Insira a equação: ")
	else:
		equation = input(str(previous))
	
	if equation == "sair":
		print("Até mais!")
		run = False
		
	#Retirada de caracteres especiais e letras
	else:
		equation = re.sub('[a-zA-Z.,()" "]', '', equation)
		
		if previous == 0:
					previous = eval(equation)
		else:
			previous = eval(str(previous) + equation)
				

while run:
	
	#Tratamento de erro
	try:
		performMath()
	except ZeroDivisionError:
		print("\nNão é possível dividir um número por 0.\n")	