namespace frmTitles
{
    partial class Menu
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.AccessData = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.QuitBtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // AccessData
            // 
            this.AccessData.Location = new System.Drawing.Point(146, 60);
            this.AccessData.Name = "AccessData";
            this.AccessData.Size = new System.Drawing.Size(134, 23);
            this.AccessData.TabIndex = 0;
            this.AccessData.Text = "AccessData";
            this.AccessData.UseVisualStyleBackColor = true;
            this.AccessData.Click += new System.EventHandler(this.AccessData_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(146, 132);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(134, 23);
            this.button1.TabIndex = 1;
            this.button1.Text = "PersonalizedSQLQueries";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // QuitBtn
            // 
            this.QuitBtn.Location = new System.Drawing.Point(146, 200);
            this.QuitBtn.Name = "QuitBtn";
            this.QuitBtn.Size = new System.Drawing.Size(134, 23);
            this.QuitBtn.TabIndex = 2;
            this.QuitBtn.Text = "Quit";
            this.QuitBtn.UseVisualStyleBackColor = true;
            this.QuitBtn.Click += new System.EventHandler(this.QuitBtn_Click);
            // 
            // Menu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(438, 309);
            this.Controls.Add(this.QuitBtn);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.AccessData);
            this.Name = "Menu";
            this.Text = "Menu";
            this.Load += new System.EventHandler(this.Menu_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button AccessData;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button QuitBtn;
    }
}