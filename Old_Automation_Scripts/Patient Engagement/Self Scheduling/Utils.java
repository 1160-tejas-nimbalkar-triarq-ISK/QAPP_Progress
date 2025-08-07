package automation_ss;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.FileInputStream;
import java.io.IOException;
public class Utils {
    
    private static final Logger logger = LogManager.getLogger(Utils.class);
    private static final String FILE_PATH = "C:\\ganesh\\ssAutomation.xlsx";

    public static void main(String[] args) {
        // Ensure you call getCredentials with correct sheet name and row number
        String[] credentials = getCredentials("Sheet1", 1);
        if (credentials.length > 0) {
            System.out.println("Username: " + credentials[0]);
            System.out.println("Password: " + credentials[1]);
        } else {
            System.out.println("Credentials not found.");
        }
    }

    public static String[] getCredentials(String sheetName, int rowNumber) {
        String[] credentials = new String[2];
        try (FileInputStream fis = new FileInputStream(FILE_PATH);
             Workbook workbook = new XSSFWorkbook(fis)) {
            Sheet sheet = workbook.getSheet(sheetName);
            if (sheet == null) {
                logger.error("Sheet '{}' not found.", sheetName);
                return credentials;
            }

            Row row = sheet.getRow(rowNumber);
            if (row == null) {
                logger.error("Row {} not found.", rowNumber);
                return credentials;
            }

            Cell usernameCell = row.getCell(0);
            Cell passwordCell = row.getCell(1);
            if (usernameCell != null && passwordCell != null) {
                credentials[0] = usernameCell.getStringCellValue();
                credentials[1] = passwordCell.getStringCellValue();
                // logger.info("Username: {}", credentials[0]);
                // logger.info("Password: {}", credentials[1]);
            }
        } catch (IOException e) {
            logger.error("Error reading the file: {}", e.getMessage());
        }
        return credentials;
    }
}
