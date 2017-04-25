import clr

clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")

import analyse_freq.py


from System.Drawing import *
from System.Windows.Forms import *

class HelloWorldForm(Form):
    def __init__(self):

       
        self.Text = 'Traitement verbatim'
        url = TextBox()
        url.Text = "Entrez le lien local de vos verbatim au format csv"
        url.Location = Point(50, 50)
        url.Height = 30
        url.Width = 500
        self.count = 0
        button = Button()
        button.Text = "Click Me"
        button.Location = Point(550, 50)
        button.Click += self.buttonPressed
        self.Controls.Add(url)
        self.Controls.Add(button)
        pass
    def buttonPressed (self,sender,args):
        motsclefs = Label()

        self.Text="hello world"

Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = HelloWorldForm()
Application.Run(form)

