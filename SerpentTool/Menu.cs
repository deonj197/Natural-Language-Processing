using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

// https://stackoverflow.com/questions/6649363/microsoft-ace-oledb-12-0-provider-is-not-registered-on-the-local-machine
//  microsoft.com/en-in/download/details.aspx?id=13255

namespace frmTitles
{
    public partial class Menu : Form
    {
        public Menu()
        {
            InitializeComponent();
        }

        private void Menu_Load(object sender, EventArgs e)
        {

        }

        private void AccessData_Click(object sender, EventArgs e)
        {
            this.Hide();
            TableList form1 = new TableList();

            form1.ShowDialog();
            this.Show();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            PersonalizedSqlQueries form2 = new PersonalizedSqlQueries();

            form2.ShowDialog();
            this.Show();
        }

        private void QuitBtn_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
