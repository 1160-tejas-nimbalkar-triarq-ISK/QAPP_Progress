package automation_ss;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
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
import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
import com.aventstack.extentreports.reporter.ExtentReporter;
import com.github.javafaker.Faker;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Returningpatient {
    WebDriver driver;
	  ExtentReports extent;
	    ExtentTest test;
	   ExtentReporter htmlReporter;
	    Faker faker = new Faker();
	    private WebDriverWait wait;
	    
	  
	  //Verify Book appointment button 
	    
   @Test(enabled = false)
   public void Verify_Clik_BookAppointment_Button() throws InterruptedException {

	  	  
	    WebElement BookappointmentButtom = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'Book Appointment')]"));
	  	  
	  	 BookappointmentButtom.click();
	  	   
	  	 driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS); 
	  	 
	  	  WebElement Dashboardpage = driver.findElement(By.xpath("//html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment/div/div[1]/div/div[1]"));
	  	  
	        Assert.assertTrue(Dashboardpage.isDisplayed(), "User not on Dashboard page");
	       
	  	
	  	  
	        Thread.sleep(5000);
	  	     
	    }
   
   //Click on Existing patient tab
   
   @Test(priority=2)    
   
   public void Verify_Click_Existing_patient_Tab() throws InterruptedException {

  	  WebElement ExistingPatient = driver.findElement(By.xpath("//span[contains(.,'Returning Patient')]"));
  	
  	ExistingPatient.click(); 
  	  
  	 Thread.sleep(5000);
       
  	 // driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS); 
  	  
 
   }
    
   //Select appointment type
   
   @Test(priority=3)
   public void Verify_Appointment_Type() throws InterruptedException 
   {
  	 
  	 
  	 WebElement dropdownElement = driver.findElement(By.xpath("//kendo-icon[contains(@class,'k-i-caret-alt-down k-icon ng-star-inserted')]"));
  	 
  	 dropdownElement.click();
  	 Thread.sleep(3000);
  	 WebElement APP_type=driver.findElement(By.xpath("//input[contains(@placeholder,'Appointment Type *')]"));
  	 APP_type.click();
  	 APP_type.sendKeys("NEW PATIENT");
  	 APP_type.sendKeys(Keys.ENTER);
  	 Thread.sleep(3000);

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
        Thread.sleep(3000);
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
   	     
   	     Thread.sleep(5000);
        
    }
    
    //Enter Location in Location field
    
    @Test(priority=6)
    public void Enter_Location_Existing() throws InterruptedException 
    {
   	 
		WebElement Location = driver.findElement(By.xpath("//input[contains(@placeholder,'Any location')]"));
		Location.click();
		Location.sendKeys("Main Location");
		Location.sendKeys(Keys.ENTER);
		Thread.sleep(4000);
		
		
		
    
    }
    
    
   //Enter Provider in Provider field
    
    @Test(priority=7)
    public void Enter_Provider_Existing() throws InterruptedException 
    {
   	 
   	 WebElement APP_type=driver.findElement(By.xpath("//input[contains(@placeholder,'Any provider')]"));
   	 APP_type.click();
   	 APP_type.sendKeys("Airiel Lungley");
   	 APP_type.sendKeys(Keys.ENTER);
   	 Thread.sleep(5000);
    
    }
    
    //clear provider and location
    
    @Test(priority=8)
    public void Verify_Existing_Clear_provider_and_Location() throws InterruptedException  
    {

   	 Thread.sleep(2000);
            
        WebElement ClrearLocation = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment-time/div/div[2]/div/div/div[1]/div[2]/kendo-combobox/span/kendo-icon-wrapper/kendo-icon"));
            
        ClrearLocation.click();
        
        Thread.sleep(5000);
        WebElement Clrearpovider = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment-time/div/div[2]/div/div/div[1]/div[3]/kendo-combobox/span/kendo-icon-wrapper/kendo-icon"));
            
            Clrearpovider.click();
       
        
        Thread.sleep(7000);
    	  
    }
   
    
    @Test(priority=9)
    public void Verify_Select_available_date_from_calendar() throws InterruptedException  {
   	    
   	 WebElement select_next = driver.findElement(By.xpath("//ion-icon[@src='../../../../../assets/svg/chevron-right.svg']"));
   	 
   	 select_next.click();
   	 
   	 Thread.sleep(3000);
   	 
    }
    
    
    @Test(priority=10)
    public void Verify_To_select_Available_Slots() throws InterruptedException 
    {
   	 WebElement SelectSlot = driver.findElement(By.xpath("(//ion-text[contains(@class,'bodyM-txt-medium montserrat ion-color-primary100 md hydrated')])[1]"));
   	 
   	 SelectSlot.click();
   	 
//    WebElement Nexttbutton = driver.findElement(By.xpath("(//ion-text[contains(@class,'bodyM-txt-medium montserrat ion-color-primary100 md hydrated')])[1]"));
        
      
        
//         Assert.assertTrue(Nexttbutton.isEnabled(), "Next Button should be enable after select available slot");
        
       Thread.sleep(3000); 
    }
    
    
    
    @Test(priority=11)
    public void Verify_Click_Next_Button() throws InterruptedException {

   	  
    WebElement NextButtom = driver.findElement(By.xpath("//ion-text[@color='white'][contains(.,'Next')]"));
   	  
         NextButtom.click();
   	   
   	  Thread.sleep(4000);
   	 
   	//   WebElement Patientinfomation = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/patient-information"));
   	  
    //     Assert.assertTrue(Patientinfomation.isDisplayed(), "User not on Patient information page");
    //     Thread.sleep(2000); 
    }
    
    
    @Test(priority=12)
    public void Verify_Click_No_Button() throws InterruptedException {

   	  
    WebElement NoButtom = driver.findElement(By.xpath("(//ion-button[@fill='outline'][contains(.,'No')])[1]"));
   	  
    NoButtom.click();
   	   
   	  Thread.sleep(3000);

	       
		 WebElement popupContent = driver.findElement(By.xpath("//div[@class='pb-20 overflowY md-popup-content'][contains(.,'Please fill in all of this information Email AddressFirst NameLast NamePreferred Name (Optional)Date of birthSEX*MaleFemaleOtherAddressZIP Codeprimary phone phone type')]"));
       
		 // Scroll down within the popup content using JavaScript Executor
		 JavascriptExecutor js = (JavascriptExecutor) driver;
		 js.executeScript("arguments[0].scrollTop = arguments[0].scrollHeight", popupContent);
	
		 // Wait a moment for the scroll to take effect
		 Thread.sleep(3000);  // Adjust timing if needed
	
		 // Verify if the content has been scrolled (you can check if the scroll position has changed)
		 long scrollTop = (Long) js.executeScript("return arguments[0].scrollTop;", popupContent);
	
		 Thread.sleep(3000);
   	 
    }
    
    
    
    @Test(priority=13)
    public void Verify_update_Demographics() throws InterruptedException {

    	 String newAddress = faker.address().streetAddress();
         String newZipCode = faker.address().zipCode();
         
         WebElement addressField = driver.findElement(By.xpath("//input[contains(@placeholder,'Address 1')]")); 
    	 WebElement addressField2 = driver.findElement(By.xpath("//input[contains(@placeholder,'Address 2')]"));
    	 WebElement zipCodeField = driver.findElement(By.xpath("//input[contains(@placeholder,'ZIP Code*')]"));
    	 
    	 addressField.clear(); 
		 Thread.sleep(1000);
    	 addressField2.clear();
    	  Thread.sleep(2000);
    	 
    	 addressField.sendKeys(newAddress);
		 Thread.sleep(1000);
    	 addressField2.sendKeys(newAddress);
    	 Thread.sleep(2000);
    	 
    	 zipCodeField.clear();
    	 Thread.sleep(2000);
    	 zipCodeField.sendKeys(newZipCode);
    	 Thread.sleep(2000);
    	 
    	 WebElement Done_Button = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'done')]")); 
    	 Done_Button.click();
   	 
    	 Thread.sleep(5000);
    }
    
    @Test(priority=14)
    public void Verify_Click_No_Button_Insurance() throws InterruptedException {

   	  
    WebElement NoButton = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'No')]"));
   	  
    NoButton.click();
   	   
   	  Thread.sleep(2000);

		 Thread.sleep(3000);
		 WebElement ScrollContent = driver.findElement(By.xpath("(//div[contains(.,'InsuranceINSURANCE CARRIERINSURERMember numberGroup numberPolicy holder Self Someone elseSubscriber NameDate of birthGender')])[7]"));
	
		 // Scroll down within the popup content using JavaScript Executor
		 JavascriptExecutor js = (JavascriptExecutor) driver;
		 js.executeScript("arguments[0].scrollTop = arguments[0].scrollHeight", ScrollContent);
	
		 // Wait a moment for the scroll to take effect
		 Thread.sleep(3000);  // Adjust timing if needed
	
		 // Verify if the content has been scrolled (you can check if the scroll position has changed)
		 long scrollTop = (Long) js.executeScript("return arguments[0].scrollTop;", ScrollContent);
		 Thread.sleep(5000);

	  
    	 
    }
	

    @Test(priority=15)
    public void Verify_update_Insurance() throws InterruptedException {
   
    	
    	WebElement Update_Group_Number= driver.findElement(By.xpath("//input[contains(@placeholder,'Group Number')]"));
    	
    	Update_Group_Number.clear(); 
    	
    	Thread.sleep(2000);
    	Update_Group_Number.sendKeys("RT4A6");
    	Thread.sleep(2000);
       	
    	WebElement Done_Button= driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'done')]"));
    	    	
    	Done_Button.click(); 

    	Thread.sleep(7000);
    	    
    	
    	
    }
	@Test(priority=16)
	public void Verify_Scroller()throws InterruptedException {
	   WebElement kendoScrollable = driver.findElement(By.xpath("(//div[contains(@class,'body')])[2]"));
   
	   JavascriptExecutor js = (JavascriptExecutor) driver;
   
	   // Scroll to the bottom of the Kendo Scrollable element
	   js.executeScript("arguments[0].scrollTop = arguments[0].scrollHeight;", kendoScrollable);
   
	   // Verify the scroll position
	   Long scrollTop = (Long) js.executeScript("return arguments[0].scrollTop;", kendoScrollable);
	   Long scrollHeight = (Long) js.executeScript("return arguments[0].scrollHeight;", kendoScrollable);
   
	   assert scrollTop.equals(scrollHeight - kendoScrollable.getSize().getHeight()) 
		   : "The scrollbar did not reach the bottom.";
		   Thread.sleep(5000);
	}

    
    @Test(priority=17)
    public void Verify_Next_Button_PT() throws InterruptedException {
    	
    	WebElement Next_Button= driver.findElement(By.xpath("//ion-text[@color='white'][contains(.,'Next')]"));
    	
    	Next_Button.click(); 
    	
    	Thread.sleep(3000);
 
    }
	@Test(priority=18)
        public void Previous_Button_Click()throws InterruptedException {
          
           
            WebElement PreviousButton_Click = driver.findElement(By.xpath("//ion-text[contains(.,'Previous')]"));
             
            PreviousButton_Click.click(); 
            
            Thread.sleep(8000);
            
            WebElement Next_button_confirmation_section = driver.findElement(By.xpath("//ion-button[contains(.,'Next')]"));
            
            Next_button_confirmation_section.click(); 
            
            Thread.sleep(4000);
        }
		@Test(priority=19)
        public void Additional_note()throws InterruptedException {
          
            WebElement Add_note_field = driver.findElement(By.xpath("//textarea[contains(@placeholder,'Anything you’d like the office to know?')]"));
            
            Add_note_field.click(); 
            
            Add_note_field.sendKeys("New Patient visit");
            
            Thread.sleep(18000);
        
        }
		@Test(priority=20)
        public void Verify_Scroller2()throws InterruptedException {
           WebElement kendoScrollable = driver.findElement(By.xpath("(//div[contains(@class,'body')])[2]"));
       
           JavascriptExecutor js = (JavascriptExecutor) driver;
       
           // Scroll to the bottom of the Kendo Scrollable element
           js.executeScript("arguments[0].scrollTop = arguments[0].scrollHeight;", kendoScrollable);
       
           // Verify the scroll position
           Long scrollTop = (Long) js.executeScript("return arguments[0].scrollTop;", kendoScrollable);
           Long scrollHeight = (Long) js.executeScript("return arguments[0].scrollHeight;", kendoScrollable);
       
           assert scrollTop.equals(scrollHeight - kendoScrollable.getSize().getHeight()) 
               : "The scrollbar did not reach the bottom.";
               Thread.sleep(5000);
        }
        
        @Test(priority=21)
        public void Book_Appointment_button()throws InterruptedException {
          
            WebElement Book_Appointment_button = driver.findElement(By.xpath("//ion-text[contains(@class,'ion-color ion-color-white md hydrated')]"));
            
            Book_Appointment_button.click(); 
             
            Thread.sleep(10000);
        
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
			 
			 
			 Thread.sleep(5000);
			 
			 driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	  }

	@AfterClass
	  public void afterClass() throws InterruptedException {
		  Thread.sleep(5000);
		 driver.quit();
		
	  }


}

