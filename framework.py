#!/usr/bin/env python3
import os
import argparse
import sys
import math
import time
import random
from tkinter import *
from PIL import Image, ImageTk

def main():
    master = Tk()
    height = round(master.winfo_screenheight()*0.9)
    # if None not in [args.x, args.y, args.magnification]:
    #     render = Framework(master, height, x=args.x, y=args.y, m=args.magnification, multi=args.noMulti,
    #                        iterations=args.iterations, imgWidth=args.width, imgHeight=args.height, save=args.save)
    # else:
    #     if not all(arg is None for arg in [args.x, args.y, args.magnification]):
    #         print("Arguments ignored. Please provide all of x, y, & m.")
    #     render = Framework(master, height, multi=args.noMulti, iterations=args.iterations,
    #                        imgWidth=args.width, imgHeight=args.height, save=args.save)
    # master.geometry("{}x{}".format(render.canvasW, render.canvasH))
    master.mainloop()


main()
