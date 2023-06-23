import { send } from 'svelte-routing';
import { smtpServer, smtpPort, senderEmail, receiverEmail, smtpUsername, smtpPassword } from '$lib/env';

export async function post(request) {
  const form_data = request.body;

  // Create the email message
  const message = {
    from: senderEmail,
    to: receiverEmail,
    subject: 'Contact Form from zambelli.group',
    text: `
      Name: ${form_data.name}
      Email: ${form_data.email}
      Subject: ${form_data.subject}
      Message: ${form_data.message}
    `
  };

  try {
    // Connect to the SMTP server
    const server = createSMTPServer(smtpServer, smtpPort);
    await server.connect();

    // Login to your email account
    await server.login(smtpUsername, smtpPassword);

    // Send the email
    await server.send(message);

    // Disconnect from the server
    await server.disconnect();

    // Return a response indicating the success of form submission
    return send(response, 200, { message: 'Form submitted successfully!' });
  } catch (error) {
    // Handle any errors that occur during email sending
    return send(response, 500, { message: `Failed to submit form. Error: ${error.message}` });
  }
}
