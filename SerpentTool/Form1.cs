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
    public partial class Form1 : Form
    {
        //Connection Object
        OleDbConnection conn;
        //Table Command 
        OleDbCommand titleCommand;
        //Data Adapter Object
        OleDbDataAdapter titleAadapter;
        //Data Table
        DataTable titlesTable;
        //Manage next, previous, last, first
        CurrencyManager titlesManager;

        OleDbCommandBuilder builderCommand;

        string state = " ";
        public int CurrentPosition { get; set; }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        //ConnecyionStrings.com according to the database that we want to connect
        //Current Standard Security
        //String to be passed into connection, make sure to put the path of db file
        
         var connString = @"Provider = Microsoft.ACE.OLEDB.12.0; Data Source = C:\Users\Marco\Desktop\Natural-Language-Processing\Books.accdb;
                        Persist Security Info = False;";
        
         conn = new OleDbConnection(connString);
            conn.Open();
            //Connection State
            TextConnect.Text = conn.State.ToString();

            //conn.Close();
            //TextConnect.Text = conn.State.ToString();
            ////Remove from memory!
            //conn.Dispose();
            //TextConnect.Text = conn.State.ToString();


            //Query that you want to perform (data that is needed from the table)
            titleCommand = new OleDbCommand("Select * from Titles", conn);

            //
            titleAadapter = new OleDbDataAdapter();
            titleAadapter.SelectCommand = titleCommand;

            //
            titlesTable = new DataTable();
            titleAadapter.Fill(titlesTable);

            //BIND CONTROLS (this are the columns names as they apper on Access Db)
            textTitle.DataBindings.Add("Text", titlesTable, "Title");
            textYear.DataBindings.Add("Text", titlesTable, "Year_Published");
            textISBN.DataBindings.Add("Text", titlesTable, "ISBN");
            textID.DataBindings.Add("Text", titlesTable, "PubId");

            //Establish currency manager (Naviigate thouthg the records)
            titlesManager = (CurrencyManager)BindingContext[titlesTable];



            //Close everything once done
           // conn.Close();
           // conn.Dispose();
           // titleAadapter.Dispose();
          //  titlesTable.Dispose();

        }

        private void buttonFirst_Click(object sender, EventArgs e)
        {
            //First position on list 
            titlesManager.Position = 0;

        }

        private void buttonPrev_Click(object sender, EventArgs e)
        {
            titlesManager.Position--;

        }

        private void buttonNext_Click(object sender, EventArgs e)
        {
            titlesManager.Position++;

        }

        private void buttonLast_Click(object sender, EventArgs e)
        {//Last Record on list
      
            titlesManager.Position = titlesManager.Count - 1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.OK;
            //Close connection

            //  TextConnect.Text = conn.State.ToString();
            ////Remove from memory!
            conn.Close();
            conn.Dispose();
            //TextConnect.Text = conn.State.ToString();
        }

        private void SaveButton_Click(object sender, EventArgs e)
        {

            //Once edit/update is done, save wiill commit changes to the db
            titlesManager.EndCurrentEdit();
            builderCommand = new OleDbCommandBuilder(titleAadapter);
            titleAadapter.Update(titlesTable);

            MessageBox.Show("Record saved", "Save", MessageBoxButtons.OK, MessageBoxIcon.Information);
  
        }

        private void DeleteButton_Click(object sender, EventArgs e)
        {
            DialogResult response;
            response = MessageBox.Show("Sure ??", "Delete", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2);

            if (response == DialogResult.No)
            {
                return;
            }
            else {

                //Remove a record from a specified index
                titlesManager.RemoveAt(titlesManager.Position);
                builderCommand = new OleDbCommandBuilder(titleAadapter);
                titleAadapter.Update(titlesTable);


                return;

            }
        }

        private void AddNewButton_Click(object sender, EventArgs e)
        {
            //Add new 
            CurrentPosition = titlesManager.Position;
            titlesManager.AddNew();
            state = "add";
        }

        private void EditButton_Click(object sender, EventArgs e)
        {
            textTitle.ReadOnly = false;
            textTitle.Focus();
        }

        private void CancelButton_Click(object sender, EventArgs e)
        {

            if (state == "add")
            {
                titlesManager.CancelCurrentEdit();
                titlesManager.Position = CurrentPosition;
            }
            else {
                titlesManager.CancelCurrentEdit();

            }

            MessageBox.Show("Transaction aborted ", "Save", MessageBoxButtons.OK, MessageBoxIcon.Information);
         
        }
    }
}
