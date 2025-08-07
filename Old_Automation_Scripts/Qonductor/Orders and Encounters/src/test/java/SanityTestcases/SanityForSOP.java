package SanityTestcases;

import org.testng.annotations.AfterClass;
import org.testng.annotations.Test;
import org.testng.annotations.AfterClass;
import org.testng.annotations.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

import base.BaseTest;

//import utility.WebBrowser;
@Test(groups = "SOP")
public class SanityForSOP extends BaseTest {
	
	

	public  void AClickOnSOPmainTab()
	{
				
	driver.findElement(By.xpath(Loc.getProperty("SOPMainTab"))).click();
	
	System.out.println(" TC-SOP-1 :By clicking on SOP MainTab tab user will see by default SOP screen");
			
	}
	
	public  void BClickonUploadSOPbtn() throws InterruptedException
	{
		//Thread.sleep(5000); 
	driver.findElement(By.xpath(Loc.getProperty("UploadSOPbtn"))).click();
	
	System.out.println("TC-SOP-2 :Upload SOP form is opened");
	//Thread.sleep(3000);
	}
	
	public  void CCheckClosebtn() throws InterruptedException
	{
		Thread.sleep(2000); 
	driver.findElement(By.xpath(Loc.getProperty("ClosebtnonUploadform"))).click();
	
	System.out.println(" TC-SOP-3 :Upload SOP form is Closed");
	Thread.sleep(3000);
	
	}

	public  void DclickonEyeicon ()throws InterruptedException
	{

		Thread.sleep(2000); 
	driver.findElement(By.xpath(Loc.getProperty("Eyeicon"))).click();
	
	System.out.println(" TC-SOP-4 :Uploaded SOP is opened");
	Thread.sleep(3000);
			
	}
	
	public  void EClosebtnonViewSOP()throws InterruptedException
	{


		Thread.sleep(2000); 
	driver.findElement(By.xpath(Loc.getProperty("ClosebtnonViewSOP"))).click();
	
	System.out.println(" TC-SOP-5 :SOP is closed");
	Thread.sleep(3000);
			
	}
	
	public  void FTabViewSOPtab()throws InterruptedException
	{

		Thread.sleep(2000); 
	driver.findElement(By.xpath(Loc.getProperty("ViewSOPtab"))).click();
	
	System.out.println(" TC-SOP-6 :SOP is closed");
	Thread.sleep(3000);
		
		
			
	}
	public  void GclickonEyeicon ()throws InterruptedException
	{

		Thread.sleep(2000); 
	driver.findElement(By.xpath(Loc.getProperty("Eyeicon"))).click();
	
	System.out.println(" TC-SOP-7 :Uploaded SOP is opened From view SOP tab");
	Thread.sleep(3000);
			
	}
	
	public  void HClosebtnonViewSOP()throws InterruptedException
	{


		Thread.sleep(2000); 
	driver.findElement(By.xpath(Loc.getProperty("ClosebtnonUploadform"))).click();
	
	System.out.println(" TC-SOP-8 :SOP is closed From view SOP tab");
	Thread.sleep(3000);
			
	}
	public  void Ibottomcount()throws InterruptedException
	{


		Thread.sleep(2000); 

	boolean BottomCount = driver.findElement(By.xpath(Loc.getProperty("BottomCount"))).isDisplayed();
	 Assert.assertTrue(BottomCount, "BottomCount is not Displaying");
	System.out.println( " TC-SOP-9 :BottomCount is displaying");
	
	WebElement BottomCountText= driver.findElement(By.xpath(Loc.getProperty("BottomCount")));
	System.out.println(BottomCountText.getText());
	Thread.sleep(3000);
			
	}
	@AfterClass
public void BackToLandingDashboard() throws InterruptedException 
{

		
		driver.findElement(By.xpath(Loc.getProperty("backtoLandingdashboard"))).click();
		//Thread.sleep(3000);
	}

}