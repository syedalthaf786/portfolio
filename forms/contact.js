// contact.js (serverless function)
import nodemailer from 'nodemailer';

const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 587,
  secure: false, // or 'STARTTLS'
  auth: {
    user: '',
    pass: '',
  },
});

export default async function handler(req, res) {
  const { name, email, subject, message } = req.body;

  // Validate form data
  if (!name || !email || !subject || !message) {
    return res.status(400).json({ error: 'All fields are required' });
  }

  // Send email using Nodemailer
  try {
    const mailOptions = {
      from: email,
      to: 'recipient-email@example.com',
      subject,
      text: message,
    };

    await transporter.sendMail(mailOptions);
    return res.status(200).json({ message: 'Form submitted successfully!' });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Failed to send email' });
  }
}
