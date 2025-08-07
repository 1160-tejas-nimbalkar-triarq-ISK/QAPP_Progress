package SanityTestcases;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.Test;

import base.BaseTest;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
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
public class createCSVFile extends BaseTest {


	

	    @Test
	    public void ACheckEncounters() throws InterruptedException, IOException {
	        driver.findElement(By.xpath(Loc.getProperty("RCMDocstab"))).click();
	        System.out.println("By clicking on RCMDocstab tab user will see by default RCMDocs screen/Dashboard ");
	        WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
	        Actions action = new Actions(driver);
	        action.moveToElement(encoutertrackingtab).perform();
	        WebElement Advancesearch = driver.findElement(By.id(Loc.getProperty("Advancesearch")));
	        Advancesearch.click();
	        driver.findElement(By.id(Loc.getProperty("btnApply"))).click();
	        Thread.sleep(1000);

	        try (FileWriter writer = new FileWriter("Encounters.csv")) {
	            writer.append("Year,Folder,Category,Client,Document Name,Current Status,Status\n");

	            for (int i = 1; i < 1000; i++) {
	                WebElement yearElement = driver.findElement(By.xpath(Loc.getProperty("Year") + "[" + i + "]"));
	                String year = yearElement.getText();
	                System.out.println("Year: " + year);

	                WebElement folderElement = driver.findElement(By.xpath(Loc.getProperty("Folder") + "[" + i + "]"));
	                String folder = folderElement.getText();
	                System.out.println("Folder: " + folder);

	                WebElement categoryElement = driver.findElement(By.xpath(Loc.getProperty("Categoryname") + "[" + i + "]"));
	                String category = categoryElement.getText();
	                System.out.println("Category: " + category);

	                WebElement clientElement = driver.findElement(By.xpath(Loc.getProperty("Clientname") + "[" + i + "]"));
	                String client = clientElement.getText();
	                System.out.println("Client: " + client);

	                WebElement documentNameElement = driver.findElement(By.xpath(Loc.getProperty("Documentname") + "[" + i + "]"));
	                String documentName = documentNameElement.getText();
	                System.out.println("Document Name: " + documentName);

	                WebElement currentStatusElement = driver.findElement(By.xpath(Loc.getProperty("CurrentStatus") + "[" + i + "]"));
	                String currentStatus = currentStatusElement.getText();
	                System.out.println("Current Status: " + currentStatus);

	                WebElement viewIcon = driver.findElement(By.xpath(Loc.getProperty("viewicon") + "[" + i + "]"));
	             //   Thread.sleep(1000);
	                viewIcon.click();
	                Thread.sleep(1000);

	                String status;
	                if (driver.findElements(By.xpath("//a[@role=\"tab\"]")).isEmpty()) {
	                    status = "Document is not processed Failed";
	                } else {
	                    status = "Document is processed successfully";
	                }
	                System.out.println("Status: " + status);

	                writer.append(String.join(",", year, folder, category, client, documentName, currentStatus, status));
	                writer.append("\n");

	                WebElement closeButton = driver.findElement(By.xpath(Loc.getProperty("Closebutton")));
	                closeButton.click();
	            }

	            System.out.println("Data has been written to the CSV file successfully.");
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	    }
	
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
   message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("shraddha.rakshe@triarqhealth.com"));
   //message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("shraddha.rakshe@triarqhealth.com,mayur.pawar@triarqhealth.com,juily.hardas@triarqhealth.com,sanket.sanap@triarqhealth.com,priyanka.nikam@triarqhealth.com"));
  //message.setRecipients(Message.RecipientType.CC, InternetAddress.parse("dhananjay.wagh@triarqhealth.com"));
   // Set Subject: header field
   message.setSubject("Testing Outlook email");
   
   // Create a multipart message
   MimeMultipart multipart = new MimeMultipart();
   
   // Create the text part
   MimeBodyPart textPart = new MimeBodyPart();
   textPart.setText("This is an email sent from Automation.Please find attacheched CSV file to check RCM encouters are processed or not."
   		+  "\n\n Thanks & Regards"
   		+ "\n\n Automation By Shraddha Rakshe"); 
   multipart.addBodyPart(textPart);
   
   // Attach the CSV file
   MimeBodyPart attachmentPart = new MimeBodyPart();
   String csvFilePath = "Encounters.csv"; // path of Excel file
   attachmentPart.attachFile(new File(csvFilePath));
   multipart.addBodyPart(attachmentPart);
   
   // Set the content of the message to be the multipart message
   message.setContent(multipart);
   
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


