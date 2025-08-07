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
@Test(groups = "QC")
public class SanityForQualityControl extends BaseTest {
	
	

	public  void AClickOnQCmainTab()
	{
				
	driver.findElement(By.xpath(Loc.getProperty("QCMainTab"))).click();
	
	System.out.println("TC-QC-1: By clicking on QCMainTab tab user will see by default QC screen/Dashboard ");
			
	}
	
	public  void BCheckApplybtnFilters() throws InterruptedException
	{
		Thread.sleep(5000); 
		   // Define an explicit wait with a timeout of 10 seconds
		
		
		//wait = new WebDriverWait(driver, 10);
	    // Wait for a specific element to be clickable
	   
		WebElement recordscount = driver.findElement(By.xpath(Loc.getProperty("recordscount")));
		
		// wait.until(ExpectedConditions.visibilityOf(recordscount));
		String S1= recordscount.getText();
		System.out.println(S1);
		driver.findElement(By.xpath(Loc.getProperty("SelectAllCheckbox"))).click();	
		driver.findElement(By.id(Loc.getProperty("btnApply"))).click();	
	Thread.sleep(3000); 
		WebElement recordscount2 = driver.findElement(By.xpath(Loc.getProperty("recordscount")));
		String S2= recordscount2.getText();
		System.out.println(S2);
		Assert.assertNotEquals(S1, S2, "Filters working Properly");
		System.out.println("TC-QC-2:Apply btn Working Properly");
	}
	
	public  void CCheckClearbtnFilters() throws InterruptedException
	{
		Thread.sleep(3000); 
		WebElement recordscount = driver.findElement(By.xpath(Loc.getProperty("recordscount")));
		String S3= recordscount.getText();
		System.out.println(S3);
		
		driver.findElement(By.id(Loc.getProperty("btnClear"))).click();	
	Thread.sleep(5000); 
		WebElement recordscount2 = driver.findElement(By.xpath(Loc.getProperty("recordscount")));
		String S4= recordscount2.getText();
		System.out.println(S4);
		Assert.assertNotEquals(S3, S4, "Filters working Properly");
		System.out.println("TC-QC-3:Clear btn Working Properly");
	}

	public  void DTabsunderInventory()
	{

		WebElement Inventory= driver.findElement(By.id(Loc.getProperty("Inventory")));
		
		Inventory.click();
		
		System.out.println( Inventory.getText()+ " tab accessed");
		System.out.println("Pending tab accessed");
		
		WebElement Assigned= driver.findElement(By.xpath(Loc.getProperty("Assigned")));
		
		Assigned.click();
		
		System.out.println( "TC-QC-4:"+Assigned.getText()+ " tab accessed");
		
		
		WebElement Passed= driver.findElement(By.xpath(Loc.getProperty("Passed")));
		
		Passed.click();
		
		System.out.println("TC-QC-5:"+ Passed.getText()+ " tab accessed");
		
		WebElement Failed= driver.findElement(By.xpath(Loc.getProperty("Failed")));
		
		Failed.click();
		
		System.out.println( Failed.getText()+ " tab accessed");
		
		WebElement CompleteProduction= driver.findElement(By.xpath(Loc.getProperty("CompleteProduction")));
		
		CompleteProduction.click();
		
		System.out.println( "TC-QC-6:"+CompleteProduction.getText()+ " tab accessed");
			
	}
	
	public  void ETabsunderProduction()
	{

		WebElement Production= driver.findElement(By.id(Loc.getProperty("Production")));
		
		Production.click();
		
		System.out.println( Production.getText()+ " tab accessed");
		System.out.println("TC-QC-7: My Task tab accessed");
		
		WebElement Failedtransaction= driver.findElement(By.xpath(Loc.getProperty("Failedtransaction")));
		
		Failedtransaction.click();
		
		System.out.println( "TC-QC-8:"+ Failedtransaction.getText()+ " tab accessed");
			
	}
	
	public  void FTabsunderQualityCheck()
	{

		WebElement QualityCheck= driver.findElement(By.id(Loc.getProperty("QualityCheck")));
		
		QualityCheck.click();
		
		System.out.println( QualityCheck.getText()+ " tab accessed");
		System.out.println("TC-QC-9:"+"Pending QC tab accessed");
		
		WebElement PendingVerification= driver.findElement(By.xpath(Loc.getProperty("PendingVerification")));
		
		PendingVerification.click();
		
		System.out.println( PendingVerification.getText()+ " tab accessed");
		
		WebElement CompletedQC= driver.findElement(By.xpath(Loc.getProperty("CompletedQC")));
		
		CompletedQC.click();
		
		System.out.println( "TC-QC-10:"+CompletedQC.getText()+ " tab accessed");
			
	}

	@AfterClass
public void BackToLandingDashboard() throws InterruptedException 
{

		
		driver.findElement(By.xpath(Loc.getProperty("backtoLandingdashboard"))).click();
		//Thread.sleep(3000);
	}

}