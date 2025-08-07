package ReportMail;
import javax.mail.*;
import javax.mail.internet.*;
import java.util.Properties;

public class EmailSender {
    public static void main(String[] args) {
    	final String username = "noreply@triarqhealth.com"; // Your email address
        final String password = "d[Mxs&H#[Kp95mg6"; // Your password
        
        // Set properties for Outlook SMTP server
        Properties props = new Properties();
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.host", "smtp.office365.com"); // Outlook SMTP server
        props.put("mail.smtp.port", "587"); // Port for TLS
        
        // Get session with authentication
        Session session = Session.getInstance(props, new Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });
        
        try {
            // Create a default MimeMessage object
            Message message = new MimeMessage(session);
            
            // Set From: header field of the header.
            message.setFrom(new InternetAddress(username));
            
            // Set To: header field of the header.
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("shraddha.rakshe@triarqhealth.com"));
            
            // Set Subject: header field
            message.setSubject("Testing Outlook email");
            
            // Now set the actual message
            message.setText("This is a test email sent from Java.1");
            
            // Send message
            Transport.send(message);
            
            System.out.println("Email sent successfully");
            
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }
}
}