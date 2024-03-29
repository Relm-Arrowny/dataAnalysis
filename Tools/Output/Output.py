'''
Created on 16 Aug 2019

@author: wvx67826
'''
import matplotlib.pyplot as plt
from win32api import GetSystemMetrics
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage
class Output():
    def __init__(self):
        pass
    
    def draw_plot(self, x, lY, lYName, lYNameUse = None, lMeta = None, lMetaName=None, logY = False, blocking = False):
    
        if lYNameUse == None: lYNameUse = lYName
        myDpi = 100
        screenWidth = GetSystemMetrics(0)
        screenHeight = GetSystemMetrics(1)

        fig = plt.figure(figsize=(screenWidth/myDpi, screenHeight/myDpi), dpi=myDpi)
        if (lMetaName != None and lMeta != None):
            title = ""
            for i,j in enumerate (lMetaName):
                print(lMeta[i])
                title = title + "%s=%s" %(j.split("/")[-1], lMeta[i])
            plt.suptitle(title)
        
        noOfPlot = len(lYNameUse)
        for i, j in enumerate(lYNameUse):
            plt.subplot(round(noOfPlot/2.0),2, i +1)
            plt.title(j)
            lNameUsed = [k for k,checkName in enumerate(lYName) if checkName == j]
            for m,l in enumerate(lNameUsed):
                plt.plot(x[m] ,lY[l])
                if "xmcd" in j: 
                    pass 
                elif logY:
                    plt.semilogy()
        fig.tight_layout()
        plt.draw()
        fig =  plt.gcf()    
        plt.show(block = blocking)
        plt.close()
        return fig
    def add_clipboard_to_figures(self):
        # use monkey-patching to replace the original plt.figure() function with
        # our own, which supports clipboard-copying
        oldfig = plt.figure

        def newfig(*args, **kwargs):
            fig = oldfig(*args, **kwargs)
            
            def clipboard_handler(event):
                if event.key == 'ctrl+c':
                    # store the image in a buffer using savefig(), this has the
                    # advantage of applying all the default savefig parameters
                    # such as background color; those would be ignored if you simply
                    # grab the canvas using Qt
                    #buf = io.BytesIO()
                    #fig.savefig(buf)
                    #img = QPixmap() 
                    #img = QImage()
                    size = fig.canvas.size()
                    width, height = size.width(), size.height()
                    im = QImage(fig.canvas.buffer_rgba(), width, height, QImage.Format_ARGB32)
                    QApplication.clipboard().setImage(im)

            fig.canvas.mpl_connect('key_press_event', clipboard_handler)
            return fig
    
        plt.figure = newfig

