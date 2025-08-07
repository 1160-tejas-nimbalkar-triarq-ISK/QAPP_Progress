package testcases;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import io.github.bonigarcia.wdm.WebDriverManager;

public class login {

	WebDriver driver;

	@BeforeClass
	public void setup() {
		WebDriverManager.chromedriver().setup(); // base
		driver = new ChromeDriver(); // base
	}

	@Test(priority = 1)
	public void mylogin() throws InterruptedException {
		driver.get("https://qonductor-qa.myqone.com/");// configfiles
		// driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		driver.manage().window().maximize();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-0']")).sendKeys("ujwala.gavit@triarqhealth.com");//// input[@id='mat-input-0']
		driver.findElement(By.xpath("//button[@type='submit']")).click(); // next button
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-1']")).sendKeys("QA@dec2023"); // password
		Thread.sleep(4000);
		driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button"))
				.click();// sign in
		// Eligibility verification
		Thread.sleep(6000);

	}

	@Test(priority = 2, dependsOnMethods = "mylogin") // Eligibility verification accessible
	public void access() throws InterruptedException {
		Thread.sleep(4000);
		driver.findElement(By.xpath("//*[@id='optEV_Project']/div/div/h5")).click();
		Thread.sleep(4000);
	}

	@AfterClass
	public void teardown() {
		driver.close();
	}

	@Test(priority = 3, dependsOnMethods = "mylogin", enabled = true)
	public void dashboard() throws InterruptedException {
		WebElement calendarIcon = driver.findElement(By.xpath("//span[@class='k-icon k-i-calendar']"));

		calendarIcon.click();

		Thread.sleep(2000);

		// driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
		driver.findElement(By.xpath("//li[@data-date-index='5'][contains(.,'Feb')]")).click();

		Thread.sleep(2000);
		driver.findElement(By.xpath("(//span[@class='k-link'][contains(.,'22')])[1]")).click();

		Thread.sleep(2000);

		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();

		Thread.sleep(2000);
		
		driver.findElement(By.xpath("//span[@title='MIUEV_02222024'][contains(.,'MIUEV_02222024')]")).click();
		Thread.sleep(4000);
		
		driver.findElement(By.id("btnClearFilter")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 4, dependsOnMethods = "mylogin", enabled = true)
	public void scrollbardashboar() throws InterruptedException {
		// Create an instance of JavascriptExecutor
		JavascriptExecutor js = (JavascriptExecutor) driver;

		// Scroll down by pixel
		js.executeScript("window.scrollBy(0, 700);");
		Thread.sleep(4000);
	}

	@Test(priority = 5, dependsOnMethods = "mylogin")
	public void accessProjects() throws InterruptedException {
		driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); // Eligibility verification
		Thread.sleep(4000);
	}

	@Test(priority = 6, dependsOnMethods = "mylogin")
	public void openviewfilter() throws InterruptedException {
		WebElement viewfilter = driver.findElement(
				By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']"));// open>>view
																													// filter
																													// options
		viewfilter.click();
		Thread.sleep(4000);
	}

	@Test(priority = 7, dependsOnMethods = "mylogin", enabled = true)
	public void openpriorityfilter() throws InterruptedException {
		// select priority filter
		try {
			WebElement dropdown = driver.findElement(By.xpath("//span[@class='k-input']"));
			dropdown.click();
//			WebDriverWait wait1 = new WebDriverWait(driver, 10);
			WebDriverWait waitsample = (WebDriverWait) driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
			WebElement dropdownOptions = waitsample
					.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));

			WebElement desiredOption = dropdownOptions.findElement(By.xpath("//li[text()='High']"));
			desiredOption.click();
			Thread.sleep(4000);
			driver.findElement(By.id("btnApplyFilter")).click();
			Thread.sleep(6000);
		} catch (Exception e) {

			System.out.println("select priority status as High and apply filter");
		}

	}

	@Test(priority = 8, dependsOnMethods = "mylogin", enabled = true)
	public void openprojectfilter() throws InterruptedException {
		// select project name
		WebElement dropdownp = driver.findElement(By.xpath("(//span[@class='k-icon k-i-arrow-s'])[2]"));
		dropdownp.click();
		Thread.sleep(4000);
//    			WebDriverWait waitp = new WebDriverWait(driver, 10);
//    			Thread.sleep(4000);
//    			WebElement dropdownOptionsp = waitp.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("(//span[@class='k-icon k-i-arrow-s'])[2]")));
//    			Thread.sleep(4000);
//    			dropdownOptionsp.click();
	}

	@Test(priority = 9, dependsOnMethods = "mylogin", enabled = true)
	public void openclearbutton() throws InterruptedException {
		driver.findElement(By.id("btnClearFilter")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 12, dependsOnMethods = "mylogin", enabled = true)
	public void importprojectbutton() throws InterruptedException {
		// click on import project
		WebElement btnimport = driver.findElement(By.xpath(
				"//*[@id=\"k-tabstrip-tabpanel-0\"]/div/app-evopenedprojectqueue/div[1]/div/div[3]/div[1]/button[3]"));
		btnimport.click();
		Thread.sleep(4000);
		// close open project window
		driver.findElement(By.xpath("//button[contains(text(),'Close') and @class='btn btn-secondary']")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 10, dependsOnMethods = "mylogin", enabled = true)
	public void openduedaten() throws InterruptedException {
		// click on open tab due date filter
		// due date
		WebElement calendar_duedate = driver.findElement(By.xpath("(//span[@class='k-icon k-i-calendar'])[1]"));

		calendar_duedate.click();

		Thread.sleep(2000);

		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();

		Thread.sleep(2000);

		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();

		Thread.sleep(2000);
		driver.findElement(By.id("btnClearFilter")).click();

	}

	@Test(priority = 11, dependsOnMethods = "mylogin", enabled = true)
	public void openapptdate() throws InterruptedException {
		// click on Appointmnet report date
		WebElement calendar_apptdate = driver.findElement(By.xpath("(//span[@class='k-icon k-i-calendar'])[2]"));

		calendar_apptdate.click();

		Thread.sleep(4000);

		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();

		Thread.sleep(4000);

		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
		Thread.sleep(4000);

		
		driver.findElement(By.id("btnClearFilter")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 13, dependsOnMethods = "mylogin", enabled = true)
	public void openscroll() throws InterruptedException {
		// Open tab scroll bar up and down
		// Create an instance of JavascriptExecutor
		JavascriptExecutor jsopen = (JavascriptExecutor) driver;

		// Scroll down by pixel
		jsopen.executeScript("window.scrollBy(0, 500);");
		Thread.sleep(4000);

		jsopen.executeScript("window.scrollBy(0, -500);");
		driver.findElement(By.xpath("//i[contains(@title,'View filters option')]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 14, dependsOnMethods = "mylogin", enabled = true)
	public void createprojectbutton() throws InterruptedException {
		// create project button click
		try {
			driver.findElement(By.xpath(
					"//*[@id=\"k-tabstrip-tabpanel-0\"]/div/app-evopenedprojectqueue/div[1]/div/div[3]/div[1]/button[5]"))
					.click();
			Thread.sleep(4000);
			WebElement radio1 = driver.findElement(By.id("fcReporttypeApp"));
			Thread.sleep(2000);
			WebElement radio2 = driver.findElement(By.id("fcReporttypeDot"));
			Thread.sleep(2000);
			radio2.click();
			Thread.sleep(2000);
			System.out.println(radio1.isSelected());
			Thread.sleep(2000);
			System.out.println(radio2.isSelected());
			Thread.sleep(4000);
			System.out.println("If interface Inactivated verified Error message");
			System.out.println("As interface is Inactivated close button clicked");
			// driver.findElement(By.xpath("(//button[@data-dismiss='modal'])[5]")).click();
			Thread.sleep(2000);

		} catch (Exception e) {
			System.out.println("As interface is Inactivated close button clicked");

		}

	}

	@Test(priority = 15, dependsOnMethods = "mylogin", enabled = true)
	public void createprojectclient() throws InterruptedException {
		// select client drop down
		try {
			// driver.findElement(By.xpath("//*[@id=\"createprojectModal\"]/div/app-evcreate-project-qinsight/div/div[3]/button[1]")).click();
			WebElement dropdownElement = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[18]"));
			dropdownElement.click();
			Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("Default client is loaded");
		}
	}

	@Test(priority = 16, dependsOnMethods = "mylogin", enabled = true)
	public void createprojectapptdate() throws InterruptedException {
		// create project button click : Appointment Report Date

		WebElement calappt = driver.findElement(By.xpath("(//span[@class='k-icon k-i-calendar'])[5]"));

		calappt.click();

		Thread.sleep(4000);

		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();

		Thread.sleep(4000);
	}

	@Test(priority = 16, dependsOnMethods = "mylogin", enabled = true)
	public void createprojectsavebtn() throws InterruptedException {
		// create project button click : Save button click
//		driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Save')])[2]")).click();
//		Thread.sleep(8000);
		driver.findElement(By.xpath("(//button[contains(.,'Close')])[2]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 17, dependsOnMethods = "mylogin", enabled = false)
	public void createprojectclosebtn() throws InterruptedException {
		// create project button click : close button click
		try {
			driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Close')])[2]")).click();
			Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("close button not click");
		}

	}

	@Test(priority = 18, dependsOnMethods = "mylogin", enabled = false)
	public void importprojectbtn() throws InterruptedException {
		// Import button
		driver.findElement(By.xpath("//button[@type='button'][contains(.,'Import Project')]")).click();
		Thread.sleep(4000);
		driver.findElement(By.xpath("(//button[contains(.,'Close')])[1]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 19, dependsOnMethods = "mylogin", enabled = false)
	public void selectfiletoimportbtn() throws InterruptedException {
		// Import button
		driver.findElement(By.xpath("//button[contains(.,'Select File To Import')]")).click();
		Thread.sleep(2000);
	}

	@Test(priority = 20, dependsOnMethods = "mylogin", enabled = false)
	public void importprojectclosepopup() throws InterruptedException {
		// Import project: close window pop up
		driver.findElement(By.xpath("(//button[contains(.,'Close')])[1]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 21, dependsOnMethods = "mylogin", enabled = true)
	public void openexporttoexcel() throws InterruptedException {
		// export to excel
		try {
			driver.findElement(By.xpath("//button[contains(.,'Export to Excel')]")).click();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//button[contains(.,'Yes')]")).click();
			Thread.sleep(4000);
		} catch (Exception e) {
			// TODO: handle exception
		}

	}

	@Test(priority = 21, dependsOnMethods = "mylogin", enabled = true)
	public void openselectgridproject() throws InterruptedException {
		// select grid check box to select project
		driver.findElement(By.xpath("(//input[@type='checkbox'])[2]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 22, dependsOnMethods = "mylogin", enabled = false)
	public void openAssignproject() throws InterruptedException {
		// assign btn click
		try {
			driver.findElement(By.xpath("//button[contains(@id,'btnAssignWork')]")).click();
			Thread.sleep(4000);
			driver.findElement(By.xpath("//button[contains(@id,'CancelWork')]")).click();
			Thread.sleep(4000);
		} catch (Exception e) {
			System.out.println("error occured during execution");
		}

	}

	@Test(priority = 23, dependsOnMethods = "mylogin", enabled = true)
	public void openInstructions() throws InterruptedException {
		// add instructions
		try {
			driver.findElement(By.xpath("//button[contains(.,'Add Instruction')]")).click();
			Thread.sleep(4000);
			driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Close')])[2]")).click();
			Thread.sleep(4000);
		} catch (Exception e) {
			// TODO: handle exception
		}

	}

	@Test(priority = 24, dependsOnMethods = "mylogin", enabled = true)
	public void open_voidbtn() throws InterruptedException {
		// void click
		try {
			driver.findElement(By.xpath("//button[contains(.,'Void Project')]")).click();
			Thread.sleep(2000);
		} catch (Exception e) {
			// TODO: handle exception
		}

	}

	@Test(priority = 25, dependsOnMethods = "mylogin", enabled = true)
	public void open_addvoidcomment() throws InterruptedException {
		try {
			// void click >> add commnet in text area
			// Locate the textarea element by using its attributes
			WebElement textarea = driver.findElement(By.cssSelector("textarea[formcontrolname='fcComment']"));

			// Type text into the textarea
			textarea.sendKeys("This project is voided due to Zero patient count.");
			Thread.sleep(4000);
			// close void pop up
			driver.findElement(By.xpath("(//button[@data-dismiss='modal'][contains(.,'Cancel')])[2]")).click();
			Thread.sleep(4000);
		} catch (Exception e) {
			// TODO: handle exception
		}

	}

	@Test(priority = 26, dependsOnMethods = "mylogin", enabled = true)
	public void open_projectdeatils() throws InterruptedException {
		try {
			driver.findElement(By.xpath("(//a[contains(@data-toggle,'modal')])[2]")).click();
			Thread.sleep(4000);

			driver.findElement(By.xpath("//span[contains(.,'Instructions(Total: 0)')]")).click(); // Instruction
			Thread.sleep(2000);

			driver.findElement(By.xpath("//span[contains(.,'Workitems (Total: 4)')]")).click(); // workitems
			Thread.sleep(6000);

			driver.findElement(By.xpath("//span[contains(.,'History')]")).click(); // history
			Thread.sleep(4000);

			driver.findElement(By.xpath("//button[@class='close']")).click(); // close
			Thread.sleep(4000);
		} catch (Exception e) {
			// TODO: handle exception
		}

	}

	@Test(priority = 27, dependsOnMethods = "mylogin", enabled = false)
	public void open_workitemspages() throws InterruptedException {
		// Click on the next page button if available
		WebElement nextPageButton = driver.findElement(By.xpath("//button[contains(@class, 'next-page')]"));
		// Replace with the actual locator of the next page button
		Thread.sleep(6000);
		if (nextPageButton.isDisplayed()) {
			nextPageButton.click();
		}
		Thread.sleep(6000);
		// Similarly, you can handle the previous page button if needed
		WebElement prevPageButton = driver.findElement(By.xpath("//button[contains(@class, 'prev-page')]"));
		// Replace with the actual locator of the previous page button
		Thread.sleep(6000);
		if (prevPageButton.isDisplayed()) {
			prevPageButton.click();
		}
		Thread.sleep(6000);
	}

	@Test(priority = 28, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab() throws InterruptedException {
		// Assigned tab
		driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); // Eligibility verification
		Thread.sleep(4000);
		driver.findElement(By.xpath("(//span[contains(@class,'k-link ng-tns-c404-0')])[2]")).click(); // Projects
																										// >>assigned
																										// tab access
		Thread.sleep(4000);
	}

	@Test(priority = 29, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab_viewfilter() throws InterruptedException {
		// Assigned tab
		WebElement viewfilter = driver.findElement(By.xpath("//i[contains(@title,'View filters option')]"));// open>>view
																											// filter
																											// options
		viewfilter.click();
		Thread.sleep(6000);
	}

	@Test(priority = 30, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab_priorityfilter() throws InterruptedException {
		// Assigned tab
		// select priority filter
		WebElement dropdown = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[4]"));
		dropdown.click();

//    	  WebDriverWait waitassign = new WebDriverWait(driver, 10);
//    	  WebElement dropdownOptions = waitassign.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));
//    	  WebElement desiredOption = dropdownOptions.findElement(By.xpath("//li[text()='High']"));
//    	  desiredOption.click();
//    	// Use explicit wait instead of Thread.sleep
//          wait.until(ExpectedConditions.elementToBeClickable(By.id("btnApplyFilter"))).click();
		driver.findElement(By.id("btnApplyFilter")).click();
	}

	@Test(priority = 31, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab_ownerfilter() throws InterruptedException {
		// Assigned tab
		// select owner filter
		WebElement dropdown_owner = driver
				.findElement(By.xpath("//div[contains(@class,'k-multiselect-wrap k-floatwrap')]"));
		dropdown_owner.click();
		Thread.sleep(4000);

		// WebElement dropdownElement =
		// driver.findElement(By.xpath("//div[@class='form-group']//kendo-dropdownlist[@formcontrolname='fcClient']"));
		// Select dropdownw = new Select(dropdownElement);
		// dropdownw.selectByVisibleText("Women Care Clinics");
	}

	@Test(priority = 32, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab_projectfilter() throws InterruptedException {
		// Assigned tab
		// select project filter
		WebElement dropdown_project = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[6]"));
		dropdown_project.click();
		Thread.sleep(4000);
	}

	@Test(priority = 33, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab_duedatefilter() throws InterruptedException {
		// Assigned tab
		// due date
		WebElement calendar_duedate = driver
				.findElement(By.xpath("(//span[contains(@class,'k-icon k-i-calendar')])[1]"));
		calendar_duedate.click();
		Thread.sleep(2000);
		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
		Thread.sleep(2000);
		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
		Thread.sleep(2000);
		driver.findElement(By.id("btnClearFilter")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 34, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab_Appointmnetfilter() throws InterruptedException {
		// Assigned tab
		// Appointmnet date
		WebElement calendar_apptdate = driver
				.findElement(By.xpath("(//span[contains(@class,'k-icon k-i-calendar')])[2]"));
		calendar_apptdate.click();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
		Thread.sleep(4000);
		driver.findElement(By.id("btnClearFilter")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 35, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab_scrollbar() throws InterruptedException {
		// Assigned tab
		// scroll bar
		// Create an instance of JavascriptExecutor
		JavascriptExecutor jsopen = (JavascriptExecutor) driver;

		// Scroll down by pixel
		jsopen.executeScript("window.scrollBy(0, 500);");
		Thread.sleep(4000);

		jsopen.executeScript("window.scrollBy(0, -500);");
		driver.findElement(By.xpath("//i[contains(@title,'View filters option')]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 36, dependsOnMethods = "mylogin", enabled = false)
	public void Assignedtab_projectdeatils() throws InterruptedException {
		// Assigned tab
		driver.findElement(By.xpath("(//a[@class='ng-star-inserted'])[1]")).click(); // project details open
		Thread.sleep(4000);

		// driver.findElement(By.xpath("(//span[@class='k-link
		// ng-tns-c402-2'])[2]")).click();
		// Thread.sleep(4000);
		//
		// driver.findElement(By.xpath("(//span[@class='k-link
		// ng-tns-c402-2'])[2]")).click();
		// Thread.sleep(4000);
		//
		// driver.findElement(By.xpath("//span[contains(.,'Workitems (Total:
		// 0)')]")).click();
		// Thread.sleep(6000);
		//
		// driver.findElement(By.xpath("//span[contains(.,'History')]")).click();
		// Thread.sleep(4000);

		driver.findElement(By.xpath("//button[@class='close']")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 38, dependsOnMethods = "mylogin", enabled = false)
	public void inprocesstab() throws InterruptedException {
		// Inprocess tab
		driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); // Eligibility verification
		Thread.sleep(4000);
		driver.findElement(By.xpath("(//span[contains(@class,'k-link ng-tns-c404-0')])[3]")).click(); // Projects
																										// >>assigned
																										// tab access
		Thread.sleep(4000);
	}

	@Test(priority = 39, dependsOnMethods = "mylogin", enabled = false)
	public void inprocess_viewfilter() throws InterruptedException {
		// Inprocess tab
		WebElement viewfilter1 = driver.findElement(By.xpath("//i[contains(@title,'View filters option')]"));// open>>view
																												// filter
																												// options
		viewfilter1.click();
		Thread.sleep(6000);
	}

	@Test(priority = 40, dependsOnMethods = "mylogin", enabled = false)
	public void inprocesstab_viewfilter() throws InterruptedException {
		// Inprocess tab
		// select priority filter
		WebElement dropdown1 = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[4]"));
		dropdown1.click();
//    	  WebDriverWait wait1view = new WebDriverWait(driver, 10);
//    	  WebElement dropdownOptions1 = wait1view.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));
//    	  WebElement desiredOption1 = dropdownOptions1.findElement(By.xpath("//li[text()='High']"));
//    	  desiredOption1.click();
		Thread.sleep(4000);
		driver.findElement(By.id("btnApplyFilter")).click();
		Thread.sleep(6000);
	}

	@Test(priority = 41, dependsOnMethods = "mylogin", enabled = false)
	public void inprocesstab_owner() throws InterruptedException {
		// Inprocess tab
		// select owner filter
		WebElement dropdown_owner1 = driver
				.findElement(By.xpath("//div[contains(@class,'k-multiselect-wrap k-floatwrap')]"));
		dropdown_owner1.click();
	}

	@Test(priority = 42, dependsOnMethods = "mylogin", enabled = false)
	public void inprocesstab_projectfilter() throws InterruptedException {
		// Inprocess tab
		// select project filter
		WebElement dropdown_project1 = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[6]"));
		dropdown_project1.click();
	}

	@Test(priority = 43, dependsOnMethods = "mylogin", enabled = false)
	public void inprocesstab_duedate() throws InterruptedException {
		// Inprocess tab
		// select due date filter
		// due date
		WebElement calendar_duedate1 = driver
				.findElement(By.xpath("(//span[contains(@class,'k-icon k-i-calendar')])[1]"));
		calendar_duedate1.click();
		Thread.sleep(2000);
		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
		Thread.sleep(2000);
		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
		Thread.sleep(2000);
		driver.findElement(By.id("btnClearFilter")).click();
		Thread.sleep(2000);
	}

	@Test(priority = 44, dependsOnMethods = "mylogin", enabled = false)
	public void inprocesstab_Appointmnet() throws InterruptedException {
		// Inprocess tab
		// Appointmnet date
		WebElement calendar_apptdate1 = driver
				.findElement(By.xpath("(//span[contains(@class,'k-icon k-i-calendar')])[2]"));
		calendar_apptdate1.click();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
		driver.findElement(By.id("btnClearFilter")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 45, dependsOnMethods = "mylogin", enabled = false)
	public void inprocesstab_scrollbar() throws InterruptedException {
		// Inprocess tab : scroll bar
		// Create an instance of JavascriptExecutor
		JavascriptExecutor jsopen1 = (JavascriptExecutor) driver;
		// Scroll down by pixel
		jsopen1.executeScript("window.scrollBy(0, 500);");
		Thread.sleep(4000);
		jsopen1.executeScript("window.scrollBy(0, -500);");
		driver.findElement(By.xpath("//i[contains(@title,'View filters option')]")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 46, dependsOnMethods = "mylogin", enabled = false)
	public void inprocesstab_projectdeatils() throws InterruptedException {
		// Inprocess tab : scroll bar
		driver.findElement(By.xpath("(//a[@class='ng-star-inserted'])[1]")).click(); // project details open
		Thread.sleep(4000);

		// driver.findElement(By.xpath("(//span[@class='k-link
		// ng-tns-c402-2'])[2]")).click();
		// Thread.sleep(4000);
		//
		// driver.findElement(By.xpath("(//span[@class='k-link
		// ng-tns-c402-2'])[2]")).click();
		// Thread.sleep(4000);
		//
		// driver.findElement(By.xpath("//span[contains(.,'Workitems (Total:
		// 0)')]")).click();
		// Thread.sleep(6000);
		//
		driver.findElement(By.xpath("//span[contains(.,'History')]")).click();
		Thread.sleep(4000);

		driver.findElement(By.xpath("//button[@class='close']")).click();
		Thread.sleep(4000);
	}

	@Test(priority = 47, dependsOnMethods = "mylogin", enabled = false)
	public void myprojecttab() throws InterruptedException {
		// my project >>Projects
		driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); // Eligibility verification
		Thread.sleep(4000);
		driver.findElement(By.xpath("(//span[contains(@class,'k-link ng-tns-c404-0')])[4]")).click();
		Thread.sleep(4000);
		driver.findElement(
				By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']"))
				.click();
		Thread.sleep(9000);
	}
}
