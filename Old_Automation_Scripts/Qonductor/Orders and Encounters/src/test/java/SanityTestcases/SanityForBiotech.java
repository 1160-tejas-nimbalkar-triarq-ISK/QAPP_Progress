package SanityTestcases;

import static org.testng.AssertJUnit.assertEquals;
import java.io.IOException;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.testng.Assert;
import org.testng.annotations.Test;


import base.BaseTest;
@Test
public class SanityForBiotech extends BaseTest
{
	
	WebElement encoutertrackingtab ;
	
	WebElement idMnuDashboard;
	WebElement idMnuDocuments;
	
	@Test
    public void AClickonEncounterTracking() throws InterruptedException, IOException 
	{
        driver.findElement(By.xpath(Loc.getProperty("Biotechtab"))).click();
        System.out.println("By clicking on Orders/Encounters tab user will see by default Biotech screen/Dashboard ");
        WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
        Actions action = new Actions(driver);
	
        action.moveToElement(encoutertrackingtab).perform();
	}
    	@Test
    	public  void BEncounterstab() throws InterruptedException
    	{
        
        driver.findElement(By.id("idSbMnuEncounters")).click();
        driver.findElement(By.id(Loc.getProperty("btnApply"))).click();
        
        WebElement recordscount2 = driver.findElement(By.xpath("//kendo-pager-info[@class=\"k-pager-info k-label ng-star-inserted\"]"));
		String S4= recordscount2.getText();
        System.out.println(S4);
        
        WebElement pageheading= driver.findElement(By.xpath("//h4[@class=\"mb-0\"]"));
        String ExpectedPageHeading="Encounters";
        
        Assert.assertEquals(pageheading.getText(), ExpectedPageHeading);
        System.out.println("You are on Correct tab " + ExpectedPageHeading );
        
        Thread.sleep(1000);
        
        boolean AssignEncounterbutton = driver.findElement(By.xpath("//button[@data-target=\"#assignOrderModal\"]")).isDisplayed();
   	 Assert.assertTrue(AssignEncounterbutton, "Assign Encounter buttonn is not Displaying");
        
        boolean ExportAllbtn = driver.findElement(By.xpath("//button[contains(text(),' Export to Excel ')]")).isDisplayed();
   	 Assert.assertTrue(ExportAllbtn, "Export All button is not Displaying");
        
        
        
        
    	}
        
    	public  void CMyEncounters() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuMyEncounters")).click();
        Thread.sleep(2000); 
        driver.findElement(By.id("btnApplyFilter")).click();
        
        
        WebElement recordscount2 = driver.findElement(By.xpath("//kendo-pager-info[@class=\"k-pager-info k-label ng-star-inserted\"]"));
		String S4= recordscount2.getText();
        System.out.println(S4);
        
        WebElement pageheading= driver.findElement(By.xpath("//h4[@class=\"mb-0\"]"));
        String ExpectedPageHeading="My Encounters";
        
        Assert.assertEquals(pageheading.getText(), ExpectedPageHeading);
        System.out.println("You are on Correct tab " + ExpectedPageHeading );
        
        Thread.sleep(1000);
        
        boolean WSEncounterbutton = driver.findElement(By.id("btnWorkSelectedTask")).isDisplayed();
   	 Assert.assertTrue(WSEncounterbutton, "Work Selected Encounter buttonn is not Displaying");
        
       // boolean ExportAllbtn = driver.findElement(By.xpath("//button[contains(text(),' Export to Excel ')]")).isDisplayed();
   	 //Assert.assertTrue(ExportAllbtn, "Export All button is not Displaying");
      
        
    	}
    	public  void DPendingReview() throws InterruptedException
    	{
    	WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    	Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuPendingReview")).click();
        //driver.findElement(By.cssSelector(".border-left")).click();
        Thread.sleep(2000); 
        driver.findElement(By.id("btnApplyFilter")).click();
        
        
        WebElement recordscount2 = driver.findElement(By.xpath("//kendo-pager-info[@class=\"k-pager-info k-label ng-star-inserted\"]"));
		String S4= recordscount2.getText();
        System.out.println(S4);
        
        WebElement pageheading= driver.findElement(By.xpath("//h4[@class=\"mb-0\"]"));
        String ExpectedPageHeading="Pending Review";
        
        Assert.assertEquals(pageheading.getText(), ExpectedPageHeading);
        System.out.println("You are on Correct tab " + ExpectedPageHeading );
        
        Thread.sleep(1000);
        
        boolean  UpdateEncounterStatusbutton = driver.findElement(By.id("btnWorkSelectedTask")).isDisplayed();
        Assert.assertTrue(UpdateEncounterStatusbutton, " Update Encounter Status buttonn is not Displaying");
        
        boolean ExportAllbtn = driver.findElement(By.xpath("//button[contains(text(),' Export to Excel ')]")).isDisplayed();
   		Assert.assertTrue(ExportAllbtn, "Export All button is not Displaying");
        
        
        
        
        
    	}
    	public  void EMyReview() throws InterruptedException
    	{
    	WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    	Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuMyReview")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void FAssistance() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuAssistance")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void GcompleteSummary() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuIncompleteSummary")).click();
        Thread.sleep(2000);
    	}
    	public  void HIncompleteEncounters() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuIncompleteEncounters")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void ICompletedEncounters() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuCompletedEncounters")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void JPendingEncounters() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuPendingEncounters")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void KArchivedEncounters() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuArchivedEncounters")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void LSearch() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        Thread.sleep(1000);
        driver.findElement(By.id("idSbMnuSearch")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
        
    	}
    	public  void MAdvancesearch() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        WebElement Advancesearch = driver.findElement(By.id(Loc.getProperty("Advancesearch")));
        Advancesearch.click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
        Thread.sleep(2000);
    	}
    	public  void NExport() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuExport")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void OReprocessFolder() throws InterruptedException
    	{
    		WebElement encoutertrackingtab = driver.findElement(By.id(Loc.getProperty("EncounterTracking")));
    		Actions action = new Actions(driver);
        action.moveToElement(encoutertrackingtab).perform();
        driver.findElement(By.id("idSbMnuReprocessFolder")).click();
        
        Thread.sleep(2000);
        WebElement MissingInformation= driver.findElement(By.id("idMnuMissingInformation"));
        MissingInformation.click();
    	}
    	public  void OUserEncounters() throws InterruptedException
    	{
        driver.findElement(By.id("idSbMnuUserEncounters")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void PPracticeAssistanceCompleted() throws InterruptedException
    	{
    		WebElement MissingInformation= driver.findElement(By.id("idMnuMissingInformation"));
    		Actions action = new Actions(driver);
        action.moveToElement(MissingInformation).perform();
        driver.findElement(By.id("idSbMnuPracticeAssistanceCompleted")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void QPracticeAssigned() throws InterruptedException
    	{
    		WebElement MissingInformation= driver.findElement(By.id("idMnuMissingInformation"));
    		Actions action = new Actions(driver);
        action.moveToElement(MissingInformation).perform();
        driver.findElement(By.id("idSbMnuPracticeAssigned")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void RPracticeCompleted() throws InterruptedException
    	{
    		WebElement MissingInformation= driver.findElement(By.id("idMnuMissingInformation"));
    		Actions action = new Actions(driver);
        action.moveToElement(MissingInformation).perform();
        driver.findElement(By.id("idSbMnuPracticeCompleted")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void SDashboard() throws InterruptedException
    	{
        Thread.sleep(2000);
        WebElement idMnuDashboard= driver.findElement(By.id("idMnuDashboard"));
        idMnuDashboard.click();
    	}
    	public  void TEncounterStatus() throws InterruptedException
    	{
        driver.findElement(By.id("idSbMnuEncounterStatus")).click();
        WebElement idMnuDashboard= driver.findElement(By.id("idMnuDashboard"));
        Thread.sleep(2000);
        driver.findElement(By.cssSelector("#k-tabstrip-tab-1 > .k-link")).click();
        driver.findElement(By.cssSelector("#k-tabstrip-tab-2 > .k-link")).click();
        driver.findElement(By.cssSelector(".k-button")).click();
       // driver.findElement(By.id("df3607ab-e32e-41ae-a7cd-7c1b62e83ac9")).click();
        driver.findElement(By.cssSelector("#k-tabstrip-tab-3 > .k-link")).click();
        driver.findElement(By.cssSelector("#k-tabstrip-tab-4 > .k-link")).click();
        driver.findElement(By.cssSelector("#k-tabstrip-tab-5 > .k-link")).click();
        Thread.sleep(2000);
        driver.findElement(By.id("btnApplyFilter")).click();
        Actions action = new Actions(driver);
        action.moveToElement(idMnuDashboard).perform();
    	}
    	public  void UBiotechAddOns() throws InterruptedException
    	{ 
        
WebElement idMnuDocuments= driver.findElement(By.id("idMnuDocuments"));
idMnuDocuments.click();
Thread.sleep(2000);
driver.findElement(By.id("idSbMnuBiotechAddOns")).click();
Thread.sleep(2000);
    	}
    	public  void VBiotechDocumentSearch() throws InterruptedException
    	{
    		WebElement idMnuDocuments= driver.findElement(By.id("idMnuDocuments"));
    		Actions action = new Actions(driver);
action.moveToElement(idMnuDocuments).perform();
driver.findElement(By.id("idSbMnuBiotechDocumentSearch")).click();
Thread.sleep(2000);
driver.findElement(By.id("btnApplyFilter")).click();
    	}
    	public  void WReadyForPrinting() throws InterruptedException
    	{

WebElement idMnuPrinting= driver.findElement(By.id("idMnuPrinting"));
idMnuPrinting.click();

driver.findElement(By.id("idSbMnuReadyForPrinting")).click();
Thread.sleep(2000);
driver.findElement(By.id("btnApplyFilter")).click();
Actions action = new Actions(driver);
action.moveToElement(idMnuPrinting).perform();
driver.findElement(By.id("idSbMnuReadyForPrinting")).click();
Thread.sleep(2000);
driver.findElement(By.id("btnApplyFilter")).click();

action.moveToElement(idMnuPrinting).perform();
driver.findElement(By.id("idSbMnuSubmittedAndPrinted")).click();
Thread.sleep(2000);
driver.findElement(By.id("btnApplyFilter")).click();
    	
	}
}

//	public WebDriver getDriver() {
//		return driver;
//		// TODO Auto-generated method stub
//		
//	}

	

