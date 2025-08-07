package SanityTestcases;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

import base.BaseTest;

//import utility.WebBrowser;
@Test
public class SanityForARTracking extends BaseTest {

	@Test
	public  void AClickOnARTrackingsmainTab() throws InterruptedException
	{
		//Thread.sleep(3000); 
	driver.findElement(By.xpath(Loc.getProperty("ARTracking"))).click();
	System.out.println("By clicking on AR tracking user will see by default screen which is Inventory");
	String actualTabName = driver.findElement(By.id(Loc.getProperty("Dashboard"))).getText();
    System.out.println(actualTabName);
    String expectedTabName = "Inventory";
    Assert.assertEquals(actualTabName, expectedTabName, "Tab name does not match");
    System.out.println("Tab name is matched");
    System.out.println("Inventory Tab Accessed");
}
	@Test
	public  void BClickOnARInventory() throws InterruptedException
	{
		Thread.sleep(3000); 
		driver.findElement(By.id(Loc.getProperty("Dashboard"))).click();
		Thread.sleep(3000);
	    driver.findElement(By.id(Loc.getProperty("PendingInventory"))).click();
	
	System.out.println("Pending Inventory Tab Accessed");
	Thread.sleep(3000);
	}
	public  void CClickonApplyBtn() throws InterruptedException
	{
		Thread.sleep(5000); 
	driver.findElement(By.id(Loc.getProperty("btnApply"))).click();
	
	System.out.println("Apply button is working");
	Thread.sleep(3000);
	}
	@Test
	public  void DClickonClearBtn() throws InterruptedException
	{
 
	driver.findElement(By.id(Loc.getProperty("btnClear"))).click();
	
	System.out.println("Clear button is working");
	Thread.sleep(3000);

//	@Test
//	public  void BDashboardContent() throws InterruptedException
//	{
//		//Thread.sleep(3000); 
//	driver.findElement(By.xpath(Loc.getProperty("ARTracking"))).click();
//	System.out.println("By clicking on AR tracking user will see by default screen which is AR dashboard");
//	String actualTabName = driver.findElement(By.xpath(Loc.getProperty("AllOpenTab"))).getText();
//    System.out.println(actualTabName);
//    String expectedTabName = "ALL OPEN";
//    Assert.assertEquals(actualTabName, expectedTabName, "Tab name does not match");
//    System.out.println("Tab name is matched");
//	
//	
//	//Thread.sleep(3000); 
//	boolean isTabContentLoaded = driver.findElement(By.xpath(Loc.getProperty("AllOpenTabContent"))).isDisplayed();
//    Assert.assertTrue(isTabContentLoaded, "Tab content is not loading properly");
//    System.out.println("tab Content is loaded succesfully");
//}
}}