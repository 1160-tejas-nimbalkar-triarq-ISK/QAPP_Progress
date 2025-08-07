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

public class View_Task {

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

	@Test(priority = 1)
	public void mylogin() throws InterruptedException {
		driver.get("https://qonductor-staging.myqone.com/");// configfiles
//		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		driver.manage().window().maximize();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-0']")).sendKeys("ujwala.gavit@triarqhealth.com");//// input[@id='mat-input-0']

		driver.findElement(By.xpath("//button[@type='submit']")).click(); // next button
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-1']")).sendKeys("Stg@2023"); // password
		Thread.sleep(4000);
		driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button"))
				.click();// sign in
		// Eligibility verification
		Thread.sleep(6000);
		// Your login code
	}

	@Test(priority = 2, dependsOnMethods = "mylogin") // This ensures that mylogin method is executed before access
	public void access() throws InterruptedException {
		Thread.sleep(4000);
		driver.findElement(By.xpath("//*[@id='optEV_Project']/div/div/h5")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 3, dependsOnMethods = "mylogin")
	public void Task_menu_access() throws InterruptedException {
		// All projects tab
		driver.findElement(By.xpath("//a[@id='idMnuTask']")).click(); // Task menu access
		Thread.sleep(4000);
	}

	@Test(priority = 4, dependsOnMethods = "mylogin")
	public void ViewTask() throws InterruptedException {
		driver.findElement(By.xpath("//a[contains(@id,'idSbMnuViewTask')]")).click(); // tasks >>view task
		Thread.sleep(4000);
	}

	@Test(priority = 5, dependsOnMethods = "mylogin", enabled = true)
	public void Tasktab_viewfilter() throws InterruptedException {
		// all projects tab
		WebElement viewfilter = driver
				.findElement(By.xpath("//i[contains(@class,'fas px-2 pointer fa-chevron-circle-down')]"));// all
																											// projects>>view
																											// filter
																											// options
		viewfilter.click();
		Thread.sleep(6000);
	}

	@Test(priority = 6, dependsOnMethods = "mylogin", enabled = false)
	public void Prcaticefilter() throws InterruptedException {
		// Myqueue tab
		// select project filter
		WebElement dropdown = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[2]"));
		dropdown.click();
		Thread.sleep(4000);
	}

	@Test(priority = 7, dependsOnMethods = "mylogin", enabled = true)
	public void Workstatusfilter() throws InterruptedException {
		// Assigned tab
		// select priority filter
		WebElement dropdown = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[6]"));
		dropdown.click();
		driver.findElement(By.xpath("(//span[@unselectable='on'][contains(.,'Assigned')])[2]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 8, dependsOnMethods = "mylogin", enabled = true)
	public void Priorityfilter() throws InterruptedException {
		// select priority filter
		WebElement dropdown = driver.findElement(By.xpath("(//span[@class='k-icon k-i-arrow-s'])[3]"));
		dropdown.click();
		driver.findElement(By.xpath("//li[text()='High']")).click();
		Thread.sleep(4000);
//  	  WebDriverWait wait = new WebDriverWait(driver, 10);
//  	  WebElement dropdownOptions = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));
//  	  WebElement desiredOption = dropdownOptions.findElement(By.xpath("//li[text()='High']"));
//  	  desiredOption.click();
		driver.findElement(By.id("btnApplyFilter")).click();
		Thread.sleep(6000);
	}

	@Test(priority = 9, dependsOnMethods = "mylogin", enabled = true)
	public void Insurancefilter() throws InterruptedException {
		// select priority filter
		WebElement dropdown_ins = driver
				.findElement(By.xpath("(//div[contains(@class,'k-multiselect-wrap k-floatwrap')])[1]"));
		dropdown_ins.click();
		driver.findElement(By.xpath("//li[text()='AAA']")).click();
		Thread.sleep(4000);
//    	  WebDriverWait wait = new WebDriverWait(driver, 10);
//    	  WebElement dropdownOptions_ins = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("(//input[@class='k-checkbox'])[103]")));
//    	  WebElement desiredOption_ins = dropdownOptions_ins.findElement(By.xpath("//li[text()='BS PPO']"));
//    	  desiredOption_ins.click();
		Thread.sleep(4000);
//    	  driver.findElement(By.id("btnApplyFilter")).click();
//    	  Thread.sleep(6000);

	}

	@Test(priority = 10, dependsOnMethods = "mylogin", enabled = true)
	public void locationdept_filter() throws InterruptedException {
		WebElement location_dropdown_owner = driver
				.findElement(By.xpath("(//div[contains(@class,'k-multiselect-wrap k-floatwrap')])[3]"));
		Thread.sleep(4000);
		location_dropdown_owner.click();
		Thread.sleep(4000);
		try {
			WebElement dept_dropdown_owner = driver
					.findElement(By.xpath("(//div[contains(@class,'k-multiselect-wrap k-floatwrap')])[4]"));
			Thread.sleep(4000);
			dept_dropdown_owner.click();
			Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("No any exception found");
		}
	}

	@Test(priority = 11, dependsOnMethods = "mylogin", enabled = true)
	public void mYqueueprojectfilter() throws InterruptedException {
		WebElement dropdown_project_my = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[14]"));
		dropdown_project_my.click();
	}

	@Test(priority = 12, dependsOnMethods = "mylogin", enabled = true)
	public void Status_projectfilter() throws InterruptedException {
		// Assigned tab
		// select project filter
		WebElement dropdown_project = driver.findElement(By.xpath("//input[@type='text']"));
		dropdown_project.sendKeys("@7878");
		Thread.sleep(2000);
		dropdown_project.click();
		Thread.sleep(2000);
		dropdown_project.clear();
		Thread.sleep(2000);
	}

	@Test(priority = 13, dependsOnMethods = "mylogin", enabled = true)
	public void upviewfilter() throws InterruptedException {
		WebElement Viewfilterup = driver.findElement(By.xpath("//i[contains(@title,'View filters option')]"));
		Viewfilterup.click();
		Thread.sleep(4000);
	}

	@Test(priority = 14, dependsOnMethods = "mylogin", enabled = true)
	public void myqueueExporttoexcel() throws InterruptedException {

		driver.findElement(By.xpath("//button[contains(.,'Export to Excel')]")).click();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//button[contains(.,'Yes')]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 15, dependsOnMethods = "mylogin", enabled = true)
	public void View_projectdeatils() throws InterruptedException {

		try {
			driver.findElement(By.xpath("(//a[@class='ng-star-inserted'])[1]")).click(); // project details open
			Thread.sleep(4000);

//    	    	  driver.findElement(By.xpath("//span[@class='k-link ng-tns-c402-5'][contains(.,'Instructions(Total: 0)')]")).click();//Summary
//    	    	  Thread.sleep(4000);
//    	    	  
//    		  driver.findElement(By.xpath("//span[@class='k-link ng-tns-c402-5'][contains(.,'Instructions(Total: 0)')]")).click(); //instrcutions
//    	    	  Thread.sleep(4000);
//    	    	  
//    	    	  driver.findElement(By.xpath("//*[@id=\"k-tabstrip-tab-2\" and @tabindex=\"0\"]")).click(); //workitems
//    	    	  Thread.sleep(6000);

			driver.findElement(By.xpath("//span[contains(.,'History')]")).click();// History
			Thread.sleep(4000);

			driver.findElement(By.xpath("(//button[contains(@type,'button')])[7]")).click();
			Thread.sleep(4000);

		} catch (Exception e) {
			// TODO: handle exception
		}

	}

	@Test(priority = 16, dependsOnMethods = "mylogin")
	public void Myprojectdetails_view() throws InterruptedException {
		try {
			driver.findElement(By.xpath("(//i[contains(@data-target,'#viewWorkitemdetailsModal')])[1]")).click();
			Thread.sleep(4000);

//driver.findElement(By.xpath("//*[@id=\"k-tabstrip-tab-1\" and @tabindex=\"0\"]")).click();
//Thread.sleep(4000);

			driver.findElement(By.xpath("(//button[@class='close'])[1]")).click();
			Thread.sleep(4000);

		} catch (Exception e) {
			// TODO: handle exception
		}

	}

	@Test(priority = 17, dependsOnMethods = "mylogin", enabled = true)
	public void view_scrollbar() throws InterruptedException {
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
			// TODO: handle exception
		}
		
	}

	

}
