package com.qapournima.java;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
//import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
//import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;

public class SignIN {

    // WebDriver instance
    WebDriver driver;
    WebDriverWait webDriverWait = new WebDriverWait(driver, Duration.ofSeconds(10));

    @BeforeMethod
    public void setUp() {
        // Initialize the Chrome WebDriver
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://qa.myqone.com/");

        // Verify the page title
        String title = driver.getTitle();
        System.out.println("Page Title: " + title);

        // Enter valid username
        WebElement Username = driver.findElement(By.id("mat-input-0"));
        Username.sendKeys("pournima.ghanmode@triarqhealth.com");
        WebElement NextButton = webDriverWait
                .until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//button[@type='submit']")));
        NextButton.click();

        // Enter incorrect password
        WebElement Password = driver.findElement(By.xpath("//input[@id='mat-input-1']"));
        Password.sendKeys("WrongPassword");
        WebElement SignInButton = webDriverWait
                .until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//button[@type='submit']")));
        SignInButton.click();

        // Verify warning message
        WebElement WarningMessage = webDriverWait.until(ExpectedConditions
                .visibilityOfElementLocated(By.xpath("//label[normalize-space()='Invalid username or password']")));
        System.out.println(WarningMessage.getText());
    }


    @AfterMethod
    public void SignOut() {
        // Close the browser
        driver.quit();
    }

}
