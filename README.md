# kukarsiserver
Python Server For KUKA Robot Sensor Interface (RSI)

KUKA Robot controller has inbuilt Ethernet port called KLI (KUKA LINE INTERFACE, Static IP) which is used for UDP/TCP IP connections from external system.

Real Time Axis/Cartesian Position corrections (Delta) can be acheived via KUKA Optional Technology Package called RSI.(Remote Sensor Interface)

Now, Here RSI installed on Controller will behave as UDP Client and External Computer/System should be Server.

#Setup Communication interface between KUKA Controller and PC by minimising HMI on KUKA Side:  Click Start >> RSI >> Create New IP. e.g: 192.168.100.100

Step 1: Use RSIVisual (Graphical XML/RSI Editor) supplied by KUKA to generate .XML and .RSI files.

Step 2: Copy all these (.RSI, .Diagram, .XML, Config.XML) files inside KUKA Controller under path: C:/KRC/Roboter/Config/User/Common/SensorInterface

Step 3: Start ServerApp.py on External Computer. (ServerApp.py Attached)

Step 4: Run RSI_Ethernet.src file on KUKA Controller. (This src is supplied by KUKA RSI — Example Folder)

Step 5: Post Connection is established with Controller, Run GUI.py to Control Axis 1 to Axis 6 in Real Time.

Enjoy!

Thanks.
