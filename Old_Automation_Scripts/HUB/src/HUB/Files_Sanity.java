package HUB;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Files_Sanity {
	
	WebDriverWait wait;
	public static void main(String[] args) throws InterruptedException 
	{
		
		System.setProperty("webdriver.chrome.driver","C:\\Users\\saurabh.kunjir\\OneDrive - TRIARQ Health\\Chrome_Driver\\chromedriver-win64 (4)\\chromedriver-win64\\chromedriver.exe");
		 WebDriver driver=new ChromeDriver();
		//implicit wait
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		//URL launch
		driver.get("https://banq-qa.myqone.com");
		driver.manage().window().maximize();
		//identify email
		WebElement l = driver.findElement(By.id("mat-input-0"));
		l.sendKeys("saurabh.kunjir@triarqhealth.com");
		WebElement b = driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[4]/button"));
		b.click();
		//identify password
		WebElement p = driver.findElement(By.cssSelector("#mat-input-1"));
		p.sendKeys("Uruli@123456");
		WebElement C = driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button"));C.click();
		System.out.println("Triarq ERA HUB web page get dispalyed");
		Thread.sleep(10000);
		//driver.manage().timeouts().implicitlyWait(50, TimeUnit.SECONDS);
		
		
		 //Click on Files
	    driver.findElement(By.xpath("//*[@id=\"navbar\"]/div/div/app-navbarlinks/div/div/ul/li[3]/a")).click();
	    System.out.println("Files");
	    Thread.sleep(2000);
	
		
		//Test Case:QAAP-TC-1255 download master file:
		//driver.findElement(By.xpath("(//a[@class='nav-link active']")).click(); //click on Files 
		
		//Filesclick.click();
		
		WebElement GroupSelection12 = driver.findElement(By.xpath("//span[@class=\"k-icon k-i-arrow-s\"][1]"));
  		
		GroupSelection12.click();
		
		if(GroupSelection12.getText().contains("Cordial Clinical Lab")) 
        {
  		for(int i=0;i<2;i++)
  		{
  		  Actions actions3 = new Actions(driver);

  		  actions3.sendKeys(GroupSelection12, Keys.ARROW_DOWN).build().perform();
  		   
  		    System.out.println("Key Down "+i+" time.");    
  		}
  		
  		GroupSelection12.click();
        }
        Thread.sleep(4000);
        
        driver.findElement(By.xpath("(//input[@role=\"spinbutton\"])[1]")).sendKeys(" 9/16/2024");
        Thread.sleep(4000);
        driver.findElement(By.xpath("(//input[@role=\"spinbutton\"])[2]")).sendKeys("9/18/2024");
//		
//		WebElement download1 = driver.findElement(By.xpath("(//button[@title='Download'])[1]")); //Download master file
//		download1.click();
		
	}}
