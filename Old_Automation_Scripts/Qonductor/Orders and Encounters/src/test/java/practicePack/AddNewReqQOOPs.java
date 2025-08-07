package practicePack;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

import base.BaseTest;

//import utility.WebBrowser;
@Test(groups = "QOOPS")
public class AddNewReqQOOPs extends BaseTest {

	@Test
	public  void AClickOnQoopsmainTab() throws InterruptedException
	{
		//Thread.sleep(3000); 
		WebElement QonductorLogo = driver.findElement(By.xpath("(//div[@class=\"d-block\"])[2]"));
		
		QonductorLogo.click();
		
		
		Thread.sleep(3000); 
	driver.findElement(By.xpath(Loc.getProperty("QooperationQ"))).click();
	System.out.println("By clicking on Qooperation Q tab user will see by default QooperationQ screen which is All Open");
	  String actualTabName = driver.findElement(By.xpath(Loc.getProperty("AllOpenTab"))).getText();
    System.out.println(actualTabName);
    String expectedTabName = "ALL OPEN";
    Assert.assertEquals(actualTabName, expectedTabName, "Tab name does not match");
    System.out.println("Tab name is matched");
	
	
	
	boolean isTabContentLoaded = driver.findElement(By.xpath(Loc.getProperty("AllOpenTabContent"))).isDisplayed();
    Assert.assertTrue(isTabContentLoaded, "Tab content is not loading properly");
    System.out.println("tab Content is loaded succesfully");

	
	
    int j=15;
    
    for(int q=0;q<j;q--)
		{

	
		Thread.sleep(2000); 
	driver.findElement(By.xpath(Loc.getProperty("AddNewRequestbtn"))).click();
	
	System.out.println("Add New Request form opened");
	
	WebElement SendTo_Selection = driver.findElement(By.id("btn1"));
		
	SendTo_Selection.click();
	Thread.sleep(3000);
  	WebElement Client_Selection = driver.findElement(By.xpath("(//span[@class='k-input'])[1]"));
		
  	Client_Selection.click();
  	Client_Selection.getText();
		System.out.println("current practice is "+Client_Selection.getText());

		//Select Practice

    if(Client_Selection.getText().contains("")) 
    {
		for(int i=1;i<2;i++)
		{
		  Actions actions3 = new Actions(driver);

		  actions3.sendKeys(Client_Selection, Keys.ARROW_DOWN).build().perform();
		   
		    System.out.println("Key Down "+i+" time.");    
		}
	
	Thread.sleep(3000);
	}
    Thread.sleep(3000);
    //TRIARQ category Selection
  	WebElement TRIARQ_Category_Selection = driver.findElement(By.xpath("(//span[@class='k-input'])[2]"));
	
  	TRIARQ_Category_Selection.click();
  	TRIARQ_Category_Selection.getText();
		System.out.println("current practice is "+TRIARQ_Category_Selection.getText());

		//Select Practice

    if(TRIARQ_Category_Selection.getText().contains("")) 
    {
		for(int i=1;i<2;i++)
		{
		  Actions actions3 = new Actions(driver);

		  actions3.sendKeys(TRIARQ_Category_Selection, Keys.ARROW_DOWN).build().perform();
		   
		    System.out.println("Key Down "+i+" time.");    
		}
		
	
	Thread.sleep(3000);
		
		
	}
	
    //Client category Selection
  	WebElement CLIENT_Category_Selection = driver.findElement(By.xpath("(//span[@class='k-input'])[3]"));
	
  	CLIENT_Category_Selection.click();
  	CLIENT_Category_Selection.getText();
		System.out.println("current practice is "+CLIENT_Category_Selection.getText());

		//Select Practice

    if(CLIENT_Category_Selection.getText().contains("")) 
    {
		for(int i=1;i<2;i++)
		{
		  Actions actions3 = new Actions(driver);

		  actions3.sendKeys(CLIENT_Category_Selection, Keys.ARROW_DOWN).build().perform();
		   
		    System.out.println("Key Down "+i+" time.");    
		}
		
		
    }
    String value1 ="DemoPatient Query for Testing "+(q);
    WebElement Patient_Code = driver.findElement(By.id("subjectname"));
   Patient_Code .sendKeys("");
   //Thread.sleep(3000);
    Patient_Code .sendKeys(value1);

	
	
	}}}