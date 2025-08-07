package com.qapournima.java;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.AfterClass;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.Select;

public class VerifyHomePageModules {

    // WebDriver instance
     WebDriver driver = new ChromeDriver();

    @BeforeClass
    public void LaunchBrowser() {
    // Initialize the Chrome WebDriver
        
    }

    @Test
    public void SignIN() {
        // Initialize the Chrome WebDriver
        
    }

    @Test
    public void VerifyLogInPageModules() {
        // Click on a Encounter Tracking dropdown and validate the options present in the dropdown
        WebElement dropdown = driver.findElement(By.id("idMnuEncounterTracking"));
        Select select = new Select(dropdown);
        select.selectByValue("My Encounters");

    }

    @AfterClass
    public void MyEncountersScreenValidation() {
        // Close the browser after the test
        if (driver.findElement(By.xpath("//td[normalize-space()='No records available.']")) != null) 
        {
            driver.findElement(By.id("btnApplyFilter"));
        }
        
    }
}
