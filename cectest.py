#!/usr/bin/env python

import time
import cec

adapters = cec.list_adapters()

if len(adapters) > 0:
   adapter = adapters[0]
   cec.init(adapter)

   d = cec.Device(0)

   # d.standby()
   # d.power_on()


   d.set_av_input(01)

 # echo "tx 4F 82 10 00" | cec-client -s -d 1