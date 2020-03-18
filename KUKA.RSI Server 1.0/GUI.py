from tkinter import *
import xml.etree.cElementTree as ET



window = Tk()

window.title("PawankumarG.com/KUKARSIServer")

window.geometry('600x600')

delta = "0.01" # Jogging speed


axis1 = Label(window, text="Axis 1")
axis2 = Label(window, text="Axis 2")
axis3 = Label(window, text="Axis 3")
axis4 = Label(window, text="Axis 4")
axis5 = Label(window, text="Axis 5")
axis6 = Label(window, text="Axis 6")


axis1.grid(column=0, row=0)
axis2.grid(column=0, row=1)
axis3.grid(column=0, row=2)
axis4.grid(column=0, row=3)
axis5.grid(column=0, row=4)
axis6.grid(column=0, row=5)



def clicked1p():
    
    print("axis 1 plus")
    delta = txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = delta
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "1"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")
    
def clicked2p():

    print("axis 2 plus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = delta
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "1"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")
def clicked3p():

    print("axis 3 plus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = delta
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "1"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")
    
def clicked4p():

    print("axis 4 plus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = delta
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "1"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")    
    
def clicked5p():

    print("axis 5 plus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = delta
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "1"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")    
    
def clicked6p():

    print("axis 6 plus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = delta
    ET.SubElement(root, "Direction").text = "1"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")    
###    
def clicked1n():

    print("axis 1 minus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = delta
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "0"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")
    
def clicked2n():

    print("axis 2 minus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = delta
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "0"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")
def clicked3n():

    print("axis 3 minus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = delta
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "0"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")
    
def clicked4n():

    print("axis 4 minus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = delta
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "0"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")    
    
def clicked5n():

    print("axis 5 minus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = delta
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "0"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")    
    
def clicked6n():

    print("axis 6 minus")
    delta =  txtfld.get()
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "0"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml")     

def ClickstartRobot():
    print("Stoping Robot")
    root = ET.Element("root")
    ET.SubElement(root, "Axis1").text = "0.0"
    ET.SubElement(root, "Axis2").text = "0.0"
    ET.SubElement(root, "Axis3").text = "0.0"
    ET.SubElement(root, "Axis4").text = "0.0"
    ET.SubElement(root, "Axis5").text = "0.0"
    ET.SubElement(root, "Axis6").text = "0.0"
    ET.SubElement(root, "Direction").text = "0"
    tree = ET.ElementTree(root)
    tree.write("axiscorr.xml") 
    
    
    

    
    
    
    
startRobot = Button(window, text="Stop Robot Movement", command=ClickstartRobot)  
inc = Label(window, text="Stop Robot Movement")         

axis1p = Button(window, text="Positive", command=clicked1p)
axis2p = Button(window, text="Positive", command=clicked2p)
axis3p = Button(window, text="Positive", command=clicked3p)
axis4p = Button(window, text="Positive", command=clicked4p)
axis5p = Button(window, text="Positive", command=clicked5p)
axis6p = Button(window, text="Positive", command=clicked6p)

axis1n = Button(window, text="Negative", command=clicked1n)
axis2n = Button(window, text="Negative", command=clicked2n)
axis3n = Button(window, text="Negative", command=clicked3n)
axis4n = Button(window, text="Negative", command=clicked4n)
axis5n = Button(window, text="Negative", command=clicked5n)
axis6n = Button(window, text="Negative", command=clicked6n)

txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.insert(END, '0.001')
startRobot.grid(column=5, row=3)
txtfld.grid(column=6, row=3)
axis1p.grid(column=1, row=0)
axis2p.grid(column=1, row=1)
axis3p.grid(column=1, row=2)
axis4p.grid(column=1, row=3)
axis5p.grid(column=1, row=4)
axis6p.grid(column=1, row=5)
axis1n.grid(column=2, row=0)
axis2n.grid(column=2, row=1)
axis3n.grid(column=2, row=2)
axis4n.grid(column=2, row=3)
axis5n.grid(column=2, row=4)
axis6n.grid(column=2, row=5)





window.mainloop()