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

