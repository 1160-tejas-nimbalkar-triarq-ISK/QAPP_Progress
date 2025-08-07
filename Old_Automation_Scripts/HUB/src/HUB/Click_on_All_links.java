package HUB;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Click_on_All_links {

	
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
		Thread.sleep(100000);
		//Click on Summery
		driver.findElement(By.xpath("(//a[@routerlinkactive='active'])[1]")).click();
		System.out.println("Summery");
		Thread.sleep(1000);
		//Click on Pending summery
		driver.findElement(By.xpath("(//a[@class='nav-link'])[2]")).click();
		System.out.println("Pending summery");
		Thread.sleep(1000);
	    //Click on Files
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[3]")).click();
	    System.out.println("Files");
	    Thread.sleep(1000);
	    //Click on File Data
	    WebElement Filedata = driver.findElement(By.xpath("(//a[@routerlink=\"/filedata\"])[1]"));
	    System.out.println("File Data");
	    Thread.sleep(1000);
	    Filedata.click();
	    //Click on Un-Matched Data
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[4]")).click();
	    System.out.println("Un-Matched Data");
	    Thread.sleep(1000);
	    //Click on Practice files
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[5]")).click();
	    System.out.println("Practice files");
	    Thread.sleep(1000);
	    //Click on My files
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[6]")).click();
	    System.out.println("My files");
	    Thread.sleep(1000);
	    //Click on Claim search
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[7]")).click();
	    System.out.println("Claim search");
	    Thread.sleep(1000);
	    //Click on Failed processing
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[8]")).click();
	    System.out.println("Failed processing");
	    Thread.sleep(1000);
	    //Click on manually matched claim
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[9]")).click();
	    System.out.println("Manually Matched Claim");
	    Thread.sleep(1000);
	    //Click on Hold payment
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[10]")).click();
	    System.out.println("Hold payment");
	    Thread.sleep(1000);
	    //Click on In-process file
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[11]")).click();
	    System.out.println("In-process file");
	    Thread.sleep(1000);
	    //Click on configuration
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[12]")).click();
	    System.out.println("Configuration");
	    Thread.sleep(1000);
	    //Click on Reports
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[13]")).click();
	    System.out.println("Configuration");
	    Thread.sleep(1000);
	    //Click on My Acccount
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[14]")).click();
	    System.out.println("Configuration");
	    Thread.sleep(1000);
	    //Click on File Summary
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[15]")).click();
	    System.out.println("Configuration");
	    Thread.sleep(1000);
	    //Click on Service Controller
	    driver.findElement(By.xpath("(//a[@class='nav-link'])[16]")).click();
	    System.out.println("Configuration");
	    Thread.sleep(2000);
	    //Click on show/Hide menu bar
	    driver.findElement(By.xpath("//button[@class='btn btn-primary btn-sm mr-3']")).click();
	    Thread.sleep(1000);
	    driver.quit();
}
}


