ingreso_mensual = 81000
gasto_mensual = 80000

#ejemplo de if anidados (un if dentro de otro if)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: #es por que gasto mas de lo que gano, osea quedo con una deuda
        print("estas en deuda")
    elif ingreso_mensual - gasto_mensual > 3000: #es por que le queda mas de 3000, entonces esta bien
        print("estas bien")
    else:
        print("estas gastando mucho") #es por que le queda poco dinero

#si if no se cumple, pasa a recorrer el codigo del elif de abajo
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")

elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
    
#si el ultimo elif no se cumple, pasa a recorrer el codigo de else
else:
    print("eres pobre")
    