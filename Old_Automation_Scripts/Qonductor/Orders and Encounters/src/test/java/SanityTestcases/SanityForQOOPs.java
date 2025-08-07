package SanityTestcases;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

import java.io.IOException;
import java.nio.file.AccessDeniedException;

import base.BaseTest;

//import utility.WebBrowser;
@Test(groups = "QOOPS")
public class SanityForQOOPs extends BaseTest  {

	@Test
	public  void AClickOnQoopsmainTab() throws IOException
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

	}
	@Test
	public  void BClickonAddNewRequestbtn() throws InterruptedException
	{
		//Thread.sleep(5000); 
	driver.findElement(By.xpath(Loc.getProperty("AddNewRequestbtn"))).click();
	
	System.out.println("TC-QOOPS-2 :Add New Request form opened");
	//Thread.sleep(3000);
	}
	@Test
	public  void CClickonCrossbtnonAddNewRequestForm() throws InterruptedException
	{
		Thread.sleep(5000); 
	driver.findElement(By.xpath(Loc.getProperty("CrossbtnonAddNewRequestForm"))).click();
	
	System.out.println("TC-QOOPS-3 :Add New Request form is closed");
	Thread.sleep(3000);
	}
	@Test
	public  void DClickonRefreshbtn() throws InterruptedException
	{
		Thread.sleep(5000); 
	driver.findElement(By.xpath(Loc.getProperty("Refreshbtn"))).click();
	
	System.out.println("TC-QOOPS-4 :Grid is refreshed");
	Thread.sleep(3000);
	}
	@Test
	public  void EClickonFilters() throws InterruptedException
	{
		Thread.sleep(5000); 
	driver.findElement(By.xpath(Loc.getProperty("Filtersbtn"))).click();
	
	System.out.println("TC-QOOPS-5 :Filters Section is opened");
	Thread.sleep(3000);
	}
	@Test
	public  void FClickonApplyBtn() throws InterruptedException
	{
		Thread.sleep(5000); 
	driver.findElement(By.id(Loc.getProperty("btnApply"))).click();
	
	System.out.println("TC-QOOPS-6 :Apply button is working");
	Thread.sleep(3000);
	}
	@Test
	public  void FClickonClearBtn() throws InterruptedException
	{
		Thread.sleep(2000); 
		driver.findElement(By.xpath(Loc.getProperty("Filtersbtn"))).click();
		Thread.sleep(1000); 
	driver.findElement(By.id(Loc.getProperty("btnClear"))).click();
	
	System.out.println("TC-QOOPS-7 :RESET button is working");
	Thread.sleep(3000);
	}
	@Test
	public  void GClickOnAllClosed() throws InterruptedException
	{
		//Thread.sleep(3000); 
	driver.findElement(By.xpath(Loc.getProperty("AllClosedTab"))).click();
	
	System.out.println("TC-QOOPS-8 :All Closed Tab Accessed");
	Thread.sleep(3000);
	}
	@Test
	public  void HClickOnAssignedToMeTab() throws InterruptedException
	{
		Thread.sleep(2000); 
	driver.findElement(By.xpath(Loc.getProperty("AssignedToMeTab"))).click();
	
	System.out.println("TC-QOOPS-9 :Assigned To Me Tab Accessed");
	Thread.sleep(2000);
	}
	@Test
	public  void IClickonExportAllbtn() throws InterruptedException
	{
		Thread.sleep(5000); 
	boolean ExportAllbtn = driver.findElement(By.xpath(Loc.getProperty("ExportAll"))).isDisplayed();
	 Assert.assertTrue(ExportAllbtn, "Export All button is not Displaying");
	   
	System.out.println("TC-QOOPS-10 :Export All button Displaying");
	Thread.sleep(3000);
	}

	@AfterClass
	public void BackToLandingDashboard() throws InterruptedException 
	{
		driver.findElement(By.xpath(Loc.getProperty("backtoLandingdashboard"))).click();
		System.out.println("Qonductor landig dashboard is displaying");
		Thread.sleep(3000);
	}
	
	
}