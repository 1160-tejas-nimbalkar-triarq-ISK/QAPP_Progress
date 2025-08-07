package automation_ss;

import java.time.Duration;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
//import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
import com.github.javafaker.Faker;

import io.github.bonigarcia.wdm.WebDriverManager;
public class ExistingPatientWithNoNpdate {
    WebDriver driver;
    ExtentReports extent;
      ExtentTest test;
      //ExtentHtmlReporter htmlReporter;
      Faker faker = new Faker();
      private WebDriverWait wait;

          
//  @Test(enabled = false)
//  public void Verify_Clik_BookAppointment_Button() throws InterruptedException {

	  	  
// 	    WebElement BookappointmentButtom = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'Book Appointment')]"));
	  	  
// 	  	 BookappointmentButtom.click();
	  	   
// 	  	 driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS); 
	  	 
// 	  	  WebElement Dashboardpage = driver.findElement(By.xpath("//html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment/div/div[1]/div/div[1]"));
	  	  
// 	        Assert.assertTrue(Dashboardpage.isDisplayed(), "User not on Dashboard page");
	       
	  	
	  	  
// 	        Thread.sleep(5000);
	  	     
// 	    }
 
 //Click on Existing patient tab
 
 @Test(priority=2)    
 
 public void Verify_Click_Existing_patient_Tab() throws InterruptedException {

	  WebElement ExistingPatient = driver.findElement(By.xpath("//span[@class='k-link ng-star-inserted'][contains(.,'Returning Patient')]"));
	
	ExistingPatient.click(); 
	  
	 Thread.sleep(3000);
     
	 // driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS); 
	  

 }
  
 //Select appointment type
 
 @Test(priority=3)
 public void Verify_Appointment_Type() throws InterruptedException 
 {
	 
	 
	 WebElement dropdownElement = driver.findElement(By.xpath("//kendo-icon[contains(@class,'k-i-caret-alt-down k-icon ng-star-inserted')]"));
	 
	 dropdownElement.click();
	 Thread.sleep(2000);
	 WebElement APP_type=driver.findElement(By.xpath("//input[contains(@placeholder,'Appointment Type *')]"));
	 APP_type.click();
	 APP_type.sendKeys("NEW PATIENT");
	 APP_type.sendKeys(Keys.ENTER);
	 Thread.sleep(2000);
	
 }
	
 //In this Test case we have fetching values from excel (Username and password)
 
  @Test(priority=4)
  public void loginTest()throws InterruptedException 
  {
      String[] credentials = Utils.getCredentials("Sheet1", 1);
      String username = credentials[0];
      String password = credentials[1];
   
      WebElement ExUsername = driver.findElement(By.xpath("//input[contains(@placeholder,'Username')]"));
      ExUsername.click();
      ExUsername.sendKeys(username);
      Thread.sleep(2000);
      
      WebElement Expass = driver.findElement(By.xpath("//input[contains(@placeholder,'Password')]"));
      Expass.click();
      Expass.sendKeys(password);
      Thread.sleep(2000);
  }
  
  //Click on Find appointment button
  
  @Test(priority=5)
  public void Click_ON_FindAppointment_Button()throws InterruptedException 
  {
      
      WebElement FIndAppointment_Button = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'Find Appointment')]"));
      FIndAppointment_Button.click();
      Thread.sleep(5000);
     
      WebElement ValidationText = driver.findElement(By.xpath("//ion-text[@class='h3-Montserrat text-blue-color md hydrated'][contains(.,'Pick an available time')]"));
	  
 	 System.out.println("ValidationText: " + ValidationText.getText());
 	  
 	  String actualText = ValidationText.getText();
 	     String expectedText = "Pick an available time";
 	     
 	     Assert.assertEquals(actualText, expectedText, "Strings are not equal!");   
 	     
 	     Thread.sleep(1000);
      
  }
  
  //Enter Location in Location field
  
  @Test(enabled = false)
  public void Enter_Location_Existing() throws InterruptedException 
  {
 	 
 	 
 	 WebElement dropdownElement = driver.findElement(By.xpath("(//kendo-icon[contains(@class,'k-i-caret-alt-down k-icon ng-star-inserted')])[2]"));
 	 
 	 dropdownElement.click();
 	 Thread.sleep(5000);
 	 
 	 WebElement APP_type=driver.findElement(By.xpath("//input[contains(@placeholder,'Any location')]"));
 	 APP_type.click();
 	 APP_type.sendKeys("Main Location");
 	 APP_type.sendKeys(Keys.ENTER);
 	 Thread.sleep(5000);
  
  }
  
  
 //Enter Provider in Provider field
  
  @Test(enabled = false)
  public void Enter_Provider_Existing() throws InterruptedException 
  {
 	 
 	 
 	 WebElement dropdownElement = driver.findElement(By.xpath("(//kendo-icon[contains(@class,'k-i-caret-alt-down k-icon ng-star-inserted')])[3]"));
 	 
 	 dropdownElement.click();
	 Thread.sleep(1000);
 	 
 	 WebElement APP_type=driver.findElement(By.xpath("//input[contains(@placeholder,'Any provider')]"));
 	 APP_type.click();
 	 APP_type.sendKeys("Airiel Lungley");
 	 APP_type.sendKeys(Keys.ENTER);
 	 Thread.sleep(5000);
  
  }
  
  //clear provider and location
  
  @Test(enabled = false)
  public void Verify_Existing_Clear_provider_and_Location() throws InterruptedException  
  {
 	 
 WebElement Clrearpovider = driver.findElement(By.xpath("(//kendo-icon[contains(@class,'k-i-x k-icon ng-star-inserted')])[3]"));
 	 
 	 Clrearpovider.click();
 	 
 	 Thread.sleep(4000);
 	 
  WebElement ClrearLocation = driver.findElement(By.xpath("(//kendo-icon[contains(@class,'k-i-x k-icon ng-star-inserted')])[2]"));
 	 
  ClrearLocation.click();
  
  Thread.sleep(4000);
  
 /* WebElement Timeoftheday = driver.findElement(By.xpath("//span[@class='k-button-text'][contains(.,'Any time')]"));
  
  Timeoftheday.click();
  
  Thread.sleep(3000);*/
  	  
  }
 
  
  @Test(priority=9)
  public void Verify_Select_available_date_from_calendar() throws InterruptedException  {
 	    
 	 WebElement select_next = driver.findElement(By.xpath("//ion-icon[@src='../../../../../assets/svg/chevron-right.svg']"));
 	 
 	 select_next.click();
 	 
 	 Thread.sleep(3000);
 	 
 	  WebElement ValidationText = driver.findElement(By.xpath("//ion-text[@color='gray80'][contains(.,'Main Location')]"));
 	  
 	 System.out.println("ValidationText: " + ValidationText.getText());
 	  
 	  String actualText = ValidationText.getText();
 	     String expectedText = "Main Location";
 	     
 	     Assert.assertEquals(actualText, expectedText, "No slot available!");
 	     
 	     Thread.sleep(2000); 
  }
  
  
  @Test(priority=10)
  public void Verify_To_select_Available_Slots() throws InterruptedException 
  {
 	 WebElement SelectSlot = driver.findElement(By.xpath("(//ion-text[contains(@class,'bodyM-txt-medium montserrat ion-color-primary100 md hydrated')])[1]"));
 	 
 	 SelectSlot.click();
 	 
 WebElement Nexttbutton = driver.findElement(By.xpath("(//ion-text[contains(@class,'bodyM-txt-medium montserrat ion-color-primary100 md hydrated')])[1]"));
      
    
      
      Assert.assertTrue(Nexttbutton.isEnabled(), "Next Button should be enable after select available slot");
      
     Thread.sleep(3000); 
  }
  
  
  
  @Test(priority=11)
  public void Verify_Click_Next_Button() throws InterruptedException {

 	  
  WebElement NextButtom = driver.findElement(By.xpath("//ion-text[@color='white'][contains(.,'Next')]"));
 	  
       NextButtom.click();
 	   
 	  Thread.sleep(1000);
 	 
 	  WebElement Patientinfomation = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/patient-information"));
 	  
      Assert.assertTrue(Patientinfomation.isDisplayed(), "User not on Patient information page");
      Thread.sleep(2000); 
  }
  
  
  @Test(priority=12)
  public void Verify_Click_yes_Button_Demographics() throws InterruptedException {

 	  
  WebElement yesButtom = driver.findElement(By.xpath("(//ion-text[@class='pr-10 md hydrated'][contains(.,'Yes')])[1]"));
 	  
  yesButtom.click();
 	   
 	  Thread.sleep(5000);
 	 
  }
  
  @Test(priority=13)
  
  public void Verify_Yes_Insurance() throws InterruptedException{
	  WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
	  WebElement Yes_Button = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("(//ion-text[@class='pr-10 md hydrated'][contains(.,'Yes')])[2]")));
	  Yes_Button.click();
	  
	  /*WebElement Yes_Button= driver.findElement(By.xpath("(//ion-text[@class='pr-10 md hydrated'][contains(.,'Yes')])[2]"));
	  Actions actions = new Actions(driver);
	  actions.doubleClick(Yes_Button).perform();*/
	
	  Thread.sleep(5000);
	  
  }
  
  

  @Test(priority=14)
  public void Verify_Next_Button_PT() throws InterruptedException {
  	
  	WebElement Next_Button= driver.findElement(By.xpath("//ion-text[@color='white'][contains(.,'Next')]"));
  	
  	Next_Button.click(); 
  	
  	Thread.sleep(3000);

  }
   
	
	  @BeforeClass
	  public  void beforeClass() throws InterruptedException {
		  
		  WebDriverManager.chromedriver().setup();
		  
			 driver=new ChromeDriver();
			  
			 /* WebDriverManager.firefoxdriver().setup();
			  
			   driver=new FirefoxDriver();*/
			  
			 driver.manage().window().maximize();
			 driver.manage().deleteAllCookies();
			 
			

			 
		driver.get("https://qschedule-qa.myqone.com/patient-appointment/f1f64c71-91e9-11eb-b050-4578cb1636b4");
			 
			 
			 Thread.sleep(3000);
			 
			 driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	  }

	@AfterClass
	  public void afterClass() throws InterruptedException {
		  Thread.sleep(5000);
		 driver.quit();
		
	  }

}
