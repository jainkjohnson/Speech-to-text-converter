#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Fri Jun 20 09:06:17 2014


from sys import byteorder
from array import array
from struct import pack
from tkFileDialog import askopenfilename

import time
from threading import *
import wx
import pyaudio
import wave
import os,sys
import Tkinter,tkFileDialog

import about

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 16000
FLAG = 0 
path = 'sas1.wav'
path1 = 'comm.wav'
data = 0
sample_width = 0
count = 1	

temp = 1	
result = ''
b = ''

# Define notification event for thread completion
EVT_RESULT_ID = wx.NewId()




# begin wxGlade: extracode
# end wxGlade


def EVT_RESULT(win, func):
       """Define Result Event."""
       win.Connect(-1, -1, EVT_RESULT_ID, func)
   
class ResultEvent(wx.PyEvent):
       
       def __init__(self, data):
           """Init Result Event."""
           wx.PyEvent.__init__(self)
           self.SetEventType(EVT_RESULT_ID)
           self.data = data
   
# Thread class that executes processing
class WorkerThread(Thread):
      
       
       
       def __init__(self, notify_window):
           """Init Worker Thread Class."""
           Thread.__init__(self)
           self._notify_window = notify_window
           self._want_abort = 0
           # This starts the thread running on creation, but you could
           # also make the GUI thread responsible for calling this
           self.start()
   
       def run(self):
       	   global result
       	   global result1
	   p = pyaudio.PyAudio()
	   stream = p.open(format=FORMAT, channels=1, rate=RATE,
		input=True, output=True,
		frames_per_buffer=CHUNK_SIZE)

	   num_silent = 0
           snd_started = False
	   r = array('h')
           """Run Worker Thread."""
           # This is the code executing in the new thread. Simulation of
           # a long process (well, 10s here) as a simple loop - you will
           # need to structure your processing so that you periodically
           # peek at the abort variable
           while 1:
               snd_data = array('h', stream.read(CHUNK_SIZE))
	       if byteorder == 'big':
		    snd_data.byteswap()
	       r.extend(snd_data)

	       time.sleep(0.01)
	       if self._want_abort:
	       	   
		   print "end"
                   sample_width = p.get_sample_size(FORMAT)
		   stream.stop_stream()
		   stream.close()
		   p.terminate()

		   
		   
		  
		   r = pack('<' + ('h'*len(r)), *r)
		   wf = wave.open(path, 'wb')
	           wf.setnchannels(1)
	           wf.setsampwidth(sample_width)
	           wf.setframerate(RATE)
	           wf.writeframes(r)
	           wf.close()
	          
	             	              
			   
		   try:

			import pocketsphinx 
			import sphinxbase
			hmdir = "/usr/share/pocketsphinx/model/hmm/en_US/hub4wsj_sc_8k"
			lmd = "/usr/share/pocketsphinx/model/lm/en_US/hub4.5000.DMP"
			dictd = "/usr/share/pocketsphinx/model/lm/en_US/cmu07a.dic"
			speechRec = pocketsphinx.Decoder(hmm = hmdir, lm = lmd, dict = dictd)
			wavfile = "sas1.wav"
			wavFile = file(wavfile,'rb')
			wavFile.seek(44)
			speechRec.decode_raw(wavFile)
			result = speechRec.get_hyp()
			print result
			
		   except:
		   	self.count = 0
			import pocketsphinx 
			hmdir = "/usr/share/pocketsphinx/model/hmm/en_US/hub4wsj_sc_8k"
			lmd = "/usr/share/pocketsphinx/model/lm/en_US/hub4.5000.DMP"
			dictd = "/usr/share/pocketsphinx/model/lm/en_US/cmu07a.dic"
			speechRec = pocketsphinx.Decoder(hmm = hmdir, lm = lmd, dict = dictd)
			wavfile = "sas1.wav"
			wavFile = file(wavfile,'rb')
			wavFile.seek(44)
			speechRec.decode_raw(wavFile)
			result = speechRec.get_hyp()
			
			print result
				
	           
	           
		   return format(result)
		   # Use a result of None to acknowledge the abort (of
                   # course you can use whatever you'd like or even
                   # a separate event type)
                  
                  
           # Here's where the result would be returned (this is an
           # example fixed result of the number 10, but it could be
           # any Python object)
	   '''wx.PostEvent(self._notify_window, ResultEvent(None))
           wx.PostEvent(self._notify_window, ResultEvent(1))'''
   
       def abort(self):
           print """abort worker thread."""
           # Method for use by main thread to signal an abort
           self._want_abort = 1
           



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_2 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X2.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_3 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X3.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_4 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X4.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_5 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X5.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_6 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X6.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_7 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X7.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_8 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X8.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_9 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/1X9.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_10 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/2X1.jpg", wx.BITMAP_TYPE_ANY))
        self.button_1 = wx.Button(self, -1, u"◉")
        self.bitmap_11 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/2X2.jpg", wx.BITMAP_TYPE_ANY))
        self.button_2 = wx.Button(self, -1, u"▆")
        self.bitmap_12 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/2X3.jpg", wx.BITMAP_TYPE_ANY))
        self.button_3 = wx.Button(self, -1, u"▶")
        self.bitmap_13 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/2X4.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_14 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/2X5.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_15 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/2X6.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_16 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/3X1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_17 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/3X2.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_18 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/3X3.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_19 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/3X4.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_20 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/3X5.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_21 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/3X6.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_22 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/3X7.jpg", wx.BITMAP_TYPE_ANY))
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.bitmap_23 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/3X8.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_24 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/4X1.jpg", wx.BITMAP_TYPE_ANY))
        self.button_4 = wx.Button(self, -1, "PROCESS")
        self.bitmap_25 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/4X3.jpg", wx.BITMAP_TYPE_ANY))
        self.button_5 = wx.Button(self, -1, "AUTO SAVE")
        self.bitmap_26 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/4X5.jpg", wx.BITMAP_TYPE_ANY))
        self.button_6 = wx.Button(self, -1, "COMMAND")
        self.bitmap_27 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/4X7.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_28 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/4X8.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_29 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/4X9.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_30 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_31 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X2.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_32 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X3.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_33 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X4.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_34 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X5.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_35 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X6.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_36 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X7.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_37 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X8.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_38 = wx.StaticBitmap(self, -1, wx.Bitmap("/media/jainz/FIstVI/cap_back/5X9.jpg", wx.BITMAP_TYPE_ANY))
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(1, "Save", "To save a Document", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(2, "Open", "To open a Document", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(5, "Clear", "To clear", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(3, "Exit", "Exiting......", wx.ITEM_NORMAL)
         
        self.frame_1_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(4, "About", 'Dilshad Radhika Revathy Jain', wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "About")
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end

        self.__set_properties()
        self.__do_layout()
	self.Bind(wx.EVT_BUTTON, self.start, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.stop, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.play, self.button_3)
        self.Bind(wx.EVT_TEXT, self.text1, self.text_ctrl_1)
        self.Bind(wx.EVT_BUTTON, self.process, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.ausave, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.command, self.button_6)
        self.Bind(wx.EVT_MENU, self.save, id=1)
        self.Bind(wx.EVT_MENU, self.open, id=2)
        self.Bind(wx.EVT_MENU, self.exit, id=3)
        self.Bind(wx.EVT_MENU, self.about, id=4)
        self.Bind(wx.EVT_MENU, self.clear, id=5)
        
        # end wxGlade
        
	

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("CAPTIONER")
        self.SetSize((703, 434))
        self.SetBackgroundColour(wx.Colour(249, 255, 250))
        self.button_1.SetMinSize((87, 27))
        self.button_1.SetBackgroundColour(wx.Colour(255, 244, 245))
        self.button_1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.button_1.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.button_2.SetMinSize((87, 27))
        self.button_2.SetBackgroundColour(wx.Colour(239, 255, 244))
        self.button_2.SetForegroundColour(wx.Colour(0, 0, 0))
        self.button_2.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.button_3.SetMinSize((87, 27))
        self.button_3.SetBackgroundColour(wx.Colour(249, 255, 254))
        self.button_3.SetForegroundColour(wx.Colour(0, 0, 0))
        self.button_3.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_1.SetMinSize((240, 172))
        self.text_ctrl_1.SetFont(wx.Font(10, wx.TELETYPE, wx.NORMAL, wx.NORMAL, 0, "Symbol"))
        self.button_4.SetMinSize((87, 27))
        self.button_4.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.button_4.SetForegroundColour(wx.Colour(0, 0, 0))
        self.button_5.SetMinSize((87, 27))
        self.button_5.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.button_6.SetMinSize((87, 27))
        self.button_6.SetBackgroundColour(wx.Colour(255, 255, 255))
        
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(5, 9, 0, 0)
        grid_sizer_1.Add(self.bitmap_1, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_2, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_3, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_4, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_5, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_6, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_7, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_8, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_9, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_10, 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_11, 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_12, 0, 0, 0)
        grid_sizer_1.Add(self.button_3, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_13, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_14, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_15, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_16, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_17, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_18, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_19, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_20, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_21, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_22, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_1, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_23, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_24, 0, 0, 0)
        grid_sizer_1.Add(self.button_4, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_25, 0, 0, 0)
        grid_sizer_1.Add(self.button_5, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_26, 0, 0, 0)
        grid_sizer_1.Add(self.button_6, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_27, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_28, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_29, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_30, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_31, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_32, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_33, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_34, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_35, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_36, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_37, 0, 0, 0)
        grid_sizer_1.Add(self.bitmap_38, 0, 0, 0)
        
        
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        
        self.worker = None
        # end wxGlade

    def save(self, event):  # wxGlade: MyFrame.<event_handler>
        root = Tkinter.Tk() 
	root.withdraw() 
	dirs=tkFileDialog.asksaveasfile(mode='w')
	dirs.write(b)
        event.Skip()
        
        
    def clear(self, event):  # wxGlade: MyFrame.<event_handler>
	self.text_ctrl_1.Clear() 
        event.Skip()	

    def open(self, event):  # wxGlade: MyFrame.<event_handler>
        root = Tkinter.Tk(); 
	root.withdraw()
	filename = askopenfilename(parent=root)
	filename

	f=open(filename)
	res = f.read()
	print res

	f.close()
	self.text_ctrl_1.SetValue(res)
        event.Skip()

    def exit(self, event):  # wxGlade: MyFrame.<event_handler>
        self.Destroy()
        event.Skip()

    def about(self, event):  # wxGlade: MyFrame.<event_handler>
        frame_1 = about.MyFrame(None, -1, "")
    	app.SetTopWindow(frame_1)
    	frame_1.Show()
    	event.Skip()

    def start(self, event):  # wxGlade: MyFrame.<event_handler>
        if not self.worker:
               
               self.worker = WorkerThread(self)
        event.Skip()

    def stop(self, event):  # wxGlade: MyFrame.<event_handler>
        if self.worker:
               
               self.worker.abort()
               self.worker = 0
        event.Skip()

    def play(self, event):  # wxGlade: MyFrame.<event_handler>
        f = wave.open("sas1.wav","rb")  
		
	p = pyaudio.PyAudio()  

	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
			channels = f.getnchannels(),  
			rate = f.getframerate(),  
			output = True)  

	data = f.readframes(CHUNK_SIZE)  


	while data != '':  
	    stream.write(data)  
	    data = f.readframes(CHUNK_SIZE)  
	stream.stop_stream()  
	stream.close()  

	p.terminate()  
        event.Skip()
        
        
    def OnResult(self, event):
           print """Show Result status."""
           if event.data is None:
               # Thread aborted (using our convention of None return)
               self.status.SetLabel('Computation aborted')
           else:
              # Process results here
              self.status.SetLabel('Computation Result: %s' % event.data)
              # In either event, the worker is done
              self.worker = None

    def process(self, event):  # wxGlade: MyFrame.<event_handler>
           global b
       	   print result
       	   res = str(result)
       	   a,b,c,d,e = res.split("'")
       	   
       	   print b
       	   
       	   
           
           self.text_ctrl_1.SetValue(b)
           
           event.Skip()

    def ausave(self, event):  # wxGlade: MyFrame.<event_handler>
           text_file = open("Output.txt", "w")

	   text_file.write(b)
	   
	   text_file.close()
 	   os.system("gedit Output.txt")
           event.Skip()

    def command(self, event):  # wxGlade: MyFrame.<event_handler>
            def record():
		    p = pyaudio.PyAudio()
		    stream = p.open(format=FORMAT, channels=1, rate=RATE,
			input=True, output=True,
			frames_per_buffer=CHUNK_SIZE)

		    num_silent = 0
		    

		    r = array('h')

	  	    while 1:
				# little endian, signed short
				snd_data = array('h', stream.read(CHUNK_SIZE))
				if byteorder == 'big':
				    snd_data.byteswap()
				r.extend(snd_data)

				

				
				num_silent += 1
				
				if num_silent > 50:
				    break

		    sample_width = p.get_sample_size(FORMAT)
		    stream.stop_stream()
		    stream.close()
		    p.terminate()

		    
		    return sample_width, r

	   
	    sample_width, data = record()
            data = pack('<' + ('h'*len(data)), *data)

	    wf = wave.open(path1, 'wb')
	    wf.setnchannels(1)
	    wf.setsampwidth(sample_width)
	    wf.setframerate(RATE)
	    wf.writeframes(data)
	    wf.close() 
	    
	    try:

			import pocketsphinx 
			import sphinxbase
			hmdir = "/usr/share/pocketsphinx/model/hmm/wsj1"
			lmd = "/usr/share/pocketsphinx/model/lm/wsj/wlist5o.3e-7.vp.tg.lm1.DMP"
			dictd = "/usr/share/pocketsphinx/model/lm/wsj/wlist5o1.dic"
			speechRec = pocketsphinx.Decoder(hmm = hmdir, lm = lmd, dict = dictd)
			wavfile = "comm.wav"
			wavFile = file(wavfile,'rb')
			wavFile.seek(44)
			speechRec.decode_raw(wavFile)
			result1 = speechRec.get_hyp()
			print result1
			
	    except:
		   	self.count = 0
			import pocketsphinx 
			hmdir = "/usr/share/pocketsphinx/model/hmm/wsj1"
			lmd = "/usr/share/pocketsphinx/model/lm/wsj/wlist5o.3e-7.vp.tg.lm1.DMP"
			dictd = "/usr/share/pocketsphinx/model/lm/wsj/wlist5o1.dic"
			speechRec = pocketsphinx.Decoder(hmm = hmdir, lm = lmd, dict = dictd)
			wavfile = "comm.wav"
			wavFile = file(wavfile,'rb')
			wavFile.seek(44)
			speechRec.decode_raw(wavFile)
			result1 = speechRec.get_hyp()
			
			print result1
	  
	    res1 = str(result1)
       	    h,i,j,k,m = res1.split("'")
       	   
       	    print i
	    if i == 'SAVE':
	    	    	
	       	    root = Tkinter.Tk() 
	       	    root.withdraw() 
	       	    dirs=tkFileDialog.asksaveasfile(mode='w')
	       	    dirs.write(b)
	       	    
	       	    print dirs
           	 
	    if i == 'OPEN':
	   	    root = Tkinter.Tk(); 
	   	    root.withdraw()
   		    filename = askopenfilename(parent=root)
		    filename

		    f=open(filename)
		    res = f.read()
		    print res
		    	
		    f.close()
		    self.text_ctrl_1.SetValue(res)
		    
		    
	    if i == 'CLEAR':
	    	    self.text_ctrl_1.Clear() 
	    	    
    	    if i == 'QUIT':
	    	    self.Destroy() 

            event.Skip()

    def text1(self, event):  # wxGlade: MyFrame.<event_handler>
        
        event.Skip()

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
