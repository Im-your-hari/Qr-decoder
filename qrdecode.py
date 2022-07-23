import os
from pyzbar.pyzbar import decode
from PIL import Image
from breezypythongui import EasyFrame
from tkinter import *
from tkinter import filedialog

#logic___________
'''
img = Image.open(r"qreee.jpg")
l = decode(img)
l=str(l[0][0])
#print(l)

for i in l.split(";"):
	j = i.split(":")
	print(j[len(j)-1])
'''

#gui____________
class Main(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(
			self,
			title="Wifi-QR-Decoder",
			background="blue",
			width=200,
			height=100
		)
		self.wifi=self.addLabel(
				text="Wi-Fi",
				row=0,
				column=0,
				columnspan=2,
				sticky="NSWE"
			)
		self.browse=self.addButton(
				text="Browse",
				row=1,
				column=0,
				command=self.read
			)
		self.exit=self.addButton(
				text="Exit",
				row=1,
				column=1,
				command=lambda:exit()
			)
		
	def read(self):
			fln = filedialog.askopenfilename(
					initialdir=os.getcwd(),
					title="Select QR Code",
					filetypes=(
							("JPG files","*.jpg"),
							("PNG files","*.png"),
							("All files","*.*")
					)
				)
			print(fln)
			self.wifi["text"]=fln			





def abc():
	Main().mainloop()
if __name__ == "__main__":
	abc()