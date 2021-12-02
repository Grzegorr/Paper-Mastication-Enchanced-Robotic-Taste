import serial
import numpy as np
import time

#Commands to Arduino:
#A - read Thermistor value
#B - read Conductance of the sample
#C - read the pH voltage


class UltimateProbe:

    def __init__(self):
        self.waitTime = 0.2 #How long to wait for the answer form arduino
        #self.no_samples = no_samples
        self.ser = serial.Serial(port='COM5', baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=10)
        line = self.ser.read_until() #workaround
        print("-------------Ultimate Probe Successfully Connected-------------\r\n")
        #default values for temperature sensor if you dont calibrate it
        self.B = 3889.6
        self.Rinf = 0.1799288

    def readPHvoltage(self):
        self.ser.flushOutput()
        self.ser.flushInput()
        self.ser.write(str.encode("C"))
        time.sleep(self.waitTime)
        line = self.ser.read_until()
        string = ""
        for i in line:
            j = chr(int(i))
            string = string + j
        # print("---" + string + "---")
        # print(string[:-1])
        value = int(string[:-1])
        voltage = 3.3 * value / 1023
        #print(voltage)
        return voltage

    def readPH(self):
        voltage = self.readPHvoltage()
        PH = 7.0 - (voltage - 1.08)/ 0.046
        print(PH)
        return PH

    def readTemperature(self):
        resistance = self.readThermistorValue()
        T = self.computeTemperature(resistance)
        return T

    def computeTemperature(self, resistance):
        T = self.B / np.log(resistance / self.Rinf)
        T = T - 273.0
        return T


    def readThermistorValue(self):
        self.ser.flushOutput()
        self.ser.flushInput()
        self.ser.write(str.encode("A"))
        time.sleep(self.waitTime)
        line = self.ser.read_until()
        string = ""
        for i in line:
            j = chr(int(i))
            string = string + j
        #print("---" + string + "---")
        #print(string[:-1])
        value = int(string[:-1])
        print(value)
        return value

    def calibrate_thermistor(self):
        print("Current temperature please[C]:")
        T1 = input()
        T1 = float(T1)
        T1 = T1 + 273 #Conversion to Kelvin
        R1 = self.readThermistorValue()
        print("Now change the temperature, and enter it in[C]:")
        T2 = input()
        T2 = float(T2)
        T2 = T2 + 273  # Conversion to Kelvin
        R2 = self.readThermistorValue()

        #Testing without the probe only
        R2 = 50000.0
        T2 = 273.0 + 37.3
        R1 = 200000.0
        T1 = 273.0 + 6.4

        B = np.log(R1/R2)/((1/T1)-(1/T2))
        Rinf = R2 * np.exp(-B/T2)
        #print(Rinf)
        #Rinf = R2 * np.exp(B/T2)
        #print(Rinf)
        print("B:" + str(B))
        print("Rinf:" + str(Rinf))

        #R = Rinf * np.exp(-B/T1)
        #print(R)
        #R = Rinf * np.exp(-B/T2)
        #print(R)
        #R = Rinf * np.exp(-B/(0.5*(T1+T2)))
        #print(R)
        #R = Rinf * np.exp(-B / 3730)
        #print(R)
        self.B = B
        self.Rinf = Rinf
        return B, Rinf

    def readConductance(self):
        self.ser.flushOutput()
        self.ser.flushInput()
        self.ser.write(str.encode("B"))
        time.sleep(self.waitTime)
        line = self.ser.read_until()
        string = ""
        for i in line:
            j = chr(int(i))
            string = string + j
        value = int(string[:-1])
        print(value)
        return value

    def tuneConductanceSensore(self):
        print("Current sample Conductance[uS]:")
        G = input()
        G = float(G)
        G_measured = self.readConductance()
        scaling = G_measured/G
        return scaling












if __name__ == '__main__':
    PROBE = UltimateProbe()
    while 1:
        PROBE.readPH()
    #PROBE.calibrate_thermistor()
    #print(PROBE.B)
    #print(PROBE.Rinf)
    #for i in range(20):
        #resistance = 10000 * i
        #T = PROBE.computeTemperature(resistance)
        #print()
        #print(resistance)
        #print(T)
        #PROBE.readConductance()
        #B, Rinf = PROBE.calibrate_thermistor()
        #print(B)
        #print(Rinf)

        #time.sleep(1)

