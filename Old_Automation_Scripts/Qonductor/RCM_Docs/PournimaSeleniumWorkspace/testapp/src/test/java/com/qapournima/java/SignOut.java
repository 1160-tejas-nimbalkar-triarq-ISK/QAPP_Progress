package com.qapournima.java;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class SignOut {
    // Close the browser after the test
    WebDriver driver;
    {
        driver = new ChromeDriver();
        driver.quit();
    }

}
