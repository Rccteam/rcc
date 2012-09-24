# -*- coding: utf-8 -*-

import curses,os 
screen = curses.initscr() 
curses.noecho() 
curses.cbreak() 
curses.start_color() 
screen.keypad(1) 

curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)

getin = None 
sub1get = None 
sub2get = None
sub3get = None
environmentmenu = None
env1get = None
environmentsubusersetmenu = None
hardwaremenu = None
hardwarenetmenu = None
hardkeysetup = None
hardsoundsetup = None
hardstoragesetup = None
hardfinehwtuning = None
statsmenu = None
softwaremenu = None


# The Raspberry-PI Control Center (RCC) Top Menu #
def topmenu():

  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)

  pos=1 
  x = None 
  h = curses.color_pair(1) #h is the coloring for a highlighted menu option
  n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
  
  while x !=ord('\n'):
    screen.clear() 
    screen.border(0)
    screen.addstr(0,18, "Welcome The Raspberry-PI Control Center (RCC)", curses.A_STANDOUT) # Title for this menu
    screen.addstr(4,2, "Please select an option...", curses.A_BOLD) #Subtitle for this menu

    if pos==1:
      screen.addstr(5,4, "1 - Basic Setup", h)
    else:
      screen.addstr(5,4, "1 - Basic Setup", n)
    if pos==2:
      screen.addstr(6,4, "2 - Advanced Tune and Setup", h)
    else:
      screen.addstr(6,4, "2 - Advanced Tune and Setup", n)
    if pos==3:
      screen.addstr(7,4, "3 - Board and Sys Information", h)
    else:
      screen.addstr(7,4, "3 - Board and Sys Information", n)
    if pos==4:
      screen.addstr(8,4, "4 - Exit", h)
    else:
      screen.addstr(8,4, "4 - Exit", n)
    screen.refresh()
    x = screen.getch() # Gets user input

    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == 258:
      if pos < 4:

	pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
	  pos += -1
	  
      else: pos = 4
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))
# The Raspberry-PI Control Center (RCC)/Basic Setup #
def submenu1():
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)
  pos=1
  x = None
  h = curses.color_pair(1)
  n = curses.A_NORMAL
  while x !=ord('\n'):
    screen.clear()
    screen.border(0)
    screen.addstr(2,2, "The Raspberry-PI Control Center (RCC)/Basic Setup", curses.A_STANDOUT)
    screen.addstr(4,2, "Please select an option...", curses.A_BOLD)

    #Detect what is higlighted
    if pos==1:
      screen.addstr(5,4, "1 - Enviroment", h)
    else:
      screen.addstr(5,4, "1 - Enviroment", n)
    if pos==2:
      screen.addstr(6,4, "2 - Hardware", h)
    else:
      screen.addstr(6,4, "2 - Hardware", n)
    if pos==3:
      screen.addstr(7,4, "3 - Software Management", h)
    else:
      screen.addstr(7,4, "3 - Software Management", n)
    if pos==4:
      screen.addstr(8,4, "4 - Hardinfo (CPU Benchmarks)", h)
    else:
      screen.addstr(8,4, "4 - Hardinfo (CPU Benchmarks)", n)
    if pos==5:
      screen.addstr(9,4, "5 - Configure Repository Sources", h)
    else:
      screen.addstr(9,4, "5 - Configure Repository Sources", n)
    if pos==6:
      screen.addstr(10,4, "6 - Dmesg Log", h)
    else:
      screen.addstr(10,4, "6 - Dmesg Log", n)
    if pos==7:
      screen.addstr(11,4, "7 - Preconfigured compilations", h)
    else:
      screen.addstr(11,4, "7 - Preconfigured compilations", n)
    if pos==8:
      screen.addstr(12,4, "8 - Return to Top Menu", h)
    else:
      screen.addstr(12,4, "8 - Return to Top Menu", n)
    screen.refresh()
    x = screen.getch()

    # What is user input?
    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == ord('5'):
      pos = 5
    elif x == ord('6'):
      pos = 6
    elif x == ord('7'):
      pos = 7
    elif x == ord('8'):
      pos = 8
    elif x == 258:
      if pos < 8:
	pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
	  pos += -1
      else: pos = 8
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))
# The Raspberry-PI Control Center (RCC)/ Advanced Tune and Setup #
def submenu2():
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)
  pos=2
  x = None
  h = curses.color_pair(1)
  n = curses.A_NORMAL
  while x !=ord('\n'):
    screen.clear()
    screen.border(0)
    screen.addstr(2,2, "The Raspberry-PI Control Center (RCC)/ Advanced Tune and Setup", curses.A_STANDOUT)
    screen.addstr(4,2, "Please select an option...", curses.A_BOLD)

    #Detect what is higlighted
    if pos==1:
      screen.addstr(5,4, "1 - GPIO PIN setup and development", h)
    else:
      screen.addstr(5,4, "1 - GPIO PIN setup and development", n)
    if pos==2:
      screen.addstr(6,4, "2 - MPI Cluster Build and Install", h)
    else:
      screen.addstr(6,4, "2 - MPI Cluster Build and Install", n)
    if pos==3:
      screen.addstr(7,4, "3 - Install Zram (RAM content compression - expanding to 512 MB)", h)
    else:
      screen.addstr(7,4, "3 - Install Zram (RAM content compression - expanding to 512 MB)", n)
    if pos==4:
      screen.addstr(8,4, "4 - Expand Swap Size (512MB)", h)
    else:
      screen.addstr(8,4, "4 - Expand Swap Size (512MB)", n)
    if pos==5:
      screen.addstr(9,4, "5 - Boot and MultiBoot setting configuration", h)
    else:
      screen.addstr(9,4, "5 - Boot and MultiBoot setting configuration", n)
    if pos==6:
      screen.addstr(10,4, "6 - Return to Top Menu", h)
    else:
      screen.addstr(10,4, "6 - Return to Top Menu", n)
    screen.refresh()
    x = screen.getch()

    # What is user input?
    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == ord('5'):
      pos = 5
    elif x == ord('6'):
      pos = 6
    elif x == 258:
    

      if pos < 6:


	pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
	  pos += -1

      else: pos = 6
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))
# The Raspberry-PI Control Center (RCC)/ Board and Sys Information #
def submenu3():
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)
  pos=1
  x = None
  h = curses.color_pair(1)
  n = curses.A_NORMAL
  while x !=ord('\n'):
    screen.clear()
    screen.border(0)
    screen.addstr(2,2, "The Raspberry-PI Control Center (RCC)/ Board and Sys Information", curses.A_STANDOUT)
    screen.addstr(4,2, "Please select an option...", curses.A_BOLD)

    #Detect what is higlighted
    if pos==1:
      screen.addstr(5,4, "1 - Current date, NTP status (online), last sync time", h)
    else:
      screen.addstr(5,4, "1 - Current date, NTP status (online), last sync time", n)
    if pos==2:
      screen.addstr(6,4, "2 - General Board status", h)
    else:
      screen.addstr(6,4, "2 - General Board status", n)
    if pos==3:
      screen.addstr(7,4, "3 - Chipset and Proc Info", h)
    else:
      screen.addstr(7,4, "3 - Chipset and Proc Info", n)
    if pos==4:
      screen.addstr(8,4, "4 - Current CPU Speed", h)
    else:
      screen.addstr(8,4, "4 - Current CPU Speed", n)
    if pos==5:
      screen.addstr(9,4, "5 - Installed RAM / Free RAM", h)
    else:
      screen.addstr(9,4, "5 - Installed RAM / Free RAM", n)
    if pos==6:
      screen.addstr(10,4, "6 - GPIO PIN info ONLINE/OFFLINE", h)
    else:
      screen.addstr(10,4, "6 - GPIO PIN info ONLINE/OFFLINE", n)
    if pos==7:
      screen.addstr(11,4, "7 - Network Status (ETH, WIFI)", h)
    else:
      screen.addstr(11,4, "7 - Network Status (ETH, WIFI)", n)
    if pos==8:
      screen.addstr(12,4, "8 - USB info (Voltage, stats)", h)
    else:
      screen.addstr(12,4, "8 - USB info (Voltage, stats)", n)
    if pos==9:
      screen.addstr(13,4, "9 - Return to Top Menu", h)
    else:
      screen.addstr(13,4, "9 - Return to Top Menu", n)
    screen.refresh()
    x = screen.getch()

    # What is user input?
    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == ord('5'):
      pos = 5
    elif x == ord('6'):
      pos = 6
    elif x == ord('7'):
      pos = 7
    elif x == ord('8'):
      pos = 8
    elif x == ord('9'):
      pos = 9	
    elif x == 258:
    

      if pos < 9:


	pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
	  pos += -1

      else: pos = 9
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))
# Basic Setup /Environment Menu #
def environmentmenu():
	
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)

  pos=1
  x = None 
  h = curses.color_pair(1) #h is the coloring for a highlighted menu option
  n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
  
  while x !=ord('\n'):
    screen.clear() 
    screen.border(0)
    screen.addstr(0,18, "The Raspberry-PI Control Center (RCC)", curses.A_STANDOUT) # Title
    screen.addstr(4,2, "Basic Setup / Environment Menu", curses.A_STANDOUT)
	
    if pos==1:
      screen.addstr(5,4, "1 - Time Sync", h)
    else:
      screen.addstr(5,4, "1 - Time Sync", n)
    if pos==2:
      screen.addstr(6,4, "2 - Language Setting", h)
    else:
      screen.addstr(6,4, "2 - Language Setting", n)
    if pos==3:
      screen.addstr(7,4, "3 - Locale Setup", h)
    else:
      screen.addstr(7,4, "3 - Locale Setup", n)
    if pos==4:
      screen.addstr(8,4, "4 - Console Setup", h)
    else:
      screen.addstr(8,4, "4 - Console Setup", n)
    if pos==5:
      screen.addstr(9,4, "5 - Check Updates", h)
    else:
      screen.addstr(9,4, "5 - Check Updates", n)
    if pos==6:
      screen.addstr(10,4, "6 - Add User and Group", h)
    else:
      screen.addstr(10,4, "6 - Add User and Group", n)
    if pos==7:
      screen.addstr(11,4, "7 - Return to the Basic Setup Menu", h)
    else:
      screen.addstr(11,4, "7 - Return to the Basic Setup Menu", n)      
    screen.refresh()
    x = screen.getch() # Gets user input

    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == ord('5'):
      pos = 5
    elif x == ord('6'):
      pos = 6
    elif x == ord('7'):
      pos = 7
    elif x == 258:
      if pos < 7:

	pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
	  pos += -1
	  
      else: pos = 7
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))
# Basic Setup / Hardware #
def hardwaremenu():
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)

  pos=1
  x = None 
  h = curses.color_pair(1) #h is the coloring for a highlighted menu option
  n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
  
  while x !=ord('\n'):
    screen.clear() 
    screen.border(0)
    screen.addstr(0,18, "The Raspberry-PI Control Center (RCC)", curses.A_STANDOUT) # Title
    screen.addstr(4,2, "Basic Setup / Hardware Menu", curses.A_STANDOUT)
	
    if pos==1:
      screen.addstr(5,4, "1 - Keyboard Setting", h)
    else:
      screen.addstr(5,4, "1 - Keyboard Setting", n)
    if pos==2:
      screen.addstr(6,4, "2 - Network Setup", h)
    else:
      screen.addstr(6,4, "2 - Network Setup", n)
    if pos==3:
      screen.addstr(7,4, "3 - Sound Setup", h)
    else:
      screen.addstr(7,4, "3 - Sound Setup", n)
    if pos==4:
      screen.addstr(8,4, "4 - Return to the menu", h)
    else:
      screen.addstr(8,4, "4 - Return to the menu", n)
    screen.refresh()
    x = screen.getch() # Gets user input

    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == 258:
      if pos < 4:

	pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
	  pos += -1
	  
      else: pos = 4
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))
# Hardware Menu / Network Menu
def hardwarenetmenu():
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)
  pos=1
  x = None 
  h = curses.color_pair(1) #h is the coloring for a highlighted menu option
  n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
  while x !=ord('\n'):
    screen.clear() 
    screen.border(0)
    screen.addstr(0,18, "The Raspberry-PI Control Center (RCC)", curses.A_STANDOUT) # Title
    screen.addstr(4,2, "Environment / Network Menu", curses.A_STANDOUT)
	
    if pos==1:
      screen.addstr(5,4, "1 - Network Service Information", h)
    else:
      screen.addstr(5,4, "1 - Network Service Information", n)
    if pos==2:
      screen.addstr(6,4, "2 - Wireless Connection Status", h)
    else:
      screen.addstr(6,4, "2 - Wireless Connection Status", n)
    if pos==3:
      screen.addstr(7,4, "3 - Ethernet Connection Status", h)
    else:
      screen.addstr(7,4, "3 - Ethernet Connection Status", n)
    if pos==4:
      screen.addstr(8,4, "4 - Return to the menu", h)
    else:
      screen.addstr(8,4, "4 - Return to the menu", n)
    screen.refresh()
    x = screen.getch() # Gets user input

    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == 258:
      if pos < 4:

	pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
	  pos += -1
	  
      else: pos = 4
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))


# All top and sub menu command part #	
while getin != ord('4'):
  sub1get = None 
  sub2get = None
  sub3get = None
  env1get = None
  hardware1get = None
  hw1net = None
  getin = topmenu() 
  
  if getin == ord('1'): # Topmenu option 1,
    while sub1get !=ord('8'): 
      sub1get = submenu1() # ------Submenu 1 Commands------#
      
      if sub1get == ord('1'): #Submenu 1 option 1
	while env1get !=ord('7'):
	  env1get = environmentmenu()
      if env1get == ord('1'): # Envmenu 1 option 1
	()
      elif env1get == ord('2'): # Envmenu 1 option 2
	()
      elif env1get == ord('3'): # Envmenu 1 option 3
	()
      elif env1get == ord('4'): # Envmenu 1 option 4
	()
      elif env1get == ord('5'): # Envmenu 1 option 5
	()
      elif env1get == ord('6'): # Envmenu 1 option 6
	()
      elif env1get == ord('7'): # Envmenu 1 option 7
	os.system('')
	
      elif sub1get == ord('2'): # Submenu 1 option 2
	while hardware1get !=ord('4'):
	  hardware1get = hardwaremenu()
      if hardware1get == ord('1'): # hardware1get 1 option 1
	()
      elif hardware1get == ord('2'): # hardware1get 1 option 2
  #----------------------------------------------------------
	while hw1net !=ord('4'):
	  hw1net = hardwarenetmenu()
      if hw1net == ord('1'): # hardnetsetup 1 option 1
	()
      elif hw1net == ord('2'): # hardnetsetup 1 option 2
	()
      elif hw1net == ord('3'): # hardnetsetup 1 option 3
	()
      elif hw1net == ord('4'): # hardnetsetup 1 option 4
	os.system('')
	
      elif hardware1get == ord('3'): # hardware1get 1 option 3
	()
      elif hardware1get == ord('4'): # hardware1get 1 option 4
	os.system('')
	
      elif sub1get == ord('3'): # Submenu 1 option 3
	()
      elif sub1get == ord('4'): # Submenu 1 option 4
	()
      elif sub1get == ord('5'): # Submenu 1 option 5
	()
      elif sub1get == ord('6'): # Submenu 1 option 6
	()
      elif sub1get == ord('7'): # Submenu 1 option 7
	()
      elif sub1get == ord('8'): # Submenu 1 option 8
	os.system('')
	
  elif getin == ord('2'): # Topmenu option 2,
    while sub2get !=ord('6'):
      sub2get = submenu2() # ------Submenu 2 Commands------#
      if sub2get == ord('1'): #Submenu 2 option 1
	() 
      elif sub2get == ord('2'): # Submenu 2 option 2
	()
      elif sub2get == ord('3'): # Submenu 2 option 3
	()
      elif sub2get == ord('4'): # Submenu 2 option 4
	()
      elif sub2get == ord('5'): # Submenu 2 option 5
	()
      elif sub2get == ord('6'): # Submenu 2 option 6
	os.system('')
	#os.system('uqm')

  elif getin == ord('3'): # Topmenu option 3
    while sub3get !=ord('9'):
      sub3get = submenu3()  # ------Submenu 3 Commands------#
      if sub3get == ord('1'): #Submenu 3 option 1
	() 
      elif sub3get == ord('2'): #Submenu 3 option 2
	()
      elif sub3get == ord('3'): #Submenu 3 option 3
	()
      elif sub3get == ord('4'): #Submenu 3 option 4
	()
      elif sub3get == ord('5'): #Submenu 3 option 5
	()
      elif sub3get == ord('6'): #Submenu 3 option 6
	()
      elif sub3get == ord('7'): #Submenu 3 option 7
	()
      elif sub3get == ord('8'): #Submenu 3 option 8
	()
      elif sub3get == ord('9'): # Submenu 3 option 9 (Exits to top menu at this point)
	os.system('')
	#os.system('uqm')
    
  elif getin == ord('4'): # Topmenu option 4
    curses.endwin()
    os.system('clear') # Clears the screen so you're left looking at a nice neat bash prompt instead of the left over window
