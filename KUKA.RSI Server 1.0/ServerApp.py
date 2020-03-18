import socket
import os
import time;
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET
import sys

localIP     = "192.168.100.111" ## Address of your Computer -- Same must be entered in RSI Config File

localPort   = 9508  ## Port on your computer

bufferSize  = 1024 ## No need to change

 


 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening for KUKA RSI !  - Set your Server Computer IP to 192.168.100.111 , Port : 9508 ")

 

# Listen for incoming datagrams

while(True):
    
    

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = format(message)
    
    clientIP  = "Client IP Address:{}".format(address)
    

    #print(clientMsg)
    
    
    receivedData = BeautifulSoup(message, 'html.parser')
    
    #print(receivedData)
    
    axis1_act = receivedData.a1.get_text()
    axis2_act = receivedData.a2.get_text()
    axis3_act = receivedData.a3.get_text()
    axis4_act = receivedData.a4.get_text()
    axis5_act = receivedData.a5.get_text()
    axis6_act = receivedData.a6.get_text()
    

    ## Write to XML Actual Position
    root = ET.Element("root")
   

    ET.SubElement(root, "Axis1").text = axis1_act
    ET.SubElement(root, "Axis2").text = axis2_act 
    ET.SubElement(root, "Axis3").text = axis3_act
    ET.SubElement(root, "Axis4").text = axis4_act
    ET.SubElement(root, "Axis5").text = axis5_act
    ET.SubElement(root, "Axis6").text = axis6_act
    
    tree = ET.ElementTree(root)
    tree.write("actualpos.xml")
    
 
##Corrections Read from XML axiscorr and apply the same
   
    
    
    
    tree1 = ET.parse('axiscorr.xml')
             
    axis1_corr = tree1.find('Axis1').text
    axis2_corr = tree1.find('Axis2').text
    axis3_corr = tree1.find('Axis3').text
    axis4_corr = tree1.find('Axis4').text
    axis5_corr = tree1.find('Axis5').text
    axis6_corr = tree1.find('Axis6').text
    direction = tree1.find('Direction').text

   

    
    
    if(direction=="0"):
                    axis1_corr = "-"+axis1_corr
                    axis2_corr = "-"+axis2_corr
                    axis3_corr = "-"+axis3_corr
                    axis4_corr = "-"+axis4_corr
                    axis5_corr = "-"+axis5_corr
                    axis6_corr = "-"+axis6_corr
                
                 
    
    
    
    ## Correction
    
    
    
    
    
    ##Sending XML to RSI Client
    
    reflectIPOC = '<Sen Type="ImFree"><EStr>Message from RSI Control Server - PPG !</EStr><AxisCorr A1="'+axis1_corr+'" A2="'+axis2_corr+'" A3="'+axis3_corr+'" A4="'+axis4_corr+'" A5="'+axis5_corr+'" A6="'+axis6_corr+'"><RKorr X="0.00001" Y="0.0000" Z="0.0000" A="0.0000" B="0.0000" C="0.0000" /><IPOC>'+receivedData.ipoc.getText()+'</IPOC></Sen>\n'
    print("Commandin with <IPOC>:"+receivedData.ipoc.getText()+", Axis Actual Pos: " + (axis1_act+","+axis2_act+","+axis3_act+","+axis4_act+","+axis5_act+","+axis6_act))
   
    bytesToSend = str.encode(reflectIPOC)
    UDPServerSocket.sendto(bytesToSend, address)
    
    



    
