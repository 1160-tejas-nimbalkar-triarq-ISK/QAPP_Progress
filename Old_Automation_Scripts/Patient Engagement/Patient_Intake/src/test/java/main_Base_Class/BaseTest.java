package main_Base_Class;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

public class BaseTest {
protected WebDriver driver;;

	    @BeforeClass
	    public void setUp() {
	        // Setup ChromeDriver and initialize WebDriver instance
	        System.setProperty("webdriver.chrome.driver", "C:\\Users\\mayur.sonawane\\Desktop\\Driver\\chrome driver latest\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe");
	        ChromeOptions options = new ChromeOptions();
	        options.addArguments("--remote-allow-origins=*");
	        driver = new ChromeDriver(options);
	        driver.manage().window().maximize();
	        System.out.println("Chrome browser initialized successfully");
	    }

	    @AfterClass
	    public void tearDown() {
	        // Quit the browser after tests
	        if (driver != null) {
	            driver.quit();
	            System.out.println("Browser closed successfully");
	        }
	    }
	}

