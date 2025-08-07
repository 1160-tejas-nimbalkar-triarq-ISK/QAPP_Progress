package base;

import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Parameters;
import java.io.FileReader;
import java.io.IOException;
import java.time.Duration;
import java.util.Properties;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.asserts.SoftAssert;
import io.github.bonigarcia.wdm.WebDriverManager;

public class BaseTest {
    
    public static WebDriver driver;
    public static Properties prop = new Properties();
    public static Properties Loc = new Properties();
    public static FileReader fr;
    public static FileReader fr1;
    public static SoftAssert softAssert = new SoftAssert();
    public static WebDriverWait wait;

    @BeforeTest
    @Parameters("browser")
    public void setUp(String browser) throws IOException, InterruptedException {
        
        // Load properties
        if(driver == null) {
            fr = new FileReader(System.getProperty("user.dir") + "\\src\\test\\resources\\configfiles\\config.properties");
            fr1 = new FileReader(System.getProperty("user.dir") + "\\src\\test\\resources\\configfiles\\locators.properties");
            prop.load(fr);
            Loc.load(fr1);
        }

        // Setup the browser driver based on the parameter passed
        switch (browser.toLowerCase()) {
            case "chrome":
                WebDriverManager.chromedriver().setup();
                driver = new ChromeDriver();
                
                
                break;
            case "edge":
                WebDriverManager.edgedriver().setup();
                driver = new EdgeDriver();
               // Thread.sleep(3000);
                break;
            case "firefox":
                WebDriverManager.firefoxdriver().setup();
                driver = new FirefoxDriver();
                break;
            default:
                throw new IllegalArgumentException("Unsupported browser: " + browser);
        }

        // Maximize window and set implicit wait
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(30));

        // Navigate to URL
        driver.get(prop.getProperty("testurl"));
        Thread.sleep(1000);
        // Perform login
        driver.findElement(By.id(Loc.getProperty("username_field"))).sendKeys(prop.getProperty("ValidUserEmailID"));
        driver.findElement(By.xpath(Loc.getProperty("subbtn1"))).click();
        driver.findElement(By.id(Loc.getProperty("password_field"))).sendKeys(prop.getProperty("ValidPassword"));
        driver.findElement(By.xpath(Loc.getProperty("subbtn1"))).click();
        
        System.out.println("User logged into Qonductor successfully.");

        // Pause for 3 seconds
        Thread.sleep(3000);
    }

    @AfterSuite
    public void tearDown() {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        if (driver != null) {
            driver.quit();
        }
        System.out.println("Teardown Successful");
    }
}
