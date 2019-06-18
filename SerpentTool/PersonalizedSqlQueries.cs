using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.OleDb;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace frmTitles
{
    public partial class PersonalizedSqlQueries : Form
    {
        OleDbConnection conn;

        public PersonalizedSqlQueries()
        {
            InitializeComponent();
        }

        private void PersonalizedSqlQueries_Load(object sender, EventArgs e)
        {
            var connString = @"Provider = Microsoft.ACE.OLEDB.12.0; Data Source = C:\Users\Marco\Desktop\Books.accdb;
                        Persist Security Info = False;";

            conn = new OleDbConnection(connString);
            conn.Open();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void Execute_Click(object sender, EventArgs e)
        {
            OleDbCommand commando;
            OleDbDataAdapter adapter = new OleDbDataAdapter();
            DataTable table = new DataTable();

            try
            {
                commando = new OleDbCommand(Command.Text, conn);
                adapter.SelectCommand = commando;

                adapter.Fill(table);
                dataGridView1.DataSource = table;



            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error in SQL COMMAND", MessageBoxButtons.OK, MessageBoxIcon.Error);

            }
        }
    }
}
