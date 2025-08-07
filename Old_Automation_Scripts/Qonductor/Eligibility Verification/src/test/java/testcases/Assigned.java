package testcases;



import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
 
import io.github.bonigarcia.wdm.WebDriverManager;
 
public class Assigned {
	WebDriver driver;
 
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
	 	//driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
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
	        driver.findElement(By.xpath("//*[@id='optEV_Project']/div/div/h5")).click();
	        Thread.sleep(4000);
	    }
	    @Test(priority=5,dependsOnMethods = "mylogin")
	    public void accessProjects() throws InterruptedException {
	    	driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); //Eligibility verification
			Thread.sleep(4000);
			}
	    @Test(priority=6,dependsOnMethods = "mylogin", enabled=true)
	    public void Assignedtab() throws InterruptedException {
	    	 //Assigned tab
	    	driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); //Eligibility verification
			Thread.sleep(4000);
	    	driver.findElement(By.xpath("//*[@id='k-tabstrip-tab-1']/span")).click();
			Thread.sleep(6000);
	    }
	    @Test(priority=7,dependsOnMethods = "mylogin", enabled=true)
	    public void Assignedtab_viewfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 WebElement viewfilter=driver.findElement(By.xpath("//i[contains(@title,'View filters option')]"));//completed>>view filter options
	    	  viewfilter.click();
	    	  Thread.sleep(6000);
	    }
	    @Test(priority=8,dependsOnMethods = "mylogin", enabled=true)
	    public void Assigned_priorityfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 //select priority filter
	    	try {
	    		WebElement dropdown = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[4]"));
		    	  dropdown.click();
		    	//  WebDriverWait wait = new WebDriverWait(driver, 10);
		    	//  WebElement dropdownOptions = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));
		    	//  WebElement desiredOption = dropdownOptions.findElement(By.xpath("//li[text()='High']"));
		    	//  desiredOption.click();
		    	  Thread.sleep(4000);
		    	  
			} catch (Exception e) {
				driver.findElement(By.id("btnApplyFilter")).click();
		    	  Thread.sleep(6000);
			}
	    	  
	    }
	    @Test(priority=9,dependsOnMethods = "mylogin", enabled=true)
	    public void Assignedtab_ownerfilter() throws InterruptedException {
	    	 //Assigned tab
	    	//select owner filter
	    	try {
	    		 WebElement comp_dropdown_owner = driver.findElement(By.xpath("//div[contains(@class,'k-multiselect-wrap k-floatwrap')]"));
		    	  comp_dropdown_owner.click();
			} catch (Exception e) {
				 WebElement dropdownElement = driver.findElement(By.xpath("//div[@class='form-group']//kendo-dropdownlist[@formcontrolname='fcClient']"));
		    	  Select dropdownw = new Select(dropdownElement);
		    	  dropdownw.selectByVisibleText("Women Care Clinics");
			}
	    	 
	    }
	    @Test(priority=10,dependsOnMethods = "mylogin", enabled=true)
	    public void Assignedtab_projectfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 //select project filter
	    	try {
	    		 WebElement dropdown_project = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[6]"));
		    	  dropdown_project.click();   
		    	  Thread.sleep(4000);
			} catch (Exception e) {
				// TODO: handle exception
			}
	    	 
	    }
	    @Test(priority=11,dependsOnMethods = "mylogin", enabled=true)
	    public void Assigned_Appointmnetfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 //due date
	    	  WebElement calendar_apptdate = driver.findElement(By.xpath("//span[contains(@class,'k-icon k-i-calendar')]"));
	    	  calendar_apptdate.click();
	    	  Thread.sleep(2000);
	    	  driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
	    	  Thread.sleep(2000);
	    	  driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
	    	  Thread.sleep(2000);
	    	  driver.findElement(By.id("btnClearFilter")).click();
	    }
	    @Test(priority=12,dependsOnMethods = "mylogin", enabled=true)
	    public void Assignedtab_Appointmnetfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 //Appointmnet date 
	    	try {
	    		 WebElement calendar_apptdate = driver.findElement(By.xpath("(//span[contains(@class,'k-icon k-i-calendar')])[2]"));
		    	  calendar_apptdate.click();
		    	  Thread.sleep(4000);
		    	  driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
		    	  Thread.sleep(4000);
		    	  driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
		    	  driver.findElement(By.id("btnClearFilter")).click();
		    	  Thread.sleep(4000);	
			} catch (Exception e) {
				System.out.println("No data found");
			}
	    	 
	    }
	    @Test(priority=13,dependsOnMethods = "mylogin", enabled=true)
	    public void Assignedtab_Exporttoexcel() throws InterruptedException {
	    	try {
	    		driver.findElement(By.xpath("//button[contains(.,'Export to Excel')]")).click();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//button[contains(.,'Yes')]")).click();
			Thread.sleep(4000);
				
			} catch (Exception e) {
				System.out.println("NO records availble to export");
			}
	    	
	    }
	    @Test(priority=14,dependsOnMethods = "mylogin", enabled=true)
	    public void Assignedtab_projectdeatils() throws InterruptedException {
	    	
	    	try {
	    		 //Assigned tab
		    	driver.findElement(By.xpath("(//a[@class='ng-star-inserted'])[1]")).click(); //project details open
		    	  Thread.sleep(4000);
	 
		    	  driver.findElement(By.xpath("//span[@class='k-link ng-tns-c402-5'][contains(.,'Instructions(Total: 0)')]")).click();//Summary
		    	  Thread.sleep(4000);
		    	  
	    	      driver.findElement(By.xpath("//span[contains(.,'Instructions(Total: 0)')]")).click(); //instrcutions
	    	      Thread.sleep(4000);
	    	  
		    	  driver.findElement(By.xpath("(//span[@class='k-link ng-tns-c404-4'])[3]")).click(); //workitems
		    	  Thread.sleep(6000);
		    	  driver.findElement(By.xpath("//span[contains(.,'History')]")).click();//History
		    	  Thread.sleep(4000);
	 
	 
		    	  driver.findElement(By.xpath("//button[@class='close']")).click();
		    	  Thread.sleep(4000);
			} catch (Exception e) {
				System.out.println("NO records availble on the grid");
			}
	    
	    }
	    @Test(priority=15,dependsOnMethods = "mylogin", enabled=false)
	    public void Assignedtab_scrollbar() throws InterruptedException {
	    	  // Create an instance of JavascriptExecutor
	    	  JavascriptExecutor jsopen = (JavascriptExecutor) driver;
 
	    	  // Scroll down by pixel
	    	  jsopen.executeScript("window.scrollBy(0, 500);");
	    	  Thread.sleep(4000);
 
	    	  jsopen.executeScript("window.scrollBy(0, -500);");
	    	  driver.findElement(By.xpath("//i[contains(@title,'View filters option')]")).click();
	    	  Thread.sleep(4000);
	    }

 

}
