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
 
public class All_Projects {
 
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
 
	    @Test(priority=1 , groups="Sanity")
	    public void mylogin() throws InterruptedException {
	    	driver.get("https://qonductor-qa.myqone.com/");// configfiles
//			driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
			driver.manage().window().maximize();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//input[@id='mat-input-0']")).sendKeys("ujwala.gavit@triarqhealth.com");////input[@id='mat-input-0']
			driver.findElement(By.xpath("//button[@type='submit']")).click(); //next button
			Thread.sleep(4000);
			driver.findElement(By.xpath("//input[@id='mat-input-1']")).sendKeys("QA@dec2023"); //password
			Thread.sleep(4000);
			driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button")).click();//sign in
			//Eligibility verification 
			Thread.sleep(6000);
	        // Your login code
	    }
 
	    @Test(priority=2 ,dependsOnMethods = "mylogin",groups="Sanity") // This ensures that mylogin method is executed before access
	    public void accessEv() throws InterruptedException {
	        Thread.sleep(4000);
	        driver.findElement(By.xpath("//*[@id='optEV_Project']/div/div/h5")).click();
	        Thread.sleep(4000);
	    }
	    @Test(priority=3,dependsOnMethods = "mylogin",description="Access Projects menu", groups="Sanity")
	    public void accessProjects() throws InterruptedException {
	    	driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//*[@id='k-tabstrip-tab-6']/span")).click();
			Thread.sleep(6000);
			}
	    @Test(priority=4,dependsOnMethods = "mylogin",description="Access Projects>> All Projects",groups="Sanity", enabled =false )
	    public void Allprjtab123() throws InterruptedException {
	    	 //All projects tab	
	    	  driver.findElement(By.xpath("(//span[@class='k-link ng-tns-c404-7'])[7]")).click(); //Projects >>all projects tab access
	    	  Thread.sleep(4000);
	    	  driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
	    	  Thread.sleep(6000);
	    }
	    @Test(priority=5,dependsOnMethods = "mylogin",description="Access Projects>> All Projects>> open view filter options",groups="Sanity")
	    public void Allprjtab_viewfilter() throws InterruptedException {
	    	 //all projects tab
	    	 WebElement viewfilter=driver.findElement(By.xpath("//i[contains(@title,'View filters option')]"));//all projects>>view filter options
	    	  viewfilter.click();
	    	  Thread.sleep(6000);
	    }
	    @Test(priority=8,description="select priority filter",groups="Sanity")
	    public void Allprjtab_priorityfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 //select priority filter
	    	  WebElement dropdown = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[4]"));
	    	  dropdown.click();
//	    	  WebDriverWait wait = new WebDriverWait(driver, 10);
//	    	  WebElement dropdownOptions = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));
//	    	  WebElement desiredOption = dropdownOptions.findElement(By.xpath("//li[text()='High']"));
//	    	  desiredOption.click();
	    	  Thread.sleep(4000);
	    	  driver.findElement(By.id("btnApplyFilter")).click();
	    	  Thread.sleep(6000);
	    }
	    @Test(priority=9,dependsOnMethods = "mylogin", groups="Sanity")
	    public void allprojects_ownerfilter() throws InterruptedException {
	    	 //Assigned tab
	    	//select owner filter
	    	  WebElement all_dropdown_owner = driver.findElement(By.xpath("//div[contains(@class,'k-multiselect-wrap k-floatwrap')]"));
	    	  all_dropdown_owner.click();
 
	    	  //WebElement dropdownElement = driver.findElement(By.xpath("//div[@class='form-group']//kendo-dropdownlist[@formcontrolname='fcClient']"));
	    	  //Select dropdownw = new Select(dropdownElement);
	    	  //dropdownw.selectByVisibleText("Women Care Clinics");
	    }
	    @Test(priority=10,dependsOnMethods = "mylogin", groups="Sanity")
	    public void Allprjtab_projectfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 //select project filter
	    	  WebElement dropdown_project = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[6]"));
	    	  dropdown_project.click();   
	    }

	    @Test(priority=10,dependsOnMethods = "mylogin", enabled=true, groups="Sanity")
	    public void Status_projectfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 //select project filter
	    	  WebElement dropdown_project = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[6]"));
	    	  dropdown_project.click();   
	    }
	    @Test(priority=11,dependsOnMethods = "mylogin", groups="Sanity")
	    public void Allprjtab_Appointmnetfilter() throws InterruptedException {
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
	    	  Thread.sleep(2000);
	    }
	   @Test(priority=12,dependsOnMethods = "mylogin",  groups="Sanity")
	    public void alltab_Appointmnetfilter() throws InterruptedException {
	    	 //Assigned tab
	    	 //Appointmnet date 
		   try {
			   WebElement calendar_apptdate_all = driver.findElement(By.xpath("(//span[contains(@class,'k-icon k-i-calendar')])[2]"));
		    	  calendar_apptdate_all.click();
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
	    @Test(priority=13,dependsOnMethods = "mylogin",groups="Sanity")
	    public void Allprjtab_Exporttoexcel() throws InterruptedException {
	    	try {
	    		 driver.findElement(By.xpath("(//span[contains(.,'Export Excel')])[1]")).click();
		    	  Thread.sleep(4000);
			} catch (Exception e) {
				System.out.println("No data found");
			}
	    	 
	    }
	    @Test(priority=14,dependsOnMethods = "mylogin", enabled=true)
	    public void Allprjtab_projectdeatils() throws InterruptedException {
	    	 //Assigned tab
	    	driver.findElement(By.xpath("(//a[@class='ng-star-inserted'])[1]")).click(); //project details open
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
 
 
	    	  driver.findElement(By.xpath("//button[@class='close']")).click();
	    	  Thread.sleep(4000);
	    }
	    @Test(priority=15,dependsOnMethods = "mylogin",groups="Sanity")
	    public void Allprjtab_scrollbar() throws InterruptedException {
	    	  // Create an instance of JavascriptExecutor
	    	try {
	    		JavascriptExecutor jsopen = (JavascriptExecutor) driver;
	    		 
		    	  // Scroll down by pixel
		    	  jsopen.executeScript("window.scrollBy(0, 500);");
		    	  Thread.sleep(4000);
	 
		    	  jsopen.executeScript("window.scrollBy(0, -500);");
		    	  driver.findElement(By.xpath("//i[contains(@title,'View filters option')]")).click();
		    	  Thread.sleep(4000);
			} catch (Exception e) {
				System.out.println("No data found");
			}
	    	  
	    }


}
