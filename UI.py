import tkinter as tk

from threads import ServantThread

shift = 0

root = tk.Tk()

ActionButtonsFrame = tk.Frame(root, bg="white")
ActionButtonsFrame.grid(row=0, column=0, columnspan=4)
viewFrame = tk.Frame(root)
viewFrame.grid(row=1, column=1, columnspan=4)


def ReinitialFrames():
    ActionButtonsFrame = tk.Frame(root, bg="white")
    ActionButtonsFrame.grid(row=0 + shift, column=0, columnspan=4)
    viewFrame = tk.Frame(root)
    viewFrame.grid(row=1 + shift, column=0, columnspan=4)


def dismissMessage(messageFrame):
    messageFrame.grid_forget()
    ReinitialFrames()


def newMessage(sender, message):
    global shift
    global ActionButtonsFrame

    shift = 1
    ReinitialFrames()
    ActionButtonsFrame.grid_forget()
    ActionButtonsFrame.grid(row=1, column=0, columnspan=4)

    messageFrame = tk.LabelFrame(root, text="from: " + sender, width=30)
    messageFrame.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
    T = tk.Text(messageFrame, height=10, width=30)
    T.grid(row=0, column=0, padx=10, pady=10)
    T.insert(tk.END, message)
    submit = tk.Button(messageFrame, text='Dismiss', width=50,
                       borderwidth="0", bg="#f44336", fg="white", command=lambda: dismissMessage(messageFrame))
    submit.grid(row=1, column=0, columnspan="1", padx=10, pady=(3, 10))


newMessage("Ali Beigi", "sdasdsd")


def RerenderView():
    global viewFrame
    global shift
    viewFrame.grid_forget()
    viewFrame = tk.Frame(root)
    viewFrame.grid(row=1 + shift, column=0, columnspan=4)


def renderList(mylist, command):
    global viewFrame
    listbox = tk.Listbox(viewFrame, borderwidth="0", width=62)
    listbox.grid(row=0, column=0, columnspan=4)

    for item in mylist:
        listbox.insert('end', item)

    if command == 'following':
        submit = tk.Button(viewFrame, text="Unfollow this User", width=50,
                           borderwidth="0", bg="#f44336", fg="white", command=lambda: Unfollow(listbox.get("active")))
        submit.grid(row=1, column=0, columnspan="1", padx=10, pady=(3, 10))


def changeToFollowers():
    global viewFrame
    RerenderView()
    renderList(["mammad", "ali", "shirin"], 'following')


def changeToFollowing():
    global viewFrame
    RerenderView()
    renderList(["mahshid", "asghar", "ladan"], 'xyz')


def changeToAddFollower():
    global viewFrame
    RerenderView()
    ipLabel = tk.Label(viewFrame, text="IP Address:")
    ipLabel.grid(row=0, column=0, columnspan=1, pady=(5, 5), padx=10, sticky='w')
    ipEntry = tk.Entry(viewFrame, width=40, borderwidth="0")
    ipEntry.grid(row=0, column=1, columnspan=3, pady=(5, 5), padx=10)

    submit = tk.Button(viewFrame, text='Add', width=50,
                       borderwidth="0", bg="#2e7d32", fg="white", command=lambda: requestAddFollower(ipEntry))
    submit.grid(row=2, column=0, columnspan="2", padx=10, pady=(3, 10))


def changeToBroadcast():
    global viewFrame
    RerenderView()
    ipLabel = tk.Label(viewFrame, text="Message:")
    ipLabel.grid(row=0, column=0, columnspan=1, pady=(5, 5), padx=10, sticky='w')
    messageText = tk.Text(viewFrame, width=30, height=5, borderwidth="0")
    messageText.grid(row=0, column=1, columnspan=3, pady=(10, 5), padx=(5, 10))

    submit = tk.Button(viewFrame, text='Submit Message', width=50,
                       borderwidth="0", bg="#2e7d32", fg="white", command=lambda: submitBroadcast(messageText))
    submit.grid(row=2, column=0, columnspan="2", padx=10, pady=(3, 10))


def changeToQuery():
    global viewFrame
    RerenderView()
    ipLabel = tk.Label(viewFrame, text="Query:")
    ipLabel.grid(row=0, column=0, columnspan=1, pady=(5, 5), padx=10, sticky='w')

    queryText = tk.Text(viewFrame, width=30, height=5, borderwidth="0")
    queryText.grid(row=0, column=1, columnspan=3, pady=(10, 5), padx=(5, 10))

    submit = tk.Button(viewFrame, text='Search this Query', width=50,
                       borderwidth="0", bg="#2e7d32", fg="white", command=lambda: submitQuery(queryText))
    submit.grid(row=2, column=0, columnspan="2", padx=10, pady=(3, 10))


followersBtn = tk.Button(ActionButtonsFrame, text='Followers', width=50,
                         borderwidth="0", bg="#00bcd4", fg="white", command=changeToFollowers)
followersBtn.grid(row=0, column=0, columnspan="1", padx=10, pady=(10, 3))

followingBtn = tk.Button(ActionButtonsFrame, text='Follwings', width=50,
                         borderwidth="0", bg="#00bcd4", fg="white", command=changeToFollowing)
followingBtn.grid(row=1, column=0, columnspan="1", padx=10, pady=3)

addFollower = tk.Button(ActionButtonsFrame, text='Add a Follower', width=50,
                        borderwidth="0", bg="#00bcd4", fg="white", command=changeToAddFollower)
addFollower.grid(row=2, column=0, columnspan="1", padx=10, pady=3)

broadcastBtn = tk.Button(ActionButtonsFrame, text='Broadcast', width=50,
                         borderwidth="0", bg="#00bcd4", fg="white", command=changeToBroadcast)
broadcastBtn.grid(row=3, column=0, columnspan="1", padx=10, pady=3)

queryBtn = tk.Button(ActionButtonsFrame, text='search a query', width=50,
                     borderwidth="0", bg="#00bcd4", fg="white", command=changeToQuery)
queryBtn.grid(row=4, column=0, columnspan="1", padx=10, pady=(3, 10))


# label1 = tk.Label(root, text= float(x1)**0.5)
# canvas1.create_window(200, 230, window=label1)

def submitBroadcast(broadcastInput):
    broadcast = broadcastInput.get("1.0", 'end-1c')
    print(broadcast)


def requestAddFollower(ipInput):
    ip = ipInput.get()
    print(ip)


def submitQuery(QueryInput):
    query = QueryInput.get("1.0", 'end-1c')
    print(query)


def Unfollow(selected):
    print(selected)


if __name__ == '__main__':
    thread = ServantThread()
    thread.start()
    root.mainloop()
