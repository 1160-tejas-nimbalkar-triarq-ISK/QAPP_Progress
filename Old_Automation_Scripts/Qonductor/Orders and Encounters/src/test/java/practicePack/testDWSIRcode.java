package practicePack;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.relevantcodes.extentreports.LogStatus;


@Test
public class testDWSIRcode
    {
        static ExtentTest test;
        static ExtentReports report;

        @BeforeClass
        public static void startTest()
        {
        report = new ExtentReports();
        test = report.startTest("ExtentDemo");
        }

    public void extentReportsDemo()
        {
        System.setProperty("webdriver.chrome.driver", "D:SubmittalExchange_TFSQAAutomation3rdpartychromechromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.google.co.in");
        if(driver.getTitle().equals("Google"))
        {
        test.log(LogStatus.PASS, "Navigated to the specified URL");
        }
        else
        {
        test.log(LogStatus.FAIL, "Test Failed");
        }
        }
        @AfterClass
        public static void endTest()
        {
        report.endTest(test);
        report.flush();
        }
}