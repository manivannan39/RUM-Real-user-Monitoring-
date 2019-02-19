from Tkinter import *
# create the canvas, size in pixels
canvas = Canvas(width = 50, height = 50, bg = 'yellow')
# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
# load the .gif image file
# put in your own gif file here, may need to add full path
# like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
gif1 = PhotoImage(file = '/home/manivannan/Downloads/Logo 1.png')
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(30, 10, image = gif1, anchor = NW)
# run it ...
mainloop()
