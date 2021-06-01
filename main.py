import tkinter as tink
count = -1
run = False
def var_name(mark):
   def value():
      if run:
         global count
         # Just beore starting
         if count == -1:
            show = "Starting"
         else:
            show = str(count)
         mark['text'] = show
         #Increment the count after
         #every 1 second
         mark.after(1000, value)
         count += 1
   value()
# While Running
def Start(mark):
   global run
   run = True
   var_name(mark)
   start['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'
# While stopped
def Stop():
   global run
   start['state'] = 'normal'
   stop['state'] = 'disabled'
   reset['state'] = 'normal'
   run = False
# For Reset
def Reset(label):
   global count
   count = -1
   if run == False:
      reset['state'] = 'disabled'
      mark['text'] = 'Welcome'
   else:
      mark['text'] = 'Start'

base = tink.Tk()
base.title("PYTHON STOPWATCH")
base.minsize(width=150, height=250)
mark = tink.Label(base,borderwidth = 6, text="Welcome To Stopwatch", fg="black",bg="white", font="Times 25 bold")
mark.pack()
start = tink.Button(base, borderwidth = 3,relief="ridge",text='START',width=25,fg="green", command=lambda: Start(mark))
stop = tink.Button(base,borderwidth = 3,relief="ridge", text='STOP', width=25, fg="red",state='disabled', command=Stop)
reset = tink.Button(base, borderwidth = 3,relief="ridge",text='RESET',width=25, fg="green",state='disabled', command=lambda: Reset(mark))
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
base.mainloop()
