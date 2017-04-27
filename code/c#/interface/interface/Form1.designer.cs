namespace WindowsFormsApp3
{
    partial class Form1
    {
        /// <summary>
        /// Variable nécessaire au concepteur.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Nettoyage des ressources utilisées.
        /// </summary>
        /// <param name="disposing">true si les ressources managées doivent être supprimées ; sinon, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Code généré par le Concepteur Windows Form

        /// <summary>
        /// Méthode requise pour la prise en charge du concepteur - ne modifiez pas
        /// le contenu de cette méthode avec l'éditeur de code.
        /// </summary>
        private void InitializeComponent()
        {
            this.url = new System.Windows.Forms.TextBox();
            this.freq = new System.Windows.Forms.RadioButton();
            this.lda = new System.Windows.Forms.RadioButton();
            this.ontologie = new System.Windows.Forms.RadioButton();
            this.HAC = new System.Windows.Forms.RadioButton();
            this.analyse = new System.Windows.Forms.Button();
            this.nb_sujets = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.num_question = new System.Windows.Forms.TextBox();
            this.trouve_questions = new System.Windows.Forms.Button();
            this.questions = new System.Windows.Forms.ListBox();
            this.label2 = new System.Windows.Forms.Label();
            this.question = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.sujets = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // url
            // 
            this.url.Location = new System.Drawing.Point(75, 52);
            this.url.Name = "url";
            this.url.Size = new System.Drawing.Size(448, 20);
            this.url.TabIndex = 0;
            this.url.Text = "URL du csv";
            // 
            // freq
            // 
            this.freq.AutoSize = true;
            this.freq.Location = new System.Drawing.Point(75, 79);
            this.freq.Name = "freq";
            this.freq.Size = new System.Drawing.Size(122, 17);
            this.freq.TabIndex = 1;
            this.freq.TabStop = true;
            this.freq.Text = "Analyse fréquentielle";
            this.freq.UseVisualStyleBackColor = true;
            // 
            // lda
            // 
            this.lda.AutoSize = true;
            this.lda.Location = new System.Drawing.Point(202, 79);
            this.lda.Name = "lda";
            this.lda.Size = new System.Drawing.Size(86, 17);
            this.lda.TabIndex = 2;
            this.lda.TabStop = true;
            this.lda.Text = "Analyse LDA";
            this.lda.UseVisualStyleBackColor = true;
            // 
            // ontologie
            // 
            this.ontologie.AutoSize = true;
            this.ontologie.Location = new System.Drawing.Point(294, 79);
            this.ontologie.Name = "ontologie";
            this.ontologie.Size = new System.Drawing.Size(120, 17);
            this.ontologie.TabIndex = 3;
            this.ontologie.TabStop = true;
            this.ontologie.Text = "Analyse ontologique";
            this.ontologie.UseVisualStyleBackColor = true;
            // 
            // HAC
            // 
            this.HAC.AutoSize = true;
            this.HAC.Location = new System.Drawing.Point(420, 78);
            this.HAC.Name = "HAC";
            this.HAC.Size = new System.Drawing.Size(87, 17);
            this.HAC.TabIndex = 4;
            this.HAC.TabStop = true;
            this.HAC.Text = "Analyse HAC";
            this.HAC.UseVisualStyleBackColor = true;
            // 
            // analyse
            // 
            this.analyse.Location = new System.Drawing.Point(259, 191);
            this.analyse.Name = "analyse";
            this.analyse.Size = new System.Drawing.Size(75, 23);
            this.analyse.TabIndex = 5;
            this.analyse.Text = "Analyser";
            this.analyse.UseVisualStyleBackColor = true;
            // 
            // nb_sujets
            // 
            this.nb_sujets.Location = new System.Drawing.Point(343, 157);
            this.nb_sujets.Name = "nb_sujets";
            this.nb_sujets.Size = new System.Drawing.Size(24, 20);
            this.nb_sujets.TabIndex = 11;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(199, 160);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(134, 13);
            this.label3.TabIndex = 12;
            this.label3.Text = "Nombre de sujets à trouver";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(199, 128);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(89, 13);
            this.label1.TabIndex = 13;
            this.label1.Text = "Numéro Question";
            // 
            // num_question
            // 
            this.num_question.Location = new System.Drawing.Point(343, 125);
            this.num_question.Name = "num_question";
            this.num_question.Size = new System.Drawing.Size(24, 20);
            this.num_question.TabIndex = 14;
            // 
            // trouve_questions
            // 
            this.trouve_questions.Location = new System.Drawing.Point(529, 49);
            this.trouve_questions.Name = "trouve_questions";
            this.trouve_questions.Size = new System.Drawing.Size(163, 23);
            this.trouve_questions.TabIndex = 15;
            this.trouve_questions.Text = "Trouver questions ouvertes";
            this.trouve_questions.UseVisualStyleBackColor = true;
            this.trouve_questions.Click += new System.EventHandler(this.trouve_questions_Click);
            // 
            // questions
            // 
            this.questions.FormattingEnabled = true;
            this.questions.Location = new System.Drawing.Point(529, 128);
            this.questions.Name = "questions";
            this.questions.Size = new System.Drawing.Size(120, 95);
            this.questions.TabIndex = 16;
            this.questions.Visible = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(72, 265);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(49, 13);
            this.label2.TabIndex = 17;
            this.label2.Text = "Question";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // question
            // 
            this.question.AutoSize = true;
            this.question.Location = new System.Drawing.Point(72, 301);
            this.question.Name = "question";
            this.question.Size = new System.Drawing.Size(0, 13);
            this.question.TabIndex = 18;
            this.question.Visible = false;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(199, 265);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(36, 13);
            this.label6.TabIndex = 20;
            this.label6.Text = "Sujets";
            // 
            // sujets
            // 
            this.sujets.FormattingEnabled = true;
            this.sujets.Location = new System.Drawing.Point(186, 281);
            this.sujets.Name = "sujets";
            this.sujets.Size = new System.Drawing.Size(120, 95);
            this.sujets.TabIndex = 21;
            this.sujets.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(739, 430);
            this.Controls.Add(this.sujets);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.question);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.questions);
            this.Controls.Add(this.trouve_questions);
            this.Controls.Add(this.num_question);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.nb_sujets);
            this.Controls.Add(this.analyse);
            this.Controls.Add(this.HAC);
            this.Controls.Add(this.ontologie);
            this.Controls.Add(this.lda);
            this.Controls.Add(this.freq);
            this.Controls.Add(this.url);
            this.Name = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox url;
        private System.Windows.Forms.RadioButton freq;
        private System.Windows.Forms.RadioButton lda;
        private System.Windows.Forms.RadioButton ontologie;
        private System.Windows.Forms.RadioButton HAC;
        private System.Windows.Forms.Button analyse;
        private System.Windows.Forms.TextBox nb_sujets;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox num_question;
        private System.Windows.Forms.Button trouve_questions;
        private System.Windows.Forms.ListBox questions;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label question;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.ListBox sujets;
    }
}

