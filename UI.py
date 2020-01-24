import tkinter as tk

shift = 0

root= tk.Tk()

ActionButtonsFrame = tk.Frame ( root, bg="white")
ActionButtonsFrame.grid(row=0, column=0, columnspan=4)
viewFrame = tk.Frame(root)
viewFrame.grid(row=1, column=1,columnspan=4)

def ReinitialFrames():
  ActionButtonsFrame = tk.Frame ( root, bg="white")
  ActionButtonsFrame.grid(row=0 + shift, column=0, columnspan=4)
  viewFrame = tk.Frame(root)
  viewFrame.grid(row=1 + shift, column=0,columnspan=4)

def newMessage(sender, message):
  global shift
  global ActionButtonsFrame

  shift = 1
  ReinitialFrames()
  ActionButtonsFrame.grid_forget()
  ActionButtonsFrame.grid(row=1, column=0, columnspan=4)

  messageFrame = tk.LabelFrame(root, text="from whooo")
  messageFrame.grid(row=0, column=0,columnspan=4, padx=20, pady=20)
  T = tk.Text(root, height=10, width=30)
  T.grid(row=0, column=0, padx=10, pady=10)
  quote = """this is a new broadcast!
  from i dont know"""

  T.insert(tk.END, quote)

newMessage("Ali Beigi", "sdasdsd")


def RerenderView():
  global viewFrame
  global shift
  viewFrame.grid_forget()
  viewFrame = tk.Frame(root)
  viewFrame.grid(row= 1 + shift, column=0,columnspan=4)

def changeToFollowers():

  global viewFrame
  RerenderView()
  sample = tk.Label(viewFrame,text="changed")
  sample.grid(row=0, column=0, columnspan=4)

def changeToAddFollower():

  global viewFrame
  RerenderView()
  ipLabel = tk.Label(viewFrame,text="IP Address:")
  ipLabel.grid(row=0, column=0, columnspan=1, pady=(5,5), padx=10, sticky='w')
  ipEntry = tk.Entry(viewFrame, width=40, borderwidth="0")
  ipEntry.grid(row=0, column=1, columnspan=3,  pady=(5,5), padx=10)

  ipLabel = tk.Label(viewFrame,text="PORT Address:")
  ipLabel.grid(row=1, column=0, columnspan=1, pady=(0,5), padx=10, sticky='w')
  ipEntry = tk.Entry(viewFrame, width=40, borderwidth="0")
  ipEntry.grid(row=1, column=1, columnspan=3,  pady=(0,5), padx=10)

  submit = tk.Button(viewFrame, text='Add', width=50,
  borderwidth="0", bg="#2e7d32", fg="white" , command=submitBroadcast)
  submit.grid(row=2, column=0, columnspan="2",padx=10, pady=(3,10))


def changeToBroadcast():
  global viewFrame
  RerenderView()
  ipLabel = tk.Label(viewFrame,text="Message:")
  ipLabel.grid(row=0, column=0, columnspan=1, pady=(5,5), padx=10, sticky='w')
  ipEntry = tk.Entry(viewFrame, width=40, borderwidth="0")
  ipEntry.grid(row=0, column=1, columnspan=3,  pady=(5,5), padx=10)

  submit = tk.Button(viewFrame, text='Submit Message', width=50,
  borderwidth="0", bg="#2e7d32", fg="white" , command=submitBroadcast)
  submit.grid(row=2, column=0, columnspan="2",padx=10, pady=(3,10))


def changeToQuery():
  global viewFrame
  RerenderView()
  ipLabel = tk.Label(viewFrame,text="Query:")
  ipLabel.grid(row=0, column=0, columnspan=1, pady=(5,5), padx=10, sticky='w')
  ipEntry = tk.Entry(viewFrame, width=40, borderwidth="0")
  ipEntry.grid(row=0, column=1, columnspan=3,  pady=(5,5), padx=10)
  submit = tk.Button(viewFrame, text='Search this Query', width=50,
  borderwidth="0", bg="#2e7d32", fg="white" , command=submitBroadcast)
  submit.grid(row=2, column=0, columnspan="2",padx=10, pady=(3,10))


followersBtn = tk.Button(ActionButtonsFrame, text='Followers', width=50,
 borderwidth="0", bg="#00bcd4", fg="white" , command=changeToFollowers)
followersBtn.grid(row=0, column=0, columnspan="1",padx=10, pady=3)

followingBtn = tk.Button(ActionButtonsFrame, text='Follwings', width=50,
 borderwidth="0", bg="#00bcd4", fg="white" , command=changeToFollowers)
followingBtn.grid(row=1, column=0, columnspan="1", padx=10, pady=3)

addFollower = tk.Button(ActionButtonsFrame, text='Add a Follower', width=50,
 borderwidth="0", bg="#00bcd4", fg="white" , command=changeToAddFollower)
addFollower.grid(row=2, column=0, columnspan="1", padx=10, pady=3)

broadcastBtn = tk.Button(ActionButtonsFrame, text='Broadcast', width=50,
 borderwidth="0", bg="#00bcd4", fg="white" , command=changeToBroadcast)
broadcastBtn.grid(row=3, column=0, columnspan="1", padx=10, pady=3)

queryBtn = tk.Button(ActionButtonsFrame, text='search a query', width=50,
 borderwidth="0", bg="#00bcd4", fg="white" , command=changeToQuery)
queryBtn.grid(row=4, column=0, columnspan="1", padx=10, pady=(3,10))


    # label1 = tk.Label(root, text= float(x1)**0.5)
    # canvas1.create_window(200, 230, window=label1)
    
def submitBroadcast():
  print ('submit broadcast!')
 
root.mainloop()