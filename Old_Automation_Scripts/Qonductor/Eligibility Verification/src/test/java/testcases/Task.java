package testcases;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
 
import io.github.bonigarcia.wdm.WebDriverManager;
 
public class Task {
 
	 private WebDriver driver;
 
	    @BeforeClass
	    public void setup() {
	        WebDriverManager.chromedriver().setup(); // base
	        driver = new ChromeDriver(); // base
	    }
	    @AfterClass
	    public void teardown() {
	    	driver.quit();
	    }
 
	    @Test(priority=1)
	    public void mylogin() throws InterruptedException {
	    	driver.get("https://qonductor-staging.myqone.com/");// configfiles
//			driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
			driver.manage().window().maximize();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//input[@id='mat-input-0']")).sendKeys("ujwala.gavit@triarqhealth.com");////input[@id='mat-input-0']
			driver.findElement(By.xpath("//button[@type='submit']")).click(); //next button
			Thread.sleep(4000);
			driver.findElement(By.xpath("//input[@id='mat-input-1']")).sendKeys("Stg@2023"); //password
			Thread.sleep(4000);
			driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button")).click();//sign in
			//Eligibility verification 
			Thread.sleep(6000);
	        // Your login code
	    }
 
	    @Test(priority=2 ,dependsOnMethods = "mylogin") // This ensures that mylogin method is executed before access
	    public void access() throws InterruptedException {
	        Thread.sleep(4000);
	        driver.findElement(By.xpath("//*[@id='optEV_Project']/div/div/h5")).click();//Eligibility verification
	        Thread.sleep(4000);
	    }
	    @Test(priority=5,dependsOnMethods = "mylogin")
	    public void accessProjects() throws InterruptedException {
	    	driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); //Projects
			Thread.sleep(4000);
			}
	    @Test(priority=6,dependsOnMethods = "mylogin", enabled=true)
	    public void Task_menu_access() throws InterruptedException {
	    	 //All projects tab
	    	  driver.findElement(By.xpath("//a[@id='idMnuTask']")).click(); //Task menu access
	    	  Thread.sleep(4000);
	    }
	    @Test(priority=7,dependsOnMethods = "mylogin", enabled=true)
	    public void Allprjtab_viewfilter() throws InterruptedException {
	    	 //all projects tab
	    	
	    	driver.findElement(By.xpath("//a[@id='idMnuTask']")).click(); //Task menu access
	    	  Thread.sleep(4000);
	    	 WebElement viewfilter=driver.findElement(By.xpath("//a[contains(@id,'idSbMnuCompletedTasks')]"));//Task >> completed task access
	    	  viewfilter.click();
	    	  Thread.sleep(6000);
	    }
	    @Test(priority=8,dependsOnMethods = "mylogin", enabled=true)
	    public void selectcompleted_filter() throws InterruptedException {
	    	
	    	try {
	    		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
    			Thread.sleep(9000);
	    		
	    		
			} catch (Exception e) {
				 //Assigned tab
		    	 //select priority filter
		    	  WebElement dropdown_p = driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-up']"));//Practice
		    	  dropdown_p.click();
//		    	  WebDriverWait wait = new WebDriverWait(driver, 10);
//		    	  WebElement dropdownOptions = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));
//		    	  WebElement desiredOption = dropdownOptions.findElement(By.xpath("//li[text()='High']"));
//		    	  desiredOption.click();
		    	  Thread.sleep(4000);
		    	  
		    	  driver.findElement(By.xpath("(//span[@unselectable='on'][contains(.,'All')])[4]")).click(); //priority
		    	  Thread.sleep(4000);
		    	  
		    	  driver.findElement(By.xpath("(//div[contains(@class,'k-multiselect-wrap k-floatwrap')])[1]")).click(); //Insurance
		    	  Thread.sleep(4000);
		    	  
		    	  
		    	  driver.findElement(By.xpath("//input[contains(@id,'k-83ceca4a-ef77-4496-814d-7b3d8ca0e6e0')]")).click(); //Location
		    	  Thread.sleep(4000);
		    	  
		    	  driver.findElement(By.xpath("//span[contains(@id,'40e0fd8d-da3c-4dc8-bbb1-2b36acbea336')]")).click(); //Projects
		    	  Thread.sleep(4000);
		    	  
		    	  driver.findElement(By.id("btnApplyFilter")).click();
		    	  Thread.sleep(6000);
		    	  
		    	  driver.findElement(By.id("btnClearFilter")).click();
		    	  Thread.sleep(4000);
			}
	    	
	    }
	   
	  
	    @Test(priority=13,dependsOnMethods = "mylogin", enabled=true)
	    public void Allprjtab_Exporttoexcel() throws InterruptedException {
	    	driver.findElement(By.xpath("//button[contains(.,'Export to Excel')]")).click();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//button[contains(.,'Yes')]")).click();
			Thread.sleep(4000);
	    }
	    @Test(priority=14,dependsOnMethods = "mylogin", enabled=false)
	    public void Allprjtab_projectdeatils() throws InterruptedException {
	    	 //Assigned tab
	    	driver.findElement(By.xpath("(//a[@data-toggle='modal'][contains(.,'2024-01-15')])[1]")).click(); //project details open
	    	  Thread.sleep(4000);
 
//	    	  driver.findElement(By.xpath("//span[@class='k-link ng-tns-c402-5'][contains(.,'Instructions(Total: 0)')]")).click();//Summary
//	    	  Thread.sleep(4000);
//	    	  
// 	  driver.findElement(By.xpath("//span[@class='k-link ng-tns-c402-5'][contains(.,'Instructions(Total: 0)')]")).click(); //instrcutions
//	    	  Thread.sleep(4000);
//	    	  
//	    	  driver.findElement(By.xpath("//*[@id=\"k-tabstrip-tab-2\" and @tabindex=\"0\"]")).click(); //workitems
//	    	  Thread.sleep(6000);
	    	  driver.findElement(By.xpath("//span[contains(.,'History')]")).click();//History
	    	  Thread.sleep(4000);
 
 
	    	  driver.findElement(By.xpath("(//button[@class='close'])[2]")).click();
	    	  Thread.sleep(4000);
	    }
	    @Test(priority=15,dependsOnMethods = "mylogin", enabled=true)
	    public void Allprjtab_scrollbar() throws InterruptedException {
	    	  // Create an instance of JavascriptExecutor
	    	  JavascriptExecutor jsopen = (JavascriptExecutor) driver;
 
	    	  // Scroll down by pixel
	    	  jsopen.executeScript("window.scrollBy(0, 500);");
	    	  Thread.sleep(4000);
 
	    	  jsopen.executeScript("window.scrollBy(0, -500);");
	    	  driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-up']")).click();
	    	  Thread.sleep(4000);
	    }


}
