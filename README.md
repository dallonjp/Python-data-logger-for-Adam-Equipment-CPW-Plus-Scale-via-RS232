# Python-data-logger-for-Adam-Equipment-CPW-Plus-Scale-via-RS232
A simple python script and tutorial for logging weight data automatically over a serial RS232 interface

In order to use this file, a few software and hardware considerations should be made:
1. This script was written to log data from an Adam Equipment CPW Plus 15 Scale, but any of the CPW series scales should work
2. A RS232 to USB cable should be used to log the data on a PC. I used this one: https://www.amazon.com/gp/product/B0769DVQM1/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&th=1 (The chip for used in this cable is a PL2303, so a driver may need to be installed on your machine in order for it to recognize it and assign a COM port) It should also be noted that the RS232 interface is male on the scale so a female cable should be used.
3. I followed this manual: https://www.adamequipment.com/media/docs/Print%20Publications/Manuals/CPWplus_UM_USA.pdf, using section 8 to change the user parameters. Specifically, I set the parity to 7 bits odd (PAR 3) and continuous RS232 data output (TRN 2).
### These parameters MUST be changed in order for this script to work.
4. With the USB to RS232 cable connected to the PC and the proper COM port selected in the script, the script can be run to log the weight data vs time into a CSV file
