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
public class MytaskEV extends BaseTest{
	public  void AClickOnEVmainTab()
	{
				
	driver.findElement(By.xpath(Loc.getProperty("EVMainTab"))).click();
	
	System.out.println("By clicking on EVMainTab tab user will see by default EV screen/Dashboard ");
			
	}
	public  void AClickOnMyTaskTab() throws InterruptedException
	{
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(15));

	  	System.out.println("You are Landing on EV Dashboard ");
	  	
	  //Click on My Task
	  	WebElement Mytask= driver.findElement(By.id("idMnuClaimWorkqueues"));
	  	Mytask.click();
	  	Thread.sleep(3000);
	  	
	  //Click on Work All button
	  	driver.findElement(By.xpath("(//button[@type=\"button\"])[4]")).click();
	  	int q=1;
        for(int j=0;j<q;j--)
        {
        	Thread.sleep(3000);
        	
      //Select Status
	  	WebElement Status_Selection = driver.findElement(By.xpath("(//span[@class=\"k-input\"])[1]"));
  		
	  	Status_Selection.click();
	  	Status_Selection.getText();
  		System.out.println("current Status is "+Status_Selection.getText());

  		for(int i=1;i<2;i++)
  		{
  		  Actions actions3 = new Actions(driver);

  		  actions3.sendKeys(Status_Selection, Keys.ARROW_DOWN).build().perform();
  		   
  		    System.out.println("Key Down "+i+" time.");    
  		}
  		
  		Status_Selection.click();
  		System.out.println("current Status is "+Status_Selection.getText());
  		Thread.sleep(3000);
  		
  		//Select Source
	  	WebElement Source_Selection = driver.findElement(By.xpath("(//span[@class=\"k-input\"])[2]"));
  		
	  	Source_Selection.click();
	  	Source_Selection.getText();
  		System.out.println("current Status is "+Source_Selection.getText());

  		


  		for(int i=1;i<2;i++)
  		{
  		  Actions actions3 = new Actions(driver);

  		  actions3.sendKeys(Source_Selection, Keys.ARROW_DOWN).build().perform();
  		   
  		  System.out.println("Key Down "+i+" time.");    
  		}
  		
  		Source_Selection.click();
  		System.out.println("current Status is "+Source_Selection.getText());
  		
  		Thread.sleep(3000);
  		
  		//Select Coverage
  		WebElement Coverage_Selection = driver.findElement(By.xpath("(//span[@class=\"k-input\"])[3]"));
  		
	      Coverage_Selection.click();
	      Coverage_Selection.getText();
  		  System.out.println("current Status is "+Coverage_Selection.getText());

  		for(int i=1;i<3;i++)
  		{
	  		  Actions actions3 = new Actions(driver);
	
	  		  actions3.sendKeys(Coverage_Selection, Keys.ARROW_DOWN).build().perform();
	  		   
	  		  System.out.println("Key Down "+i+" time.");    
  		}
  		
			Coverage_Selection.click();
			System.out.println("current Status is "+Coverage_Selection.getText());
			
			//Click on Save&Next button
			
			driver.findElement(By.id("btnSave_Next")).click();	
	}
}

  		
  		
}
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
  		
