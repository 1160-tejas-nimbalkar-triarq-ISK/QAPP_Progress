package automation_ss;
import java.util.ArrayList;
import java.util.Set;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
//import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
import com.github.javafaker.Faker;

import io.github.bonigarcia.wdm.WebDriverManager;

public class ChangeSetting {

    WebDriver driver;
	  ExtentReports extent;
	    ExtentTest test;
	    Faker faker = new Faker();
	    private WebDriverWait wait;
    
	    @Test(priority=1)
	    public void Login_to_MyQone() throws InterruptedException {
	    	
	    	  Thread.sleep(5000);
	    	
	 
	 /*((JavascriptExecutor) driver).executeScript("window.open('about:blank', '_blank');");
	        for (String handle : driver.getWindowHandles()) {
	            driver.switchTo().window(handle);
	        }*/
	    	  
			
			// driver.get("https://accounts-qa.myqone.com/#/login");
			 
			/* Set<String> allWindowHandles = driver.getWindowHandles();
		        ArrayList<String> tabs = new ArrayList<>(allWindowHandles);
		        driver.switchTo().window(tabs.get(1));

			  Thread.sleep(5000);*/
	  
	        String[] credentials = Utils.getCredentials("Sheet2", 1);
	        String username = credentials[0];
	        String password = credentials[1];
	     
	        WebElement ExUsername = driver.findElement(By.xpath("//input[contains(@formcontrolname,'email')]"));
	        ExUsername.click();
	        ExUsername.sendKeys(username);
	        Thread.sleep(2000);
	        
	        WebElement Next = driver.findElement(By.xpath("//button[@type='submit'][contains(.,'Next')]"));
	        Next.click();
	        Thread.sleep(4000);
	        
	        WebElement Expass = driver.findElement(By.xpath("//input[contains(@formcontrolname,'password')]"));
	        Expass.click();
	        Expass.sendKeys(password);
	        Thread.sleep(4000);
	        WebElement Signin = driver.findElement(By.xpath("//button[@type='submit'][contains(.,'Sign in')]"));
	        Signin.click();
	        Thread.sleep(20000);
	        
	         
	    }
	    
	    
	    @Test(priority=2)
	    public void Clik_on_Admin() throws InterruptedException {
	    	
	    	
	    	  WebElement Admin = driver.findElement(By.xpath("(//img[contains(@class,'border-0 svgicon')])[6]"));
	    	  Thread.sleep(6000);
	    	  Admin.click();
	    	  Thread.sleep(10000);
	    	  
	    	   String parentWindow = driver.getWindowHandle();
	           Set<String> allWindows = driver.getWindowHandles();
	           String secondWindow = null;

	           for (String window : allWindows) {
	               if (!window.equals(parentWindow)) {
	                   secondWindow = window;
	                   break;
	               }
	           }

	           if (secondWindow != null) {
	               driver.switchTo().window(secondWindow);
	           }
	           System.out.println("Second Window Title: " + driver.getTitle());
	    }
	    
	    
	    
	    @Test(priority=3)
	    public void Clik_on_setting() throws InterruptedException { 
	    	  WebElement setting = driver.findElement(By.xpath("//a[@routerlink='/settings/applicationsetting'][contains(.,'Settings')]"));
	    	  setting.click();
	    	  Thread.sleep(3000);
	    	
	    }
	    
	    @Test(priority=4)
	    public void Clik_on_SS_setting() throws InterruptedException { 
	    	  WebElement ss_setting = driver.findElement(By.xpath("//a[@routerlink='/settings/SelfScheduling'][contains(.,'Self Scheduling')]"));
	    	  ss_setting.click();
	    	  Thread.sleep(3000);
			  WebElement setting = driver.findElement(By.xpath("//a[@href='#Settings']"));
	    	  setting.click();
	    	  Thread.sleep(3000);
	    }
	    
	    
	    @Test(priority=5)
	    public void Clik_on_Practice_DD() throws InterruptedException { 
	    	  WebElement dd_arrow = driver.findElement(By.xpath("//span[contains(@class,'k-icon k-i-arrow-s')]"));
	    	  dd_arrow.click();
	    	  Thread.sleep(5000);
	    	  
	    	  WebElement search = driver.findElement(By.xpath("//input[contains(@tabindex,'-1')]"));
	    	  search.click();
	    	  Thread.sleep(2000);
	    	  search.sendKeys("triarq practice services");
	    	  search.sendKeys(Keys.ENTER);
	    	  Thread.sleep(3000);
	    	  
	    	
	    }

	    
	    
	    @Test(priority=6)
	    public void Clik_on_newwindow() throws InterruptedException { 
	        String parentWindow = driver.getWindowHandle();
	        String secondWindow = driver.getWindowHandle();
	    	 ((ChromeDriver) driver).executeScript("window.open('https://qschedule-qa.myqone.com/patient-appointment/f1f64c71-91e9-11eb-b050-4578cb1636b4');");
	    	 Thread.sleep(20000);
	         Set<String> updatedWindows = driver.getWindowHandles();
	         String thirdWindow = null;

	         for (String window : updatedWindows) {
	             if (!window.equals(parentWindow) && !window.equals(secondWindow)) {
	                 thirdWindow = window;
	                 break;
	             }
	         }

	         if (thirdWindow != null) {
	             driver.switchTo().window(thirdWindow);
	         }
		
	         System.out.println("Third Window URL: " + driver.getCurrentUrl());  

	         driver.switchTo().window(secondWindow);
	         
	         System.out.println("Switched back to Parent Window Title: " + driver.getTitle());

			 Thread.sleep(3000);

			
			}
	    	
	    
	    
		@Test(priority=7)
	    public void Edit_NewPatient () throws InterruptedException { 
	    	  WebElement Editbutton = driver.findElement(By.xpath("(//em[contains(@class,'fa fa-pencil-square-o')])[4]"));
	    	  Editbutton.click();
	    	  Thread.sleep(2000);
	    	  
	    	  WebElement ValueField = driver.findElement(By.xpath("(//textarea[contains(@id,'settingdescriptionValue')])[2]"));
	    	  ValueField.clear();
	    	  Thread.sleep(2000);
	    	  ValueField.sendKeys("false");
			  Thread.sleep(2000);
			  WebElement savebutton = driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Save')])[2]"));
	    	  savebutton.click();;
	    	  Thread.sleep(3000);
	
	    }

	 @Test(priority=8)
	     public void Clik_on_Again_third_window() throws InterruptedException { 
		
			String parentWindow = driver.getWindowHandle();
	        String secondWindow = driver.getWindowHandle();
	    	 ((ChromeDriver) driver).executeScript("window.open('https://qschedule-qa.myqone.com/patient-appointment/f1f64c71-91e9-11eb-b050-4578cb1636b4');");
	    	 Thread.sleep(20000);
	         Set<String> updatedWindows = driver.getWindowHandles();
	         String thirdWindow = null;

	         for (String window : updatedWindows) {
	             if (!window.equals(parentWindow) && !window.equals(secondWindow)) {
	                 thirdWindow = window;
	                 break;
	             }
	         }

	         if (thirdWindow != null) {
	             driver.switchTo().window(thirdWindow);
	         }
		
	         System.out.println("Third Window URL: " + driver.getCurrentUrl());  

	         driver.switchTo().window(secondWindow);
	         
	         System.out.println("Switched back to Parent Window Title: " + driver.getTitle());

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
				 
				

				 
			driver.get("https://accounts-qa.myqone.com/#/login");
				 
				 
				 Thread.sleep(6000);
				 
				 driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		  }

		@AfterClass
		  public void afterClass() throws InterruptedException {
			  Thread.sleep(5000);
			 driver.quit();
			
		  }

    
}
