package base;

import java.io.FileReader;
import java.io.IOException;
import java.time.Duration;
import java.util.Properties;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.BeforeSuite;
import org.testng.asserts.SoftAssert;

import io.github.bonigarcia.wdm.WebDriverManager;


public class basetest{
	
	public static WebDriver driver;
	public static Properties prop = new Properties();
	public static Properties Loc = new Properties();
	public static FileReader fr;
	public static FileReader fr1;
	public static SoftAssert softAssert = new SoftAssert();
	@BeforeSuite
	public static void setUp() throws IOException, InterruptedException {
		
		WebDriverManager.chromedriver().setup();
		WebDriver driver=new ChromeDriver();
		driver.get("https://qonductor-Staging.myqone.com/");// configfiles
		driver.manage().window().maximize();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-0']")).sendKeys("ujwala.gavit@triarqhealth.com");////input[@id='mat-input-0']
		Thread.sleep(4000);
		driver.findElement(By.xpath("//button[@type='submit']")).click(); //next button
		Thread.sleep(4000);
		driver.findElement(By.xpath("//input[@id='mat-input-1']")).sendKeys("Stg@2023"); //password
		Thread.sleep(4000);
		driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button")).click();//sign in
		Thread.sleep(4000);
		driver.findElement(By.xpath("/html/body/app-root/app-home-layout/div/app-landing-dashboard/div/div[2]/div/div[1]/div[4]")).click();//Eligibility verification 
		Thread.sleep(4000);

//		if(driver==null) {
//			FileReader fr = new FileReader(System.getProperty("user.dir")+("\\src\\test\\resources\\configfiles\\config.properties"));
//			FileReader fr1 = new FileReader(System.getProperty("user.dir")+("\\src\\test\\resources\\configfiles\\locators.properties"));
//			
//			
//			prop.load(fr);
//			Loc.load(fr1);
//		
//		}
		if(prop.getProperty("browser").equalsIgnoreCase("chrome")) {
			WebDriverManager.chromedriver().setup();// base
			driver = new ChromeDriver();// base
			driver.get(prop.getProperty("testurl"));// properties
			driver.manage().window().maximize();
			
			
			
		}
		
		if(prop.getProperty("browser").equalsIgnoreCase("firefox")) {
			WebDriverManager.chromedriver().setup();// base
			driver = new FirefoxDriver();// base
			driver.get(prop.getProperty("testurl"));// properties
			
		}
	 driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(40));
	  ChromeOptions options =new ChromeOptions();
	  options.addArguments("--remote-allow-origins=*");
	  options.addArguments("--disable-notifications");
      driver.findElement(By.xpath(Loc.getProperty("username_field"))).sendKeys(prop.getProperty("ValidUserEmailID"));

      driver.findElement(By.xpath("//button[@type='submit']")).click(); //next button

      driver.findElement(By.xpath(Loc.getProperty("password_field"))).sendKeys(prop.getProperty("ValidPassword"));

     
      

   // Introduce a static wait of 5 seconds using Thread.sleep()

           try {

               Thread.sleep(3000); // 5000 milliseconds = 5 seconds

           } catch (InterruptedException e) {

               e.printStackTrace();

           }


		
           //driver.findElement(By.xpath("//ion-button[contains(text(),'Login')]")).click();
          // driver.findElement(By.xpath("/html/body/app-root/app-login/div/div/div[1]/div/form/span/div/div[3]/button")).click();//sign in
//           driver.findElement(By.xpath(Loc.getProperty("login_button"))).click();

           

            // Introduce a static wait of 5 seconds using Thread.sleep()

           try {

               Thread.sleep(3000); // 5000 milliseconds = 5 seconds

           } catch (InterruptedException e) {

               e.printStackTrace();

           }
  }

	
	 
}



