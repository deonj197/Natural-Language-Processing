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
    public partial class TokenizedWord : Form
    {
        //Connection Object
        OleDbConnection conn;
        //Table Command 
        OleDbCommand TokenWordCommand;
        //Data Adapter Object
        OleDbDataAdapter TokenWordAdapter;
        //Data Table
        DataTable TokenWordTable;
        //Manage next, previous, last, first
        CurrencyManager TokenWordManager;

        OleDbCommandBuilder builderCommand;

        string state = " ";
        public int CurrentPosition { get; set; }

        public TokenizedWord()
        {
            InitializeComponent();
        }

        private void TokenizedWord_Load(object sender, EventArgs e)
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

            //Query that you want to perform (data that is needed from the table)
            TokenWordCommand = new OleDbCommand("Select * from Tokenized", conn);

            //
            TokenWordAdapter = new OleDbDataAdapter();
            TokenWordAdapter.SelectCommand = TokenWordCommand;

            //
            TokenWordTable = new DataTable();
            TokenWordAdapter.Fill(TokenWordTable);

            //BIND CONTROLS (this are the columns names as they apper on Access Db)
            textID.DataBindings.Add("Text", TokenWordTable, "ID");
            textWord.DataBindings.Add("Text", TokenWordTable, "Word");
            textTag.DataBindings.Add("Text", TokenWordTable, "Tag");
            textInfo.DataBindings.Add("Text", TokenWordTable, "Info");

            //Establish currency manager (Naviigate thouthg the records)
            TokenWordManager = (CurrencyManager)BindingContext[TokenWordTable];

        }

        private void buttonFirst_Click(object sender, EventArgs e)
        {
            //First position on list 
            TokenWordManager.Position = 0;

        }

        private void buttonPrev_Click(object sender, EventArgs e)
        {
            TokenWordManager.Position--;

        }

        private void buttonNext_Click(object sender, EventArgs e)
        {
            TokenWordManager.Position++;

        }

        private void buttonLast_Click(object sender, EventArgs e)
        {//Last Record on list

            TokenWordManager.Position = TokenWordManager.Count - 1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.OK;
        }

        private void SaveButton_Click(object sender, EventArgs e)
        {

            //Once edit/update is done, save wiill commit changes to the db
            TokenWordManager.EndCurrentEdit();
            builderCommand = new OleDbCommandBuilder(TokenWordAdapter);
            TokenWordAdapter.Update(TokenWordTable);

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
            else
            {

                //Remove a record from a specified index
                TokenWordManager.RemoveAt(TokenWordManager.Position);
                builderCommand = new OleDbCommandBuilder(TokenWordAdapter);
                TokenWordAdapter.Update(TokenWordTable);


                return;

            }
        }

        private void AddNewButton_Click(object sender, EventArgs e)
        {
            //Add new 
            CurrentPosition = TokenWordManager.Position;
            TokenWordManager.AddNew();
            state = "add";
        }

        private void EditButton_Click(object sender, EventArgs e)
        {
            textWord.ReadOnly = false;
            textWord.Focus();
        }

        private void CancelButton_Click(object sender, EventArgs e)
        {

            if (state == "add")
            {
                TokenWordManager.CancelCurrentEdit();
                TokenWordManager.Position = CurrentPosition;
            }
            else
            {
                TokenWordManager.CancelCurrentEdit();

            }

            MessageBox.Show("Transaction aborted ", "Save", MessageBoxButtons.OK, MessageBoxIcon.Information);

        }

        private void GoBack_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.OK;
            conn.Close();
            conn.Dispose();
        }
    }
}
