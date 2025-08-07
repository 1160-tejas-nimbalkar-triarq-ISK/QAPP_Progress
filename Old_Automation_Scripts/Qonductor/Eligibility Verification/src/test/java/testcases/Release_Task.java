package testcases;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Release_Task {

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
    	//driver.navigate().to("https://qonductor-staging.myqone.com/");
    	String title= driver.getTitle();
    	System.out.println("title is" +title);
    	//String url=driver.getCurrentUrl();
    	//System.out.println("URL is "+url);
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
    @Test(priority=3,dependsOnMethods = "mylogin")
    public void accessTasks() throws InterruptedException {
    	WebElement taskLink = driver.findElement(By.xpath("//a[@id='idMnuTask' and contains(text(), 'Task')]"));
        taskLink.click();
    	//driver.findElement(By.xpath("(//a[contains(@id,'idMnuClaimWorkqueues')])[1]")).click(); //tasks menu access
		Thread.sleep(4000);
		}
    @Test(priority=4,dependsOnMethods = "mylogin", enabled=true)
    public void ComplTask() throws InterruptedException {
    	 //MyQueue tab
    	  driver.findElement(By.xpath("//a[contains(@id,'idSbMnuReleaseTasks')]")).click(); //completed task
    	  Thread.sleep(4000);
    }
    @Test(priority=5,dependsOnMethods = "mylogin", enabled=true)
    public void TaskComp_viewfilter() throws InterruptedException {
    	 //all projects tab
    	 WebElement viewfilter=driver.findElement(By.xpath("//i[contains(@title,'View filters option')]"));//all projects>>view filter options
    	  viewfilter.click();
    	  Thread.sleep(6000);
    }
  @Test(priority=6,dependsOnMethods = "mylogin", enabled=false)
    public void Prcaticefilter1() throws InterruptedException {
    	 //select filter:
    	 //select practice filter
    	 WebElement dropdown1 = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[2]"));
    	 dropdown1.click();
    	 WebElement searchBox = driver.findElement(By.xpath("//li[contains(.,'Women Care Clinics')]"));
    	 searchBox.click();
    	// searchBox.sendKeys("Women Care Clinics");
    	 Thread.sleep(4000);
    	 searchBox.submit();
//    	 driver.findElement(By.xpath("//button[contains(@id,'btnApplyFilter')]")).click();
//    	 Thread.sleep(4000);
//    	
    }
    @Test(priority=7,dependsOnMethods = "mylogin", enabled=true)
    public void Project_filter() throws InterruptedException {
    	 //select priority filter
   	 WebElement dropdown_priority = driver.findElement(By.xpath("(//span[@unselectable='on'][contains(.,'All')])[2]"));
   	 dropdown_priority.click();
   	 WebElement searchBox_priority = driver.findElement(By.xpath("//li[contains(.,'High')]"));
   	 searchBox_priority.click();
   	 Thread.sleep(4000);
   	/* WebElement searchBox_priority = driver.findElement(By.xpath("//input[contains(@tabindex,'1')]"));
   	 searchBox_priority.sendKeys("High");
   	 Thread.sleep(4000);
   	driver.findElement(By.xpath("//button[contains(@id,'btnApplyFilter')]")).click();*/
    }

    @Test(priority=8,dependsOnMethods = "mylogin", enabled=false)
    public void Projects_filter() throws InterruptedException {
    	 //select Project filter
      	 WebElement dropdown_Project = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[10]"));
      	 dropdown_Project.click();
      	 WebElement searchBox_Project = driver.findElement(By.xpath("//li[contains(.,'2023-10-19_01')]"));//(//span[contains(.,'2023-10-19_01')])[4]
      	 searchBox_Project.click();
      	 Thread.sleep(4000);
    }
    @Test(priority=9,dependsOnMethods = "mylogin", enabled=true)
    public void ptcode_search() throws InterruptedException {
    	 //select Project filter
      	 WebElement ptcode_search = driver.findElement(By.xpath("//input[contains(@type,'text')]"));
//        	  WebElement dropdown_project = driver.findElement(By.xpath("//input[@type='text']"));
      	ptcode_search.sendKeys("@7878");
        	  Thread.sleep(2000);
        	  ptcode_search.click();
        	  Thread.sleep(2000);
        	//  ptcode_search.clear();
        	  driver.findElement(By.id("btnApplyFilter")).click();
          	  Thread.sleep(4000);
          	 driver.findElement(By.id("btnClearFilter")).click();////button[@id='btnClearFilter']
         	  Thread.sleep(4000);
    }
	//select record to released ://a[contains(@id,'idSbMnuReleaseTasks')]
    @Test(priority=10,dependsOnMethods = "mylogin", enabled=true)
    public void Relesaed_Record() throws InterruptedException {
    	 //Myqueue tab
    	 //select project filter
    	  driver.findElement(By.xpath("(//input[contains(@class,'k-checkbox ng-star-inserted')])[2]")).click();
    	  Thread.sleep(4000);
    	  driver.findElement(By.xpath("//button[@type='button'][contains(.,'Release Tasks 1')]")).click();
    	  Thread.sleep(2000);
    	  driver.findElement(By.xpath("//button[@type='button'][contains(.,'Yes')]")).click();
    	  Thread.sleep(4000);
    }
    @Test(priority=11,dependsOnMethods = "mylogin",enabled=false)
    public void accessProjectsfromreleased() throws InterruptedException {
    	driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); //Eligibility verification
		Thread.sleep(4000);
    }
    @Test(priority=12,dependsOnMethods = "mylogin",enabled=false)
    public void accessProjectsfromreleased1() throws InterruptedException {
		driver.findElement(By.xpath("(//span[contains(@class,'k-link ng-tns-c402-0')])[5]")).click();
	  	  Thread.sleep(4000);
		}
    @Test(priority=13,dependsOnMethods = "mylogin",enabled=false)
    public void Pending_patientdetails() throws InterruptedException {
    	//my project >>Projects 
    			driver.findElement(By.xpath("(//i[contains(@title,'View Patient Details')])[1]")).click();	
    			Thread.sleep(4000);
    			driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
    			Thread.sleep(4000);
    }
    @Test(priority=14,dependsOnMethods = "mylogin",enabled=false)
    public void Pending_projectdetails_view() throws InterruptedException {
    	//Bypatient >>Assign button click >>Assign work
    	driver.findElement(By.xpath("(//i[contains(@data-target,'#viewWorkitemdetailsModal')])[1]")).click();
    	Thread.sleep(4000);
    	driver.findElement(By.xpath("//ul[@class='k-reset k-tabstrip-items ng-tns-c402-2 ng-star-inserted']/li[@role='tab'][2]/span[@class='k-link ng-tns-c402-2']")).click();
    	Thread.sleep(4000);

    	driver.findElement(By.xpath("(//button[@class='close'])[1]")).click();
    	Thread.sleep(4000);
    }

    @Test(priority=15,dependsOnMethods = "mylogin",enabled=false)
    public void Pendingtab() throws InterruptedException {
  	  driver.findElement(By.xpath("(//i[contains(@data-target,'#viewWorkitemdetailsModal')])[1]")).click();
  	  Thread.sleep(4000);
  	  driver.findElement(By.xpath("(//span[@title='New'][contains(.,'New')])[1]")).click();
  	  Thread.sleep(4000);
    }
    @Test(priority=16,dependsOnMethods = "mylogin",enabled=false)
    public void automateFilters() {
        // Navigate to the Qonductor page
//        driver.get("https://qonductor-staging.myqone.com/#/evreleasetasks");
//
//        // Wait for the page to load (you may need to adjust the timeout)
//        WebDriverWait wait = new WebDriverWait(driver, 10);
//        wait.until(ExpectedConditions.urlContains("/evreleasetasks"));
 
        // Locate and interact with Assigned To filter
        WebElement assignedToDropdown = driver.findElement(By.xpath("(//div[contains(@class,'k-multiselect-wrap k-floatwrap')])[1]"));
        Select assignedToSelect = new Select(assignedToDropdown);
        assignedToSelect.selectByVisibleText("Ujwala");
 
        // Locate and interact with Location filter
        WebElement locationDropdown = driver.findElement(By.id("location"));
        Select locationSelect = new Select(locationDropdown);
        locationSelect.selectByVisibleText("AAA");
 
        // Locate and interact with Insurance filter
        WebElement insuranceDropdown = driver.findElement(By.id("insurance"));
        Select insuranceSelect = new Select(insuranceDropdown);
        insuranceSelect.selectByVisibleText("A");
 
        // Optionally, perform additional actions as needed
 
    }


	
}
