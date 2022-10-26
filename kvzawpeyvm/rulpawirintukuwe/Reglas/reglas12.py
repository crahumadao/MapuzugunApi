#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def rulpawe(txt): 
	#txt=re.sub()	ex		#A,a	A,a	
	txt=re.sub('ch','c',txt)	#Ch,ch 	C,c
	txt=re.sub('Ch','C',txt)	#Ch,ch 	C,c
	txt=re.sub('CH','C',txt)	#Ch,ch 	C,c
	txt=re.sub('d','z',txt)		#D,d	Z,z
	txt=re.sub('D','Z',txt)		#D,d	Z,z
	#txt=re.sub()			#E,e	E,e
	#txt=re.sub()			#F,f	F,f
	txt=re.sub('ng','d',txt)	#Ng,ng	G,g
	txt=re.sub('Ng','D',txt)	#Ng,ng	G,g
	txt=re.sub('NG','D',txt)	#Ng,ng	G,g
	txt=re.sub('g','q',txt)		#G,g	Q,q
	txt=re.sub('G','Q',txt)		#G,g	Q,q
	txt=re.sub('d','g',txt)		#G,g	Q,q
	txt=re.sub('D','G',txt)		#G,g	Q,q
	#txt=re.sub()			#I,i	I,i
	#txt=re.sub()			#K,k	K,k
	#txt=re.sub()			#L,l	L,l
	txt=re.sub('l_','b',txt)	#L_,l_	B,b
	txt=re.sub('L_','b',txt)	#L_,l_	B,b
	txt=re.sub('ll','j',txt)	#Ll,ll	J,j
	txt=re.sub('Ll','J',txt)	#Ll,ll	J,j
	txt=re.sub('LL','J',txt)	#Ll,ll	J,j
	#txt=re.sub()			#M,m	M,m
	#txt=re.sub()			#N,n	N,n
	#txt=re.sub()			#Ñ,ñ	Ñ,ñ
	txt=re.sub('n_','h',txt)	#N_,n_	H,h
	txt=re.sub('N_','H',txt)	#N_,n_	H,h
	#txt=re.sub()			#T,t	T,t
	txt=re.sub('tr','x',txt)	#Tr,tr	X,x
	txt=re.sub('Tr','X',txt)	#Tr,tr	X,x
	txt=re.sub('TR','X',txt)	#Tr,tr	X,x
	txt=re.sub('T_','T',txt)	#T_,t_	---
	txt=re.sub('t_','t',txt)	#T_,t_	---
	#txt=re.sub()			#U,u	U,u
	txt=re.sub('ü','v',txt)		#Ü,ü	V,v
	txt=re.sub(r'Ü','V',txt)	#Ü,ü	V,v
	#txt=re.sub()			#W,w	W,w
	#txt=re.sub()			#Y,y	Y,y
	return txt


def mapuchewvn(txt):
	txt=re.sub('Á','A',txt)
	txt=re.sub('á','a',txt)
	txt=re.sub('É','E',txt)
	txt=re.sub('é','e',txt)
	txt=re.sub('Í','I',txt)
	txt=re.sub('í','i',txt)
	txt=re.sub('Ó','O',txt)
	txt=re.sub('ó','o',txt)
	txt=re.sub('Ú','U',txt)
	txt=re.sub('ú','u',txt)
	#txt=re.sub(r'','',txt) #A
	txt=re.sub(r'B','F',txt) #B
	txt=re.sub(r'b','f',txt) #B
	txt=re.sub(r'C(?=[aouAOU])','K',txt)#C
	txt=re.sub(r'c(?=[aouAOU])','k',txt)#C
	txt=re.sub(r'C(?=[eiEI])','S',txt)#C
	txt=re.sub(r'c(?=[eiEI])','s',txt)#C
	#txt=re.sub(r'','',txt)	#CH
	#txt=re.sub(r'','',txt)	#D
	#txt=re.sub(r'','',txt)	#E
	#txt=re.sub(r'','',txt)	#F
	txt=re.sub(r'G[Uu]*[Ii]','Ki',txt)	#G
	txt=re.sub(r'g[Uu]*[Ii]','ki',txt)	#G
	txt=re.sub(r'G[Ee]','Ke',txt)	#G
	txt=re.sub(r'g[Ee]','ke',txt)	#G
	txt=re.sub(r'G[Üü]','W',txt)	
	txt=re.sub(r'gü','w',txt)
	txt=re.sub(r'G[Uu](?=[aoAO])','W',txt)
	txt=re.sub(r'g[u](?=[aoAO])','w',txt)
	txt=re.sub(r'[^cC][H][Uu]','W',txt)#H
	txt=re.sub(r'[^cC][h][Uu]','W',txt)#H
	txt=re.sub(r'[^Cc]H[aeioAEIO]','',txt)#H
	txt=re.sub(r'[^Cc]h[aeioAEIO]','',txt)#H
	#txt=re.sub(r'','',txt)	#I
	txt=re.sub(r'J','K',txt)	#J
	txt=re.sub(r'j','k',txt)	#J
	#txt=re.sub(r'','',txt)	#K
	#txt=re.sub(r'','',txt)	#L
	#txt=re.sub(r'','',txt)	#LL
	#txt=re.sub(r'','',txt)	#M
	#txt=re.sub(r'','',txt)	#N
	#txt=re.sub(r'','',txt)	#Ñ
	#txt=re.sub(r'','',txt)	#O
	#txt=re.sub(r'','',txt)	#P
	txt=re.sub(r'Q[uU]','K',txt)#Q
	txt=re.sub(r'q[uU]','k',txt)#Q
	txt=re.sub(r'R[Rr]','R',txt)#R[RR]
	txt=re.sub(r'r[Rr]','r',txt)#R[RR]
	txt=re.sub(r'(?=[bcdfgkpv])[r]','ür',txt)
	txt=re.sub(r'(?<=[BCDFGKPVbcdfgkpv])r','ür',txt)
	txt=re.sub(r'[sS]\Z','',txt)#S
	txt=re.sub(r'[sS](?![a-zA-ZüÜáéíóúÁÉÍÓÚ])','',txt)#S
	#txt=re.sub(r'','',txt)	#T
	#txt=re.sub(r'','',txt)	#U
	txt=re.sub(r'V','F',txt)#V
	txt=re.sub(r'v','f',txt)#V
	#txt=re.sub(r'','',txt)	#W
	txt=re.sub(r'X','Ks',txt)#X
	txt=re.sub(r'x','ks',txt)#X
	#txt=re.sub(r'','',txt)	#Y
	txt=re.sub(r'Z','S',txt)#Z
	txt=re.sub(r'z','s',txt)#Z
	return txt
