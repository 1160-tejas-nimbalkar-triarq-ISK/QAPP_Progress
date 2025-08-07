package testcases;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.github.bonigarcia.wdm.WebDriverManager;

public class demologin {

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		WebDriverManager.chromedriver().setup();
		WebDriver driver=new ChromeDriver();
		driver.get("https://qonductor-qa.myqone.com/");// configfiles
		driver.manage().window().maximize();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-0']")).sendKeys("ujwala.gavit@triarqhealth.com");////input[@id='mat-input-0']
		driver.findElement(By.xpath("//button[@type='submit']")).click(); //next button
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-1']")).sendKeys("QA@dec2023"); //password
		Thread.sleep(4000);
		driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button")).click();//sign in
		
		//Eligibility verification access
		Thread.sleep(4000);
		driver.findElement(By.xpath("//div[@class='ml-3']/h5[text()='Eligibility Verification']")).click();
		Thread.sleep(4000);
		
		//Project Status By Appointment Date

		driver.findElement(By.xpath("//span[@class='//span[@class='k-dateinput-wrap']']")).click(); //Appointment Report Date

	       Thread.sleep(4000);
	       driver.findElement(By.xpath("(//span[contains(.,'Today')])[4]")).click();
	       
	       Thread.sleep(2000);
	       
			driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();

			Thread.sleep(2000);
	//scroll bar
			// Create an instance of JavascriptExecutor
	        JavascriptExecutor js = (JavascriptExecutor) driver;

	        // Scroll down by pixel
	        js.executeScript("window.scrollBy(0, 700);");
	        Thread.sleep(4000);
	        //pagination

		
		//click on apply button 
		driver.findElement(By.xpath("//button[@id='btnApplyFilter']")).click();
		Thread.sleep(2000);
		//click on clear button
		driver.findElement(By.xpath("//button[@id='btnClearFilter']")).click();
	
//		driver.navigate ().refresh ();
		
		//open projects tab
		
		driver.findElement(By.xpath("//*[@id='idMnuProjects']")).click(); //Eligibility verification
		Thread.sleep(6000);
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();//open>>view filter options
		Thread.sleep(6000);
		
		//select priority filter
				WebElement dropdown = driver.findElement(By.xpath("//span[@class='k-input']"));
				dropdown.click();
				WebDriverWait wait =new WebDriverWait(driver, Duration.ofSeconds(10));
				WebElement dropdownOptions = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-list k-reset']")));
				WebElement desiredOption = dropdownOptions.findElement(By.xpath("//li[text()='High']"));
				desiredOption.click();
				Thread.sleep(4000);
				driver.findElement(By.id("btnApplyFilter")).click();
				Thread.sleep(6000);
			    driver.findElement(By.id("btnClearFilter")).click();
			    
				//select project name
			    try {
			    	WebElement dropdownp = driver.findElement(By.xpath("//span[@id='13d24e53-e870-470f-9b61-997820c4e659']"));
					dropdownp.click();
					WebDriverWait waitp =new WebDriverWait(driver, Duration.ofSeconds(10));
					WebElement dropdownOptionsp = waitp.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//ul[@class='k-icon k-i-arrow-s']")));
					WebElement desiredOptionp = dropdownOptionsp.findElement(By.xpath("//li[text()='MIU 09282023 ADD ONS_ 1']"));
					desiredOptionp.click();
					Thread.sleep(4000);
					driver.findElement(By.id("btnApplyFilter")).click();
					
				} catch (Exception e) {
					// TODO: handle exception
				}
				
		
		driver.findElement(By.xpath("//*[@id='k-tabstrip-tab-1']/span")).click();
        Thread.sleep(6000);
        driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
        Thread.sleep(6000);
        driver.findElement(By.xpath("//*[@id='k-tabstrip-tab-2']/span")).click();
        Thread.sleep(6000);
        driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
        Thread.sleep(6000);
		driver.findElement(By.xpath("//*[@id='k-tabstrip-tab-3']/span")).click();
		Thread.sleep(6000);
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
		driver.findElement(By.xpath("//*[@id='k-tabstrip-tabpanel-3']/div/app-evmyprojectqueue/div/div/p/kendo-buttongroup/button[2]")).click();
		Thread.sleep(9000);
		driver.findElement(By.xpath("//div//i[@title=\"View filters option\"]")).click();
		Thread.sleep(9000);
		
		//my project >>Projects 
		try
	{driver.findElement(By.xpath("//button[@title='View grid information by Projects']")).click();	//by projects
		Thread.sleep(6000);
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(9000);}
		catch (Exception e) {
			System.out.println(e.getMessage());
		}
//		driver.findElement(By.xpath("//button[@class='col-md-12 k-button k-primary' and @id='btnApplyFilter']")).click();
//		Thread.sleep(9000);
		//pending projects------------------------
		driver.findElement(By.xpath("//li[@id='k-tabstrip-tab-4']")).click();
		driver.findElement(By.xpath("//body/app-root[1]/app-home-layout[1]/div[1]/app-evprojectqueue[1]/div[1]/kendo-tabstrip[1]/ul[1]/li[5]/span[1]")).click();
		Thread.sleep(9000);
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(9000);
		//completed projects
		driver.findElement(By.xpath("//li[@id='k-tabstrip-tab--5']")).click();
		Thread.sleep(6000);
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(9000);
		//All projects
		driver.findElement(By.xpath("//*[@id='k-tabstrip-tab-6']/span")).click();
		Thread.sleep(6000);
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
		//My tasks >> My queue
		WebElement element = driver.findElement(By.xpath("//*[@id='idMnuClaimWorkqueues']"));
		element.click();
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
		//Task >> Completed Task
		WebElement elementtask = driver.findElement(By.xpath("//*[@id='idMnuTask']"));
		elementtask.click();
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
		//View Tasks
		driver.findElement(By.xpath("//*[@id='idSbMnuCompletedTasks']")).click();
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
		//view task :
		WebElement elementtaskview = driver.findElement(By.xpath("//*[@id='idMnuTask']"));
		elementtaskview.click();
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
		driver.findElement(By.xpath("//a[@id='idSbMnuViewTask' and @routerlink='/evviewtasks']")).click();
		
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(9000);
		//WebDriverWait wait = new WebDriverWait(driver,30);
		//WebElement elementView = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id='idSbMnuViewTask']"));
		//elementView.click();
		//Release task
		WebElement elementtask_release = driver.findElement(By.xpath("//*[@id='idMnuTask']"));
		elementtask_release.click();
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
		driver.findElement(By.xpath("//a[@id='idSbMnuReleaseTasks' and @routerlink='/evreleasetasks']")).click();
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
		driver.findElement(By.xpath("//a[@id='idMnuClaimWorkqueues' and @routerlink='/evinsurancecrosswalk']")).click();
		driver.findElement(By.xpath("//i[@class='fas px-2 pointer fa-chevron-circle-down' and @title='View filters option']")).click();
		Thread.sleep(6000);
//		WebElement elementRelaese = driver.findElement(By.xpath("//*[@id='idSbMnuReleaseTasks']"));
//		elementRelaese.click();
//		WebElement elementIns = driver.findElement(By.xpath("//*[@id='idMnuClaimWorkqueues']"));
//		elementIns.click();
		// Introduce a static wait of 5 seconds using Thread.sleep()
		try {
			Thread.sleep(2000); // 5000 milliseconds = 5 seconds
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

		driver.findElement(By.xpath("//ion-button[contains(text(),'Login')]")).click();
	}

}
