import RPi.GPIO as GPIO
import time
import sys

class sr:
  def __init__(self, p, t, nl):
    self.p = p
    self.t = t
    self.nl = nl

  def inisialisasi(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      GPIO.setup(int(self.p[0]), GPIO.OUT)
      GPIO.setup(int(self.p[1]), GPIO.OUT)
      GPIO.setup(int(self.p[2]), GPIO.OUT)

  def digit(self):
      for y in range(8):
        n = '0' * y + '1' + '0' * (7 - y)
        self.t.append(n)

  def proses(self):
      GPIO.output(int(self.p[1]), 0)
      for x in range(1, len(self.t) + 1):
        num = self.t[x-1]
        GPIO.output(int(self.p[0]), int(num[x-1]))
        GPIO.output(int(self.p[2]), 1)
        GPIO.output(int(self.p[2]), 0)

        time.sleep(2)
        GPIO.output(int(self.p[1]), 1)
        print(f"\nSilahkan cek output pin Q{x-1} shift register\nDigit: {num}\n")
        
      GPIO.output(int(self.p[0]), 0)
      GPIO.output(int(self.p[2]), 1)
      GPIO.output(int(self.p[2]), 0)

  def default(self):
    try:
      print(f"\nPin Default\n  Data: {self.p[0]}\n  Latch: {self.p[1]}\n  Clock: {self.p[2]}\n")
      self.inisialisasi()
      self.digit()
      self.proses()
      time.sleep(2)
      GPIO.output(int(self.p[1]), 1)
      print(f"\nMengembalikan semua nilai shift register\nDigit: {self.nl}\n")
      GPIO.cleanup()

    except KeyboardInterrupt:
      GPIO.cleanup()
      print("\nProgram Close ya\n")

  def custom(self):
    try:
      print(f"\nPin Custom\n  Data: {self.p[0]}\n  Latch: {self.p[1]}\n  Clock: {self.p[2]}\n")
      self.inisialisasi()
      self.digit()
      self.proses()
      time.sleep(2)
      GPIO.output(int(self.p[1]), 1)
      print(f"\nMengembalikan semua nilai shift register\nDigit: {self.nl}\n")
      GPIO.cleanup()

    except KeyboardInterrupt:
      GPIO.cleanup()
      print("\nProgram Close ya\n")


if __name__ == "__main__":
  tes = []
  nul = '0' * 8
  if len(sys.argv) == 4:
    newpin = sys.argv[-3:]
    run = sr(newpin, tes, null)
    run.custom()
  elif len(sys.argv) == 1:
    pins = [16, 12, 5]
    run = sr(pins, tes, null)
    run.default()
  elif len(sys.argv) == 2 and ((sys.argv[1] == "-h") or (sys.argv[1] == "--help")):
    print("\nSHIFT REGISTER for 74HC595\n\nInfo:\n  Data - isikan pin data\n  Latch - isikan pin latch\n  Clock - isikan pin clock\n\nPenggunaan:\n  Default:\n    python.exe shiftReg.py\n\n  Custom:\n    python.exe shiftReg.py [data] [latch] [clock]\n")
  else:
    print("\nUntuk bantuan:\n  python.exe shiftReg.py -h\n")
