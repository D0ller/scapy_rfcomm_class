#!/usr/bin/python3
# -*- coding: utf-8 -*-

from rfcomm import *
from binascii import hexlify

def tests():

    pkt = RFCOMM_Frame(control="UIH",CR=1,rfcomm_payload=(MCC_Hdr()/MCC_PN(channel=12)))
    b  = pkt.build()
    print(hexlify(b))
    RFCOMM_Frame(b).show()

    pkt = RFCOMM_Frame(control="UIH",CR=0,rfcomm_payload=(MCC_Hdr()/MCC_MSC(channel=12)))
    b  = pkt.build()
    print(hexlify(b))
    RFCOMM_Frame(b).show()

    bind_layers(L2CAP_Hdr, RFCOMM_Frame, cid=0x40)
    
    pkt = L2CAP_Hdr(cid=0x40)/RFCOMM_Frame(control="SABM P/F",CR=1)
    b  = pkt.build()
    print(hexlify(b))
    L2CAP_Hdr(b).show()

    pkt = L2CAP_Hdr(cid=0x40)/RFCOMM_Frame(channel=10,control="UIH P/F",CR=0,rfcomm_payload=RFCOMM_Credit_Based_Payload(credits=1,data="AT+BRSF=702\r"))
    b  = pkt.build()
    print(hexlify(b))
    L2CAP_Hdr(b).show()

    pkt = L2CAP_Hdr(cid=0x40)/RFCOMM_Frame(channel=10,control="UIH",CR=1,rfcomm_payload=RFCOMM_Payload(data="A"))
    b  = pkt.build()
    print(hexlify(b))
    L2CAP_Hdr(b).show()

if __name__ == '__main__':
    tests()
