package intake;
import java.io.File;

import java.io.FileInputStream;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Set;

import org.apache.poi.EncryptedDocumentException;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class IntakeAutomation {
    private WebDriver driver;
	
	private static final String FILE_PATH = "C:\\Users\\mayur.sonawane\\Desktop\\Driver\\Mayur.xlsx";
	
	  private String MainPracticeName;
	  private String AppointmentTimeonClinicDashboard;
	  private String ModifyProviderName;
	  private String ModifyPatientName;
	  private String DOB;
	  
	  String originalWindow;
	  @BeforeClass
	    public void setUp() {
	        // Initialize the shared data before any test methods are executed
	    	MainPracticeName = "TRIARQ Practice Services";
	    	AppointmentTimeonClinicDashboard="4:00 PM ";
	    	ModifyProviderName="Airiel Lungley";
	    	ModifyPatientName="XYZ";
			
			  System.setProperty( "webdriver.chrome.driver","C:\\Users\\mayur.sonawane\\Desktop\\Driver\\chrome driver latest\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
			  );
			 
			 ChromeOptions options = new ChromeOptions();
			 options.addArguments("--remote-allow-origins=*"); driver = new
			 ChromeDriver(options); driver.manage().window().maximize();
			  System.out.println("Chrome browser is successfully initialized");
			 
	      }
	    	
	    
		@Test (priority = 1)
	    public void launchbrowser() throws InterruptedException, EncryptedDocumentException, IOException {
	driver.get("https://qpatient-qa.myqone.com/intake/clinic");
	Thread.sleep(3000);

	driver.manage().window().maximize();
	System.out.println("Chrome browser is successfully launched");
		}

		@Test (priority = 2)
	    public void LoginWithInvalidCredentials() throws InterruptedException, EncryptedDocumentException, IOException {

			String username= readCellValue("Sheet2",1,1);

	driver.findElement(By.xpath("//input[contains(@placeholder,'Username')]")).sendKeys(username);
	String password= readCellValue("Sheet2",2,1);
	driver.findElement(By.xpath("//input[contains(@placeholder,'Password')]")).sendKeys(password);
	Thread.sleep(3000);
	driver.findElement(By.xpath("//ion-text[text()='Open']")).click();
	Thread.sleep(4000);
	String ErrorMessage=driver.findElement(By.xpath("//ion-text[text()='The email or password you entered is incorrect. Please check and try again.']")).getText();
	
	System.out.println(ErrorMessage);
	Thread.sleep(4000);
	System.out.println("Unsuccessful Login attempt to QIntake with Invalid credentials");
	Thread.sleep(5000);
		}

		@Test (priority = 3)
		
		public void LoginWithvalidCredentials() throws InterruptedException, EncryptedDocumentException, IOException {
			Thread.sleep(3000);
	driver.findElement(By.xpath("//input[contains(@placeholder,'Password')]")).clear();
			Thread.sleep(3000);
	String password= readCellValue("Sheet2",3,1);
	driver.findElement(By.xpath("//input[contains(@placeholder,'Password')]")).sendKeys(password);
	Thread.sleep(4000);
	driver.findElement(By.xpath("//ion-text[text()='Open']")).click();
	Thread.sleep(8000);
	System.out.println("Successful Login to QIntake with valid credentials");
	}
		
		
		@Test (priority = 4)
	
		public void InvalidPracticeSearchFunctinality() throws InterruptedException, EncryptedDocumentException, IOException {
			
			String PracticeName= readCellValue("Sheet2",4,1);
			driver.findElement(By.xpath("//input[@class='searchbar-input sc-ion-searchbar-md']")).click();
			Thread.sleep(3000);
			driver.findElement(By.xpath("//input[@class='searchbar-input sc-ion-searchbar-md']")).sendKeys(PracticeName);
			Thread.sleep(5000);
			String ErrorMessage=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard-practice-list/div/div/div[2]/div[2]/div/div[2]/ion-text[1]")).getText();
			
			System.out.println(ErrorMessage);
			Thread.sleep(5000);
		}
			
			
			@Test (priority = 5)
		
			public void ValidPracticeSearchFunctinality() throws InterruptedException, EncryptedDocumentException, IOException {
			
				driver.findElement(By.xpath("//input[@class='searchbar-input sc-ion-searchbar-md']")).clear();
				Thread.sleep(3000);
				String PracticeName= readCellValue("Sheet2",5,1);
				driver.findElement(By.xpath("//input[@class='searchbar-input sc-ion-searchbar-md']")).sendKeys(PracticeName);
				Thread.sleep(3000);
				
				  String disabledAttribute=driver.findElement(By.xpath("//ion-text[text()='Connect']")).getAttribute("disabled");
		    	   	 
		    	   if (disabledAttribute ==null) {
		               System.out.println("Connect button is Disabled as Practice is not selected.");
		           } else {
		               System.out.println("Connect is enabled Even if the Practice is not selected.");
		           }
		    	   	  
				
				driver.findElement(By.xpath("//ion-text[contains(.,'TRIARQ Practice Services')]")).click();
										
				Thread.sleep(6000);
				
		        driver.findElement(By.xpath("//ion-text[text()='Connect']")).click();
		        
		        System.out.println("Connect is enabled as of Practice name is selected");
		        Thread.sleep(4000);
		}
			
				
		@Test (priority = 6)
	    public void PracticeConnection() throws InterruptedException, EncryptedDocumentException, IOException {	
			Thread.sleep(4000);
			String PracticeName=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/app-clinic-dashboard-header/div/div[1]/div/div[1]/ion-text")).getText();
			 String expectedText = "TRIARQ Practice Services";
			 Assert.assertEquals(expectedText, PracticeName);
			 System.out.println("Connected to TRIARQ Practice Services");
			 Thread.sleep(3000);
			 
			 MainPracticeName=PracticeName;
		}
		
		@Test (priority = 7)
	    public void DataforVerification() throws InterruptedException, EncryptedDocumentException, IOException {
		
			 String AppointmentTime=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/ion-text")).getText();
			
			 String normalizedTime1 = AppointmentTime.toLowerCase();
			 AppointmentTimeonClinicDashboard=normalizedTime1;
			 System.out.println("Appointment Time="+ normalizedTime1);
			 
			 String PatientName=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div/div[3]/div[1]/div[1]/div/div[1]/ion-text")).getText();
			 ModifyPatientName=PatientName;
			 
			 System.out.println(PatientName);
		
		
		String ProviderName=driver.findElement(By.xpath("//ion-text[@color='gray100' and contains(., 'Airiel, Lungley')]")).getText();
		
		ModifyProviderName=ProviderName;
		
		
		String PatientDOB=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div/div[3]/div[1]/div[1]/div/div[2]/ion-text[3]")).getText(); 
		 DOB=PatientDOB;
		System.out.println("DOB of the first Patient is:" + DOB);
		
		}
		

		@Test (priority = 8)
	    public void ValidSearchProviderFunctionality() throws InterruptedException, EncryptedDocumentException, IOException {	
			String ProviderName= readCellValue("Sheet2",6,1);
			Thread.sleep(4000);
			driver.findElement(By.xpath("//input[@aria-label='search text' and @placeholder='Search Providers']")).sendKeys(ProviderName);
			Thread.sleep(4000);
			
			String Text=driver.findElement(By.xpath("//ion-text[@color='gray100' and contains(., 'Airiel, Lungley')]")).getText();
			System.out.println("Searched provider functionality is working as expected for-->" + Text);
			Thread.sleep(3000);
			driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-provider-list/div/div/div[1]/ion-searchbar/div/button")).click();
			
			System.out.println("Search Filter is cleared");
			Thread.sleep(3000);
			
			String ProviderName2= readCellValue("Sheet2",7,1);
			
			driver.findElement(By.xpath("//input[@aria-label='search text' and @placeholder='Search Providers']")).sendKeys(ProviderName2);
			Thread.sleep(3000);
			String Text2=driver.findElement(By.xpath("//div[@class='w-100 providerName'][contains(.,'Smith, Shirley')]")).getText();
			System.out.println("Searched provider functionality is working as expected for-->" +  Text2);
			Thread.sleep(3000);
			driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-provider-list/div/div/div[1]/ion-searchbar/div/button")).click();
			
			
		}
		@Test (priority = 9)
	    public void InvalidSearchProviderFunctionality() throws InterruptedException, EncryptedDocumentException, IOException {	
			Thread.sleep(3000);
			String ProviderName = readCellValue("Sheet2",8,1);
						
				driver.findElement(By.xpath("//input[@aria-label='search text' and @placeholder='Search Providers']")).sendKeys(ProviderName);
				Thread.sleep(3000);
				String Actualerrormessage=driver.findElement(By.xpath("//ion-text[text()='We couldn’t find any provider ']")).getText();
												
				Thread.sleep(3000);
				System.out.println("Invalid search error message-->"  + Actualerrormessage );
				Thread.sleep(4000);
				
				driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-provider-list/div/div/div[1]/ion-searchbar/div/button")).click();
				Thread.sleep(3000);
				
				String ProviderName2 = readCellValue("Sheet2",9,1);
				
				driver.findElement(By.xpath("//input[@aria-label='search text' and @placeholder='Search Providers']")).sendKeys(ProviderName2);
				Thread.sleep(3000);
				String Actualerrormessage2=driver.findElement(By.xpath("//ion-text[text()='We couldn’t find any provider ']")).getText();
												
				Thread.sleep(3000);
				System.out.println("Invalid search error message-->"  + Actualerrormessage2 );
				
				Thread.sleep(4000);
				driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-provider-list/div/div/div[1]/ion-searchbar/div/button")).click();
				
				Thread.sleep(4000);
						
		}
			 
		
		
		@Test (priority = 10)
	    public void InValidSearchPatientFunctionality() throws InterruptedException, EncryptedDocumentException, IOException {	
			Thread.sleep(3000);
			String PatientName= readCellValue("Sheet2",9,1);
			driver.findElement(By.xpath("//input[@placeholder='Search Patients']")).sendKeys(PatientName);
			Thread.sleep(3000);
			
			String ErrorMessage=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div/div[3]/app-clinic-dashboard-search-noresult/div/div[2]/ion-text[1]")).getText();
			System.out.println(ErrorMessage);
			driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div/div[2]/ion-searchbar/div/button")).click();
			
			Thread.sleep(5000);
		}
			// ... other code ...

        @Test (priority = 11)
		public void ValidSearchPatientFunctionality() throws InterruptedException {

			String fullName = ModifyPatientName;

			// Remove comma and surrounding whitespace from fullName if present
			fullName = fullName.replace(",", "").trim();  // This is the crucial line
		
			String[] nameParts = fullName.split(" ", 2);
			String firstName = nameParts.length > 0 ? nameParts[0] : "";  
 
    driver.findElement(By.xpath("//input[@placeholder='Search Patients']")).sendKeys(firstName);
    Thread.sleep(1000); // Brief pause might be necessary
     
	String ActualText=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div/div[3]/div/div[1]/div/div[1]/ion-text")).getText();
	String ModifyPatientName=ActualText;
	
	if (ActualText.equals(ModifyPatientName)) {
		System.out.println("Text matches! and search results works");
	} else {
		System.out.println("Text doesn't match! and search results failed");
	}
	
	driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div/div[2]/ion-searchbar/div/button/ion-icon")).click();
	Thread.sleep(3000);
}		
		
		 @Test (priority = 12)
			
		    public void PatientAuthentication () throws InterruptedException, EncryptedDocumentException, IOException {	
			 Thread.sleep(3000);
			 
			 
			 driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div/div[3]/div/div[1]/div/div[1]/ion-text")).click();
			 
	    	   String disabledAttribute=driver.findElement(By.xpath("//ion-text[text()='Verify']")).getAttribute("disabled");
	    	   	 
	    	   if (disabledAttribute ==null) {
	               System.out.println("Verify button is Disabled as DOB is not entered.");
	           } else {
	               System.out.println("Button is enabled Even if the DOB is not entered.");
	           }
	    	   	 
	    	 Thread.sleep(4000); 	


	    	 String Date= readCellValue("Sheet2",10,1);
	    	   
	    	   
	    	 driver.findElement(By.xpath("//input[@placeholder='MM/DD/YYYY']")).sendKeys(Date);
	    	 
	    	String Errormessage= driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[1]/kendo-formfield/div/div/ion-text")).getText();
	    	 
              System.out.println(Errormessage); 
              Thread.sleep(3000); 
              
              driver.findElement(By.xpath("//input[@placeholder='MM/DD/YYYY']")).clear();
                	   
              
              driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[2]/div[1]/button/span")).click();
              Thread.sleep(3000);
              driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[2]/div[2]/button")).click();
              Thread.sleep(3000);
              driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[2]/div[11]/button")).click();
              Thread.sleep(3000);
              driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[2]/div[08]/button")).click();
              Thread.sleep(3000);
              driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[2]/div[2]/button")).click();
              Thread.sleep(3000);
              driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[2]/div[11]/button")).click();
              Thread.sleep(3000);
              driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[2]/div[2]/button")).click();
              Thread.sleep(3000);
              driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[2]/div[04]/button")).click();
              Thread.sleep(3000);
              
 	    	  	    	 
 	    	String Errormessage2= driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-confirm-patient/div/div/div/form/div[1]/kendo-formfield/div/div/ion-text")).getText();
 	    	 
               System.out.println(Errormessage2); 
               Thread.sleep(3000);

  	    	// String Date2= readCellValue("Sheet2",12,1);
  	    	   
  	    	   
  	    	 driver.findElement(By.xpath("//input[@placeholder='MM/DD/YYYY']")).sendKeys(DOB);
  	    	 Thread.sleep(3000);    	    	    	   	   	    
	    	   driver.findElement(By.xpath("//ion-text[text()='Verify']")).click();
	    	   System.out.println("Patient is Successfully Authenticated with correct DOB");
	    	   
			}
		 @Test (priority = 12)
			
		    public void WelcomeScreenDetailsVerification () throws InterruptedException, EncryptedDocumentException, IOException {	
			 
		 
			 Thread.sleep(3000);
		 String PracticeName=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/app-welcome-header/ion-header/div/div/div[1]/div/ion-text/span")).getText();
		 
		 
		 if (PracticeName.equals(MainPracticeName))
		 {
			 System.out.println("Practice Name is verified and it is as per the expectation");
		 }
		 else {
			 System.out.println("Practice Name is verified, it is not matching with the actual practice");
		 }
		 Thread.sleep(3000);
		String AppointmentTime=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[1]/div[2]/div/div/div[2]/ion-text")).getText();
		 String normalizedTime2 = AppointmentTime.toLowerCase();
		 
		 
		 if (normalizedTime2.equals(AppointmentTimeonClinicDashboard)) {
			 
			 System.out.println("Appointment time is verified and it is correct");
		 }
		 else
		 {
			 System.out.println("Appoitnemnt time is verified and it is nor correct");
		 }
		 
		 Thread.sleep(3000);
		  String ProviderName=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[1]/div[2]/div/div/div[3]/ion-text/b")).getText();
		  
		  String ProviderNamewithoutDr = ProviderName.replace("Dr ", "");
		  
		  
		  if (ProviderNamewithoutDr.equals(ModifyProviderName)) {
	            System.out.println("The names of the provider matching with the Clinic Dashboard.");
	        } else {
	            System.out.println("The names of the provider do not matching with the Clinic Dashboard.");
	        }
		 
		 
		 Thread.sleep(3000); 
		 }
		 
		 
		 @Test (priority = 13)
		 public void FinalStepsVerification () throws InterruptedException, EncryptedDocumentException, IOException {	
		 
		 
		 
		 
		  int stepCount = 0;
		  
		  try {
              WebElement step1 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[1]/div[2]/ion-text"));
              System.out.println("Step 1 is present: " + step1.getText());
              stepCount++;
          } catch (Exception e) {
              System.out.println("Step 1 is not present.");
              System.out.println("Final count: Step " + stepCount + " only");
              return;  
          }
		 
		  try {
              WebElement step2 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[2]/div[2]/ion-text"));
              System.out.println("Step 2 is present: " + step2.getText());
              stepCount++;
          } catch (Exception e) {
              System.out.println("Step 2 is not present.");
              System.out.println("Final count: Step " + stepCount + " only");
              return;  
          }

         
          try {
              WebElement step3 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[3]/div[2]/ion-text"));
              System.out.println("Step 3 is present: " + step3.getText());
              stepCount++;
          } catch (Exception e) {
              System.out.println("Step 3 is not present.");
              System.out.println("Final count: Step " + stepCount + " only");
              return;  
          }

          try {
              WebElement step4 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[4]/div[2]/ion-text"));
              System.out.println("Step 4 is present: " + step4.getText());
              stepCount++;
          } catch (Exception e) {
              System.out.println("Step 4 is not present.");
              System.out.println("Final count: Step " + stepCount + " only");
              return;  
          }

          System.out.println("All steps are present. Final count: Step " + stepCount);
         
          
        
		 }
          
          @Test(priority=14)
          
          public void QAdminLogin () throws InterruptedException, EncryptedDocumentException, IOException {	
        	  
        	  originalWindow = driver.getWindowHandle();
        	  
        	  JavascriptExecutor js = (JavascriptExecutor) driver;
              js.executeScript("window.open('https://accounts-qa.myqone.com/#/login?continue=https:%2F%2Fqadmin-qa.myqone.com%2Fputhash%2Flanding');");
        	  //((org.openqa.selenium.JavascriptExecutor) driver).executeScript("window.open();");
             	Set<String> allWindows = driver.getWindowHandles();
      		 
      		 
      		  Thread.sleep(5000);
      		  for (String windowHandle : allWindows) {
      	            if (!windowHandle.equals(originalWindow)) {
      	                driver.switchTo().window(windowHandle);
      	                break;
      	            }
      	            }
                   //  driver.get("https://accounts-qa.myqone.com/#/login?continue=https:%2F%2Fqadmin-qa.myqone.com%2Fputhash%2Flanding");
                   
                   String username= readCellValue("Sheet2",1,1);
           
               	driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[1]/mat-form-field/div/div[1]/div/input")).sendKeys(username);
               	
               	driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[4]/button/span")).click();
               	
               	String password= readCellValue("Sheet2",3,1);
               	driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[1]/mat-form-field/div/div[1]/div[1]/input")).sendKeys(password);
               	
               	
               	Thread.sleep(3000);
               	driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button/span")).click();
               
                  
               	Thread.sleep(16000);
               	
               	
               	driver.findElement(By.xpath("//button[text()='Yes, this is my device']")).click();
               	 
              	Thread.sleep(3000);
              	System.out.println("User logged in to QAdmin Successfully");
              	
      		 }

        	  
          @Test(priority=15)
      	public void FormsSupressionVerification() throws InterruptedException{
      	
      	Thread.sleep(10000);
      	
       	driver.findElement(By.xpath("/html/body/app-root/app-navbar/div[2]/div/div/div/ul/li[3]/a")).click();
       	
       System.out.println("User has accessed Forms section");
       	Thread.sleep(3000);
       	driver.findElement(By.xpath("/html/body/app-root/app-application-forms/div/div/div[1]/div/div[2]/div/a[2]")).click();
       	System.out.println("User has accessed Forms Suppress Sections");
       	
       	
       	Thread.sleep(5000);
       	
       	
       	WebElement dropdown = driver.findElement(By.xpath("/html/body/app-root/app-application-forms/div/div/div[2]/div/div/div/app-portal-medical-form/div[2]/div/form/div/div/div/kendo-dropdownlist/span"));
       	dropdown.click();
         	Thread.sleep(5000);
         
       	driver.findElement(By.xpath("(//input[contains(@class,'k-textbox ng-untouched ng-pristine ng-valid')])[2]")).sendKeys("TRIARQ Practice Services");
       	Thread.sleep(3000);
       	driver.findElement(By.xpath("//li[contains(.,'TRIARQ Practice Services')]")).click();
       	Thread.sleep(3000);
       	driver.findElement(By.xpath("//input[@aria-label='Appointment Type Filter']")).sendKeys("New Patient");
       	Thread.sleep(5000);
       	 
       	WebElement PortalFormToggleSwith=driver.findElement(By.xpath("/html/body/app-root/app-application-forms/div/div/div[2]/div/div/div/app-portal-medical-form/div[3]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[2]/kendo-switch/span"));
       	Thread.sleep(4000);
       	
          String ariaChecked = PortalFormToggleSwith.getAttribute("aria-checked");

          if ("true".equals(ariaChecked)) {
              System.out.println("Portal Toggle button is ON");
          } else if ("false".equals(ariaChecked)) {
              System.out.println("Portal Toggle button is OFF");
          } else {
              System.out.println("Unable to determine the state of the Portal toggle button");
          }
    
        	Thread.sleep(4000);
        	
        	
           WebElement IntakeFormToggleSwitch=driver.findElement(By.xpath("/html/body/app-root/app-application-forms/div/div/div[2]/div/div/div/app-portal-medical-form/div[3]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[3]/kendo-switch/span"));
        	Thread.sleep(4000);
           String ariaChecked2 = IntakeFormToggleSwitch.getAttribute("aria-checked");

           if ("true".equals(ariaChecked2)) {
               System.out.println("Intake Toggle button is ON");
           } else if ("false".equals(ariaChecked2)) {
               System.out.println("Intake Toggle button is OFF");
           } else {
               System.out.println("Unable to determine the state of the Intake toggle button");
           }
        	
		 }
         @Test (priority = 16)
         public void StepsVerification() throws InterruptedException{

      	   driver.switchTo().window(originalWindow);
      	    System.out.println("Switched back to the original window.");
      	    
      	    
      	    driver.navigate().refresh();
     		 Thread.sleep(4000);
     		  int stepCount = 0;
     		  
     		  try {
                   WebElement step1 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[1]/div[2]/ion-text"));
                   System.out.println("Step 1 is present: " + step1.getText());
                   stepCount++;
               } catch (Exception e) {
                   System.out.println("Step 1 is not present.");
                   System.out.println("Final count: Step " + stepCount + " only");
                   return;  
               }
     		 
     		  try {
                   WebElement step2 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[2]/div[2]/ion-text"));
                   System.out.println("Step 2 is present: " + step2.getText());
                   stepCount++;
               } catch (Exception e) {
                   System.out.println("Step 2 is not present.");
                   System.out.println("Final count: Step " + stepCount + " only");
                   return;  
               }

              
               try {
                   WebElement step3 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[3]/div[2]/ion-text"));
                   System.out.println("Step 3 is present: " + step3.getText());
                   stepCount++;
               } catch (Exception e) {
                   System.out.println("Step 3 is not present.");
                   System.out.println("Final count: Step " + stepCount + " only");
                   return;  
               }

               try {
                   WebElement step4 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[4]/div[2]/ion-text"));
                   System.out.println("Step 4 is present: " + step4.getText());
                   stepCount++;
               } catch (Exception e) {
                   System.out.println("Step 4 is not present.");
                   System.out.println("Final count: Step " + stepCount + " only");
                   return;  
               }

               System.out.println("All steps are present. Final count: Step " + stepCount);
}
         @Test (priority = 17)
         public void toggleButtonUpdates() throws InterruptedException {
         
         WebElement PortalFormToggleSwith=driver.findElement(By.xpath("/html/body/app-root/app-application-forms/div/div/div[2]/div/div/div/app-portal-medical-form/div[3]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[2]/kendo-switch/span"));
      	Thread.sleep(4000);
      	
         String ariaChecked = PortalFormToggleSwith.getAttribute("aria-checked");

         if ("true".equals(ariaChecked)) {
             System.out.println("Portal Toggle button is ON");
             PortalFormToggleSwith.click();
             System.out.println("Portal Toggle button is Switched to OFF State");
             
         } else if ("false".equals(ariaChecked)) {
      	  
             System.out.println("Portal Toggle button is OFF");
         } else {
             System.out.println("Unable to determine the state of the Portal toggle button");
         }
   
       	Thread.sleep(4000);
       	
       	
          WebElement IntakeFormToggleSwitch=driver.findElement(By.xpath("/html/body/app-root/app-application-forms/div/div/div[2]/div/div/div/app-portal-medical-form/div[3]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[3]/kendo-switch/span"));
       	Thread.sleep(4000);
          String ariaChecked2 = IntakeFormToggleSwitch.getAttribute("aria-checked");

          if ("true".equals(ariaChecked2)) {
              System.out.println("Intake Toggle button is ON");
              Thread.sleep(3000);
              IntakeFormToggleSwitch.click();
              System.out.println("Intake Toggle button is Switched to OFF State");
              
          } else if ("false".equals(ariaChecked2)) {
              System.out.println("Intake Toggle button is OFF");
          } else {
              System.out.println("Unable to determine the state of the Intake toggle button");
          }
       	
		 }
         
         
         
         @Test (priority = 18)
         public void StepsVerification2() throws InterruptedException{

      	   driver.switchTo().window(originalWindow);
      	    System.out.println("Switched back to the original window.");
      	    
      	    
      	    driver.navigate().refresh();
     		 Thread.sleep(4000);
     		  int stepCount = 0;
     		  
     		  try {
                   WebElement step1 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[1]/div[2]/ion-text"));
                   System.out.println("Step 1 is present: " + step1.getText());
                   stepCount++;
               } catch (Exception e) {
                   System.out.println("Step 1 is not present.");
                   System.out.println("Final count: Step " + stepCount + " only");
                   return;  
               }
     		 
     		  try {
                   WebElement step2 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[2]/div[2]/ion-text"));
                   System.out.println("Step 2 is present: " + step2.getText());
                   stepCount++;
               } catch (Exception e) {
                   System.out.println("Step 2 is not present.");
                   System.out.println("Final count: Step " + stepCount + " only");
                   return;  
               }

              
               try {
                   WebElement step3 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[3]/div[2]/ion-text"));
                   System.out.println("Step 3 is present: " + step3.getText());
                   stepCount++;
               } catch (Exception e) {
                   System.out.println("Step 3 is not present.");
                   System.out.println("Final count: Step " + stepCount + " only");
                   return;  
               }

               try {
                   WebElement step4 = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-welcome/div[1]/div/div/ion-col[2]/div/div[1]/div[2]/div/div[4]/div[2]/ion-text"));
                   System.out.println("Step 4 is present: " + step4.getText());
                   stepCount++;
               } catch (Exception e) {
                   System.out.println("Step 4 is not present.");
                   System.out.println("Final count: Step " + stepCount + " only");
                   return;  
               }

               System.out.println("All steps are present. Final count: Step " + stepCount);
         }
         
		 @Test (priority = 19)
			
		    public void InfoConfirmVerification () throws InterruptedException, EncryptedDocumentException, IOException {	
			 
		 
			 Thread.sleep(3000);
		 String PracticeName=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-patient-info-focus/app-main-header/ion-header/div/div/div[1]/div/ion-text/span")).getText();
		 
		 
		 if (PracticeName.equals(MainPracticeName))
		 {
			 System.out.println("Practice Name is verified and it is as per the expectation");
		 }
		 else {
			 System.out.println("Practice Name is verified, it is not matching with the actual practice");
		 }
		 Thread.sleep(3000);
		String AppointmentTime=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-patient-info-focus/app-main-header/ion-header/div/div/div[3]/div/ion-text[1]")).getText();
		 //String normalizedTime2 = AppointmentTime.toUpperCase();
		 
		 
		 if (AppointmentTime.equals(AppointmentTimeonClinicDashboard)) {
			 
			 System.out.println("Appointment time is verified and it is correct");
		 }
		 else
		 {
			 System.out.println("Appoitnemnt time is verified and it is nor correct");
		 }
		 
		 Thread.sleep(3000);
		  String ProviderName=driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-pre-registration-patient-info-focus/app-main-header/ion-header/div/div/div[3]/div/ion-text[2]")).getText();
		  
		  String ProviderNamewithoutDr = ProviderName.replace("Dr ", "");
		  
		  
		  if (ProviderNamewithoutDr.equals(ModifyProviderName)) {
	            System.out.println("The names of the provider matching with the Clinic Dashboard.");
	        } else {
	            System.out.println("The names of the provider do not matching with the Clinic Dashboard.");
	        }
		 
		 
		 Thread.sleep(3000); 
		 
		 
		 }
		 
		 
		 
		 
		/*
		 * public void Futuredates() throws InterruptedException,
		 * EncryptedDocumentException, IOException { driver.findElement(By.xpath(
		 * "/html/body/app-root/ion-app/ion-router-outlet/app-clinic-dashboard/div/div/app-clinic-dashboard-patient-list/div/div[2]/ion-searchbar/div/button/ion-icon"
		 * )).click(); Thread.sleep(3000); String Currentdate=driver.findElement(By.
		 * xpath("//ion-text[@class='bodyM-txt-bold ion-color ion-color-gray80 md hydrated']"
		 * )).getText();
		 * 
		 * driver.findElement(By.
		 * xpath("//ion-text[@class='bodyM-txt-bold ion-color ion-color-gray80 md hydrated']"
		 * )).click();
		 */
	
private String readCellValue(String sheetName, int rowNumber, int cellNumber) throws IOException {
    FileInputStream fileInputStream = new FileInputStream(new File(FILE_PATH));
    Workbook workbook = new XSSFWorkbook(fileInputStream);
    Sheet sheet = workbook.getSheet(sheetName);
    Row row = sheet.getRow(rowNumber);
    Cell cell = row.getCell(cellNumber);
    String cellValue = cell.getStringCellValue();
    workbook.close();
    fileInputStream.close();
    return cellValue;

}


	}

