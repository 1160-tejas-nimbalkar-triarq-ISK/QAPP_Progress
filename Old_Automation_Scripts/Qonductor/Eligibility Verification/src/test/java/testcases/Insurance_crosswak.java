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

public class Insurance_crosswak {

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
   public void a_mylogin() throws InterruptedException {
   	driver.get("https://qonductor-staging.myqone.com/");// configfiles
//		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
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
   public void b_access() throws InterruptedException {
       Thread.sleep(4000);
       driver.findElement(By.xpath("//*[@id='optEV_Project']/div/div/h5")).click();//Eligibility verification
       Thread.sleep(4000);
   }
   
   @Test(priority=3 ,dependsOnMethods = "mylogin") // This ensures that mylogin method is executed before access
   public void c_access_Ins_crosswalk() throws InterruptedException {
       driver.findElement(By.xpath("//a[@routerlink='/evinsurancecrosswalk'][contains(.,'Insurance Crosswalk')]")).click();
       Thread.sleep(4000);
   }
   
   
   @Test(priority=4 ,dependsOnMethods = "mylogin") // This ensures that mylogin method is executed before access
   public void d_Scrollbar_Ins_crosswalk() throws InterruptedException {
   	 //scroll bar
   	// Create an instance of JavascriptExecutor
       JavascriptExecutor js = (JavascriptExecutor) driver;

       // Scroll down by pixel
       js.executeScript("window.scrollBy(0, 700);");
       Thread.sleep(4000);
       
       //js.executeScript("window.scrollBy(0, -700);");

   }
   
   @Test(priority=5 ,dependsOnMethods = "mylogin") // This ensures that mylogin method is executed before access
   public void e_Pagination_Ins_crosswalk() throws InterruptedException {
	   try {
		   driver.findElement(By.xpath("//a[@aria-label='Page 2']")).click();
		   	Thread.sleep(2000);
		   	driver.findElement(By.xpath("//a[@aria-label='Page 3']")).click();
		   	Thread.sleep(2000);
		   	driver.findElement(By.xpath("//a[@aria-label='Page 4']")).click();
		   	Thread.sleep(2000);
	} catch (Exception e) {
		System.out.println("no data");
	}

   
   	
   	
   	/*
   	// Specify the range of pages you want to click
       int startPage = 2;
       int endPage = 4;

       // Iterate through the specified range of pages
       for (int currentPage = startPage; currentPage <= endPage; currentPage++) {
           // Click on the current page link
           WebElement pageLink = driver.findElement(By.xpath("//a[@aria-label='Page " + currentPage + "']"));
           pageLink.click();

           // Validate that the correct page is displayed
           System.out.println("Current Page: " + currentPage);

           // Add your assertions or validations for the data on the current page

           // Optionally, you can take screenshots or perform other actions

           // Wait for a short duration before moving to the next page
           try {
               Thread.sleep(2000);
           } catch (InterruptedException e) {
               e.printStackTrace();
           }
       }
       
    // XPath for the last page link
   	String lastPageXPath = "//a[@class='k-link k-pager-nav k-pager-last' and @title='Go to the last page']";

   	// Find the last page element
   	WebElement lastPageLink = driver.findElement(By.xpath(lastPageXPath));

   	// Click on the last page link
   	lastPageLink.click();
*/
   	
   }
   
   @Test(priority=6 ,dependsOnMethods = "mylogin") // This ensures that mylogin method is executed before access
   
   public void f_filter() throws InterruptedException {

   	 // Locate the input field using the specified XPath
       WebElement inputField = driver.findElement(By.xpath("(//input[@class='k-textbox ng-untouched ng-pristine ng-valid'])[1]"));

       // Send keys (enter text) into the input field
       inputField.sendKeys("AARP"); // Replace "Your text here" with the desired input
       Thread.sleep(2000);
       inputField.clear();
       
   }
   
   
@Test(priority=7 ,dependsOnMethods = "mylogin") // This ensures that mylogin method is executed before access
   
   public void g_referral_filter() throws InterruptedException {

	  // Perform horizontal scroll by pixels (e.g., scrolling to the right by 500 pixels)
   horizontalScrollByPixels(driver, 500);
   Thread.sleep(4000);
}
//Function to perform horizontal scroll by pixels
   private static void horizontalScrollByPixels(WebDriver driver, int pixels) {
       JavascriptExecutor js = (JavascriptExecutor) driver;
       js.executeScript("window.scrollBy(" + pixels + ", 0);");
}
	
}
