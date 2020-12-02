import nmap
import csv
import sys
import tkinter 

def nmap():
	target = input("Enter the IP: ")
	scanner = nmap.PortScanner()

	for i in range(50, 120):
		res = scanner.scan(target, str(i))
		print(scanner.csv(),file=open("csv_lectures.csv", "w"))


window = tkinter.Tk()
window.geomtry("400x300")
window.configure(bg = "blue")
button = tkinter.Button(window, text = "Nmap.CSV", padx = 15, pady = 15, command = nmap, bg = "gray")
button.pack(expand = True)
window.mainloop()


