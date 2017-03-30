using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Text;
using IronPython.Hosting;

namespace panel
{
    static class Program
    {
        /// <summary>
        /// Point d'entrée principal de l'application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            //https://bytes.com/topic/python/insights/950783-two-ways-run-python-programs-c
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            //Application.Run(new Form1());

            var ipy = Python.CreateRuntime();
            dynamic test = ipy.UseFile("C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\analyse_freq.py");
            test.Simple();
            test.programme();
        }
    }
}