import it
import ice
from it.It3Command import It3Command

from PythonQt.QtGui import QDialogButtonBox
from PythonQt.QtGui import QHBoxLayout
from PythonQt.QtGui import QLabel
from PythonQt.QtGui import QPushButton
from PythonQt.QtGui import QColorDialog
from PythonQt.QtGui import QPixmap, QImage
from PythonQt.QtGui import QPlainTextEdit


# Example on how to create a custom command can be found here:
# https://renderman.pixar.com/resources/RenderMan_20/itCommands.html
# This code is highly inspired from it


class RenderCustomCommand(It3Command):
    ''' Enable the user to pick a color and render a sphere/teapot with chosen color
    then display rendered image and output log.

    Extends It3Command class. Add a custom command menu in 'it'. '''


    def __init__(self):
        self.m_menuPath = 'Commands/Custom commands/Render with color'
        self.m_dlg = None

        # doesn't do anything but required (inherited from It3Command)
        self.m_stdButtons = QDialogButtonBox.Close |  QDialogButtonBox.Apply


    def Invoke(self):
        ''' Called when user clicks on menu path item.

        Reproduced from example. '''

        if self.m_dlg == None:
            # since we're going to run modeless need to hang onto the
            # dialog object or it'll get deleted when Invoke exits.
            # 'it' has a hold of 'self' so we won't go away.
            self.m_dlg = self.initUI()
        self.m_dlg.show()
        self.m_dlg.raise_()
        self.m_dlg.activateWindow()


    def display_color_picker(self):
        ''' Display color picker & set chosen color and render button to visible. '''

        color = QColorDialog.getColor()

        if color.isValid():
            self.color = color
            self.color_label.setVisible(True)
            self.color_label.setText(str(self.color))
            self.render_button.setVisible(True)


    def launch_render(self):
        ''' Performs the render and set render views to visible. '''

        ### TO DO:
        # - actual render
        # - waiting process (render should be finished before setting render image and output)
        # - access path to rendered image and its output log

        # rendered image
        #self.image_label.setPixmap(QPixmap('pixar.jpg')) # doesn't seem to work
        self.image_label.setText("*** SHOULD BE AN IMAGE! ***")
        self.image_label.setVisible(True)

        # output log of rendered image
        self.render_log_textedit.setVisible(True)
        self.render_log_textedit.setPlainText("OUTOPUT LOG TEXT OF RENDERED IMAGE")
        self.render_log_textedit.setReadOnly(True)


    def initUI(self):
        dlg = self.CreateDialog('Render...')
        contents = dlg.findChild(QVBoxLayout, 'contents')

        # color picker
        layout = QHBoxLayout()
        contents.addLayout(layout)
        color_button = QPushButton("Color")
        layout.addWidget(color_button)
        color_button.connect('clicked()', self.display_color_picker)
        # display color ==> useful to know if a color has been selected
        self.color_label = QLabel("")
        self.color_label.setVisible(False)
        layout.addWidget(self.color_label)

        # render button
        layout = QHBoxLayout()
        contents.addLayout(layout)
        self.render_button = QPushButton("Render")
        self.render_button.setVisible(False)
        layout.addWidget(self.render_button)
        self.render_button.connect('clicked()', self.launch_render)

        # view for rendered image
        layout = QHBoxLayout()
        contents.addLayout(layout)
        self.image_label = QLabel()
        self.image_label.setVisible(False)
        layout.addWidget(self.image_label)

        # view for log of rendered image
        layout = QHBoxLayout()
        contents.addLayout(layout)
        self.render_log_textedit = QPlainTextEdit()
        self.render_log_textedit.setVisible(False)
        layout.addWidget(self.render_log_textedit)

        return dlg


it.commands.append(RenderCustomCommand)
