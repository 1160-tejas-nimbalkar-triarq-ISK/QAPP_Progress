package SanityTestcases;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Properties;

import javax.mail.Authenticator;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;

import org.apache.commons.collections4.map.HashedMap;
import org.apache.poi.sl.usermodel.Sheet;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.Test;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;
import base.BaseTest;
import java.io.File;
public class sentEmailonly {
	
	
	
	@Test
         public  void Bmailsend() {
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
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("shraddha.rakshe@triarqhealth.com,saurabh.Kunjir@triarqhealth.com"));
            
            // Set Subject: header field
            message.setSubject("Testing Outlook email");
            
            
            // Set HTML content
            String htmlContent = "\r\n"
            		+ "\r\n"
            		+ "      <h5>Hello All,</h5>\r\n"
            		+ "      \r\n"
            		+ "      <p>RCM Encounters verification done on  <div id=\"datetime\"></div></p>\r\n"
            		+ "\r\n"
            		+ "    <script>\r\n"
            		+ "        // Get the current date and time\r\n"
            		+ "        var currentDateTime = new Date();\r\n"
            		+ "\r\n"
            		+ "        // Format the date and time to display in Indian standard time\r\n"
            		+ "        var options = { timeZone: 'Asia/Kolkata' };\r\n"
            		+ "        var formattedDateTime = currentDateTime.toLocaleString('en-IN', options);\r\n"
            		+ "\r\n"
            		+ "        // Display the formatted date and time on the webpage\r\n"
            		+ "        document.getElementById(\"datetime\").innerHTML = formattedDateTime;\r\n"
            		+ "    </script>\r\n"
            		+ "   <p>Please find the attached CSV file which contains all encounters list.</p>\r\n"
            		+ "      <p><strong><em>Disclaimer:</em></strong></p><ul><li><em>This is an auto-generated email hence no need to reply.</em></li></ul>\r\n"
            		+ "      <p><strong>Regards,</strong><br />Qonductor Administrator</p>\r\n";
            		
            // Set the email content
            message.setContent(htmlContent, "text/html");
            // Create a multipart message
            MimeMultipart multipart = new MimeMultipart();
//            
//            // Create the text part
//            MimeBodyPart textPart = new MimeBodyPart();
//            textPart.setText("This is a test email sent from Java.");
//            multipart.addBodyPart(textPart);
            
            // Attach the CSV file
            MimeBodyPart attachmentPart = new MimeBodyPart();
            String csvFilePath = "Encounters.csv"; // path of Excel file
            attachmentPart.attachFile(new File(csvFilePath));
            multipart.addBodyPart(attachmentPart);
            
            // Set the content of the message to be the multipart message
          //  message.setContent(multipart);
            
            // Send message
            Transport.send(message);
            
            System.out.println("Email sent successfully");
            
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
	
	
	
	
	
