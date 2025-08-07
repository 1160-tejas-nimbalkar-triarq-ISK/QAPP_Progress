package testcases;


import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class EvDashborad {

	public static void main(String[] args) throws InterruptedException {
		WebDriverManager.chromedriver().setup();
		WebDriver driver = new ChromeDriver();
		driver.get("https://qonductor-qa.myqone.com/");// configfiles
		driver.manage().window().maximize();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-0']")).sendKeys("ujwala.gavit@triarqhealth.com");//// input[@id='mat-input-0']
		Thread.sleep(4000);
		driver.findElement(By.xpath("//button[@type='submit']")).click(); // next button
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-1']")).sendKeys("QA@dec2023"); // password
		Thread.sleep(4000);
		driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button")).click();// sign in
		
		
		// Eligibility verification access
		Thread.sleep(8000);
		driver.findElement(By.xpath("//*[@id='optEV_Project']/div/div/h5")).click();
		Thread.sleep(4000);
		// select priority filter

		// driver.findElement(By.id("btnClearFilter")).click();
		// Assuming there's a button to open the date picker, locate and click on it
//		By calendarIconLocator = By.xpath("//span[@class='k-icon k-i-calendar']");
//		WebElement calendarIcon = driver.findElement(By.xpath("//span[@class='k-icon k-i-calendar']"));
//		calendarIcon.click(); 
		Thread.sleep(4000);
//		 driver.findElement(By.xpath("(//span[contains(.,'Today')])[4]")).click();

		WebElement calendarIcon = driver.findElement(By.xpath("//span[@class='k-icon k-i-calendar']"));
		calendarIcon.click();
		Thread.sleep(2000);
		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
		Thread.sleep(2000);
		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
		Thread.sleep(2000);

		/*
		 * // System.out.println("click "); // Thread.sleep(2000); //
		 * calendarIcon.clear(); // System.out.println("clear"); //
		 * driver.findElement(By.xpath("(//span[contains(.,'Today')])[4]")).click(); //
		 * Thread.sleep(4000);
		 * 
		 * 
		 * // Get the current date in the desired format driver.findElement(By.xpath(
		 * "//*[@id=\"k-3c33b178-e941-47a9-944d-26dc6b2a1537\"]")).click();
		 * SimpleDateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy"); String
		 * currentDate = dateFormat.format(new Date());
		 * 
		 * // Locate and click on the cell corresponding to the current date in the date
		 * picker By currentDateCellLocator =
		 * By.xpath("//td[@aria-selected='true' and text()='" +
		 * currentDate.split("/")[1] + "']"); WebElement currentDateCell =
		 * driver.findElement(currentDateCellLocator); currentDateCell.click();
		 * 
		 * // Assuming there's a submit button By submitButtonLocator =
		 * By.id("submitButtonId"); WebElement submitButton =
		 * driver.findElement(submitButtonLocator); submitButton.click();
		 * Thread.sleep(4000); By inputFieldXPath =
		 * By.xpath("//input[@class='k-input' and @aria-valuetext='2023/11/28']");
		 * WebElement inputField = driver.findElement(inputFieldXPath);
		 * inputField.click();
		 * 
		 */

		// scroll bar
		// Create an instance of JavascriptExecutor
		JavascriptExecutor js = (JavascriptExecutor) driver;

		// Scroll down by pixel
		js.executeScript("window.scrollBy(0, 700);");
		Thread.sleep(4000);
		// pagination
		
		//Projects menu >>open

		driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); 
		Thread.sleep(4000);
		WebElement viewfilter = driver.findElement(
				By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']"));// open>>view
																													// filter
																													// options
		viewfilter.click();
		Thread.sleep(6000);
//select priority filter
		/*
		WebElement dropdown = driver.findElement(By.xpath("//span[@class='k-input']"));
		dropdown.click();
	
		WebDriverWait wait1 = new WebDriverWait(driver, 10);
		WebElement dropdownOptions = wait1.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));
		WebElement desiredOption = dropdownOptions.findElement(By.xpath("//li[text()='High']"));
		desiredOption.click();
		Thread.sleep(4000);
		driver.findElement(By.id("btnApplyFilter")).click();
		Thread.sleep(6000);
//driver.findElement(By.id("btnClearFilter")).click();
//Thread.sleep(4000);
// viewfilter.clear();
 * 
 * 
 */
//select project name
		
		/*
		WebElement dropdownp = driver.findElement(By.xpath("(//span[@class='k-icon k-i-arrow-s'])[2]"));
		dropdownp.click();
		Thread.sleep(4000);
		WebDriverWait waitp = new WebDriverWait(driver, 10);
		Thread.sleep(4000);
		WebElement dropdownOptionsp = waitp.until(
				ExpectedConditions.visibilityOfElementLocated(By.xpath("(//span[@class='k-icon k-i-arrow-s'])[2]")));
		Thread.sleep(4000);
		dropdownOptionsp.click();

//Thread.sleep(4000);
//WebElement desiredOptionp = dropdownOptionsp.findElement(By.xpath("(//span[@unselectable='on'][contains(.,'All')])[4]"));
//desiredOptionp.click();
//Thread.sleep(4000);
//driver.findElement(By.id("btnApplyFilter")).click();
//Thread.sleep(4000);
//driver.findElement(By.id("btnClearFilter")).click();
		Thread.sleep(4000);
		
		
//click on project
//WebElement btnimport =driver.findElement(By.xpath("//*[@id=\"k-tabstrip-tabpanel-0\"]/div/app-evopenedprojectqueue/div[1]/div/div[3]/div[1]/button[3]"));
//btnimport.click();
//
//driver.findElement(By.xpath("//button[contains(text(),'Close') and @class='btn btn-secondary']")).click();
//due date
//WebElement calendar_duedate = driver.findElement(By.xpath("(//span[@class='k-icon k-i-calendar'])[1]"));
//
//calendar_duedate.click();
//
//Thread.sleep(2000);
//
//driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();
//
//Thread.sleep(2000);
//
//driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
//
//Thread.sleep(2000);
//
//driver.findElement(By.id("btnClearFilter")).click();
 * 
 * 
 */

//Appointmnet date 
		WebElement calendar_apptdate = driver.findElement(By.xpath("(//span[@class='k-icon k-i-calendar'])[2]"));

		calendar_apptdate.click();

		Thread.sleep(4000);

		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();

		Thread.sleep(4000);

		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
//
//
//Thread.sleep(2000);
//scroll bar
// Create an instance of JavascriptExecutor
		JavascriptExecutor jsopen = (JavascriptExecutor) driver;

// Scroll down by pixel
		jsopen.executeScript("window.scrollBy(0, 500);");
		Thread.sleep(4000);

		jsopen.executeScript("window.scrollBy(0, -500);");
		driver.findElement(By.xpath("//i[contains(@title,'View filters option')]")).click();
		Thread.sleep(4000);

//create project button click
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
		Thread.sleep(2000);

//select client drop down

//Locate the dropdown element
//driver.findElement(By.xpath("//*[@id=\"createprojectModal\"]/div/app-evcreate-project-qinsight/div/div[3]/button[1]")).click();
		WebElement dropdownElement = driver.findElement(By.xpath("(//span[contains(@unselectable,'on')])[18]"));
		Thread.sleep(4000);
		dropdownElement.click();

//apptdate

		WebElement calappt = driver.findElement(By.xpath("(//span[@class='k-icon k-i-calendar'])[5]"));

		calappt.click();

		Thread.sleep(4000);

		driver.findElement(By.xpath("//span[contains(.,'TODAY')]")).click();

		Thread.sleep(4000);

//driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Save')])[2]")).click();
//Thread.sleep(4000);
		driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Close')])[2]")).click();
		Thread.sleep(4000);

//Import button
		driver.findElement(By.xpath("//button[@type='button'][contains(.,'Import Project')]")).click();
		Thread.sleep(4000);

		driver.findElement(By.xpath("(//button[contains(.,'Close')])[1]")).click();
		Thread.sleep(4000);

//export to excel
		driver.findElement(By.xpath("//button[contains(.,'Export to Excel')]")).click();
		Thread.sleep(4000);

		driver.findElement(By.xpath("(//input[@type='checkbox'])[2]")).click();
		Thread.sleep(4000);

//assign btn click

		driver.findElement(By.xpath("//button[@id='btnAssignWork']")).click();
		Thread.sleep(2000);
		driver.findElement(By.xpath("//button[contains(@id,'CancelWork')]")).click();
		Thread.sleep(4000);

//add instructions
		driver.findElement(By.xpath("//button[contains(.,'Add Instruction')]")).click();
		Thread.sleep(4000);
		driver.findElement(By.xpath("(//button[@type='button'][contains(.,'Close')])[2]")).click();
		Thread.sleep(4000);

//void click
		driver.findElement(By.xpath("//button[contains(.,'Void Project')]")).click();
		Thread.sleep(2000);

//Locate the textarea element by using its attributes
		WebElement textarea = driver.findElement(By.cssSelector("textarea[formcontrolname='fcComment']"));

//Type text into the textarea
		textarea.sendKeys("This is an example text.");
		Thread.sleep(4000);

		driver.findElement(By.xpath("(//button[@data-dismiss='modal'][contains(.,'Cancel')])[2]")).click();
		Thread.sleep(4000);

		driver.findElement(By.xpath("(//a[contains(@title,' 1')])[1]")).click();
		Thread.sleep(4000);

		driver.findElement(By.xpath("//span[contains(.,'Instructions(Total: 0)')]")).click();
		Thread.sleep(4000);

		driver.findElement(By.xpath("//span[contains(.,'Workitems (Total: 1935)')]")).click();
		Thread.sleep(6000);

		driver.findElement(By.xpath("//span[contains(.,'History')]")).click();
		Thread.sleep(4000);

		driver.findElement(By.xpath("//button[@class='close']")).click();
		Thread.sleep(4000);

		driver.close();

//Create a Select object
//Select dropdown_client = new Select(dropdownElement);
//Thread.sleep(4000);

//Hardcoded value to select
//String valueToSelect = "Women Care Clinics";
//Thread.sleep(4000);

//Select the value by visible text
//dropdown_client.selectByVisibleText(valueToSelect);
//Thread.sleep(4000);

	}

}
