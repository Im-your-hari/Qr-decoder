import os
from pyzbar.pyzbar import decode
from PIL import Image as Im
from breezypythongui import EasyFrame
from tkinter import *
from tkinter import filedialog


#gui____________
class Main(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(
			self,
			title="Wifi-QR-Decoder",
			background="blue",
			width=200,
			height=200
		)
		self.wifi=self.addLabel(
				text="Wi-Fi QR Decoder",
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
			#self.wifi["text"]=fln
			img = Im.open(r"{0}".format(fln))
			l = decode(img)
			l=str(l[0][0])
			a=2
			titles = ["Name : ","Type : ","Key : ","Connection : ",]
			for i in l.split(";"):
				j = i.split(":")
				print(j[len(j)-1])
				#self.wifi["text"]=j[len(j)-1]
				a+=1
				if a<6:
					self.addLabel(text=titles[a-3],row=a,column=0,sticky="NSWE",background="blue")
					self.addTextField(text=j[len(j)-1],row=a,column=1,sticky="NSWE",state="disabled")





def abc():
	Main().mainloop()
if __name__ == "__main__":
	abc()