package automation_ss;
import java.io.File;
import java.text.SimpleDateFormat;
import java.time.Duration;
import java.util.Date;
import java.util.Locale;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
//import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
import com.aventstack.extentreports.reporter.configuration.Theme;
import com.github.javafaker.Faker;

import io.github.bonigarcia.wdm.WebDriverManager;
public class Newpatient {
    WebDriver driver;
	  ExtentReports extent;
	    ExtentTest test;
	   // ExtentHtmlReporter htmlReporter;
	    Faker faker = new Faker();
	    private WebDriverWait wait;
    
 
        @Test(priority=2)    
 
        public void Verify_Click_Newpatient_Tab() throws InterruptedException {
           Thread.sleep(3000);
             WebElement Newpatienttab = driver.findElement(By.xpath("//span[@class='k-link ng-star-inserted'][contains(.,'New Patient')]"));
           
             Newpatienttab.click(); 
             
            /*  WebElement Dashboardpage = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment/div/div[2]/div/div[2]/div[2]/kendo-tabstrip/div[2]/div[1]/kendo-combobox/kendo-searchbar/input"));
            
             Assert.assertTrue(Dashboardpage.isDisplayed(), "User not on new patienttab");*/
            
             driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS); 
             
             Thread.sleep(3000);
        }
        
       
        
        //Verifying Appointment Type Drop down
        
        @Test(priority=3)
        public void Verify_Appointment_Type() throws InterruptedException 
        {
            
            
            WebElement dropdownElement = driver.findElement(By.xpath("(//kendo-icon[contains(@class,'k-i-caret-alt-down k-icon ng-star-inserted')])[1]"));
            
            dropdownElement.click();
            
            WebElement APP_type=driver.findElement(By.xpath("//input[contains(@placeholder,'Appointment Type *')]"));
            APP_type.click();
            APP_type.sendKeys("NEW PATIENT");
            APP_type.sendKeys(Keys.ENTER);
            Thread.sleep(2000);
            
            WebElement FindApptbutton = driver.findElement(By.xpath("//div[@class='py-10 text-center ng-star-inserted'][contains(.,'Find Appointment')]"));
            
            
            Assert.assertTrue(FindApptbutton.isEnabled(), "Button should be enable afte select Appointment Type");
            
            
            driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
               
        }
        
       //Verifying Location Drop down Frank Mend
        
        @Test(priority=4)
        
        public void Verify_Location_Dropdown() throws InterruptedException 
        
        {
        WebElement Location = driver.findElement(By.xpath("//input[contains(@placeholder,'Any location')]"));
            Location.click();
            Location.sendKeys("Main Location");
            Location.sendKeys(Keys.ENTER);
            Thread.sleep(4000);
            
            //WebElement selectedOption = driver.findElement(By.xpath("/html[1]/body[1]/app-root[1]/kendo-popup[1]/div[1]/kendo-list[1]/div[1]/ul[1]/li[22]/span[1]"));
            
            //selectedOption.click();
            
          
            
           /* System.out.println("Selected option: " + selectedOption.getText());
            
            String actualText = selectedOption.getText();
            String expectedText = "Remote Location";
            
            Assert.assertEquals(actualText, expectedText, "The selected option is not as expected.");*/
            
            driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
            
        }
        
        
       //Verifying Provider Drop down
        
        @Test(priority=5)
        public void Verify_Provider_Dropdown() throws InterruptedException 
        {
        WebElement Provider = driver.findElement(By.xpath("//input[contains(@placeholder,'Any provider')]"));	 
        Provider.click();
        Provider.sendKeys("Airiel Lungley");
        Provider.sendKeys(Keys.ENTER);
            Thread.sleep(4000);
           
           
         
        }
        
        
       //Verifying Time of the day
        
        @Test(priority=6)
        public void Verify_Time_of_the_day() throws InterruptedException 
        {
            WebElement Timeoftheday = driver.findElement(By.xpath("//span[@class='k-button-text'][contains(.,'AM')]"));
            
            Timeoftheday.click();
            
            
            //Assert.assertTrue(Timeoftheday.isEnabled(), "Button should be enable afte Click on am time of the day");
            
            Thread.sleep(3000);
        }
        
        //Verify Click On FindAppointment button
        
        @Test(priority=7)
        public void Verify_Click_On_Findappointment_Button() throws InterruptedException 
        {
            WebElement Findappointbutton = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'Find Appointment')]"));
            
            Findappointbutton.click();
            
            
             WebElement ValidationText = driver.findElement(By.xpath("//ion-text[@class='h3-Montserrat text-blue-color md hydrated'][contains(.,'Pick an available time')]"));
             
            System.out.println("ValidationText: " + ValidationText.getText());
             
             String actualText = ValidationText.getText();
                String expectedText = "Pick an available time";
                
                Assert.assertEquals(actualText, expectedText, "Strings are not equal!");   
                
                Thread.sleep(10000);
        }
        
       //Verifying Current date slots
        
        @Test(priority=8)
        public void Verify_current_date_slots() throws InterruptedException 
        {
            
             WebElement ValidationText = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment-time/div/div[2]/div/div/div[2]/div[3]/div/ion-text"));
             
            System.out.println("ValidationText: " + ValidationText.getText());
             
             String actualText = ValidationText.getText();
                String expectedText = "No Slots Available";
                System.out.println("For Current date and applied filter no slots available");
                
                Assert.assertEquals(actualText, expectedText, "Not showing No slots available");
                
               Thread.sleep(10000);
             
        }
        
       //Verifying Clear Time of the day,provider and location fields
          
        @Test(priority=9)
       
        public void Verify_Clear_provider_and_Location() throws InterruptedException  
        {
           WebElement Timeoftheday = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment-time/div/div[2]/div/div/div[1]/div[4]/kendo-buttongroup/button[1]/span"));
        
           Timeoftheday.click();	 
       
            Thread.sleep(5000);
            
        WebElement ClrearLocation = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment-time/div/div[2]/div/div/div[1]/div[2]/kendo-combobox/span/kendo-icon-wrapper/kendo-icon"));
            
        ClrearLocation.click();
        
        Thread.sleep(5000);
        WebElement Clrearpovider = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patient-appointment-time/div/div[2]/div/div/div[1]/div[3]/kendo-combobox/span/kendo-icon-wrapper/kendo-icon"));
            
            Clrearpovider.click();
       
        
        Thread.sleep(7000);
              
        }
        
       //Verifying Select available dates from calendar
        
        @Test(priority=10)
        public void Verify_Select_available_date_from_calendar() throws InterruptedException  {
               
            WebElement select_next = driver.findElement(By.xpath("//ion-icon[@src='../../../../../assets/svg/chevron-right.svg']"));
            
            select_next.click();
            
            
             /*WebElement ValidationText = driver.findElement(By.xpath("//ion-text[@color='gray80'][contains(.,'Main Location')]"));
             
            System.out.println("ValidationText: " + ValidationText.getText());
             
             String actualText = ValidationText.getText();
                String expectedText = "Main Location";
                
                Assert.assertEquals(actualText, expectedText, "No slot available!");*/
                
                Thread.sleep(5000); 
        }
        
       //Verifying Select Appointment Slot
        
        @Test(priority=11)
        public void Verify_To_select_Available_Slots() throws InterruptedException 
        {
            WebElement SelectSlot = driver.findElement(By.xpath("(//ion-text[contains(@class,'bodyM-txt-medium montserrat ion-color-primary100 md hydrated')])[1]"));
            
            SelectSlot.click();
            
       WebElement Nexttbutton = driver.findElement(By.xpath("(//ion-text[contains(@class,'bodyM-txt-medium montserrat ion-color-primary100 md hydrated')])[1]"));
            
          
            
            Assert.assertTrue(Nexttbutton.isEnabled(), "Next Button should be enable after select available slot");
            
           Thread.sleep(3000); 
        }
        
           // Verifying Click on Next button
        
        @Test(priority=12)
        public void Verify_Click_Next_Button() throws InterruptedException {
       
             
        WebElement NextButtom = driver.findElement(By.xpath("//ion-text[@color='white'][contains(.,'Next')]"));
             
             NextButtom.click();
              
             Thread.sleep(4000);
            
             /*  WebElement Patientinfomation = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/patient-information"));
             
            Assert.assertTrue(Patientinfomation.isDisplayed(), "User not on Patient information page");*/
            Thread.sleep(2000); 
        }
        
       //Verifying Click on start button
        
        @Test(priority=13)
        public void Verify_Click_on_Start_Button() throws InterruptedException {
             
        WebElement StartButtom = driver.findElement(By.xpath("//ion-text[@class='bodyL-txt-bold md hydrated'][contains(.,'Start')]"));
             
        StartButtom.click();
                
        Thread.sleep(3000);
        
        }
       
         //Verifying Email in Demographics
        
         @Test(priority=14)
         public void Verify_email() throws InterruptedException{
           
             String email = faker.internet().emailAddress();
             System.out.println("email= " + email);
             WebElement emailField = driver.findElement(By.xpath("//input[contains(@placeholder,'Email Address*')]"));
             emailField.sendKeys(email);
              Thread.sleep(2000); 
         }
        
       //Verifying Enter First_Name
        
        @Test(priority=15)
        public void Verify_FirstName()throws InterruptedException {
          
            String firstName = faker.name().firstName();
            System.out.println("FirtNmae= " + firstName);
            WebElement firstNameField = driver.findElement(By.xpath("//input[contains(@placeholder,'First Name*')]"));
             firstNameField.sendKeys(firstName);
             Thread.sleep(3000);
        }
        
        //Verifying Last name in demographics section
        
        @Test(priority=16)
        public void Verify_Lastname() throws InterruptedException{
          
            String lastName = faker.name().lastName();
            System.out.println("Lastname= " + lastName);
            WebElement lastNameField = driver.findElement(By.xpath("//input[contains(@placeholder,'Last Name*')]"));
            lastNameField.sendKeys(lastName);
            Thread.sleep(3000); 
        }
        
        //Verifying preferred name in Demographics
        
        @Test(priority=17)
        public void Verify_preferredName()throws InterruptedException {
          
            String preferredName = faker.name().name(); 
            System.out.println("preferredName= " + preferredName);
            WebElement preferredNameField = driver.findElement(By.xpath("//input[contains(@placeholder,'Preferred Name')]"));
             preferredNameField.sendKeys(preferredName);
             Thread.sleep(3000); 
        }
        
        //Verifying DOB in Demographcs
        
        @Test(priority=18)
        public void Verify_DOB_with()throws InterruptedException {
          
            Date dateOfBirth = faker.date().birthday(18, 70); 
            
            SimpleDateFormat dateFormat = new SimpleDateFormat("MMddyyyy");   
            
            String formattedDOB = dateFormat.format(dateOfBirth);    
            
            System.out.println("DOB= " + formattedDOB);  
            
            WebElement dateOfBirthField = driver.findElement(By.xpath("//input[@placeholder='MM/DD/YYYY *']")); 
            
            dateOfBirthField.click();
            
            Thread.sleep(1000);
            
            dateOfBirthField.sendKeys(formattedDOB); 
            
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
        
        //Verifying Address field in Demographics
        
        @Test(priority=19)
        public void Verify_Address()throws InterruptedException {
          
            String address = faker.address().streetAddress();
            System.out.println("Adress= " + address);
            WebElement addressField = driver.findElement(By.xpath("//input[contains(@placeholder,'Address 1')]")); 
            WebElement addressField2 = driver.findElement(By.xpath("//input[contains(@placeholder,'Address 2')]"));
             addressField.sendKeys(address);
             Thread.sleep(1000); 
             addressField2.sendKeys(address);
             Thread.sleep(3000); 
        }
        
        //Verifying Zip Code in Demographics
        
        @Test(priority=20)
        public void Verify_Zip() throws InterruptedException{
          
            String zipCode = faker.address().zipCode();
            System.out.println("Zipcode= " + zipCode);
            WebElement zipCodeField = driver.findElement(By.xpath("//input[contains(@placeholder,'ZIP Code*')]"));
            zipCodeField.sendKeys(zipCode);
             Thread.sleep(3000);  
        }
        
        @Test(priority=21)
        public void Verify_gender() throws InterruptedException{
          
            String gender = faker.options().option("Male", "Female"); // Assuming gender options are Male or Female
            System.out.println("gender= " + gender);
            WebElement maleRadioButton = driver.findElement(By.xpath("(//input[contains(@type,'radio')])[1]"));
            WebElement femaleRadioButton = driver.findElement(By.xpath("(//input[contains(@type,'radio')])[2]"));
       
            if ("Male".equalsIgnoreCase(gender)) {
                maleRadioButton.click();
            } else {
                femaleRadioButton.click();
            }
             Thread.sleep(4000);
        }
        
        
        //Verifying Phone number in Demographics
       
        /*@Test(priority=22)
       public void Verify_phone() throws InterruptedException {
           WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
           
           // Select Phone Type
           WebElement selectPhonetype = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//input[contains(@placeholder,'Phone type*')]")));
           selectPhonetype.click();
           Thread.sleep(4000); // Adjust timing based on behavior
           selectPhonetype.sendKeys("Cell");
           selectPhonetype.sendKeys(Keys.ENTER);
       
           // Generate Phone Number
           String phoneNumber = faker.phoneNumber().phoneNumber().replaceAll("[^0-9]", "");
           phoneNumber = phoneNumber.length() > 10 ? phoneNumber.substring(0, 10) : phoneNumber;
           System.out.println("mobileNumber= " + phoneNumber);
       
           // Enter Phone Number
           WebElement phoneNumberField = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//input[contains(@id,'k-ff92310f-5f57-4485-9a59-9378e0a9bc7f')]")));
           phoneNumberField.click();
           Thread.sleep(3000);
           phoneNumberField.clear();
           Thread.sleep(2000);
           phoneNumberField.sendKeys(phoneNumber);
           Thread.sleep(3000);
       }*/
        
        @Test(priority=22)
        public void Verify_phone() throws InterruptedException{
            
            WebElement selectPhonetype = driver.findElement(By.xpath("//input[contains(@placeholder,'Phone type*')]"));
            selectPhonetype.click();
            Thread.sleep(4000);
            selectPhonetype.sendKeys("Cell");
            selectPhonetype.sendKeys(Keys.ENTER);
            Thread.sleep(5000);
            String phoneNumber = faker.phoneNumber().phoneNumber().replaceAll("[^0-9]", "");
            phoneNumber = phoneNumber.length() > 10 ? phoneNumber.substring(0, 10) : phoneNumber;
            System.out.println("mobileNumber= " + phoneNumber);
       
            WebElement phoneNumberField = driver.findElement(By.xpath("//input[@type='text']"));
            Thread.sleep(3000);
            phoneNumberField.click();
            Thread.sleep(5000);
            
            phoneNumberField.sendKeys(phoneNumber);
       
                 Thread.sleep(5000); 
        }
        
        
        //Verifying Gender in Demographics
        
       
           
        
        //Verifying Done button in Demographics
        
        @Test(priority=23)
        public void Verify_Click_On_Done()throws InterruptedException {
          
           
            WebElement DoneButton = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'done')]"));
            DoneButton.click(); 
            Thread.sleep(5000);
        }
        
        
        //Verifying Yes Button in Insurance section
        
        @Test(priority=24)
       
        public void Verify_Click_On_Yes()throws InterruptedException {
          
           
            WebElement Yes_Button = driver.findElement(By.xpath("//ion-text[@class='pr-10 md hydrated'][contains(.,'Yes')]"));
            Yes_Button.click(); 
           
            Thread.sleep(3000);
        }
        
        
        //Verifying Self pay option in Insurance section
        
        
        @Test(priority=25)
        public void Click_selfpay()throws InterruptedException {
          
            WebElement selfpay = driver.findElement(By.xpath("//input[contains(@value,'SelfPay')]"));
            selfpay.click(); 
       
            Thread.sleep(2000);
            
        }
       
       //Verifying Insurance option  in Insurance section
        
        @Test(priority=26)
        public void Click_Again_select_Insurance()throws InterruptedException {
          
            WebElement Insurance_RButton = driver.findElement(By.xpath("//input[contains(@value,'Insurance')]"));
            Insurance_RButton.click(); 
       
            Thread.sleep(2000);
            
        }
        
         @Test(priority=27)
        public void Verify_Click_On_Insurance_carrier()throws InterruptedException {
          
            WebElement Insurance_Carrier_DD = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/patient-information/div[2]/kendo-dialog/div[2]/div/div/patient-insurance-popup/div[1]/div/div[2]/form/div/div[1]/div[1]/kendo-formfield/div/kendo-combobox/button/kendo-icon-wrapper/kendo-icon"));
            Insurance_Carrier_DD.click(); 
            
            Thread.sleep(2000);
            WebElement select_Insurance = driver.findElement(By.xpath("(//span[contains(@class,'k-list-item-text ng-star-inserted')])[2]"));
            select_Insurance.click(); 
            
            Thread.sleep(7000);
        }
        
        @Test(priority=28)
        public void Verify_Click_On_Insurance_plan()throws InterruptedException {
          
            WebElement Insurance_plan_DD = driver.findElement(By.xpath("/html/body/app-root/ion-app/ion-router-outlet/app-main/div/patient-information/div[2]/kendo-dialog/div[2]/div/div/patient-insurance-popup/div[1]/div/div[2]/form/div/div[1]/div[2]/kendo-formfield/div/kendo-combobox/button/kendo-icon-wrapper/kendo-icon"));
            Insurance_plan_DD.click(); 
            
            Thread.sleep(3000);
            WebElement select_Insurance = driver.findElement(By.xpath("//span[@class='k-list-item-text ng-star-inserted'][contains(.,'Triarqinsurance')]"));
            select_Insurance.click(); 
            
            Thread.sleep(4000);
        }
        
       
        @Test(priority=29)
        public void Enter_member_number()throws InterruptedException {
          
            WebElement Member_number = driver.findElement(By.xpath("//input[contains(@placeholder,'Member number*')]"));
            Member_number.click(); 
            Member_number.sendKeys("Abc123D");
            Thread.sleep(3000);
            
        }
        
       
        @Test(priority=30)
        public void Enter_Group_number()throws InterruptedException {
          
            WebElement Group_number = driver.findElement(By.xpath("//input[contains(@placeholder,'Group Number')]"));
            Group_number.click(); 
            Group_number.sendKeys("JTY623D");
            Thread.sleep(3000);
            
        }
        
       
        @Test(priority=31)
        public void Click_Someoneelse_radiobutton()throws InterruptedException {
          
            WebElement SomeoneElse = driver.findElement(By.xpath("//input[contains(@value,'Someone')]"));
            SomeoneElse.click(); 
       
            Thread.sleep(3000);
            WebElement ScrollContent = driver.findElement(By.xpath("//div[@class='md-popup-content overflowY'][contains(.,'Insurance Self PayINSURANCE CARRIERINSURERMember numberGroup numberPolicy holder Self Someone elseSubscriber NameDate of birthGender')]"));
       
            // Scroll down within the popup content using JavaScript Executor
            JavascriptExecutor js = (JavascriptExecutor) driver;
            js.executeScript("arguments[0].scrollTop = arguments[0].scrollHeight", ScrollContent);
       
            // Wait a moment for the scroll to take effect
            Thread.sleep(3000);  // Adjust timing if needed
       
            // Verify if the content has been scrolled (you can check if the scroll position has changed)
            long scrollTop = (Long) js.executeScript("return arguments[0].scrollTop;", ScrollContent);
            Thread.sleep(4000);
        }
        
        @Test(priority=32)
        public void Verify_Subscriber_Dropdown()throws InterruptedException {
          
            WebElement Subscriber_DD = driver.findElement(By.xpath("//input[contains(@placeholder,'Subscriber relationship*')]"));
            Subscriber_DD.click(); 
            Subscriber_DD.sendKeys("Child");
            Subscriber_DD.sendKeys(Keys.ENTER);
            Thread.sleep(2000);
            
        }
        
        @Test(priority=33)
        public void Enter_Firstname_Of_Sub()throws InterruptedException {
          
            String SfirstName = faker.name().firstName();
            System.out.println("FirtName= " + SfirstName);
            WebElement sfirstNameField = driver.findElement(By.xpath("//input[contains(@placeholder,'First Name*')]"));
             sfirstNameField.sendKeys(SfirstName);
             Thread.sleep(3000);
        }
        
        @Test(priority=34)
        public void Enter_Mname_Of_Sub()throws InterruptedException {
          
            String mfirstName = faker.name().firstName();
            System.out.println("MiddleName= " + mfirstName);
            WebElement mNameField = driver.findElement(By.xpath("//input[contains(@placeholder,'Middle Name')]"));
             mNameField.sendKeys(mfirstName);
             Thread.sleep(3000);
        }
        
        @Test(priority=35)
        public void Enter_lastname_Of_Sub()throws InterruptedException {
          
            String sLastName = faker.name().firstName();
            System.out.println("LastName= " + sLastName);
            WebElement slastNameField = driver.findElement(By.xpath("//input[contains(@placeholder,'Last Name*')]"));
            slastNameField.sendKeys(sLastName);
             Thread.sleep(3000);
        }
        
        @Test(priority=36)
        public void Verify_DOB_Of_Sub()throws InterruptedException {
          
            Date dateOfBirth = faker.date().birthday(18, 70); 
            
            SimpleDateFormat dateFormat = new SimpleDateFormat("MMddyyyy");   
            
            String formattedDOB = dateFormat.format(dateOfBirth);    
            
            System.out.println("DOB= " + formattedDOB);  
            
            WebElement dateOfBirthField = driver.findElement(By.xpath("//input[contains(@placeholder,'MM/DD/YYYY*')]")); 
            
            dateOfBirthField.click();
            
            Thread.sleep(1000);
            
            dateOfBirthField.sendKeys(formattedDOB); 
            
            Thread.sleep(1000);
        }
        
        @Test(priority=37)
        public void Verify_SGender_Dropdown()throws InterruptedException {
          
            WebElement Subscriber_DD = driver.findElement(By.xpath("//input[contains(@placeholder,'Select Gender*')]"));
            Subscriber_DD.click(); 
            Subscriber_DD.sendKeys("male");
            Subscriber_DD.sendKeys(Keys.ENTER);
            Thread.sleep(2000);
            
        }
        
        @Test(priority=38)
        public void Verify_Click_On_Insurance_Done()throws InterruptedException {
          
           
            WebElement DoneButton = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'done')]"));
            DoneButton.click(); 
            Thread.sleep(5000);
           
        }
        @Test(priority=39)
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
        @Test(enabled = false)
        public void Verify_Click_On_Insurance_Yes()throws InterruptedException {
          
           
            WebElement YesButton = driver.findElement(By.xpath("//ion-text[@class='pr-10 md hydrated'][contains(.,'Yes')]"));
            YesButton.click(); 
            Thread.sleep(5000);
        }
        
        @Test(priority=40)
        public void Verify_Click_On_Add_Insurance()throws InterruptedException {
          
           
            WebElement AddInsuance_Link = driver.findElement(By.xpath("//ion-text[@class='bodyM-txt text-HLblue-color md hydrated'][contains(.,'+ Add Insurance Policy')]"));
            AddInsuance_Link.click(); 
            Thread.sleep(7000);
        }
        
        @Test(priority=41)
        public void Verify_Click_On_cancel_in_Add_Insurance()throws InterruptedException {
          
           Thread.sleep(2000);
            WebElement Cancel_Button = driver.findElement(By.xpath("//ion-text[@class='md hydrated'][contains(.,'Cancel')]"));
            Cancel_Button.click(); 
            Thread.sleep(5000);
        }
        
        @Test(enabled = false)
        public void Verify_Click_On_Add_Insurance_card()throws InterruptedException {
          
           
            WebElement Add_Insurance_card_Button = driver.findElement(By.xpath("//ion-text[contains(.,'View/Update Insurance Card Photo')]"));
            Add_Insurance_card_Button.click(); 
            Thread.sleep(3000);
        }
        
        @Test(enabled = false)
        public void Verify_Click_On_Take_new_photo()throws InterruptedException {
          
           
            WebElement Take_new_photo_Button = driver.findElement(By.xpath("//span[@class='bodyM-txt-bold'][contains(.,'Take / Upload a new photos')]"));
            Take_new_photo_Button.click(); 
            Thread.sleep(3000);
        }
        
        @Test(enabled = false)
        public void Verify_Click_On_Take_Front_photo()throws InterruptedException {
          
           
            WebElement Take_front = driver.findElement(By.xpath("(//ion-text[contains(@class,'bodyL-txt text-HLblue-color md hydrated')])[1]"));
             
            Take_front.click(); 
            Thread.sleep(3000);
        }
        
        
        @Test(enabled = false)//
        public void Verify_Click_On_Choose_photo()throws InterruptedException {
            
              // Use WebDriverWait to ensure the element is present before interacting with it
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
       
            // Execute JavaScript to check if the element is fully visible
            JavascriptExecutor js = (JavascriptExecutor) driver;
            boolean isDisplayed = (Boolean) js.executeScript(
                "var elem = document.querySelector('label[for=\"_pwa-elements-camera-input\"]');" +
                "if (elem) {" +
                "  var rect = elem.getBoundingClientRect();" +
                "  return (rect.top >= 0 && rect.left >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && rect.right <= (window.innerWidth || document.documentElement.clientWidth));" +
                "} else { return false; }"
            );
       
            // Assert whether the element is visible
            Assert.assertTrue(isDisplayed, "The 'Choose Image' label is not fully visible on the screen.");
       
            // Find the label element
            WebElement label = driver.findElement(By.xpath("//label[@for='_pwa-elements-camera-input']"));
       
            // Optionally, scroll into view if needed
            js.executeScript("arguments[0].scrollIntoView(true);", label);
       
            // Click the label
            label.click();
        
             System.out.println("test case partially excuted");
             // You can add assertions here to verify the result, e.g., checking visibility, text, etc.
          
           
            WebElement uploadElement = driver.findElement(By.xpath("/html/body/pwa-camera-modal-instance//div/div/pwa-camera//div/div[2]/label"));
           
            Thread.sleep(3000);
            File file = new File("C:\\Users\\ganesh.nawale\\OneDrive - Triarq Health\\Desktop\\junk\\123.png");
            
            uploadElement.sendKeys(file.getAbsolutePath());
            
            System.out.println("Click on choose photo");
            
                   // Locate the file input element by its id
                  /* By fileInput = By.id("_pwa-elements-camera-input");
                   Thread.sleep(2000);
                   
                   // Get the absolute path of the image to upload
                   File file = new File("C:\\Users\\ganesh.nawale\\OneDrive - Triarq Health\\Desktop\\junk\\123.png");
                   Thread.sleep(5000);
                   String absolutePath = file.getAbsolutePath();
                   Thread.sleep(2000);
                   // Upload the image by sending the file path to the input element
                   WebElement fileUploadElement = driver.findElement(fileInput);
                   Thread.sleep(2000);
                   fileUploadElement.sendKeys(absolutePath);
                   Thread.sleep(2000);
       
                   // Example: Check if the file upload is complete or wait for some success message
                   // This depends on how your application signals that the file has been uploaded
                   WebElement successMessage = driver.findElement(By.className("upload-success-message")); // Adjust as per your HTML
                   Assert.assertTrue(successMessage.isDisplayed(), "File upload was not successful.");*/
               }
        
        @Test(priority=46)
        public void Next_button_Book_information()throws InterruptedException {
          
           
            WebElement Next_button_confirmation_section = driver.findElement(By.xpath("//ion-button[contains(.,'Next')]"));
             
            Next_button_confirmation_section.click(); 
            Thread.sleep(3000);
        }
        
        @Test(priority=47)
        public void Previous_Button_Click()throws InterruptedException {
          
           
            WebElement PreviousButton_Click = driver.findElement(By.xpath("//ion-text[contains(.,'Previous')]"));
             
            PreviousButton_Click.click(); 
            
            Thread.sleep(8000);
            
            WebElement Next_button_confirmation_section = driver.findElement(By.xpath("//ion-button[contains(.,'Next')]"));
            
            Next_button_confirmation_section.click(); 
            
            Thread.sleep(4000);
        }
        
        
        @Test(priority=48)
        public void Additional_note()throws InterruptedException {
          
            WebElement Add_note_field = driver.findElement(By.xpath("//textarea[contains(@placeholder,'Anything you’d like the office to know?')]"));
            
            Add_note_field.click(); 
            
            Add_note_field.sendKeys("New Patient visit");
            
            Thread.sleep(5000);
        
        }
        @Test(enabled = false)
        public void reCAPTCHA_Check()throws InterruptedException {
          
            WebElement reCAPTCHA_Box = driver.findElement(By.xpath("(//div[contains(@class,'recaptcha-checkbox-border')])[1]"));
            
            reCAPTCHA_Box.click(); 
            
            Thread.sleep(6000);
       
        
        }
        @Test(priority=49)
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
        
        @Test(priority=50)
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
           
           
           Thread.sleep(3000);
           
           driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
    }

    @AfterClass
  public void afterClass() throws InterruptedException {
	  Thread.sleep(5000);
	 driver.quit();
	
  }

}