package practicePack;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

import base.BaseTest;

//import utility.WebBrowser;

public class ClosedRequestAutomation extends BaseTest {

	@Test
	public  void AClickOnQoopsmainTab() throws InterruptedException
	{
		//Thread.sleep(3000); 
	driver.findElement(By.xpath(Loc.getProperty("QooperationQ"))).click();
	System.out.println("TC-QOOPS-1.1 : By clicking on Qooperation Q tab user will see by default QooperationQ screen which is All Open");
	  String actualTabName = driver.findElement(By.xpath(Loc.getProperty("AllOpenTab"))).getText();
    System.out.println(actualTabName);
    String expectedTabName = "ALL OPEN";
    Assert.assertEquals(actualTabName, expectedTabName, "Tab name does not match");
    System.out.println("TC-QOOPS-1.2 :Tab name is matched");
	
	
	//Thread.sleep(3000); 
	boolean isTabContentLoaded = driver.findElement(By.xpath(Loc.getProperty("AllOpenTabContent"))).isDisplayed();
    Assert.assertTrue(isTabContentLoaded, "Tab content is not loading properly");
    System.out.println("TC-QOOPS-1.3 :tab Content is loaded succesfully");


		for (int i = 1; i < 1000; i++) 
		{
			Thread.sleep(1000);
            WebElement Req = driver.findElement(By.xpath(Loc.getProperty("Request") + "[" + i + "]"));
            Thread.sleep(1000);
            Req.click();
            Thread.sleep(1000);
            WebElement Closereq = driver.findElement(By.xpath(Loc.getProperty("Close")));
            Closereq.click();
            
            Thread.sleep(1000);
            
            WebElement yesbtn = driver.findElement(By.xpath(Loc.getProperty("YES")));
            yesbtn.click();
            
         }
	}


	
}