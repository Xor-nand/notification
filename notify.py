import gi

# GTK version
gi.require_version('Notify', '0.7')


from gi.repository import Notify
import os


#  initialization of libnotify
Notify.init("DOOMSDAY TRASH")

#  notification object
title = "Cleaning script is active"
body = "Trash and download folders are going to be deleted, backup anything you need.\n you only have 5 minutes."

notification = Notify.Notification.new(
	title,
	body,
)

#  function to call back

def repl():
	Notify.Notification.new(
	"cleaning script delayed",
	"in 20 minutes, all your trash is going to be erased forever.",
	"/home/tommaso/Pictures/alert.png"
	).show()

	return

#add reply button

notification.add_action(
	"action_click",
	"WAIT!",
	repl,
	None #  Arguments
)

notification.set_urgency(2) #  highest priority notification


notification.show()

