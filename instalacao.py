#!/usr/bin/python3
# coding: utf-8 -*-
from os import system

'''
Pós instalação do arch linux
'''

def banner():
	system('clear')
	print ("""
          \033[01;32m\t\t\t █████╗ ██████╗  ██████╗██╗  ██╗      ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
         \t\t\t██╔══██╗██╔══██╗██╔════╝██║  ██║      ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
         \t\t\t███████║██████╔╝██║     ███████║█████╗██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ 
         \t\t\t██╔══██║██╔══██╗██║     ██╔══██║╚════╝██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ 
         \t\t\t██║  ██║██║  ██║╚██████╗██║  ██║      ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
         \t\t\t╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝      ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝\033[01;37m""")
	print ('\t\t\t\t\t\t\t\t\t      :-}GRUPO WHITE HAT HACKERS ;-)')

def navegadoress():
	banner()
	print ('\033[01;34m\t\t\t\t\t\t############\033[01;37m')
	print ('\033[01;34m\t\t\t\t\t\tNAVEGADORES\033[01;37m')
	print ('\033[01;34m\t\t\t\t\t\t############\033[01;37m')
	listaNavegadores=['[1] FIREFOX','[2] CHROME','[3] CHROMIUM','[4] OPERA']
	for navegadores in listaNavegadores:
		print ("\n\t\t\t\t\t\t %s"%navegadores)
		listaNavegadores
	print ('\n\t\t\t\t\t\t QUAL NAVEGADOR DESEJA INSTALAR')
	escolha = int(input("\t\t\t\t\t\t ?.: "))

	if escolha == 1:
		print ('\n\t\t\t\t\t\tINSTALANDO FIREFOX')
		system('sudo pacman -S firefox')
	elif escolha ==2:
		print ('\n\t\t\t\t\t\tINSTALANDO CHROME')
		system('yaourt -S google-chrome')
	elif escolha == 3:
		print ('\n\t\t\t\t\t\tINSTALANDO CHROMIUM')
		system('sudo pacman -S chromium')
	elif escolha == 4:
		system('sudo pacman -S opera')
	else:
		navegadoress()
def touchpad():
	banner()
	print ('\033[01;34m\n\t\t\t\t\t\t############\033[01;37m')
	print ('\033[01;34m\t\t\t\t\t\t  TOUCHPAD\033[01;37m')
	print ('\033[01;34m\t\t\t\t\t\t############\033[01;37m')
	system('sudo pacman -S xf86-input-synaptics')
	banner()
	
def mensageirosIrcs():
	banner()
	print ('\033[01;34m\n\t\t\t\t\t\t\t####################\033[01;37m')
	print ("\033[01;34m\t\t\t\t\t\t\t MENSAGEIROS E IRC\033[01;37m")
	print ('\033[01;34m\t\t\t\t\t\t\t####################\033[01;37m')
	listaMensageiros=['[1] emesene','[2] amsn','[3] pidgin','[4] skype','[5] xchat','[6] weechat']
	for mensageiros in listaMensageiros:
		print ("\n\t\t\t\t\t\t\t\t%s"%mensageiros)

	print ('\n\t\t\t\t\t\t QUAL NAVEGADOR DESEJA INSTALAR')
	escolha = int(input("\t\t\t\t\t\t ?.: "))

	if escolha ==1:
		system('sudo pacman -S emesene')
	elif escolha ==2:
		system('sudo pacman -S amsn')
	elif escolha ==3 :
		system('sudo pacman -S pidgin')
	elif escolha ==4:
		system('yaourt -S skype')
	elif escolha== 5:
		system('sudo pacman -S xchat')
	elif escolha == 6:
		system('sudo pacman -S weechat')
	else:
		mensageirosIrcs()

def flashPlayer():
	banner()
	print ('\033[01;34m\n\t\t\t\t\t\t\t####################\033[01;37m')
	print("\033[01;34m\t\t\t\t\t\t\tPUGINS FLASH PLAYERS\033[01;37m")
	print ('\033[01;34m\t\t\t\t\t\t\t####################\033[01;37m')
	listaFlashPlayer=['[1] gnash-gtk','[2] flashplayer-plugin']
	for flashs in listaFlashPlayer:
		print ("\n\t\t\t\t\t\t\t%s"%flashs)

	print ('\n\t\t\t\t\t\t QUAL NAVEGADOR DESEJA INSTALAR')
	escolha = int(input("\t\t\t\t\t\t ?.: "))

	if escolha ==1:
		system('sudo pacman -S gnash-gtk')
	elif escolha ==2:
		system('sudo pacman -S flashplayer-plugin')
	else:
		flashPlayer()
def codecss():
	banner()
	print ('\033[01;34m\n\t\t\t\t\t\t\t####################\033[01;37m')
	print ("\033[01;34m\t\t\t\t\t\t\t\tCODECS\033[01;37m ")
	print ('\033[01;34m\t\t\t\t\t\t\t####################\033[01;37m')
	listaCodecs=['[1] gstreamer','[2] xine']
	for codecs in listaCodecs:
		print ("\n\t\t\t\t\t\t\t%s"%codecs)
	print ('\n\t\t\t\t\t\t QUAL NAVEGADOR DESEJA INSTALAR')
	escolha = int(input("\t\t\t\t\t\t ?.: "))

	if escolha ==1:
		system('sudo pacman -S gstreamer0.10-bad gstreamer0.10-bad-plugins gstreamer0.10-base gstreamer0.10-base-plugins gstreamer0.10-ffmpeg gstreamer0.10-good gstreamer0.10-good-plugins gstreamer0.10-ugly gstreamer0.10-ugly-plugins libcanberra-gstreamer gstreamermm perl-gstreamer')
	elif escolha ==2:
		system('sudo pacman -S xine-lib libquicktime lame lsdvd libdvbpsi libstdc++5 libdvdread libdvdnav libdvdcss gecko-mediaplayer')		
	else:
		codecss()
def multimidia():
	banner()
	print ('\033[01;34m\n\t\t\t\t\t\t\t####################\033[01;37m')
	print ("\033[01;34m\t\t\t\t\t\t\t      MULTIMiDIA\033[01;37m")
	print ('\033[01;34m\t\t\t\t\t\t\t####################\033[01;37m')
	listaMultimidia=['[1] smplayer','[2] amaroc','[3] vlc']
	for mult in listaMultimidia:
		print ("\n\t\t\t\t\t\t\t %s"%mult)
	print ('\n\t\t\t\t\t\t QUAL NAVEGADOR DESEJA INSTALAR')
	escolha = int(input("\t\t\t\t\t\t ?.: "))
	if escolha ==1:
		system('sudo pacman -S smplayer')
	elif escolha ==2:
		system('sudo pacman -S amaroc')
	elif escolha ==3:
		system('sudo pacman -S vlc')
	else:
		multimidia()
def webcan():
	banner()
	print ('\033[01;34m\n\t\t\t\t\t\t\t####################\033[01;37m')
	print ("\033[01;34m\t\t\t\t\t\t\t       WEBCAN\033[01;37m")
	print ('\033[01;34m\t\t\t\t\t\t\t####################\033[01;37m')
	system('sudo pacman -S cheese')
	banner()
	
def interfaces_graficas():
	banner()
	print ('\033[01;34m\n\t\t\t\t\t\t\t####################\033[01;37m')
	print ("\033[01;34m\t\t\t\t\t\t\t INTERFACES GRAFICAS\033[01;37m")
	print ('\033[01;34m\t\t\t\t\t\t\t####################\033[01;37m')
	listaInterfaceGrafica=['[1] xfce4','[2] gnome']
	for interfacesG in listaInterfaceGrafica:
		print ("\n\t\t\t\t\t\t\t%s"%interfacesG)
	print ('\n\t\t\t\t\t\t QUAL NAVEGADOR DESEJA INSTALAR')
	escolha = int(input("\t\t\t\t\t\t ?.: "))

	if escolha ==1:
		system('sudo pacman -S xfce4 xfce4-goodies')
	elif escolha ==2:
		system('sudo pacman -S gnome-packagekit gnome-settings-daemon-updates')
	else:
		interfaces_graficas()

def desenvolvimento():
	banner()
	print ('\033[01;34m\n\t\t\t\t\t\t\t####################\033[01;37m')
	print ("\033[01;34m\t\t\t\t\t\t\t DESENVOLVIMENTO\033[01;37m")
	print ('\033[01;34m\t\t\t\t\t\t\t####################\033[01;37m')
	listaDesenvolvimento=['[1] eclipse','[2] netbeans','[3] codeblocks','[4] geany e plugins']
	for desenvolvimentos in listaDesenvolvimento:
		print ("\n\t\t\t\t\t\t\t %s"%desenvolvimentos)

	print ('\n\t\t\t\t\t\t QUAL NAVEGADOR DESEJA INSTALAR')
	escolha = int(input("\t\t\t\t\t\t ?.: "))

	if escolha ==1:
		system('sudo pacman -S eclipse')
	elif escolha ==2:
		system('sudo pacman -S netbeans')
	elif escolha ==3:
		system('sudo pacman -S codeblocks')
	elif escolha ==4:
		system('sudo pacman -S geany-plugins')
	else:
		desenvolvimento()
def funcaoMain():
	
	try:
		banner()
		print ("\033[01;34m\t\t\t\t******************************************************************************\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[1]>NAVEGADORES \t\t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[2]>TOUCHPAD \t\t\t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[3]>MENSAGEIROS \t\t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[4]>PLUGINS FLASH PLAYERS \t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[5]>CODECS \t\t\t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[6]>MULTIMIDIA \t\t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[7]>WEBCAN \t\t\t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[8]>INTERFACES GRAFICAS \t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[9]>DESENVOLVIMENTO \t\t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t*[10]>EXIT(SAIR) \t\t\t\t\t\t\t     *\033[01;37m")
		print ("\033[01;34m\t\t\t\t******************************************************************************\033[01;37m")

		instalacao=int(input("\t\t\t\tESCOLHA UMA DAS OPÇÕES ACIMA.: ")) 
		if instalacao == 1:
			navegadoress()
			funcaoMain()
		elif instalacao == 2:
			touchpad()
			funcaoMain()
		elif instalacao == 3:
			mensageirosIrcs()
			funcaoMain()
		elif instalacao == 4:
			flashPlayer()
			funcaoMain()
		elif instalacao == 5:
			codecss()
			funcaoMain()
		elif instalacao == 6:
			multimidia()
			funcaoMain()
		elif instalacao == 7:
			webcan()
			funcaoMain()
		elif instalacao == 8:
			interfaces_graficas()
			funcaoMain()
		elif instalacao == 9:
			desenvolvimento()
			funcaoMain()
		elif instalacao == 10:
			print ("\n\t\t\t\t\t\t******************************************")
			print ('\t\t\t\t\t\tScript Criado Por @utor:davidToreli\n\t\t\t\t\t\t@mail:davidjrtoreli@gmail.com')
			print ("\t\t\t\t\t\t******************************************")
			system('exit')

	except KeyboardInterrupt:
		
		print ("\n\t\t\t\t\t\t\t VOCÊ PRESSIONOU CTRL+C")
		
	
funcaoMain()
