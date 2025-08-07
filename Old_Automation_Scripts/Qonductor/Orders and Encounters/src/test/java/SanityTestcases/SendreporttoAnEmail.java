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
import java.nio.file.AccessDeniedException;

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
public class SendreporttoAnEmail {
	
	
	
	@Test
         public  void Bmailsend() throws InterruptedException {
		final String username = "noreply@triarqhealth.com"; // Your email address
        final String password = "RWv~rq;hzC3b=Xtp"; // Your password
        
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
            
            // Create a multipart message
            MimeMultipart multipart = new MimeMultipart();
            
            // Create the text part
            MimeBodyPart textPart = new MimeBodyPart();
            textPart.setText("This is an email sent from Automation.Please find attacheched html report."
            		+  "\n\n Thanks & Regards"
            		+ "\n\n Automation By Shraddha Rakshe");   
            multipart.addBodyPart(textPart);  
            
            // Attach the CSV file
            MimeBodyPart attachmentPart = new MimeBodyPart();
            
            Thread.sleep(3000);
            String reportFilePath = "C:\\Users\\shraddha.rakshe\\Old Eclips\\eclipse-workspace\\Qonductor Sanity\\TestAutomationForQonductorSanity\\test-output\\emailable-report.html"; // path of Excel file
            attachmentPart.attachFile(new File(reportFilePath));
            multipart.addBodyPart(attachmentPart);
            
            // Set the content of the message to be the multipart message
            message.setContent(multipart);
            
            // Send message
            Transport.send(message);
            
            System.out.println("Email sent successfully");
            
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        } catch (IOException  e) {
            e.printStackTrace();
        }
    }
}
	
	
	
	
	

