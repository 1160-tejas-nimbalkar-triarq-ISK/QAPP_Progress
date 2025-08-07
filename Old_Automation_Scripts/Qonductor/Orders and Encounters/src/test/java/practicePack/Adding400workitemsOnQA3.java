package practicePack;


import java.time.Duration;
import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.Test;

import base.BaseTest;
import utilities.WebBrowser;
@Test
public class Adding400workitemsOnQA3 extends BaseTest{
	public  void AAClickOnQCmainTab()
	{
				
	driver.findElement(By.xpath(Loc.getProperty("QCMainTab"))).click();
	
	System.out.println("By clicking on QCMainTab tab user will see by default QC screen/Dashboard ");
			
	}
	public  void AClickOnARTrackingsmainTab() throws InterruptedException
	{
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(15));

	  	System.out.println("You are Landing on QC Dashboard ");
	  	
	  	WebElement Prod_Mytask= driver.findElement(By.xpath("//a[@id=\"idMnuMyWorkItem\"]"));
	  	Prod_Mytask.click();
	  	Thread.sleep(3000);
	  	WebElement Practice_Selection = driver.findElement(By.xpath("(//span[@class='k-input'])[2]"));
  		
  		Practice_Selection.click();
  		Practice_Selection.getText();
  		System.out.println("current practice is "+Practice_Selection.getText());

  		//Select Practice

        if(Practice_Selection.getText().contains("All")) 
        {
  		for(int i=0;i<3;i++)
  		{
  		  Actions actions3 = new Actions(driver);

  		  actions3.sendKeys(Practice_Selection, Keys.ARROW_DOWN).build().perform();
  		   
  		    System.out.println("Key Down "+i+" time.");    
  		}
  		
  		Practice_Selection.click();

  	   //Select Workitem type
       WebElement WorkItemType_Selection = driver.findElement(By.xpath("(//span[@class='k-input'])[3]"));
  		
       WorkItemType_Selection.click();
       WorkItemType_Selection.getText();
  		System.out.println("current workitem type is "+WorkItemType_Selection.getText());

  		

        if(WorkItemType_Selection.getText().contains("Select")) 
        {
  		for(int i=0;i<4;i++)
  		{
  		  Actions actions3 = new Actions(driver);

  		  actions3.sendKeys(WorkItemType_Selection, Keys.ARROW_DOWN).build().perform();
  		   
  		    System.out.println("Key Down "+i+" time.");    
  		}
	}
        int j=15;
       
        for(int i=0;i<j;i--)
  		{
   //Enter patient Code
  		String value1 ="DemoPatient"+(i);
        WebElement Patient_Code = driver.findElement(By.xpath("//input[@formcontrolname=\"fcAccount\"]"));
       Patient_Code .sendKeys("");
       //Thread.sleep(3000);
        Patient_Code .sendKeys(value1);
//  		ArrayList<Object> arrayList = new ArrayList<>();
//  		arrayList.add(i, Patient_Code);
        
        //Enter Claim no.
        String value2 ="DemoClaim"+(i);
        WebElement Claim = driver.findElement(By.xpath("//input[@formcontrolname=\"fcClaim\"]"));
        Claim .sendKeys("");
      // Thread.sleep(3000);
        Claim .sendKeys(value2);
        
        String value3 ="Testing Note "+(i);
        WebElement note = driver.findElement(By.xpath("//div//input[@formcontrolname='fcaddNote']"));
        note .sendKeys("");
      // Thread.sleep(3000);
        note .sendKeys(value3);
        
      //Click on Add Button 
  		
       WebElement Addbtn = driver.findElement(By.xpath("//div//button[@id=\"btnAddWorkItem\"]"));
       JavascriptExecutor executor = (JavascriptExecutor)driver;
       executor.executeScript("arguments[0].click();", Addbtn);
       // Addbtn.click();
        System.out.println("Done");
        System.out.println(value2);
        Thread.sleep(5000);
        System.out.println(i);
  		}
        
        }
        
        
        

}}
        

