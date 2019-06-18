using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace frmTitles
{
    public partial class TableList : Form
    {
        public TableList()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            Form1 form1 = new Form1();

            form1.ShowDialog();
            this.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.OK;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            TokenizedWord form1 = new TokenizedWord();

            form1.ShowDialog();
            this.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.Hide();
            Language form1 = new Language();

            form1.ShowDialog();
            this.Show();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            this.Hide();
            Verb form1 = new Verb();

            form1.ShowDialog();
            this.Show();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            this.Hide();
            SynonymVerb form1 = new SynonymVerb();

            form1.ShowDialog();
            this.Show();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            this.Hide();
            SynonymNoun form1 = new SynonymNoun();

            form1.ShowDialog();
            this.Show();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            this.Hide();
            Statement form1 = new Statement();

            form1.ShowDialog();
            this.Show();
        }

        private void TableList_Load(object sender, EventArgs e)
        {

        }

        private void NounBtn_Click(object sender, EventArgs e)
        {
            this.Hide();
            Noun form1 = new Noun();

            form1.ShowDialog();
            this.Show();
        }

        private void PersonBtn_Click(object sender, EventArgs e)
        {
            this.Hide();
            Person form1 = new Person();

            form1.ShowDialog();
            this.Show();
        }

        private void PODBtn_Click(object sender, EventArgs e)
        {
            this.Hide();
            POD form1 = new POD();

            form1.ShowDialog();
            this.Show();
        }

        private void SourceBtn_Click(object sender, EventArgs e)
        {
            this.Hide();
            Source form1 = new Source();

            form1.ShowDialog();
            this.Show();
        }
    }
}
