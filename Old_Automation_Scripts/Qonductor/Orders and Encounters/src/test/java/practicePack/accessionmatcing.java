package practicePack;

import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.poi.sl.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellType;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import base.BaseTest;

public class accessionmatcing extends BaseTest {
	File file = new File("path/to/your/excel/file.xlsx");
	FileInputStream fis = new FileInputStream(file);
	Workbook workbook = new XSSFWorkbook(fis);
	Sheet sheet = (Sheet) workbook.getSheet("Sheet1"); // Replace "Sheet1" with the name of your sheet
	List<Map<String, String>> excelData = new ArrayList<>();

	for (int i = 1; i <= sheet.getLastRowNum(); i++) { // Start from 1 to skip header row
	Row row = ((org.apache.poi.ss.usermodel.Sheet) sheet).getRow(i);
	Map<String, String> rowData = new HashMap<>();
	for (int j = 0; j < row.getLastCellNum(); j++) {
	Cell cell = row.getCell(j);
	String columnName = ((org.apache.poi.ss.usermodel.Sheet) sheet).getRow(0).getCell(j).getStringCellValue(); // Assumes the first row contains column names
	String cellValue = "";
	if (cell.getCellType() == CellType.STRING) {
	cellValue = cell.getStringCellValue();
	} else if (cell.getCellType() == CellType.NUMERIC) {
	cellValue = String.valueOf(cell.getNumericCellValue());
	} else if (cell.getCellType() == CellType.BOOLEAN) {
	cellValue = String.valueOf(cell.getBooleanCellValue());
	}
	rowData.put(columnName, cellValue);
	}
	excelData.add(rowData);
	 // Use appropriate driver based on your browser
	driver.get("https://example.com"); // Replace with the URL of your webpage
	List<Map<String, String>> matchedData = new ArrayList<>();

	for (Map<String, String> rowData1 : excelData) {
	String expectedValue = rowData1.get("ExpectedColumnName"); // Replace with the column name in Excel that contains the expected value
	String actualValue = driver.findElement(By.xpath("xpath/to/element")).getText(); // Replace with appropriate locator for the webpage element that contains the actual value
	if (expectedValue.equals(actualValue)) {
	matchedData.add(rowData1);
	driver.quit();
	workbook.close();
	fis.close();
	}
	}
	}
}}
