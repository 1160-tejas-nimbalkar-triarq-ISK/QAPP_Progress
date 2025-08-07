package utilities;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import org.openqa.selenium.chrome.ChromeDriver;


public class WebBrowser {

	public static void main(String[] args) throws InterruptedException {
		System.setProperty("webdriver.chrome.driver","C:\\Program Files\\Java\\chromedriver.exe");
 		WebDriver driver = new ChromeDriver();
driver.get("https://accounts-qa.myqone.com/#/login");
driver.manage().window().maximize();
driver.findElement(By.id("mat-input-0")).sendKeys("shraddha.rakshe@triarqhealth.com");
driver.findElement(By.xpath("//div//button")).click();
//driver.getTitle().equals("https://accounts-staging.myqone.com/#/login?continue=https:%2F%2Fstaging.myqone.com%2Fputhash%2");
System.out.println(driver.getCurrentUrl().equals("https://accounts-qa.myqone.com/#/login"));
//System.out.println(driver.getCurrentUrl());
Thread.sleep(1000);
driver.findElement(By.xpath("//div//input")).sendKeys("Rani@2022");
driver.findElement(By.xpath("(//div//button)[1]")).click();
Thread.sleep(1000);
driver.switchTo().frame("iframe");
driver.findElement(By.xpath("(//div[@class='d-block'])[3]")).click();
//driver.get("https://qonductor-qa.myqone.com/#/dashboard/GuIyzyUs%2FjakQt73w8%2Bahg%3D%3D");
//driver.findElement(By.xpath("(//div[@class="ml-3"])[1]")).click();
//Locating the Main Menu (Parent element)
//WebDriverWait wait = new WebDriverWait(driver);
//wait.wait(10,20);


//WebElement mainMenu = driver.findElement(By.xpath("(//div[@class="ml-3"])[1]"));

//Instantiating Actions class
//Actions actions = new Actions(driver);

//Hovering on main menu


	}

}