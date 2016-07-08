#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Creado por Jean Pierre Pacheco Avila


from numpy import *
import matplotlib.pyplot as plt
# y' = -y
def oscilador(t,y):
    return array([y[1],-y[0]])

# Oscilador armonico amortiguado
def osc_arm_amor(t,Y):
    y1, y2 = Y
    return array([y2,-3*y1 - 1.5*y2])


# Usando el cambio de variable llegamos a la siguiente forma
# bidimiensional del sistema
mu = 0.25
def vander(t,Y):
    x,y = Y
    return array([mu*(x-((x**3)/3.)- y),(1/mu)*x])



def ecuacion(t,Y):
	return 12*exp((-log(2)/5600)*t)

# Runga-Kutta de orden 2

def rk2(x_inicio,t_inicial,t_final,delta_t,f):
    dt = delta_t
    t = t_inicial
    x = x_inicio
    time=[]
    sol=[]

    #Algoritmo de intgración de Runge Kutta
    while (t < t_final):
        time.append(t)
        sol.append(x)
        k1 = dt*f(t,x)
        k2 = dt*f(t + dt,x + k1)
        x = x + (1/2.)*(k1 + k2)
        t = t + dt

    return [time,sol]


def rk(x_inicio,t_inicial,t_final,delta_t,f):
    x0 = x_inicio
    t0 = t_inicial
    dt = delta_t
    t = t0
    x = x0
    time=[]
    sol=[]

    #Algoritmo de intgración de Runge Kutta
    while (t < t_final):
        time.append(t)
        sol.append(x)
        k1 = dt*f(t,x)
        k2 = dt*f(t + 0.5*dt,x + 0.5*k1)
        k3 = dt*f(t + 0.5*dt,x + 0.5*k2)
        k4 = dt*f(t + dt,x + 1.0*k3)
        x = x + (1./6.)*(k1 + 2.*k2 + 2.*k3 + k4)
        t = t + dt
    return [time,sol]



#solucion2 = rk2([0,1],0,10,0.1,oscilador)
#solucion2 = rk2([0,1],0,10,0.1,osc_arm_amor)
"""""
solucion2 = rk2([3,6],0,10,0.1,vander)
solucion3 = rk2([1,1],0,10,0.1,vander)
solucion4 = rk2([0,0],0,10,0.1,vander)
solucion5 = rk2([6,4],0,10,0.1,vander)
"""""


"""""
solucion2 = rk2([3,6],0,10,0.1,osc_arm_amor)
solucion3 = rk2([1,1],0,10,0.1,osc_arm_amor)
solucion4 = rk2([0,0],0,10,0.1,osc_arm_amor)
solucion5 = rk2([6,4],0,10,0.1,osc_arm_amor)
"""""


solucion2 = rk2([0,12],0,1000,0.1,ecuacion)
print solucion2

#solucion3 = rk2([1,1],0,10,0.1,ecuacion)
#solucion4 = rk2([0,0],0,10,0.1,ecuacion)
#solucion5 = rk2([6,4],0,10,0.1,ecuacion)


plt.plot(solucion2[0],solucion2[1])
"""""
plt.plot(solucion3[0],solucion3[1])
plt.plot(solucion4[0],solucion4[1])
plt.plot(solucion5[0],solucion5[1])
"""""
plt.show()
