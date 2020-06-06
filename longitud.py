print("________________________conversion de unidades de logitud__________________________")
print("")
print("recomendacion:al momento  de ingresar un numero decimal usa punto en ves de coma")

print("***********************************************************************************")


altura= float(input("ingresa tu altura en centimetros o en metros:"))
print("numero guardado"+ " " + str(altura))


centimetros = 100
metros=1
resultado1= altura / centimetros
resultado2= altura * metros
redondo =(round(resultado1,5))

if altura < 400 :
	
	print("este es tu resultado en metros:" + " " + str(redondo)+"m")
	

elif altura < 4.00:
	round(resultado2,1)
	print("este es tu resultado en centimetros:" + " " + str(resultado2)+"cm")


else:
	print("lo siento tavez no ingresaste tu numero bien")


#Juan Sebastian Naranjo
#Colombia
#04/06/2020 17:49 