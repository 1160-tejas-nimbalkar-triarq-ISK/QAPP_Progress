// package SanityTestcases;

// import org.testng.ITestContext;
// import org.testng.ITestListener;
// import org.testng.ITestResult;
// import org.openqa.selenium.WebDriver;
// import org.openqa.selenium.chrome.ChromeDriver;

// public class ScreenshotListener implements ITestListener {
//     WebDriver driver;

//     @Override
//     public void onTestFailure(ITestResult result) {
//         // Get driver from the test class (you can use other ways to get the driver instance)
//         Object currentClass = result.getInstance();
//         driver = ((SanityForBiotech) currentClass).getDriver();

//         String screenshotName = result.getMethod().getMethodName() + "_" + ScreenshotUtil.getCurrentTimeStamp();
//         ScreenshotUtil.takeScreenshot(driver, screenshotName);
//     }

//     @Override
//     public void onStart(ITestContext context) {
//     }

//     @Override
//     public void onFinish(ITestContext context) {
//     }

//     @Override
//     public void onTestStart(ITestResult result) {
//     }

//     @Override
//     public void onTestSuccess(ITestResult result) {
//     }

//     @Override
//     public void onTestSkipped(ITestResult result) {
//     }

//     @Override
//     public void onTestFailedButWithinSuccessPercentage(ITestResult result) {
//     }
// }

