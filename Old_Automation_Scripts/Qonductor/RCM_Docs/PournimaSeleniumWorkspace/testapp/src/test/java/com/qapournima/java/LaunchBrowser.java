package com.qapournima.java;

import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


        public class LaunchBrowser {
            public static void main( String[] args ){
                WebDriver driver = new ChromeDriver();

                //Launch browser with myqone and maximize the window
                driver.manage().window().maximize();
                WebDriverWait webDriverWait = new WebDriverWait(driver, Duration.ofSeconds(10));
                driver.get("https://qa.myqone.com/");
                
                //Enter valid username
                WebElement Username = driver.findElement(By.id("mat-input-0"));
                Username.sendKeys("pournima.ghanmode@triarqhealth.com");
                WebElement NextButton = webDriverWait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//span[@class='mat-button-wrapper']")));
                NextButton.click();
                
                //Enter incorrect password
                WebElement Password = driver.findElement(By.xpath("//input[@id='mat-input-1']"));
                Password.sendKeys("WrongPassword");
                WebElement SignInButton = webDriverWait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//button[@type='submit']")));
                SignInButton.click();
                
                //Verify warning message
                WebElement WarningMessage = webDriverWait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//label[normalize-space()='Invalid username or password']")));
                System.out.println(WarningMessage.getText());
                
                //close the browser
                driver.close();
                
            }
            
    }


    