# cinesite
Python tests for Cinesite


**** General Python test *****
- Write a function that finds all animated sequences in a given directory and prints their frame ranges in the following format: 
  - 'name: 1001-2000' if there are no gaps
  - 'name: 1001, 1003-1500, 1600-2000' if there are gaps
- The format for an animated sequence is name.####.ext e.g. /job/.../my_render_v001.1001.jpg


==> repository "frame_range" 

It uses the Python library named "fileseq" for parsing frame ranges and file sequences. 
GitHub source code: https://github.com/sqlboy/fileseq.git

The test only asks for a function. 
Using the fileseq library, it amounts to writing this: 

    from fileseq import filesequence
    from fileseq.filesequence import FileSequence

    def print_sequences_frame_range(path):
      ''' Prints the frame ranges of animated sequences in given directory.

      @param path: path to the directory.
      '''

      # *.@@@@.* will match the animated sequence format: name.####.ext
      pattern = path + '*.@@@@.*'
      seq_list = FileSequence.findSequencesOnDisk(pattern)

      for seq in seq_list:
          print("%s: %s"%(seq.basename()[:-1], seq.frameSet()))
      return

Some unrequested additional material have been made to this: including parsing arguments from command line and using a logger to print.

The repository "frame_range" thus includes a script (framerange.py) that can be called from command line and that does print frame ranges for animated sequences in given directory. 
Usage: python framerange.py </path/to/directory/>

It also includes sequence examples. 

Another solution (not using fileseq) could have been to parse the directory and use a regex to find sequences which would match the format name.####.ext. 
The regex could potentially (not robust to "weird" file naming such as names with whitespaces or characters like '.') have been:

    seq_regex = re.compile("(\w+)\.(\d{4})\.(\w+)")

Then the frames could have been processed to determinate the first frame, the end frame and gaps if any. 


**** PyQt/rendering/installation test *****
- Download and install Prman or Arnold (prman is free for Non-commercial use, Arnold renders images with watermarks)
- Write a PyQt dialog that has the following elements:
  - a view for displaying rendered image
  - a view for displaying output log of the renderer
  - a color picker to change the color of the objects in the scene
  - a render button
- When user clicks render button, the program should use renderer python API to render a sphere/teapot with user-defined color and display image and the log in the UI. Please note that you are not expected to write a custom display driver for prman/arnold - you should simply render to disk and load image into the UI.

==> repository "render"

Please note this is a WIP! UI is incomplete and the core implementation (mostly performing the actual render) is absent. 

I opted for prman (on Mac OS): https://renderman.pixar.com/install

The file custom_render.py contains the implementation of the UI. 
It works as a plugin in 'it': https://rmanwiki.pixar.com/pages/viewpage.action?pageId=30474445

The repository contains resulting screenshots.

When Pixar's RenderMan is installed, in my case, it created a folder named "RenderManProServer-22.3" with the following structure: 
- bin
- etc
- include
- lib

The 'it' application is located inside the 'bin' folder.

The custom_render.py script should be placed in the folder 'RenderManProServer-22.3/lib/it/python/'. 

In order for 'it' to detect the script, the following should be added to 'RenderManProServer-22.3/etc/it.ini': 

    # This extension can be accessed from the Console command line and 
    # and renders a sphere/teacup from user selected color & displays it
    LoadExtension python [file join $pydir custom_render.py]
