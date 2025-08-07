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
public class openbatchissue2 extends BaseTest{
	
	@Test
    public void AClickOnQCmainTab() throws InterruptedException, IOException {
        driver.findElement(By.xpath(Loc.getProperty("RCMDocstab"))).click();
        System.out.println("By clicking on RCMDocstab tab user will see by default RCMDocs screen/Dashboard ");
        WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
        Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        WebElement encouterters = driver.findElement(By.id(Loc.getProperty("Encounters")));
        encouterters.click();
        Thread.sleep(2000);

        Workbook workbook = new XSSFWorkbook();
        org.apache.poi.ss.usermodel.Sheet sheet = workbook.createSheet("Data");
        Row headerRow = sheet.createRow(0);
        headerRow.createCell(0).setCellValue("Document Name");
        headerRow.createCell(1).setCellValue("Status");
        
        for (int i = 1; i < 300; i++) {
        	
        	
            WebElement documentNameElement = driver.findElement(By.xpath(Loc.getProperty("Documentname") + "[" + i + "]"));
            String documentName = documentNameElement.getText();
            System.out.println("Document Name: " + documentName);

            WebElement viewIcon = driver.findElement(By.xpath(Loc.getProperty("viewicon") + "[" + i + "]"));
            Thread.sleep(2000);
            viewIcon.click();
            Thread.sleep(2000);

            List<WebElement> pageDisplayed = driver.findElements(By.xpath("//a[@role=\"tab\"]"));
            String status;
            if (pageDisplayed.isEmpty()) {
                status = "Document is not processed Failed";
            } else {
                status = "Document is processed successfully";
            }
            System.out.println("Status: " + status);

            Row row = sheet.createRow(i);
            row.createCell(0).setCellValue(documentName);
            row.createCell(1).setCellValue(status);

            WebElement closeButton = driver.findElement(By.xpath(Loc.getProperty("Closebutton")));
            closeButton.click();
        

        try (FileOutputStream fileOut = new FileOutputStream("C:\\Users\\shraddha.rakshe\\Documents\\data.xlsx")) {
            workbook.write(fileOut);
            System.out.println("Data has been written to the Excel file successfully.");
        } catch (IOException e) {
            e.printStackTrace();
        } 
        }
    	try {
        workbook.close();
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
            
            // Set Subject: header field
            message.setSubject("Testing Outlook email");
            
            // Create a multipart message
            MimeMultipart multipart = new MimeMultipart();
            
            // Create the text part
            MimeBodyPart textPart = new MimeBodyPart();
            textPart.setText("This is a test email sent from Java.");
            multipart.addBodyPart(textPart);
            
            // Attach the CSV file
            MimeBodyPart attachmentPart = new MimeBodyPart();
            String csvFilePath = "C:\\Users\\shraddha.rakshe\\Documents\\data.xlsx"; // path of Excel file
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
	
	
	
	
	
