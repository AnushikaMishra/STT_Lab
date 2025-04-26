using System;

namespace lab12_2
{
    public partial class Form1 : Form
    {
        private DateTime targetTime;
        private Random random = new Random();

        public Form1()
        {
            InitializeComponent();
        }
        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.BackColor = Color.FromArgb(random.Next(256), random.Next(256), random.Next(256));

            if (DateTime.Now.ToString("HH:mm:ss") == targetTime.ToString("HH:mm:ss"))
            {
                timer1.Stop();
                MessageBox.Show("Target time reached!");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (DateTime.TryParse(textBox1.Text, out targetTime))
            {
                timer1.Start();
            }
            else
            {
                MessageBox.Show("Invalid time format! Please enter in HH:MM:SS format.");
            }
        }
    }
}
