package testcases;


import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import io.github.bonigarcia.wdm.WebDriverManager;

public class Pending_projects {
	
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
      
    }
 
    @Test(priority=2 ,dependsOnMethods = "mylogin") // This ensures that mylogin method is executed before access
    public void access() throws InterruptedException {
        Thread.sleep(4000);
        driver.findElement(By.xpath("//*[@id='optEV_Project']/div/div/h5")).click();
        Thread.sleep(4000);
    }
    @Test(priority=3,dependsOnMethods = "mylogin")
    public void accessProjects() throws InterruptedException {
    	driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); //Eligibility verification
		Thread.sleep(4000);
		}
  @Test(priority=4,dependsOnMethods = "mylogin",enabled=true)
    public void pendingtabaccess() throws InterruptedException {
    	//Projects >>Pending tab accessed 
    			driver.findElement(By.xpath("//*[@id='k-tabstrip-tab-4']/span")).click();	
    			Thread.sleep(4000);
    			driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
    			Thread.sleep(9000);
    }
    @Test(priority=5,dependsOnMethods = "mylogin",enabled=true)
    public void Pending_Appdetails() throws InterruptedException {
    	try {
    		driver.findElement(By.xpath("(//i[contains(@title,'View Patient Details')])[1]")).click();	
			Thread.sleep(4000);
			driver.findElement(By.xpath("(//span[@class='k-link ng-tns-c404-7'])[2]")).click();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//*[@id=\"viewWorkitemdetailsModal\"]/app-evpatient-history/div/div[1]/button")).click();
			Thread.sleep(4000);

	//scroll bar
			// Create an instance of JavascriptExecutor
	        JavascriptExecutor js = (JavascriptExecutor) driver;

	        // Scroll down by pixel
	        js.executeScript("window.scrollBy(0, 700);");
	        Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("No data found");
		}
		
    			
    }
    
    @Test(priority=6,dependsOnMethods = "mylogin")
    public void pending_assign_btn() throws InterruptedException {
    	try {
    		driver.findElement(By.xpath("//*[@id=\"k-tabstrip-tabpanel-4\"]/div/app-evmyprojectqueuebypatient/div[1]/div/div/div[4]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[1]")).click();//select record from grid on tick check box
        	Thread.sleep(4000);
        	driver.findElement(By.xpath("//button[contains(@id,'btnAssignWork')]")).click();
        	Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("No data found");
		}
    	
    }
    
    @Test(priority=7,dependsOnMethods = "mylogin")
    public void Pending_assign_Work() throws InterruptedException {
    	try {
    		WebElement dropdown_agent = driver.findElement(By.xpath("(//span[@unselectable='on'][contains(.,'Select')])[2]"));
        	dropdown_agent.click();
        	Thread.sleep(4000);
        	WebElement searchdropdown= driver.findElement(By.xpath("//input[contains(@tabindex,'-1')]"));
        	Thread.sleep(4000);
        	searchdropdown.sendKeys(Keys.ENTER);
        	Thread.sleep(4000);
        	driver.findElement(By.xpath("//button[contains(@id,'CancelWork')]")).click();
        	Thread.sleep(4000);
        	driver.findElement(By.xpath("//input[@id='k-grid3-checkbox0']")).click();//select record from grid on tick check box to untick records
        	Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("No data found");
		}
    	
    }
    
    @Test(priority=8,dependsOnMethods = "mylogin")
    public void Pending_projectdetails() throws InterruptedException {
    	//pending >> view patient details
    	try {
    		driver.findElement(By.xpath("(//i[contains(@title,'View Patient Details')])[1]")).click();
        	Thread.sleep(4000);
        	/*
        	//instructions
        	driver.findElement(By.xpath("(//span[contains(@class,'k-link ng-tns-c402-14')])[2]")).click();
        	Thread.sleep(4000);
        	//workitems
        	driver.findElement(By.xpath("(//span[contains(@class,'k-link ng-tns-c402-14')])[3]")).click();
        	Thread.sleep(4000);
        	//History
        	driver.findElement(By.xpath("(//span[contains(@class,'k-link ng-tns-c402-14')])[4]")).click();
        	Thread.sleep(4000);
        	*/
        	//close
//        	driver.findElement(By.xpath("(//button[@class='close'])[2]")).click();
//        	Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("No data found");
		}
    
   }

    @Test(priority=9,dependsOnMethods = "mylogin")
    public void Pending_projectdetails_view() throws InterruptedException {
    	try {
    		driver.findElement(By.xpath("(//i[contains(@data-target,'#viewWorkitemdetailsModal')])[1]")).click();
        	Thread.sleep(4000);
        	driver.findElement(By.xpath("(//span[@class='k-link ng-tns-c404-1'])[2]")).click();
        	Thread.sleep(4000);
        	driver.findElement(By.xpath("(//button[@class='close'])[1]")).click();
        	Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("No data found");
		}
    
    }

    @Test(priority=11,dependsOnMethods = "mylogin")
    public void Pending_Assign() throws InterruptedException {
    	//Byproject button click
    	try {
    		driver.findElement(By.xpath("(//input[contains(@class,'k-checkbox ng-star-inserted')])[1]")).click(); //select checkbox for project select
        	Thread.sleep(4000);
        /*	//check assign button enabled :option 1
        	 // Locate the "Assign" button using its ID
        //	driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Assign')])[1]")).click(); //assign enabled and click
            WebElement assignButton = driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Assign')])[1]"));
            // Check if the button is enabled before clicking
            if (assignButton.isEnabled()) {
                // Click the "Assign" button
                assignButton.click();
                Thread.sleep(4000);
            } else {
                System.out.println("The Assign button is disabled.");
                // Handle the case where the button is disabled, if needed
            }
        	Thread.sleep(4000);*/
        	// option 2
        	driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Assign')])[1]")).click(); //assign enabled and click
        	Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("No data found");
		}
    

    }
  /*  @Test(priority=13,dependsOnMethods = "mylogin")
    public void Complete_projects() throws InterruptedException {
    	//Byproject button click
    	driver.findElement(By.xpath("//*[@id='k-tabstrip-tab-5']/span")).click();
    	Thread.sleep(9000);
//		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
//		Thread.sleep(9000);
    }    */

    @Test(priority=14,dependsOnMethods = "mylogin")
    public void PendingProjects_exporttoexcel() throws InterruptedException {
		try {
			driver.findElement(By.xpath("//button[contains(.,'Export to Excel')]")).click();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//button[@type='button'][contains(.,'Yes')]")).click();
			Thread.sleep(2000);
		} catch (Exception e) {
			System.out.println("No data found");
		}
		
	}
}
